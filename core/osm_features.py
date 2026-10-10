"""
OSM Data Toolkit - OSM Feature Specifications
===============================================

This module defines the OpenStreetMap (OSM) feature types supported
by the OSM Data Toolkit plugin.

Development stage
-----------------
Step 2.1 — OSM Feature Specifications

This module is intentionally focused on FEATURE DEFINITIONS only.

It does NOT:
    - build Overpass queries
    - download OSM data
    - process OSM responses
    - create output layers
    - add layers to QGIS

Those functions will be implemented in later modules.

The feature definitions in this module are used as the central
configuration for the rest of the OSM download workflow.

Feature categories
------------------
1. Public Transport & Places
2. Linear Features
3. Land & Built Environment

Total feature definitions
-------------------------
12

Notes
-----
Some tag definitions intentionally use different value types:

    True
        Match any value associated with the OSM key.

    "value"
        Match one specific OSM tag value.

    ["value1", "value2"]
        Match any of the listed OSM tag values.

The interpretation of these tag definitions will be implemented
later by the Overpass query generator.
"""

from dataclasses import dataclass
from typing import Dict, List, Union


# ============================================================================
# TAG VALUE TYPE
# ============================================================================
#
# An OSM tag definition can contain:
#
#     True
#         Match any value for the specified OSM key.
#
#     "value"
#         Match one specific OSM value.
#
#     ["value1", "value2"]
#         Match any of several specified values.
#
# Keeping this flexible allows the feature specification to remain
# readable while the Overpass query generator handles the actual
# interpretation.
# ============================================================================

TagValue = Union[bool, str, List[str]]


# ============================================================================
# FEATURE CATEGORIES
# ============================================================================
#
# These category names are also used by the GUI.
# Keep them centralized so that spelling/capitalization remains
# consistent throughout the plugin.
# ============================================================================

CATEGORY_PUBLIC_TRANSPORT_PLACES = "Public Transport & Places"

CATEGORY_LINEAR_FEATURES = "Linear Features"

CATEGORY_LAND_BUILT_ENVIRONMENT = "Land & Built Environment"


# ============================================================================
# TAG MATCH MODES
# ============================================================================
#
# These constants define how multiple tag conditions within a feature
# are combined by the future Overpass query generator.
#
# MATCH_ANY
#     An OSM object matches when ANY ONE of the specified tag conditions
#     is satisfied.
#
# MATCH_ALL
#     An OSM object matches only when ALL specified tag conditions
#     are satisfied.
#
# The current feature specifications use MATCH_ANY because the
# different tags represent alternative ways an OSM object can be
# classified as the requested feature.
# ============================================================================

MATCH_ANY = "OR"

MATCH_ALL = "AND"


# ============================================================================
# OSM FEATURE DATA CLASS
# ============================================================================
#
# Each supported OSM feature is represented by one OSMFeature object.
#
# The object stores:
#
#     feature_id
#         Internal identifier used by the plugin.
#
#     name
#         Human-readable name displayed in the GUI.
#
#     category
#         GUI category.
#
#     geometry
#         Expected output geometry:
#             point
#             line
#             polygon
#             mixed
#
#     tags
#         OSM tag definitions used later by the Overpass query builder.
#
#     match_mode
#         Defines how multiple tag conditions are combined:
#             MATCH_ANY
#             MATCH_ALL
#
#     description
#         Explanation of what the feature represents.
# ============================================================================

@dataclass(frozen=True)
class OSMFeature:

    feature_id: str

    name: str

    category: str

    geometry: str

    tags: Dict[str, TagValue]

    match_mode: str

    description: str


# ============================================================================
# OSM FEATURE DEFINITIONS
# ============================================================================
#
# IMPORTANT:
#
# This dictionary is the central definition of the OSM feature types
# supported by the plugin.
#
# Do not place download logic, API calls or processing code here.
#
# The Overpass query generator will use these definitions later.
# ============================================================================

