"""
OSM Data Toolkit - Overpass Download Worker
===========================================

This module provides a background worker for Overpass downloads.

Development Stage
------------------
Step 2.4 — Background download worker.

Purpose
-------
The Overpass downloader performs network requests that may take
several seconds or minutes.

Those requests must NOT run directly on the QGIS GUI thread because
doing so can make QGIS appear frozen while waiting for Overpass.

This module provides a QObject-based worker that can be moved into
a QThread.

Architecture
------------

    QGIS GUI thread
          |
          | starts worker
          v
    QThread
          |
          v
    OverpassDownloadWorker
          |
          v
    osm_downloader.download_overpass_data()
          |
          v
    Overpass API
          |
          v
    Raw JSON response
          |
          v
    finished signal
          |
          v
    QGIS GUI thread


Important
---------
This module does NOT:

    - generate Overpass queries;
    - define OSM feature tags;
    - process OSM geometries;
    - create output files;
    - add layers to QGIS.

It only provides the background execution layer around the
existing Overpass downloader.
"""

# =============================================================================
# IMPORTS
# =============================================================================

from threading import Event
from typing import Any, Dict, List, Optional

from qgis.PyQt.QtCore import (
    QObject,
    pyqtSignal,
)

from .cache import load_cached_response, save_cached_response

from .osm_downloader import (
    DEFAULT_INITIAL_BACKOFF,
    DEFAULT_BACKOFF_MULTIPLIER,
    DEFAULT_OVERPASS_SERVERS,
    DEFAULT_REQUEST_TIMEOUT,
    OverpassDownloadCancelled,
    download_overpass_data,
    summarize_overpass_response,
)


# =============================================================================
# WORKER CLASS
# =============================================================================

