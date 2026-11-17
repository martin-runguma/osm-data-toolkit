"""Polish (Polski) translation pack for the OSM Data Toolkit plugin.
Keys remain the English source strings; preserve placeholders and HTML."""
TEXT = {
 '\n<h3>Quick start</h3>\n<ol>\n  <li><b>Choose an area.</b> Use the current map extent, draw a rectangle\n      on the map, or use the bounding box of selected features or a\n      layer\'s extent.</li>\n  <li><b>Tick the OSM categories</b> you need (POI, stops, roads,\n      buildings, boundaries, landuse, ...).</li>\n  <li><b>Choose an output format and folder</b>, then click\n      <b>Download OSM Data</b>.</li>\n</ol>\n\n<h3>Good to know</h3>\n<ul>\n  <li><b>GeoPackage is recommended.</b> A Shapefile cannot hold very many\n      attribute columns, so on large areas some rarely used tag columns\n      may be left out (the log tells you when this happens).</li>\n  <li><b>Keep the area focused.</b> Very large areas produce huge Overpass\n      responses and can be slow or rejected by the public servers.</li>\n  <li><b>The cache</b> lets repeat downloads of the same query reuse\n      earlier results.</li>\n  <li><b>"Unclassified OSM elements"</b> in the log is informational: they\n      are mostly untagged vertices of lines and polygons that do not belong\n      to any selected category.</li>\n</ul>\n\n<p>Data &copy; OpenStreetMap contributors, available under the\n<a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a>.</p>\n<p><i>This plugin is not endorsed by or affiliated with the\nOpenStreetMap Foundation.</i></p>\n':
 '\n<h3>Szybki start</h3>\n<ol>\n  <li><b>Wybierz obszar.</b> Użyj bieżącego zasięgu mapy, narysuj prostokąt\n      na mapie lub użyj ramki otaczającej wybranych obiektów albo\n      zasięgu warstwy.</li>\n  <li><b>Zaznacz potrzebne kategorie OSM</b> (POI, przystanki, drogi,\n      budynki, granice, użytkowanie terenu, ...).</li>\n  <li><b>Wybierz format wyjściowy i folder</b>, a następnie kliknij\n      <b>Pobierz dane OSM</b>.</li>\n</ol>\n\n<h3>Warto wiedzieć</h3>\n<ul>\n  <li><b>Zalecany jest GeoPackage.</b> Shapefile nie mieści zbyt wielu\n      kolumn atrybutów, więc na dużych obszarach niektóre rzadko używane\n      kolumny tagów mogą zostać pominięte (dziennik poinformuje Cię, gdy\n      to nastąpi).</li>\n  <li><b>Utrzymuj obszar w rozsądnych granicach.</b> Bardzo duże obszary\n      generują ogromne odpowiedzi Overpass i mogą być wolne lub odrzucane\n      przez publiczne serwery.</li>\n  <li><b>Pamięć podręczna</b> pozwala ponownym pobraniom tego samego\n      zapytania wykorzystać wcześniejsze wyniki.</li>\n  <li><b>„Niesklasyfikowane elementy OSM”</b> w dzienniku to informacja:\n      są to głównie nieotagowane wierzchołki linii i poligonów, które nie\n      należą do żadnej wybranej kategorii.</li>\n</ul>\n\n<p>Dane &copy; OpenStreetMap contributors, dostępne na licencji\n<a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a>.</p>\n<p><i>Ta wtyczka nie jest popierana przez OpenStreetMap Foundation ani\nz nią powiązana.</i></p>\n',
 ' responded successfully.': ' odpowiedział pomyślnie.',
 ' seconds...': ' sekund…',
 '" style="color:#0B5E8E; text-decoration:none;">OpenStreetMap contributors</a> (ODbL)':
   '" style="color:#0B5E8E; text-decoration:none;">OpenStreetMap contributors</a> (ODbL)',
 ', east=': ', wschód=',
 ', north=': ', północ=',
 ', west=': ', zachód=',
 '0 selected': '0 zaznaczonych',
 '<p>Plugin version': '<p>Wersja wtyczki',
 'A download is already running.': 'Pobieranie już trwa.',
 'A labelled column of feature checkboxes.':
   'Oznaczona kolumna pól wyboru obiektów.',
 'AOI drawing cancelled.': 'Rysowanie AOI anulowane.',
 'AOI geometry is empty.': 'Geometria AOI jest pusta.',
 'AOI geometry is missing.': 'Brak geometrii AOI.',
 'AOI name': 'Nazwa AOI',
 'AOI rectangle captured successfully.':
   'Prostokąt AOI został pomyślnie przechwycony.',
 'AOI source CRS is invalid.': 'Źródłowy CRS AOI jest nieprawidłowy.',
 'AOI validation failed:': 'Walidacja AOI nie powiodła się:',
 'AOI:': 'AOI:',
 'AOI: QGIS interface is not available.':
   'AOI: interfejs QGIS jest niedostępny.',
 "AOI: click 'Draw AOI', then drag a rectangle on the QGIS map.":
   'AOI: kliknij „Narysuj AOI”, a następnie przeciągnij prostokąt na mapie QGIS.',
 "AOI: click 'Use Layer Extent' to use the full extent of the active QGIS layer.":
   'AOI: kliknij „Użyj zasięgu warstwy”, aby użyć pełnego zasięgu aktywnej warstwy QGIS.',
 'AOI: click and drag on the QGIS map.':
   'AOI: kliknij i przeciągnij na mapie QGIS.',
 'AOI: failed to resolve active layer extent':
   'AOI: nie udało się ustalić zasięgu aktywnej warstwy',
 'AOI: failed to resolve selected features':
   'AOI: nie udało się ustalić wybranych obiektów',
 'AOI: invalid': 'AOI: nieprawidłowy',
 'AOI: no active QGIS layer.': 'AOI: brak aktywnej warstwy QGIS.',
 'AOI: no feature(s) selected in the active layer.':
   'AOI: nie zaznaczono żadnych obiektów w aktywnej warstwie.',
 'AOI: not yet resolved': 'AOI: jeszcze nie ustalono',
 "AOI: select feature(s) in the active QGIS layer, then click 'Use Selected Features'.":
   'AOI: zaznacz obiekty w aktywnej warstwie QGIS, a następnie kliknij „Użyj zaznaczonych obiektów”.',
 'AOI: the active layer is not a vector layer.':
   'AOI: aktywna warstwa nie jest warstwą wektorową.',
 'AOI: unable to create': 'AOI: nie można utworzyć',
 'AOI: unable to resolve': 'AOI: nie można ustalić',
 'Activate the interactive rectangle AOI map tool.':
   'Aktywuj interaktywne narzędzie mapy do rysowania prostokąta AOI.',
 'Active layer extent': 'Zasięg aktywnej warstwy',
 'Active-layer extent AOI is invalid.':
   'AOI z zasięgu aktywnej warstwy jest nieprawidłowy.',
 'Active-layer extent captured successfully.':
   'Zasięg aktywnej warstwy został pomyślnie przechwycony.',
 'Active-layer extent validation failed:':
   'Walidacja zasięgu aktywnej warstwy nie powiodła się:',
 'Administrative boundaries': 'Granice administracyjne',
 'Administrative boundary filter: all levels (no admin_level filter).':
   'Filtr granic administracyjnych: wszystkie poziomy (bez filtra admin_level).',
 'Administrative boundary levels': 'Poziomy granic administracyjnych',
 'Administrative boundary levels:': 'Poziomy granic administracyjnych:',
 'Administrative levels must be an integer, a numeric string, a sequence of levels, or None.':
   'Poziomy administracyjne muszą być liczbą całkowitą, ciągiem numerycznym, sekwencją poziomów lub None.',
 'All OSM feature categories cleared.': 'Wyczyszczono wszystkie kategorie obiektów OSM.',
 'All OSM feature categories selected.': 'Wybrano wszystkie kategorie obiektów OSM.',
 'All Overpass server URLs must be non-empty strings.':
   'Wszystkie adresy URL serwerów Overpass muszą być niepustymi ciągami.',
 'All Overpass servers and retry attempts failed.':
   'Wszystkie serwery Overpass i próby ponowienia nie powiodły się.',
 'All administrative levels will be included.':
   'Wszystkie poziomy administracyjne zostaną uwzględnione.',
 'All administrative levels will be included; no admin_level filter will be added to the query.':
   'Wszystkie poziomy administracyjne zostaną uwzględnione; do zapytania nie zostanie dodany filtr admin_level.',
 'All attempts failed for server ': 'Wszystkie próby nie powiodły się dla serwera ',
 'All levels (0–15; no admin_level filter)':
   'Wszystkie poziomy (0–15; bez filtra admin_level)',
 'An existing output directory is required for Shapefile export.':
   'Istniejący katalog wyjściowy jest wymagany do eksportu Shapefile.',
 'An output GeoPackage path is required.':
   'Wymagana jest ścieżka wyjściowa GeoPackage.',
 'An output name is required for Shapefile export.':
   'Nazwa wyjściowa jest wymagana do eksportu Shapefile.',
 'Append a timestamped message to the processing log.':
   'Dodaj wiadomość ze znacznikiem czasu do dziennika przetwarzania.',
 'Append an exported feature count to the processing log.':
   'Dodaj liczbę wyeksportowanych obiektów do dziennika przetwarzania.',
 'Area of Interest': 'Obszar zainteresowania',
 'At least one OSM feature must be selected.':
   'Należy wybrać co najmniej jeden obiekt OSM.',
 'At least one OSM feature must be supplied.':
   'Należy podać co najmniej jeden obiekt OSM.',
 'At least one Overpass server must be provided.':
   'Należy podać co najmniej jeden serwer Overpass.',
 'Attempt details:': 'Szczegóły prób:',
 'Automatically add downloaded layers to QGIS':
   'Automatycznie dodawaj pobrane warstwy do QGIS',
 'Background Overpass download started.':
   'Rozpoczęto pobieranie Overpass w tle.',
 'Browse': 'Przeglądaj',
 'Browse…': 'Przeglądaj…',
 'Buildings': 'Budynki',
 'Bus stops': 'Przystanki autobusowe',
 'CRS:': 'CRS:',
 'Cache hit:': 'Trafienie w pamięć podręczną:',
 'Cache hit: using saved Overpass response ({age} day(s) old).':
   'Trafienie w pamięć podręczną: używam zapisanej odpowiedzi Overpass (wiek: {age} dni).',
 'Cache miss:': 'Brak trafienia w pamięć podręczną:',
 'Cache miss: could not read saved response ({error}).':
   'Brak trafienia w pamięć podręczną: nie można odczytać zapisanej odpowiedzi ({error}).',
 'Cache miss: query hash does not match the saved response.':
   'Brak trafienia w pamięć podręczną: skrót zapytania nie pasuje do zapisanej odpowiedzi.',
 'Cache miss: saved response is incomplete or invalid.':
   'Brak trafienia w pamięć podręczną: zapisana odpowiedź jest niekompletna lub nieprawidłowa.',
 'Cache miss: saved response is older than {days} days.':
   'Brak trafienia w pamięć podręczną: zapisana odpowiedź jest starsza niż {days} dni.',
 'Cache miss: saved response uses an unsupported cache format.':
   'Brak trafienia w pamięć podręczną: zapisana odpowiedź używa nieobsługiwanego formatu pamięci podręcznej.',
 'Cached Overpass response:': 'Buforowana odpowiedź Overpass:',
 'Cancel': 'Anuluj',
 'Cancellation has already been requested.': 'Anulowanie zostało już zlecone.',
 'Cancellation requested': 'Zlecono anulowanie',
 'Cancellation requested. If an HTTP request is already active, the downloader will stop when that request returns or times out.':
   'Zlecono anulowanie. Jeśli żądanie HTTP jest już aktywne, pobieranie zatrzyma się, gdy to żądanie zwróci wynik lub przekroczy limit czasu.',
 'Cancellation requested; waiting for the current request to finish...':
   'Zlecono anulowanie; oczekiwanie na zakończenie bieżącego żądania…',
 'Cannot draw AOI because the QGIS interface is unavailable.':
   'Nie można narysować AOI, ponieważ interfejs QGIS jest niedostępny.',
 'Cannot resolve active-layer extent because QGIS is unavailable.':
   'Nie można ustalić zasięgu aktywnej warstwy, ponieważ QGIS jest niedostępny.',
 'Cannot resolve current map extent because QGIS is unavailable.':
   'Nie można ustalić bieżącego zasięgu mapy, ponieważ QGIS jest niedostępny.',
 'Cannot resolve selected-feature AOI because QGIS is unavailable.':
   'Nie można ustalić AOI z zaznaczonych obiektów, ponieważ QGIS jest niedostępny.',
 'Cannot transform an empty geometry.':
   'Nie można przekształcić pustej geometrii.',
 'Capture the current QGIS map canvas extent.':
   'Przechwyć bieżący zasięg kanwy mapy QGIS.',
 'Choose all available levels, or select one or more levels to download (for example, 5–8 or level 5).':
   'Wybierz wszystkie dostępne poziomy lub zaznacz jeden bądź kilka poziomów do pobrania (na przykład 5–8 lub poziom 5).',
 'Choose an output directory before downloading.':
   'Wybierz katalog wyjściowy przed pobraniem.',
 'City name': 'Nazwa miasta',
 'Classifying OSM elements and preparing GeoPackage layers.':
   'Klasyfikowanie elementów OSM i przygotowywanie warstw GeoPackage.',
 'Classifying OSM elements and preparing Shapefile outputs.':
   'Klasyfikowanie elementów OSM i przygotowywanie danych wyjściowych Shapefile.',
 'Clear all': 'Wyczyść wszystko',
 'Clear log': 'Wyczyść dziennik',
 'Clear only the visible log, without changing processing settings.':
   'Wyczyść tylko widoczny dziennik, nie zmieniając ustawień przetwarzania.',
 'Clear selected levels so the user can make a narrower selection.':
   'Wyczyść zaznaczone poziomy, aby użytkownik mógł dokonać węższego wyboru.',
 'Clear the messages currently shown in the Processing Log.':
   'Wyczyść wiadomości aktualnie wyświetlane w dzienniku przetwarzania.',
 'Clear the previous AOI and display guidance for the chosen method.':
   'Wyczyść poprzedni AOI i wyświetl wskazówki dla wybranej metody.',
 'Close': 'Zamknij',
 'Collect optional filename components before exporting OSM data.':
   'Zbierz opcjonalne składniki nazwy pliku przed eksportem danych OSM.',
 'Compact product header above the scrollable workflow.':
   'Kompaktowy nagłówek produktu nad przewijanym przepływem pracy.',
 'Connection error on server ': 'Błąd połączenia z serwerem ',
 'Continue to Download': 'Przejdź do pobierania',
 'Convert a name component into a Windows-safe filename token.':
   'Przekształć składnik nazwy w token nazwy pliku bezpieczny dla Windows.',
 'Convert the drawn rectangle into the standard AOI object.':
   'Przekształć narysowany prostokąt w standardowy obiekt AOI.',
 'Converting OSM response to GeoPackage...':
   'Konwertowanie odpowiedzi OSM do GeoPackage…',
 'Converting OSM response to Shapefiles...':
   'Konwertowanie odpowiedzi OSM do Shapefile…',
 'Could not combine the selected feature geometries.':
   'Nie udało się połączyć geometrii zaznaczonych obiektów.',
 "Could not create Shapefile staging layer '{layer_name}'.":
   'Nie udało się utworzyć warstwy pośredniej Shapefile „{layer_name}”.',
 'Could not create an empty bus_stops_points layer.':
   'Nie udało się utworzyć pustej warstwy bus_stops_points.',
 "Could not create temporary QGIS layer '{layer_name}'.":
   'Nie udało się utworzyć tymczasowej warstwy QGIS „{layer_name}”.',
 'Could not create temporary layer for admin_level {admin_level}.':
   'Nie udało się utworzyć warstwy tymczasowej dla admin_level {admin_level}.',
 'Could not create the merged bus_stops_points layer.':
   'Nie udało się utworzyć scalonej warstwy bus_stops_points.',
 'Could not delete temporary file': 'Nie udało się usunąć pliku tymczasowego',
 "Could not load feature definition '{feature_key}': {error}":
   'Nie udało się wczytać definicji obiektu „{feature_key}”: {error}',
 'Could not merge bus-station centroids into bus-stop points.':
   'Nie udało się scalić centroidów dworców autobusowych z punktami przystanków autobusowych.',
 'Could not overwrite existing output file: {error}':
   'Nie udało się nadpisać istniejącego pliku wyjściowego: {error}',
 'Could not populate Shapefile for admin_level {admin_level}.':
   'Nie udało się wypełnić Shapefile dla admin_level {admin_level}.',
 "Could not populate temporary layer '{layer_name}'.":
   'Nie udało się wypełnić tymczasowej warstwy „{layer_name}”.',
 'Could not prepare the Overpass query:':
   'Nie udało się przygotować zapytania Overpass:',
 "Could not reopen intermediate GeoPackage layer '{layer_name}'.":
   'Nie udało się ponownie otworzyć pośredniej warstwy GeoPackage „{layer_name}”.',
 'Could not restore previous QGIS map tool:':
   'Nie udało się przywrócić poprzedniego narzędzia mapy QGIS:',
 'Could not search for temporary GeoPackages:':
   'Nie udało się wyszukać tymczasowych plików GeoPackage:',
 'Country name': 'Nazwa kraju',
 'Create one section panel and return it with its body layout.':
   'Utwórz jeden panel sekcji i zwróć go wraz z układem treści.',
 'Created bus_stops_points from bus-station polygon centroids.':
   'Utworzono bus_stops_points z centroidów poligonów dworców autobusowych.',
 'Current QGIS map extent': 'Bieżący zasięg mapy QGIS',
 'Current QGIS map extent resolved.':
   'Ustalono bieżący zasięg mapy QGIS.',
 'Data © <a href="': 'Dane © <a href="',
 'Deleted temporary workspace file:':
   'Usunięto tymczasowy plik obszaru roboczego:',
 'Details:': 'Szczegóły:',
 'Download': 'Pobierz',
 'Download OSM Data': 'Pobierz dane OSM',
 'Download OpenStreetMap data for any area and load it straight into QGIS.':
   'Pobierz dane OpenStreetMap dla dowolnego obszaru i wczytaj je bezpośrednio do QGIS.',
 'Download cancelled because existing output files were not approved for overwrite.':
   'Pobieranie anulowane, ponieważ nie zatwierdzono nadpisania istniejących plików wyjściowych.',
 'Download cancelled before it started.':
   'Pobieranie anulowane przed rozpoczęciem.',
 'Download cancelled before results were returned.':
   'Pobieranie anulowane przed zwróceniem wyników.',
 'Download cancelled before starting.':
   'Pobieranie anulowane przed rozpoczęciem.',
 'Download cancelled in the output-naming dialog.':
   'Pobieranie anulowane w oknie dialogowym nazywania danych wyjściowych.',
 'Download cancelled.': 'Pobieranie anulowane.',
 'Download cancelled; existing files preserved.':
   'Pobieranie anulowane; istniejące pliki zachowane.',
 'Download stopped.': 'Pobieranie zatrzymane.',
 'Download succeeded, but export failed.':
   'Pobieranie powiodło się, ale eksport nie powiódł się.',
 'Downloading OSM data from Overpass...':
   'Pobieranie danych OSM z Overpass…',
 'Draw AOI': 'Narysuj AOI',
 'Draw a rectangle on the QGIS map to define the AOI.':
   'Narysuj prostokąt na mapie QGIS, aby zdefiniować AOI.',
 'Draw rectangle on map': 'Narysuj prostokąt na mapie',
 'Draw the AOI rectangle on the QGIS map.':
   'Narysuj prostokąt AOI na mapie QGIS.',
 'Drawn AOI validation failed:':
   'Walidacja narysowanego AOI nie powiodła się:',
 'Drawn rectangle': 'Narysowany prostokąt',
 'Drawn rectangle AOI captured successfully.':
   'Narysowany prostokąt AOI został pomyślnie przechwycony.',
 'ERROR:': 'BŁĄD:',
 'East:': 'Wschód:',
 'Enable level checkboxes only when a specific selection is active.':
   'Włączaj pola wyboru poziomów tylko wtedy, gdy aktywny jest konkretny wybór.',
 'Enable only the AOI action button for the selected method.':
   'Włącz tylko przycisk akcji AOI dla wybranej metody.',
 'Enable or disable controls while a download is running.':
   'Włączaj lub wyłączaj kontrolki podczas trwającego pobierania.',
 'Enter at least one name (City, Country, Region, or AOI).':
   'Wprowadź co najmniej jedną nazwę (miasto, kraj, region lub AOI).',
 'Enter one or more name components. Blank fields will be skipped, and the remaining names will be joined with underscores. The selected output format will be retained.':
   'Wprowadź jeden lub więcej składników nazwy. Puste pola zostaną pominięte, a pozostałe nazwy zostaną połączone podkreśleniami. Wybrany format wyjściowy zostanie zachowany.',
 'Enter_a_name_to_preview': 'Wpisz_nazwe_aby_zobaczyc_podglad',
 'Export cancelled: output name is missing.':
   'Eksport anulowany: brak nazwy wyjściowej.',
 'Export complete:': 'Eksport zakończony:',
 'Export the downloaded response and optionally load its layers.':
   'Wyeksportuj pobraną odpowiedź i opcjonalnie wczytaj jej warstwy.',
 'Failed to activate rectangle AOI tool:':
   'Nie udało się aktywować narzędzia prostokąta AOI:',
 'Failed to create AOI.': 'Nie udało się utworzyć AOI.',
 'Failed to process drawn rectangle AOI:':
   'Nie udało się przetworzyć narysowanego prostokąta AOI:',
 'Failed to resolve active-layer extent.':
   'Nie udało się ustalić zasięgu aktywnej warstwy.',
 'Failed to resolve active-layer extent:':
   'Nie udało się ustalić zasięgu aktywnej warstwy:',
 'Failed to resolve current QGIS map extent:':
   'Nie udało się ustalić bieżącego zasięgu mapy QGIS:',
 'Failed to resolve selected-feature AOI.':
   'Nie udało się ustalić AOI z zaznaczonych obiektów.',
 'Failed to resolve selected-feature AOI:':
   'Nie udało się ustalić AOI z zaznaczonych obiektów:',
 "Failed to write layer '{layer_name}' to '{output_path}': {error}":
   'Nie udało się zapisać warstwy „{layer_name}” do „{output_path}”: {error}',
 "Feature '{feature_key}' has no tag definitions.":
   'Obiekt „{feature_key}” nie ma definicji tagów.',
 'Feature specification  does not expose a tag-filter mapping.':
   'Specyfikacja obiektu nie udostępnia mapowania filtrów tagów.',
 'Ferry stops': 'Przystanki promowe',
 'Filename preview': 'Podgląd nazwy pliku',
 'Full documentation': 'Pełna dokumentacja',
 'Generated Overpass query (': 'Wygenerowane zapytanie Overpass (',
 'GeoPackage': 'GeoPackage',
 'GeoPackage layer(s) to QGIS.': 'warstw GeoPackage do QGIS.',
 'GeoPackage saved:': 'Zapisano GeoPackage:',
 'HTTP error on server ': 'Błąd HTTP na serwerze ',
 'HTTP error — ': 'błąd HTTP — ',
 'HTTP {status} error on server {index}/{total}.':
   'Błąd HTTP {status} na serwerze {index}/{total}.',
 'Handle a drawing tool deactivation initiated outside this dialog.':
   'Obsłuż dezaktywację narzędzia rysowania zainicjowaną poza tym oknem dialogowym.',
 'Help': 'Pomoc',
 'Invalid east longitude: {value}': 'Nieprawidłowa długość geograficzna wschodnia: {value}',
 'Invalid north latitude: {value}': 'Nieprawidłowa szerokość geograficzna północna: {value}',
 'Invalid response from server ': 'Nieprawidłowa odpowiedź z serwera ',
 'Invalid south latitude: {value}': 'Nieprawidłowa szerokość geograficzna południowa: {value}',
 'Invalid west longitude: {value}': 'Nieprawidłowa długość geograficzna zachodnia: {value}',
 'Keep the numeric readout in step with the progress bar.':
   'Utrzymuj odczyt liczbowy w zgodzie z paskiem postępu.',
 'Land & built environment': 'Teren i środowisko zabudowane',
 'Landuse': 'Użytkowanie terenu',
 'Language:': 'Język:',
 'Linear features': 'Obiekty liniowe',
 'Load the saved interface language and translate visible UI strings.':
   'Wczytaj zapisany język interfejsu i przetłumacz widoczne ciągi interfejsu.',
 'Local response cache is disabled.':
   'Lokalna pamięć podręczna odpowiedzi jest wyłączona.',
 'Main OSM Data Toolkit window.': 'Główne okno OSM Data Toolkit.',
 'Manually capture the map extent after the user pans or zooms.':
   'Ręcznie przechwyć zasięg mapy po przesunięciu lub powiększeniu przez użytkownika.',
 'Merged bus-station polygon centroids into bus_stops_points.':
   'Scalono centroidy poligonów dworców autobusowych do bus_stops_points.',
 'No Overpass selectors were generated.':
   'Nie wygenerowano żadnych selektorów Overpass.',
 'No active QGIS layer is available.':
   'Brak dostępnej aktywnej warstwy QGIS.',
 'No active layer is available.': 'Brak dostępnej aktywnej warstwy.',
 'No exportable features matched the selected categories. Try another AOI or select additional OSM feature categories.':
   'Żadne obiekty nadające się do eksportu nie pasowały do wybranych kategorii. Spróbuj innego AOI lub wybierz dodatkowe kategorie obiektów OSM.',
 'No features are selected in the active layer.':
   'W aktywnej warstwie nie zaznaczono żadnych obiektów.',
 'No levels selected. Select at least one level to continue.':
   'Nie wybrano żadnych poziomów. Wybierz co najmniej jeden poziom, aby kontynuować.',
 'No selected features found.': 'Nie znaleziono zaznaczonych obiektów.',
 'No valid Area of Interest is available. Select an AOI method and resolve the AOI before downloading.':
   'Brak prawidłowego obszaru zainteresowania. Wybierz metodę AOI i ustal AOI przed pobraniem.',
 'North:': 'Północ:',
 'Note: {layer_name} has too many tag columns for one Shapefile (DBF size limit); {count} rarely-used columns were left out.':
   'Uwaga: {layer_name} ma zbyt wiele kolumn tagów dla jednego Shapefile (limit rozmiaru DBF); pominięto {count} rzadko używanych kolumn.',
 'OSM Data Toolkit': 'OSM Data Toolkit',
 'OSM Data Toolkit initialised.': 'Zainicjowano OSM Data Toolkit.',
 'OSM Feature Categories': 'Kategorie obiektów OSM',
 'OSM export completed successfully.':
   'Eksport OSM zakończony pomyślnie.',
 'One or more output files with this name already exist. Do you want to overwrite the matching output files?':
   'Co najmniej jeden plik wyjściowy o tej nazwie już istnieje. Czy chcesz nadpisać pasujące pliki wyjściowe?',
 'Only the selected levels': 'Tylko wybrane poziomy',
 'Only validated Overpass responses can be cached.':
   'Tylko zwalidowane odpowiedzi Overpass mogą być buforowane.',
 'Open public spaces': 'Otwarte przestrzenie publiczne',
 'Open the in-plugin help with links to the online documentation.':
   'Otwórz pomoc wtyczki z odnośnikami do dokumentacji online.',
 'Output Settings': 'Ustawienia wyjściowe',
 'Output directory': 'Katalog wyjściowy',
 'Output directory selected:': 'Wybrano katalog wyjściowy:',
 'Output format': 'Format wyjściowy',
 'Output settings': 'Ustawienia wyjściowe',
 'Overpass download cancelled.': 'Pobieranie Overpass anulowane.',
 'Overpass download completed:': 'Pobieranie Overpass zakończone:',
 'Overpass download failed.': 'Pobieranie Overpass nie powiodło się.',
 'Overpass download failed:': 'Pobieranie Overpass nie powiodło się:',
 'Overpass download running...': 'Pobieranie Overpass trwa…',
 'Overpass download was cancelled by the caller.':
   'Pobieranie Overpass zostało anulowane przez wywołującego.',
 'Overpass query must be a non-empty string.':
   'Zapytanie Overpass musi być niepustym ciągiem.',
 "Overpass response 'elements' field is not a list.":
   'Pole „elements” odpowiedzi Overpass nie jest listą.',
 "Overpass response does not contain an 'elements' field.":
   'Odpowiedź Overpass nie zawiera pola „elements”.',
 'Overpass response is not a JSON object.':
   'Odpowiedź Overpass nie jest obiektem JSON.',
 'Overpass response received successfully:':
   'Odpowiedź Overpass otrzymana pomyślnie:',
 'Overpass server ': 'Serwer Overpass ',
 'Overpass server returned invalid JSON. Response preview: ':
   'Serwer Overpass zwrócił nieprawidłowy JSON. Podgląd odpowiedzi: ',
 'Overpass servers available:': 'Dostępne serwery Overpass:',
 'Overpass timeout must be greater than zero.':
   'Limit czasu Overpass musi być większy od zera.',
 'Plugin version': 'Wersja wtyczki',
 'Points of interest (POI)': 'Punkty zainteresowania (POI)',
 'Prepared {index:,} of {total:,} OSM elements for export...':
   'Przygotowano {index:,} z {total:,} elementów OSM do eksportu…',
 'Preparing Overpass download...': 'Przygotowywanie pobierania Overpass…',
 'Preparing Overpass query.': 'Przygotowywanie zapytania Overpass.',
 'Processing Options': 'Opcje przetwarzania',
 'Processing log': 'Dziennik przetwarzania',
 'Processing messages will appear here...':
   'Wiadomości przetwarzania pojawią się tutaj…',
 'Processing options': 'Opcje przetwarzania',
 'Public transport & places': 'Transport publiczny i miejsca',
 'QGIS interface object was not detected. Canvas-dependent AOI tools are disabled.':
   'Nie wykryto obiektu interfejsu QGIS. Narzędzia AOI zależne od kanwy są wyłączone.',
 'QGIS map canvas could not be accessed.':
   'Nie można uzyskać dostępu do kanwy mapy QGIS.',
 'QGIS map canvas is unavailable.': 'Kanwa mapy QGIS jest niedostępna.',
 'Rail stops': 'Przystanki kolejowe',
 'Railways': 'Koleje',
 'Read the plugin version from metadata.txt (empty string if absent).':
   'Odczytaj wersję wtyczki z metadata.txt (pusty ciąg, jeśli brak).',
 'Read, validate and store the current QGIS map canvas extent.':
   'Odczytaj, zwaliduj i zapisz bieżący zasięg kanwy mapy QGIS.',
 'Ready.': 'Gotowe.',
 'Rectangle AOI drawing tool activated.':
   'Aktywowano narzędzie rysowania prostokąta AOI.',
 'Rectangle AOI drawing was cancelled.':
   'Rysowanie prostokąta AOI zostało anulowane.',
 'Region name': 'Nazwa regionu',
 'Report an issue': 'Zgłoś problem',
 'Request cooperative cancellation of the background worker.':
   'Zażądaj kooperatywnego anulowania procesu roboczego w tle.',
 'Request error on server ': 'Błąd żądania na serwerze ',
 'Restore default GUI settings when the dialog closes.':
   'Przywróć domyślne ustawienia GUI po zamknięciu okna dialogowego.',
 'Restore the GUI once the background thread has stopped.':
   'Przywróć GUI po zatrzymaniu wątku działającego w tle.',
 'Restore the QGIS map tool active before rectangle drawing.':
   'Przywróć narzędzie mapy QGIS aktywne przed rysowaniem prostokąta.',
 'Restore the map tool and reset state before hiding the dialog.':
   'Przywróć narzędzie mapy i zresetuj stan przed ukryciem okna dialogowego.',
 'Retrying in ': 'Ponowna próba za ',
 'Return selected levels, or None when all levels are requested.':
   'Zwróć wybrane poziomy lub None, gdy żądane są wszystkie poziomy.',
 'Return the combined, sanitized filename prefix.':
   'Zwróć połączony, oczyszczony prefiks nazwy pliku.',
 'Return the mapping between feature keys and GUI checkboxes.':
   'Zwróć mapowanie między kluczami obiektów a polami wyboru GUI.',
 'Return the selected GUI feature keys.':
   'Zwróć wybrane klucze obiektów GUI.',
 'Roads': 'Drogi',
 'Run a modal dialog on both Qt5 and Qt6.':
   'Uruchom modalne okno dialogowe zarówno w Qt5, jak i Qt6.',
 'Select Output Directory': 'Wybierz katalog wyjściowy',
 'Select a vector layer with selected features.':
   'Wybierz warstwę wektorową z zaznaczonymi obiektami.',
 'Select all': 'Zaznacz wszystko',
 'Select an active QGIS layer.': 'Wybierz aktywną warstwę QGIS.',
 'Select at least one OSM feature category before downloading.':
   'Wybierz co najmniej jedną kategorię obiektów OSM przed pobraniem.',
 'Select at least one administrative level, or choose All levels.':
   'Wybierz co najmniej jeden poziom administracyjny lub wybierz „Wszystkie poziomy”.',
 'Select at least one administrative level, or use None to retrieve all levels.':
   'Wybierz co najmniej jeden poziom administracyjny lub użyj None, aby pobrać wszystkie poziomy.',
 'Select levels 0–15 and switch to specific-level mode.':
   'Zaznacz poziomy 0–15 i przełącz na tryb konkretnych poziomów.',
 'Select one or more features in the active layer.':
   'Zaznacz jeden lub więcej obiektów w aktywnej warstwie.',
 'Select output directory...': 'Wybierz katalog wyjściowy…',
 'Selected administrative levels:': 'Wybrane poziomy administracyjne:',
 'Selected feature IDs:': 'Identyfikatory zaznaczonych obiektów:',
 'Selected feature(s) in active layer':
   'Zaznaczone obiekty w aktywnej warstwie',
 'Selected features (': 'Zaznaczone obiekty (',
 'Selected-feature AOI captured successfully (':
   'AOI z zaznaczonych obiektów przechwycony pomyślnie (',
 'Selected-feature AOI captured successfully.':
   'AOI z zaznaczonych obiektów został pomyślnie przechwycony.',
 'Selected-feature AOI is invalid.':
   'AOI z zaznaczonych obiektów jest nieprawidłowy.',
 'Selected-feature AOI requires a vector layer.':
   'AOI z zaznaczonych obiektów wymaga warstwy wektorowej.',
 'Selected-feature AOI validation failed:':
   'Walidacja AOI z zaznaczonych obiektów nie powiodła się:',
 'Sending query to Overpass...': 'Wysyłanie zapytania do Overpass…',
 'Server ': 'Serwer ',
 'Shapefile': 'Shapefile',
 'Shapefile export completed in:': 'Eksport Shapefile zakończony w:',
 'Shapefile field names shortened for':
   'Nazwy pól Shapefile skrócone dla',
 'Shapefile layer(s) to QGIS.': 'warstw Shapefile do QGIS.',
 'Short in-plugin help with links to the full online documentation.':
   'Krótka pomoc wtyczki z odnośnikami do pełnej dokumentacji online.',
 'Show AOI coordinates and source CRS in the dialog.':
   'Pokaż współrzędne AOI i źródłowy CRS w oknie dialogowym.',
 'Show a concise description of the active administrative filter.':
   'Pokaż zwięzły opis aktywnego filtra administracyjnego.',
 'Source CRS is invalid.': 'Źródłowy CRS jest nieprawidłowy.',
 'South latitude cannot be greater than north latitude.':
   'Szerokość geograficzna południowa nie może być większa niż północna.',
 'South:': 'Południe:',
 'Starting Overpass download...': 'Rozpoczynanie pobierania Overpass…',
 'Supporting copy: muted, wrapped and visually quiet.':
   'Tekst pomocniczy: wyciszony, zawijany i wizualnie spokojny.',
 "Tag '{tag}' contains an empty value list.":
   'Tag „{tag}” zawiera pustą listę wartości.',
 'Temporary workspace cleanup complete:':
   'Czyszczenie tymczasowego obszaru roboczego zakończone:',
 'Temporary workspace cleanup complete: no matching files found.':
   'Czyszczenie tymczasowego obszaru roboczego zakończone: nie znaleziono pasujących plików.',
 'Temporary-file cleanup skipped: workspace directory is invalid.':
   'Czyszczenie plików tymczasowych pominięte: katalog obszaru roboczego jest nieprawidłowy.',
 'The OSM download succeeded, but the output could not be created.':
   'Pobieranie OSM powiodło się, ale nie udało się utworzyć danych wyjściowych.',
 "The Overpass response must be a JSON object with an 'elements' list.":
   'Odpowiedź Overpass musi być obiektem JSON z listą „elements”.',
 'The QGIS map canvas CRS is invalid.':
   'CRS kanwy mapy QGIS jest nieprawidłowy.',
 'The active layer CRS is invalid.':
   'CRS aktywnej warstwy jest nieprawidłowy.',
 'The active layer extent is empty.': 'Zasięg aktywnej warstwy jest pusty.',
 'The active layer must be a vector layer.':
   'Aktywna warstwa musi być warstwą wektorową.',
 'The combined name is too long. Shorten one or more components.':
   'Połączona nazwa jest zbyt długa. Skróć jeden lub więcej składników.',
 'The combined selected-feature geometry is empty.':
   'Połączona geometria zaznaczonych obiektów jest pusta.',
 'The current AOI is invalid:': 'Bieżący AOI jest nieprawidłowy:',
 'The current QGIS map extent is empty.':
   'Bieżący zasięg mapy QGIS jest pusty.',
 'The dialog cannot close while a download thread is running. Cancellation has been requested; close the dialog after it stops.':
   'Nie można zamknąć okna dialogowego, gdy działa wątek pobierania. Zlecono anulowanie; zamknij okno dialogowe po jego zatrzymaniu.',
 'The download completed, but no confirmed output name was available.':
   'Pobieranie zakończone, ale nie było potwierdzonej nazwy wyjściowej.',
 "The exported Shapefile '{path}' could not be opened in QGIS.":
   'Nie można otworzyć wyeksportowanego Shapefile „{path}” w QGIS.',
 "The exported layer '{layer_name}' could not be opened in QGIS.":
   'Nie można otworzyć wyeksportowanej warstwy „{layer_name}” w QGIS.',
 'The output name does not contain any valid filename characters.':
   'Nazwa wyjściowa nie zawiera żadnych prawidłowych znaków nazwy pliku.',
 'The output name is empty after filename validation.':
   'Nazwa wyjściowa jest pusta po walidacji nazwy pliku.',
 'The selected features contain no valid geometry.':
   'Zaznaczone obiekty nie zawierają prawidłowej geometrii.',
 'The selected output directory does not exist. Choose an existing folder.':
   'Wybrany katalog wyjściowy nie istnieje. Wybierz istniejący folder.',
 'There is no active download to cancel.':
   'Brak aktywnego pobierania do anulowania.',
 'Timeout on server ': 'Przekroczono limit czasu na serwerze ',
 'Translate widget labels while preserving each original English string.':
   'Przetłumacz etykiety widżetów, zachowując każdy oryginalny ciąg angielski.',
 'Trying Overpass server ': 'Próbowanie serwera Overpass ',
 'Unable to start AOI drawing:': 'Nie można rozpocząć rysowania AOI:',
 'Unclassified OSM elements not written to feature layers:':
   'Niesklasyfikowane elementy OSM, których nie zapisano do warstw obiektów:',
 'Unsupported geometry family: {geometry_family}':
   'Nieobsługiwana rodzina geometrii: {geometry_family}',
 "Unsupported geometry type '{geometry_type}' for feature '{feature_key}'.":
   'Nieobsługiwany typ geometrii „{geometry_type}” dla obiektu „{feature_key}”.',
 'Unsupported geometry type for Shapefile export: {geometry_type}':
   'Nieobsługiwany typ geometrii dla eksportu Shapefile: {geometry_type}',
 "Unsupported match mode '{mode}' for feature '{feature_key}'.":
   'Nieobsługiwany tryb dopasowania „{mode}” dla obiektu „{feature_key}”.',
 'Unsupported output format:': 'Nieobsługiwany format wyjściowy:',
 "Unsupported tag value type for '{feature_key}': {value_type}":
   'Nieobsługiwany typ wartości tagu dla „{feature_key}”: {value_type}',
 'Update Current QGIS Map Extent':
   'Zaktualizuj bieżący zasięg mapy QGIS',
 'Update the "N selected" count next to the category heading.':
   'Zaktualizuj licznik „N zaznaczonych” obok nagłówka kategorii.',
 'Update the filename preview as the user edits the components.':
   'Aktualizuj podgląd nazwy pliku podczas edycji składników przez użytkownika.',
 'Use Layer Extent': 'Użyj zasięgu warstwy',
 'Use Selected Features': 'Użyj zaznaczonych obiektów',
 'Use local cache where available':
   'Używaj lokalnej pamięci podręcznej, gdy jest dostępna',
 'Use selected features in the active vector layer as the AOI.':
   'Użyj zaznaczonych obiektów w aktywnej warstwie wektorowej jako AOI.',
 'Use the full extent of the active QGIS layer as the AOI.':
   'Użyj pełnego zasięgu aktywnej warstwy QGIS jako AOI.',
 'Use the full extent of the active QGIS layer.':
   'Użyj pełnego zasięgu aktywnej warstwy QGIS.',
 'Use the selected features of the active vector layer as the AOI.':
   'Użyj zaznaczonych obiektów aktywnej warstwy wektorowej jako AOI.',
 'Using cached data; no Overpass network request was needed.':
   'Używam danych z pamięci podręcznej; żądanie sieciowe Overpass nie było potrzebne.',
 'Validate filename and any explicitly selected admin levels.':
   'Zwaliduj nazwę pliku i wszelkie jawnie wybrane poziomy administracyjne.',
 'Validate inputs and start the background Overpass download.':
   'Zwaliduj dane wejściowe i rozpocznij pobieranie Overpass w tle.',
 'WGS84 AOI bbox: south=': 'Ramka AOI WGS84: południe=',
 'WGS84 AOI geometry is not available.':
   'Geometria AOI w WGS84 jest niedostępna.',
 'Warning: download succeeded, but the response could not be cached:':
   'Ostrzeżenie: pobieranie powiodło się, ale nie udało się zapisać odpowiedzi w pamięci podręcznej:',
 'Waterways': 'Drogi wodne',
 'West longitude cannot be greater than east longitude.':
   'Długość geograficzna zachodnia nie może być większa niż wschodnia.',
 'West:': 'Zachód:',
 'Writing Shapefile {layer_index}/{total}: {layer_name}...':
   'Zapisywanie Shapefile {layer_index}/{total}: {layer_name}…',
 'Writing layer {layer_index}/{total}: {layer_name} ({count:,} features)...':
   'Zapisywanie warstwy {layer_index}/{total}: {layer_name} ({count:,} obiektów)…',
 'attempt ': 'próba ',
 'characters).': 'znaków).',
 'connection error — ': 'błąd połączenia — ',
 'e.g. CBD': 'np. CBD',
 'e.g. Kenya': 'np. Kenia',
 'e.g. Nairobi': 'np. Nairobi',
 'e.g. NairobiCounty': 'np. NairobiCounty',
 'elements (': 'elementów (',
 'export failed:': 'eksport nie powiódł się:',
 'feature records).': 'rekordów obiektów).',
 'feature(s)).': 'obiekt(ów)).',
 'features written.': 'obiektów zapisanych.',
 'file(s) deleted.': 'plik(ów) usunięto.',
 'relation geometry assignment(s); relation-member geometry assembly is not implemented yet.':
   'przypisań geometrii relacji; składanie geometrii elementów relacji nie jest jeszcze zaimplementowane.',
 'relations).': 'relacji).',
 'response_data must be a dictionary.':
   'response_data musi być słownikiem.',
 "response_data['elements'] must be a list.":
   "response_data['elements'] musi być listą.",
 'temporary file(s) could not be deleted. They may still be in use by QGIS or another process.':
   'nie udało się usunąć plików tymczasowych. Mogą być nadal używane przez QGIS lub inny proces.',
 'timeout — ': 'limit czasu — ',
 '{output_format} export failed: {error}':
   'Eksport {output_format} nie powiódł się: {error}',
 '— Confirm Overwrite': '— Potwierdź nadpisanie',
 '— Export Error': '— Błąd eksportu',
 '— Help': '— Pomoc',
 '— Output Naming': '— Nazewnictwo danych wyjściowych',
}