OSM_FEATURES: Dict[str, OSMFeature] = {

    # ------------------------------------------------------------------------
    # 1. POI
    # ------------------------------------------------------------------------

    "poi": OSMFeature(
        feature_id="poi",
        name="POI",
        category=CATEGORY_PUBLIC_TRANSPORT_PLACES,
        geometry="point",

        tags={
            "landuse": [
                "industrial",
                "commercial",
                "retail",
            ],

            "industrial": True,

            "office": True,

            "shop": True,

            "leisure": [
                "shopping_center",
                "stadium",
                "sports_centre",
                "park",
                "fitness_centre",
                "pitch",
            ],

            "amenity": [
                "school",
                "college",
                "university",
                "kindergarten",
                "hospital",
                "clinic",
                "pharmacy",
                "doctors",
                "place_of_worship",
                "community_centre",
                "bank",
                "post_office",
                "police",
                "fire_station",
                "bus_station",
                "ferry_terminal",
                "parking",
                "marketplace",
                "theatre",
                "cinema",
                "arts_centre",
                "restaurant",
                "cafe",
                "bar",
                "hotel",
                "townhall",
                "courthouse",
                "embassy",
            ],

            "building": [
                "church",
                "mosque",
                "temple",
                "school",
                "university",
                "hospital",
                "commercial",
                "industrial",
                "retail",
                "office",
                "warehouse",
                "stadium",
                "hotel",
                "public",
            ],
        },

        match_mode=MATCH_ANY,

        description=(
            "General points of interest including selected land-use, "
            "industrial, office, shop, leisure, amenity and building "
            "features."
        ),
    ),


    # ------------------------------------------------------------------------
    # 2. BUS STOPS
    # ------------------------------------------------------------------------

    "bus_stops": OSMFeature(
        feature_id="bus_stops",
        name="Bus stops",
        category=CATEGORY_PUBLIC_TRANSPORT_PLACES,
        geometry="mixed",

        # NOTE:
        # These tag definitions are intentionally preserved exactly
        # from the current feature specification.
        #
        # `public_tra` and `railway: [" "]` will be clarified before
        # we implement the Overpass query generator.

        tags={
            "amenity": [
                "bus_station",
            ],

            "highway": [
                "bus_stop",
            ],

            "public_transport": [
                "platform",
                "station",
            ],

            "railway": [
                " ",
            ],
        },

        match_mode=MATCH_ANY,

        description=(
            "Bus stops, bus stations and public transport platforms "
            "associated with bus services."
        ),
    ),


    # ------------------------------------------------------------------------
    # 3. RAIL STOPS
    # ------------------------------------------------------------------------

    "rail_stops": OSMFeature(
        feature_id="rail_stops",
        name="Rail stops",
        category=CATEGORY_PUBLIC_TRANSPORT_PLACES,
        geometry="point",

        tags={
            "railway": [
                "halt",
                "platform",
                "station",
                "subway_entrance",
                "tram_stop",
            ],
        },

        match_mode=MATCH_ANY,

        description=(
            "Railway and rail-transit passenger stops, including "
            "halts, platforms, stations, subway entrances and tram stops."
        ),
    ),


    # ------------------------------------------------------------------------
    # 4. FERRY STOPS
    # ------------------------------------------------------------------------

    "ferry_stops": OSMFeature(
        feature_id="ferry_stops",
        name="Ferry stops",
        category=CATEGORY_PUBLIC_TRANSPORT_PLACES,
        geometry="point",

        tags={
            "amenity": [
                "ferry_terminal",
            ],
        },

        match_mode=MATCH_ANY,

        description=(
            "Ferry terminals and ferry passenger transport locations."
        ),
    ),


    # ------------------------------------------------------------------------
    # 5. ROADS
    # ------------------------------------------------------------------------

    "roads": OSMFeature(
        feature_id="roads",
        name="Roads",
        category=CATEGORY_LINEAR_FEATURES,
        geometry="line",

        tags={
            "highway": True,
        },

        match_mode=MATCH_ANY,

        description=(
            "Road and highway features mapped with the OSM "
            "highway tag."
        ),
    ),


    # ------------------------------------------------------------------------
    # 6. RAILWAYS
    # ------------------------------------------------------------------------

    "railways": OSMFeature(
        feature_id="railways",
        name="Railways",
        category=CATEGORY_LINEAR_FEATURES,
        geometry="line",

        tags={
            "railway": True,
        },

        match_mode=MATCH_ANY,

        description=(
            "Railway and rail-transit features mapped with the OSM "
            "railway tag."
        ),
    ),


    # ------------------------------------------------------------------------
    # 7. WATER LINES
    # ------------------------------------------------------------------------

    "water_lines": OSMFeature(
        feature_id="water_lines",
        name="Water lines",
        category=CATEGORY_LINEAR_FEATURES,
        geometry="line",

        tags={
            "waterway": True,
        },

        match_mode=MATCH_ANY,

        description=(
            "Linear water features including rivers, streams, canals, "
            "drains, ditches and other mapped waterways."
        ),
    ),


    # ------------------------------------------------------------------------
    # 8. WATER POLYGONS
    # ------------------------------------------------------------------------

    "water_polygons": OSMFeature(
        feature_id="water_polygons",
        name="Water polygons",
        category=CATEGORY_LINEAR_FEATURES,
        geometry="polygon",

        tags={
            "natural": [
                "water",
                "wetland",
                "bay",
                "coastline",
            ],

            "water": True,

            "landuse": [
                "reservoir",
                "basin",
            ],
        },

        match_mode=MATCH_ANY,

        description=(
            "Polygon water features including mapped water bodies, "
            "wetlands, bays, reservoirs and basins."
        ),
    ),


    # ------------------------------------------------------------------------
    # 9. BUILDINGS
    # ------------------------------------------------------------------------

    "buildings": OSMFeature(
        feature_id="buildings",
        name="Buildings",
        category=CATEGORY_LAND_BUILT_ENVIRONMENT,
        geometry="polygon",

        tags={
            "building": True,
            "slum": "yes",
            "informal": "yes",
        },

        # Match when ANY of the following is true:
        #
        #     building = any value
        #     OR slum = yes
        #     OR informal = yes

        match_mode=MATCH_ANY,

        description=(
            "Mapped building features, including buildings tagged as "
            "slum or informal."
        ),
    ),


    # ------------------------------------------------------------------------
    # 10. ADMINISTRATIVE BOUNDARIES
    # ------------------------------------------------------------------------

    "administrative_boundaries": OSMFeature(
        feature_id="administrative_boundaries",
        name="Administrative boundaries",
        category=CATEGORY_LAND_BUILT_ENVIRONMENT,
        geometry="polygon",

        tags={
            "boundary": "administrative",
        },

        match_mode=MATCH_ANY,

        description=(
            "Administrative boundaries mapped in OpenStreetMap."
        ),
    ),


    # ------------------------------------------------------------------------
    # 11. LANDUSE
    # ------------------------------------------------------------------------

    "landuse": OSMFeature(
        feature_id="landuse",
        name="Landuse",
        category=CATEGORY_LAND_BUILT_ENVIRONMENT,
        geometry="polygon",

        tags={
            "landuse": True,
            "slum": "yes",
            "informal": "yes",
        },

        # Match when ANY of the following is true:
        #
        #     landuse = any value
        #     OR slum = yes
        #     OR informal = yes

        match_mode=MATCH_ANY,

        description=(
            "Mapped land-use areas, including land-use features "
            "tagged as slum or informal."
        ),
    ),


    # ------------------------------------------------------------------------
    # 12. OPEN PUBLIC SPACES
    # ------------------------------------------------------------------------

    "open_public_spaces": OSMFeature(
        feature_id="open_public_spaces",
        name="Open public spaces",
        category=CATEGORY_LAND_BUILT_ENVIRONMENT,
        geometry="mixed",

        tags={
            "landuse": [
                "forest",
                "cemetery",
            ],

            "leisure": [
                "recreation_ground",
                "park",
                "dog_park",
                "playground",
            ],

            "natural": [
                "beach",
            ],

            "waterway": [
                "riverbank",
            ],
        },

        match_mode=MATCH_ANY,

        description=(
            "Open and recreational spaces including forests, cemeteries, "
            "recreation grounds, parks, dog parks, playgrounds, beaches "
            "and riverbanks."
        ),
    ),
}


