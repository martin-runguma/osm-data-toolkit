# OSM Data Toolkit — Website

This folder contains a five-page, responsive product website for the OSM Data Toolkit QGIS plugin. It uses HTML5, CSS3 and vanilla JavaScript; no framework, package manager, font CDN or build step is required.

## Website structure

```text
website/
├── index.html                 # Product overview
├── features.html              # AOI methods, supported categories and capabilities
├── workflow.html              # Download and processing workflow
├── installation.html          # Installation and first-download guide
├── documentation.html         # Technical reference and troubleshooting
├── assets/
│   ├── css/style.css
│   ├── js/site.js
│   └── images/                # Local SVG fallbacks for repository artwork
└── README-WEBSITE.md
```

The pages reuse the repository's existing illustrations and icon when the website is located in the repository as `website/`:

- `../docs/images/banner.svg`
- `../docs/images/workflow.svg`
- `../docs/images/categories.svg`
- `../docs/images/output.svg`
- `../docs/images/pipeline.svg`
- `../icon.png`

Those original files are referenced, not copied over or modified. Local SVG fallbacks are included inside `assets/images/` so the website still renders when previewed outside the full repository.

## Preview locally

1. Copy the `website/` folder into the root of the existing `osm-data-toolkit` repository.
2. From the repository root, start a local static server:

   ```bash
   python -m http.server 8000
   ```

3. Open `http://localhost:8000/website/` in a browser.

You can also open `website/index.html` directly. A local HTTP server is recommended because it behaves more like the deployed website. The bundled fallback artwork is used if the original repository images are not available.

## Integrate into the plugin repository

1. Download and extract this website archive.
2. Copy the `website/` directory into the root of `https://github.com/martin-runguma/osm-data-toolkit`.
3. Keep the existing plugin source, `README.md`, `LICENSE`, `docs/`, `icon.png` and other repository files unchanged.
4. Commit and push the new `website/` directory.

The pages link to the original root-level `docs/images/` illustrations and `icon.png` when served from `/website/`. The local fallbacks keep the website usable if those files are not present.

## Enable GitHub Pages

GitHub Pages' branch-folder publishing options do not directly publish an arbitrary nested `website/` folder as the site root. This archive therefore includes `github-pages.yml.example` beside the `website/` directory. After copying `website/` into the repository:

1. Copy `github-pages.yml.example` to `.github/workflows/pages.yml` in the repository (create the `.github/workflows/` folders if needed).
2. Open the repository on GitHub and go to **Settings → Pages**.
3. Under **Build and deployment**, choose **GitHub Actions** as the source.
4. Push the workflow and website files to the `main` branch. The workflow publishes the website files at the Pages site root and also copies the existing repository illustrations and plugin icon into the published artifact.
5. Once the workflow completes, use the Pages URL shown in **Settings → Pages**.

The workflow only reads `website/`, `docs/images/` and `icon.png` to assemble the published static site. It does not alter the plugin code or source documentation.

## Update the website

- Treat the repository `README.md`, plugin source and official QGIS Plugin Repository metadata as the authoritative sources for product behaviour and compatibility.
- Update the matching page when AOI methods, category rules, endpoint behaviour, output fields, formats or supported QGIS versions change.
- Keep the common navigation, footer, colours, spacing and typography consistent across all five pages.
- Add new local assets under `website/assets/`; continue to prefer existing repository artwork when it is available.
- Check internal page links, section anchors, image fallbacks and the mobile navigation before publishing.

## Content and attribution notes

- Plugin licence: **GNU General Public License, version 3**. The repository's root `LICENSE` remains authoritative; this website does not replace it.
- OpenStreetMap data: **© OpenStreetMap contributors**, available under the **Open Database Licence (ODbL)**. Credit OpenStreetMap contributors when publishing maps or data made with the plugin.
- OSM Data Toolkit is an independent community project and is not endorsed by or affiliated with the OpenStreetMap Foundation.

## Technical notes

- Static HTML pages: `index.html`, `features.html`, `workflow.html`, `installation.html` and `documentation.html`.
- Shared stylesheet: `assets/css/style.css`.
- Shared script: `assets/js/site.js` (responsive navigation, active-page state, year and image fallbacks).
- No third-party runtime dependencies are required.