class OverpassDownloadWorker(QObject):
    """
    Background worker for downloading OSM data from Overpass.

    The object should be moved to a QThread by the caller.

    Example architecture:

        thread = QThread()
        worker = OverpassDownloadWorker(query)

        worker.moveToThread(thread)

        thread.started.connect(worker.run)

        worker.finished.connect(...)
        worker.error.connect(...)

        thread.start()
    """

    # =========================================================================
    # SIGNALS
    # =========================================================================

    # -------------------------------------------------------------------------
    # Emitted when the worker starts.
    # -------------------------------------------------------------------------

    started = pyqtSignal()

    # -------------------------------------------------------------------------
    # Informational status messages.
    #
    # The GUI can display these directly in its log.
    # -------------------------------------------------------------------------

    status = pyqtSignal(str)

    # -------------------------------------------------------------------------
    # Download successfully completed.
    #
    # The complete raw Overpass JSON dictionary is returned.
    # -------------------------------------------------------------------------

    finished = pyqtSignal(dict)

    # -------------------------------------------------------------------------
    # Download failed.
    #
    # A readable error message is returned.
    # -------------------------------------------------------------------------

    error = pyqtSignal(str)

    # -------------------------------------------------------------------------
    # Emitted when cancellation has been requested.
    #
    # Note:
    # The current downloader cannot interrupt an HTTP request that is
    # already inside requests.post(). Cancellation therefore takes effect
    # between operations rather than forcibly terminating requests.post().
    # -------------------------------------------------------------------------

    cancelled = pyqtSignal()

    # -------------------------------------------------------------------------
    # Emitted after the worker has completely finished its run, regardless
    # of success, failure or cancellation.
    #
    # This is useful for cleaning up the QThread in the GUI.
    # -------------------------------------------------------------------------

    completed = pyqtSignal()

    # =========================================================================
    # INITIALIZATION
    # =========================================================================

    def __init__(
        self,
        query: str,
        *,
        overpass_servers: Optional[List[str]] = None,
        request_timeout: int = DEFAULT_REQUEST_TIMEOUT,
        retries_per_server: int = 3,
        initial_backoff: float = DEFAULT_INITIAL_BACKOFF,
        backoff_multiplier: float = DEFAULT_BACKOFF_MULTIPLIER,
        use_cache: bool = True,
        cache_dir: Optional[str] = None,
        parent: Optional[QObject] = None,
    ):
        """
        Initialize the Overpass download worker.

        Parameters
        ----------
        query:
            Complete Overpass QL query.

        overpass_servers:
            Optional list of Overpass API servers.

        request_timeout:
            Maximum HTTP request duration in seconds.

        retries_per_server:
            Number of attempts per Overpass server.

        initial_backoff:
            Initial delay between retry attempts.

        backoff_multiplier:
            Multiplier used for exponential backoff.

        parent:
            Optional Qt parent.
        """

        super().__init__(parent)

        # ---------------------------------------------------------------------
        # Store the download configuration.
        # ---------------------------------------------------------------------

        self.query = query

        self.overpass_servers = (
            list(overpass_servers)
            if overpass_servers is not None
            else list(DEFAULT_OVERPASS_SERVERS)
        )

        self.request_timeout = request_timeout
        self.retries_per_server = retries_per_server
        self.initial_backoff = initial_backoff
        self.backoff_multiplier = backoff_multiplier
        self.use_cache = bool(use_cache)
        self.cache_dir = cache_dir

        # ---------------------------------------------------------------------
        # Thread-safe cancellation event.
        #
        # request_cancel() may be called from the QGIS GUI thread while run()
        # is executing in a background thread. threading.Event safely shares
        # the cancellation request between those threads.
        # ---------------------------------------------------------------------

        self._cancel_event = Event()

    # =========================================================================
    # CANCELLATION
    # =========================================================================

    def request_cancel(self) -> None:
        """
        Request cancellation of the current operation.

        The downloader uses a blocking HTTP request, so this cannot
        forcibly interrupt an active requests.post() call.

        Instead, the downloader checks this event between requests, before
        retries/server changes, and during retry backoff delays. If an HTTP
        request is already in progress, cancellation takes effect after that
        request returns or times out.
        """

        self._cancel_event.set()

    # =========================================================================
    # MAIN WORKER METHOD
    # =========================================================================

    def run(self) -> None:
        """
        Execute the Overpass download.

        This method is intended to be connected to QThread.started.

        It must NOT be called directly from the GUI thread.
        """

        try:

            # -----------------------------------------------------------------
            # Notify the GUI that work has started.
            # -----------------------------------------------------------------

            self.started.emit()

            self.status.emit(
                "Starting Overpass download..."
            )

            # -----------------------------------------------------------------
            # Check cancellation before starting the network operation.
            # -----------------------------------------------------------------

            if self._cancel_event.is_set():

                self.status.emit(
                    "Download cancelled before starting."
                )

                self.cancelled.emit()

                return

            # -----------------------------------------------------------------
            # Basic query status.
            # -----------------------------------------------------------------

            self.status.emit(
                "Sending query to Overpass..."
            )

            # -----------------------------------------------------------------
            # Reuse a recent response when caching is enabled. The exact query
            # text includes the AOI and selected feature categories, so a cache
            # entry is only reused for an identical request.
            # -----------------------------------------------------------------
            response_data = None
            if self.use_cache and self.cache_dir:
                response_data, cache_message = load_cached_response(
                    self.query, self.cache_dir
                )
                self.status.emit(cache_message)
            else:
                self.status.emit("Local response cache is disabled.")

            # -----------------------------------------------------------------
            # Cache miss: call Overpass in this worker thread. Save successful
            # responses after download; cache-write errors must not discard a
            # response that has already been downloaded successfully.
            # -----------------------------------------------------------------
            if response_data is None:
                response_data = download_overpass_data(
                    self.query,
                    overpass_servers=self.overpass_servers,
                    request_timeout=self.request_timeout,
                    retries_per_server=self.retries_per_server,
                    initial_backoff=self.initial_backoff,
                    backoff_multiplier=self.backoff_multiplier,
                    progress_callback=self.status.emit,
                    cancel_check=self._cancel_event.is_set,
                )
                if self.use_cache and self.cache_dir:
                    try:
                        cache_path = save_cached_response(
                            self.query, response_data, self.cache_dir
                        )
                        self.status.emit(f"Cached Overpass response: {cache_path}")
                    except Exception as cache_error:
                        self.status.emit(
                            f"Warning: download succeeded, but the response could not be cached: {cache_error}"
                        )
            else:
                self.status.emit("Using cached data; no Overpass network request was needed.")

            # -----------------------------------------------------------------
            # Check cancellation after the download.
            # -----------------------------------------------------------------

            if self._cancel_event.is_set():

                self.status.emit(
                    "Download cancelled before results were returned."
                )

                self.cancelled.emit()

                return

            # -----------------------------------------------------------------
            # Create a summary for the GUI log.
            # -----------------------------------------------------------------

            summary = summarize_overpass_response(
                response_data
            )

            self.status.emit(
                "Overpass download completed: "
                f"{summary['total_elements']} elements "
                f"({summary['nodes']} nodes, "
                f"{summary['ways']} ways, "
                f"{summary['relations']} relations)."
            )

            # -----------------------------------------------------------------
            # Return the complete raw response to the GUI/controller.
            # -----------------------------------------------------------------

            self.finished.emit(
                response_data
            )

        except OverpassDownloadCancelled:

            # -----------------------------------------------------------------
            # Cancellation is an expected control-flow outcome, not a failure.
            # Emit a status and the dedicated cancellation signal instead of
            # displaying it through the worker's error signal.
            # -----------------------------------------------------------------

            self.status.emit("Overpass download cancelled.")
            self.cancelled.emit()

        except Exception as exc:

            # -----------------------------------------------------------------
            # Convert any unexpected failure into a readable error signal.
            #
            # The GUI will decide how to display the error.
            # -----------------------------------------------------------------

            self.error.emit(
                f"{type(exc).__name__}: {exc}"
            )

        finally:

            # -----------------------------------------------------------------
            # Always tell the controller that this worker has finished.
            #
            # This allows the GUI to clean up the QThread reliably.
            # -----------------------------------------------------------------

            self.completed.emit()


# =============================================================================
# MODULE TEST
# =============================================================================

if __name__ == "__main__":

    """
    The worker itself is normally controlled by main_dialog.py.

    A full QThread test is therefore performed from the QGIS Python
    Console rather than directly here.

    This block only confirms that the module can be imported and that
    the class can be constructed.
    """

    print("=" * 70)
    print("OSM DATA TOOLKIT — DOWNLOAD WORKER MODULE TEST")
    print("=" * 70)

    TEST_QUERY = """
[out:json]
[timeout:60];
(
  way["highway"](-1.285,36.810,-1.280,36.815);
);
out body geom;
""".strip()

    try:

        worker = OverpassDownloadWorker(
            TEST_QUERY,
            request_timeout=90,
            retries_per_server=2,
        )

        print("\nWorker created successfully.")
        print(
            f"Query length: {len(TEST_QUERY)} characters"
        )
        print(
            f"Servers configured: "
            f"{len(worker.overpass_servers)}"
        )
        print(
            f"Request timeout: "
            f"{worker.request_timeout} seconds"
        )
        print(
            f"Retries per server: "
            f"{worker.retries_per_server}"
        )

        print("\nModule test PASSED.")

    except Exception as exc:

        print("\nMODULE TEST FAILED")
        print(type(exc).__name__)
        print(str(exc))

    print("\n" + "=" * 70)
    print("TEST COMPLETE")
    print("=" * 70)