# ============================================================================
# FEATURE DISPLAY ORDER
# ============================================================================
#
# This controls the order in which features are presented by the GUI
# and by other parts of the plugin.
#
# Keep this order aligned with the intended GUI order.
# ============================================================================

FEATURE_ORDER = [
    "poi",
    "bus_stops",
    "rail_stops",
    "ferry_stops",

    "roads",
    "railways",
    "water_lines",
    "water_polygons",

    "buildings",
    "administrative_boundaries",
    "landuse",
    "open_public_spaces",
]


# ============================================================================
# FEATURE ACCESS HELPERS
# ============================================================================
#
# These small helper functions provide a clean interface for other
# modules.
#
# Other modules should preferably use these functions instead of
# directly manipulating OSM_FEATURES.
# ============================================================================


def get_feature(feature_id: str) -> OSMFeature:
    """
    Return one OSM feature definition by its internal ID.

    Parameters
    ----------
    feature_id : str
        Internal feature identifier.

    Returns
    -------
    OSMFeature
        Requested feature definition.

    Raises
    ------
    KeyError
        If the feature ID does not exist.
    """

    return OSM_FEATURES[feature_id]


def get_all_features() -> List[OSMFeature]:
    """
    Return all OSM feature definitions in the configured display order.

    Returns
    -------
    list[OSMFeature]
        All supported OSM features.
    """

    return [
        OSM_FEATURES[feature_id]
        for feature_id in FEATURE_ORDER
    ]


