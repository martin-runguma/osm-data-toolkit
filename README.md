# OSM Data Toolkit

<img src="OSM_Data_Toolkit/icon.png" alt="OSM Data Toolkit icon" width="96" align="right">

A QGIS plugin that downloads OpenStreetMap data for an area of interest from the Overpass API and turns it into organised, ready-to-use layers, without leaving QGIS.

- Works with QGIS 3.28+ (Qt5) and QGIS 4 (Qt6)
- Exports to **GeoPackage** or **Shapefile**
- Free and open source

## Features

- **Choose your area** by drawing a rectangle on the map, using the current map extent, the bounding box of selected features, or a layer's extent
- **Pick the OSM categories** you need:
  - Points of interest, bus stops, rail stops, ferry stops
  - Roads, railways, waterways
  - Buildings, administrative boundaries, landuse, open public spaces
- **Separate point, line and polygon layers** for each category
- **Administrative boundaries** can also be split by `admin_level`
- **Local cache** so repeat downloads of the same query are quick
- **Auto-load** results into your QGIS project
- **Processing log** with progress for large downloads

## Installation

### From the QGIS Plugin Manager (once published)

1. In QGIS, open **Plugins → Manage and Install Plugins…**
2. Search for **OSM Data Toolkit** and click **Install Plugin**.

### Manual installation

1. Download this repository as a ZIP, or the plugin ZIP from the [Releases](https://github.com/martin-runguma/osm-data-toolkit/releases) page.
2. In QGIS, open **Plugins → Manage and Install Plugins… → Install from ZIP** and select the file.

## Usage

1. Open the plugin from the **Plugins** menu or the toolbar icon.
2. **Define the area of interest.** Keep it focused; very large areas are slow.
3. **Tick the feature categories** you need.
4. **Choose the output format and folder**, then click **Download OSM Data**.
5. When it finishes, the layers are written to your output location and (optionally) added to the project.

## Tips and troubleshooting

**Use GeoPackage for large areas.** A Shapefile's attribute table is limited to about 65 KB per row and 254 characters per text field. Large areas contain hundreds of different OSM tags, so for Shapefile output the plugin sizes columns to their data and, if still too wide, leaves out the rarest tag columns (the log lists them). GeoPackage keeps every tag.

**"Unclassified OSM elements not written to feature layers".** This line in the log is informational. The Overpass response includes the untagged vertices that make up lines and polygons. They don't belong to any selected category and their coordinates are already part of the way geometry, so they are not written as separate features.

**Download fails or times out.** The public Overpass servers are shared and can reject or throttle very large queries. Try a smaller area, fewer categories, or try again later.

**Tags that differ only by letter case** (for example `fixme` and `FIXME`) are exported as separate columns, with a numeric suffix on the later ones (`FIXME_2`), because GeoPackage and Shapefile field names are case-insensitive.

## Reporting problems

Please open an [issue](https://github.com/martin-runguma/osm-data-toolkit/issues) and include your QGIS version, the output format, the approximate area size, and the text of any error message from the Processing Log.

## Data and attribution

Map data © [OpenStreetMap](https://www.openstreetmap.org/copyright) contributors, available under the [Open Database Licence (ODbL)](https://opendatacommons.org/licenses/odbl/). If you publish maps or data made with this plugin, please credit OpenStreetMap contributors.

## Author

Martin Runguma

## License

See the [LICENSE](LICENSE) file.