def get_features_by_category(category: str) -> List[OSMFeature]:
    """
    Return all feature definitions belonging to a category.

    Parameters
    ----------
    category : str
        Category name.

    Returns
    -------
    list[OSMFeature]
        Features belonging to the requested category.
    """

    return [
        feature
        for feature in get_all_features()
        if feature.category == category
    ]


def get_feature_ids() -> List[str]:
    """
    Return all feature IDs in display order.

    Returns
    -------
    list[str]
        Ordered feature IDs.

    Notes
    -----
    A copy is returned so that callers cannot accidentally modify
    FEATURE_ORDER directly.
    """

    return FEATURE_ORDER.copy()


# ============================================================================
# MODULE TEST
# ============================================================================
#
# This block runs only when the module is executed directly.
#
# It does not run when the module is imported by the plugin.
#
# The test prints all feature definitions and their tags, allowing
# the developer to inspect the specification independently.
# ============================================================================

if __name__ == "__main__":

    print("=" * 70)
    print("OSM DATA TOOLKIT — OSM FEATURE DEFINITIONS")
    print("=" * 70)

    for feature in get_all_features():

        print()
        print(f"ID:          {feature.feature_id}")
        print(f"Name:        {feature.name}")
        print(f"Category:    {feature.category}")
        print(f"Geometry:    {feature.geometry}")
        print(f"Match mode:  {feature.match_mode}")
        print(f"Description: {feature.description}")
        print("Tags:")

        for key, value in feature.tags.items():
            print(f"    {key} = {value}")

    print()
    print("=" * 70)
    print(f"Total features: {len(OSM_FEATURES)}")
    print("=" * 70)