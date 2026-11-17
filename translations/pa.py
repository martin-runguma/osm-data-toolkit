"""Punjabi (ਪੰਜਾਬੀ) translation pack for the OSM Data Toolkit plugin.
Keys remain the English source strings; preserve placeholders and HTML."""
TEXT = {
 '\n<h3>Quick start</h3>\n<ol>\n  <li><b>Choose an area.</b> Use the current map extent, draw a rectangle\n      on the map, or use the bounding box of selected features or a\n      layer\'s extent.</li>\n  <li><b>Tick the OSM categories</b> you need (POI, stops, roads,\n      buildings, boundaries, landuse, ...).</li>\n  <li><b>Choose an output format and folder</b>, then click\n      <b>Download OSM Data</b>.</li>\n</ol>\n\n<h3>Good to know</h3>\n<ul>\n  <li><b>GeoPackage is recommended.</b> A Shapefile cannot hold very many\n      attribute columns, so on large areas some rarely used tag columns\n      may be left out (the log tells you when this happens).</li>\n  <li><b>Keep the area focused.</b> Very large areas produce huge Overpass\n      responses and can be slow or rejected by the public servers.</li>\n  <li><b>The cache</b> lets repeat downloads of the same query reuse\n      earlier results.</li>\n  <li><b>"Unclassified OSM elements"</b> in the log is informational: they\n      are mostly untagged vertices of lines and polygons that do not belong\n      to any selected category.</li>\n</ul>\n\n<p>Data &copy; OpenStreetMap contributors, available under the\n<a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a>.</p>\n<p><i>This plugin is not endorsed by or affiliated with the\nOpenStreetMap Foundation.</i></p>\n':
 '\n<h3>ਤੇਜ਼ ਸ਼ੁਰੂਆਤ</h3>\n<ol>\n  <li><b>ਇੱਕ ਖੇਤਰ ਚੁਣੋ।</b> ਮੌਜੂਦਾ ਨਕਸ਼ਾ ਸੀਮਾ ਵਰਤੋ, ਨਕਸ਼ੇ \'ਤੇ ਇੱਕ\n      ਆਇਤ ਖਿੱਚੋ, ਜਾਂ ਚੁਣੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਜਾਂ ਲੇਅਰ ਦੀ ਸੀਮਾ ਦੀ\n      ਬਾਊਂਡਿੰਗ ਬਾਕਸ ਵਰਤੋ।</li>\n  <li><b>ਲੋੜੀਂਦੀਆਂ OSM ਸ਼੍ਰੇਣੀਆਂ ਟਿੱਕ ਕਰੋ</b> (POI, ਸਟਾਪ, ਸੜਕਾਂ,\n      ਇਮਾਰਤਾਂ, ਸੀਮਾਵਾਂ, ਜ਼ਮੀਨ ਵਰਤੋਂ, ...)।</li>\n  <li><b>ਆਉਟਪੁੱਟ ਫਾਰਮੈਟ ਅਤੇ ਫੋਲਡਰ ਚੁਣੋ</b>, ਫਿਰ\n      <b>OSM ਡੇਟਾ ਡਾਊਨਲੋਡ ਕਰੋ</b> \'ਤੇ ਕਲਿੱਕ ਕਰੋ।</li>\n</ol>\n\n<h3>ਜਾਣਨਯੋਗ</h3>\n<ul>\n  <li><b>GeoPackage ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।</b> Shapefile ਬਹੁਤ ਸਾਰੇ\n      ਗੁਣ ਕਾਲਮ ਨਹੀਂ ਰੱਖ ਸਕਦਾ, ਇਸ ਲਈ ਵੱਡੇ ਖੇਤਰਾਂ \'ਤੇ ਕੁਝ ਘੱਟ ਵਰਤੇ ਜਾਣ\n      ਵਾਲੇ ਟੈਗ ਕਾਲਮ ਛੱਡ ਦਿੱਤੇ ਜਾ ਸਕਦੇ ਹਨ (ਲੌਗ ਤੁਹਾਨੂੰ ਦੱਸਦਾ ਹੈ ਜਦੋਂ\n      ਅਜਿਹਾ ਹੁੰਦਾ ਹੈ)।</li>\n  <li><b>ਖੇਤਰ ਨੂੰ ਕੇਂਦ੍ਰਿਤ ਰੱਖੋ।</b> ਬਹੁਤ ਵੱਡੇ ਖੇਤਰ ਬਹੁਤ ਜ਼ਿਆਦਾ Overpass\n      ਜਵਾਬ ਪੈਦਾ ਕਰਦੇ ਹਨ ਅਤੇ ਹੌਲੀ ਹੋ ਸਕਦੇ ਹਨ ਜਾਂ ਜਨਤਕ ਸਰਵਰਾਂ ਦੁਆਰਾ\n      ਰੱਦ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ।</li>\n  <li><b>ਕੈਸ਼</b> ਇੱਕੋ ਕਵੈਰੀ ਦੇ ਦੁਹਰਾਏ ਡਾਊਨਲੋਡ ਨੂੰ ਪਹਿਲਾਂ ਦੇ\n      ਨਤੀਜਿਆਂ ਦੀ ਮੁੜ ਵਰਤੋਂ ਕਰਨ ਦਿੰਦਾ ਹੈ।</li>\n  <li>ਲੌਗ ਵਿੱਚ <b>"ਅਵਰਗੀਕ੍ਰਿਤ OSM ਤੱਤ"</b> ਜਾਣਕਾਰੀ ਭਰਪੂਰ ਹੈ: ਇਹ\n      ਮੁੱਖ ਤੌਰ \'ਤੇ ਲਾਈਨਾਂ ਅਤੇ ਬਹੁਭੁਜਾਂ ਦੇ ਟੈਗ ਰਹਿਤ ਸਿਰੇ ਹੁੰਦੇ ਹਨ ਜੋ\n      ਕਿਸੇ ਚੁਣੀ ਸ਼੍ਰੇਣੀ ਨਾਲ ਸੰਬੰਧਿਤ ਨਹੀਂ ਹੁੰਦੇ।</li>\n</ul>\n\n<p>ਡੇਟਾ &copy; OpenStreetMap ਯੋਗਦਾਨੀ, <a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a> ਅਧੀਨ ਉਪਲਬਧ।</p>\n<p><i>ਇਹ ਪਲੱਗਇਨ OpenStreetMap Foundation ਦੁਆਰਾ ਸਮਰਥਿਤ ਜਾਂ ਸੰਬੰਧਿਤ ਨਹੀਂ ਹੈ।</i></p>\n',
 ' responded successfully.': ' ਨੇ ਸਫਲਤਾਪੂਰਵਕ ਜਵਾਬ ਦਿੱਤਾ।',
 ' seconds...': ' ਸਕਿੰਟ…',
 '" style="color:#0B5E8E; text-decoration:none;">OpenStreetMap contributors</a> (ODbL)':
   '" style="color:#0B5E8E; text-decoration:none;">OpenStreetMap ਯੋਗਦਾਨੀ</a> (ODbL)',
 ', east=': ', ਪੂਰਬ=',
 ', north=': ', ਉੱਤਰ=',
 ', west=': ', ਪੱਛਮ=',
 '0 selected': '0 ਚੁਣੇ',
 '<p>Plugin version': '<p>ਪਲੱਗਇਨ ਸੰਸਕਰਣ',
 'A download is already running.': 'ਇੱਕ ਡਾਊਨਲੋਡ ਪਹਿਲਾਂ ਹੀ ਚੱਲ ਰਿਹਾ ਹੈ।',
 'A labelled column of feature checkboxes.':
   'ਵਿਸ਼ੇਸ਼ਤਾ ਚੈੱਕਬਾਕਸਾਂ ਦਾ ਲੇਬਲ ਕੀਤਾ ਕਾਲਮ।',
 'AOI drawing cancelled.': 'AOI ਖਿੱਚਣਾ ਰੱਦ ਕੀਤਾ।',
 'AOI geometry is empty.': 'AOI ਜਿਓਮੈਟਰੀ ਖਾਲੀ ਹੈ।',
 'AOI geometry is missing.': 'AOI ਜਿਓਮੈਟਰੀ ਗੁੰਮ ਹੈ।',
 'AOI name': 'AOI ਨਾਮ',
 'AOI rectangle captured successfully.':
   'AOI ਆਇਤ ਸਫਲਤਾਪੂਰਵਕ ਕੈਪਚਰ ਕੀਤੀ ਗਈ।',
 'AOI source CRS is invalid.': 'AOI ਸਰੋਤ CRS ਅਵੈਧ ਹੈ।',
 'AOI validation failed:': 'AOI ਪ੍ਰਮਾਣਿਕਤਾ ਅਸਫਲ:',
 'AOI:': 'AOI:',
 'AOI: QGIS interface is not available.':
   'AOI: QGIS ਇੰਟਰਫੇਸ ਉਪਲਬਧ ਨਹੀਂ ਹੈ।',
 "AOI: click 'Draw AOI', then drag a rectangle on the QGIS map.":
   'AOI: "AOI ਖਿੱਚੋ" \'ਤੇ ਕਲਿੱਕ ਕਰੋ, ਫਿਰ QGIS ਨਕਸ਼ੇ \'ਤੇ ਆਇਤ ਖਿੱਚੋ।',
 "AOI: click 'Use Layer Extent' to use the full extent of the active QGIS layer.":
   'AOI: ਸਰਗਰਮ QGIS ਲੇਅਰ ਦੀ ਪੂਰੀ ਸੀਮਾ ਵਰਤਣ ਲਈ "ਲੇਅਰ ਸੀਮਾ ਵਰਤੋ" \'ਤੇ ਕਲਿੱਕ ਕਰੋ।',
 'AOI: click and drag on the QGIS map.':
   'AOI: QGIS ਨਕਸ਼ੇ \'ਤੇ ਕਲਿੱਕ ਕਰੋ ਅਤੇ ਖਿੱਚੋ।',
 'AOI: failed to resolve active layer extent':
   'AOI: ਸਰਗਰਮ ਲੇਅਰ ਸੀਮਾ ਨਿਰਧਾਰਿਤ ਨਹੀਂ ਕੀਤੀ ਜਾ ਸਕੀ',
 'AOI: failed to resolve selected features':
   'AOI: ਚੁਣੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਨਿਰਧਾਰਿਤ ਨਹੀਂ ਕੀਤੀਆਂ ਜਾ ਸਕੀਆਂ',
 'AOI: invalid': 'AOI: ਅਵੈਧ',
 'AOI: no active QGIS layer.': 'AOI: ਕੋਈ ਸਰਗਰਮ QGIS ਲੇਅਰ ਨਹੀਂ।',
 'AOI: no feature(s) selected in the active layer.':
   'AOI: ਸਰਗਰਮ ਲੇਅਰ ਵਿੱਚ ਕੋਈ ਵਿਸ਼ੇਸ਼ਤਾ ਚੁਣੀ ਨਹੀਂ ਗਈ।',
 'AOI: not yet resolved': 'AOI: ਅਜੇ ਨਿਰਧਾਰਿਤ ਨਹੀਂ',
 "AOI: select feature(s) in the active QGIS layer, then click 'Use Selected Features'.":
   'AOI: ਸਰਗਰਮ QGIS ਲੇਅਰ ਵਿੱਚ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਚੁਣੋ, ਫਿਰ "ਚੁਣੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਵਰਤੋ" \'ਤੇ ਕਲਿੱਕ ਕਰੋ।',
 'AOI: the active layer is not a vector layer.':
   'AOI: ਸਰਗਰਮ ਲੇਅਰ ਵੈਕਟਰ ਲੇਅਰ ਨਹੀਂ ਹੈ।',
 'AOI: unable to create': 'AOI: ਬਣਾਉਣ ਵਿੱਚ ਅਸਮਰੱਥ',
 'AOI: unable to resolve': 'AOI: ਨਿਰਧਾਰਿਤ ਕਰਨ ਵਿੱਚ ਅਸਮਰੱਥ',
 'Activate the interactive rectangle AOI map tool.':
   'ਇੰਟਰਐਕਟਿਵ ਆਇਤ AOI ਨਕਸ਼ਾ ਸਾਧਨ ਸਰਗਰਮ ਕਰੋ।',
 'Active layer extent': 'ਸਰਗਰਮ ਲੇਅਰ ਸੀਮਾ',
 'Active-layer extent AOI is invalid.':
   'ਸਰਗਰਮ ਲੇਅਰ ਸੀਮਾ AOI ਅਵੈਧ ਹੈ।',
 'Active-layer extent captured successfully.':
   'ਸਰਗਰਮ ਲੇਅਰ ਸੀਮਾ ਸਫਲਤਾਪੂਰਵਕ ਕੈਪਚਰ ਕੀਤੀ ਗਈ।',
 'Active-layer extent validation failed:':
   'ਸਰਗਰਮ ਲੇਅਰ ਸੀਮਾ ਪ੍ਰਮਾਣਿਕਤਾ ਅਸਫਲ:',
 'Administrative boundaries': 'ਪ੍ਰਸ਼ਾਸਕੀ ਸੀਮਾਵਾਂ',
 'Administrative boundary filter: all levels (no admin_level filter).':
   'ਪ੍ਰਸ਼ਾਸਕੀ ਸੀਮਾ ਫਿਲਟਰ: ਸਾਰੇ ਪੱਧਰ (ਕੋਈ admin_level ਫਿਲਟਰ ਨਹੀਂ)।',
 'Administrative boundary levels': 'ਪ੍ਰਸ਼ਾਸਕੀ ਸੀਮਾ ਪੱਧਰ',
 'Administrative boundary levels:': 'ਪ੍ਰਸ਼ਾਸਕੀ ਸੀਮਾ ਪੱਧਰ:',
 'Administrative levels must be an integer, a numeric string, a sequence of levels, or None.':
   'ਪ੍ਰਸ਼ਾਸਕੀ ਪੱਧਰ ਇੱਕ ਪੂਰਨ ਅੰਕ, ਸੰਖਿਆਤਮਕ ਸਤਰ, ਪੱਧਰਾਂ ਦਾ ਕ੍ਰਮ ਜਾਂ None ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।',
 'All OSM feature categories cleared.': 'ਸਾਰੀਆਂ OSM ਵਿਸ਼ੇਸ਼ਤਾ ਸ਼੍ਰੇਣੀਆਂ ਸਾਫ਼ ਕੀਤੀਆਂ।',
 'All OSM feature categories selected.': 'ਸਾਰੀਆਂ OSM ਵਿਸ਼ੇਸ਼ਤਾ ਸ਼੍ਰੇਣੀਆਂ ਚੁਣੀਆਂ।',
 'All Overpass server URLs must be non-empty strings.':
   'ਸਾਰੇ Overpass ਸਰਵਰ URL ਖਾਲੀ ਨਾ ਹੋਣ ਵਾਲੀਆਂ ਸਤਰਾਂ ਹੋਣੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ।',
 'All Overpass servers and retry attempts failed.':
   'ਸਾਰੇ Overpass ਸਰਵਰ ਅਤੇ ਮੁੜ-ਕੋਸ਼ਿਸ਼ਾਂ ਅਸਫਲ।',
 'All administrative levels will be included.':
   'ਸਾਰੇ ਪ੍ਰਸ਼ਾਸਕੀ ਪੱਧਰ ਸ਼ਾਮਲ ਕੀਤੇ ਜਾਣਗੇ।',
 'All administrative levels will be included; no admin_level filter will be added to the query.':
   'ਸਾਰੇ ਪ੍ਰਸ਼ਾਸਕੀ ਪੱਧਰ ਸ਼ਾਮਲ ਕੀਤੇ ਜਾਣਗੇ; ਕਵੈਰੀ ਵਿੱਚ ਕੋਈ admin_level ਫਿਲਟਰ ਨਹੀਂ ਜੋੜਿਆ ਜਾਵੇਗਾ।',
 'All attempts failed for server ': 'ਸਰਵਰ ਲਈ ਸਾਰੀਆਂ ਕੋਸ਼ਿਸ਼ਾਂ ਅਸਫਲ: ',
 'All levels (0–15; no admin_level filter)':
   'ਸਾਰੇ ਪੱਧਰ (0–15; ਕੋਈ admin_level ਫਿਲਟਰ ਨਹੀਂ)',
 'An existing output directory is required for Shapefile export.':
   'Shapefile ਨਿਰਯਾਤ ਲਈ ਮੌਜੂਦਾ ਆਉਟਪੁੱਟ ਫੋਲਡਰ ਲੋੜੀਂਦਾ ਹੈ।',
 'An output GeoPackage path is required.':
   'ਆਉਟਪੁੱਟ GeoPackage ਪਾਥ ਲੋੜੀਂਦਾ ਹੈ।',
 'An output name is required for Shapefile export.':
   'Shapefile ਨਿਰਯਾਤ ਲਈ ਆਉਟਪੁੱਟ ਨਾਮ ਲੋੜੀਂਦਾ ਹੈ।',
 'Append a timestamped message to the processing log.':
   'ਪ੍ਰੋਸੈਸਿੰਗ ਲੌਗ ਵਿੱਚ ਸਮਾਂ-ਛਾਪ ਵਾਲਾ ਸੁਨੇਹਾ ਸ਼ਾਮਲ ਕਰੋ।',
 'Append an exported feature count to the processing log.':
   'ਪ੍ਰੋਸੈਸਿੰਗ ਲੌਗ ਵਿੱਚ ਨਿਰਯਾਤ ਕੀਤੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦੀ ਗਿਣਤੀ ਸ਼ਾਮਲ ਕਰੋ।',
 'Area of Interest': 'ਦਿਲਚਸਪੀ ਦਾ ਖੇਤਰ',
 'At least one OSM feature must be selected.':
   'ਘੱਟੋ-ਘੱਟ ਇੱਕ OSM ਵਿਸ਼ੇਸ਼ਤਾ ਚੁਣੀ ਜਾਣੀ ਚਾਹੀਦੀ ਹੈ।',
 'At least one OSM feature must be supplied.':
   'ਘੱਟੋ-ਘੱਟ ਇੱਕ OSM ਵਿਸ਼ੇਸ਼ਤਾ ਪ੍ਰਦਾਨ ਕੀਤੀ ਜਾਣੀ ਚਾਹੀਦੀ ਹੈ।',
 'At least one Overpass server must be provided.':
   'ਘੱਟੋ-ਘੱਟ ਇੱਕ Overpass ਸਰਵਰ ਪ੍ਰਦਾਨ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ।',
 'Attempt details:': 'ਕੋਸ਼ਿਸ਼ ਵੇਰਵੇ:',
 'Automatically add downloaded layers to QGIS':
   'ਡਾਊਨਲੋਡ ਕੀਤੀਆਂ ਲੇਅਰਾਂ ਆਪਣੇ-ਆਪ QGIS ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ',
 'Background Overpass download started.':
   'ਬੈਕਗ੍ਰਾਊਂਡ Overpass ਡਾਊਨਲੋਡ ਸ਼ੁਰੂ ਹੋਇਆ।',
 'Browse': 'ਬ੍ਰਾਊਜ਼ ਕਰੋ',
 'Browse…': 'ਬ੍ਰਾਊਜ਼ ਕਰੋ…',
 'Buildings': 'ਇਮਾਰਤਾਂ',
 'Bus stops': 'ਬੱਸ ਸਟਾਪ',
 'CRS:': 'CRS:',
 'Cache hit:': 'ਕੈਸ਼ ਹਿੱਟ:',
 'Cache hit: using saved Overpass response ({age} day(s) old).':
   'ਕੈਸ਼ ਹਿੱਟ: ਸੰਭਾਲਿਆ Overpass ਜਵਾਬ ਵਰਤ ਰਿਹਾ ਹੈ ({age} ਦਿਨ ਪੁਰਾਣਾ)।',
 'Cache miss:': 'ਕੈਸ਼ ਮਿਸ:',
 'Cache miss: could not read saved response ({error}).':
   'ਕੈਸ਼ ਮਿਸ: ਸੰਭਾਲਿਆ ਜਵਾਬ ਪੜ੍ਹਿਆ ਨਹੀਂ ਜਾ ਸਕਿਆ ({error})।',
 'Cache miss: query hash does not match the saved response.':
   'ਕੈਸ਼ ਮਿਸ: ਕਵੈਰੀ ਹੈਸ਼ ਸੰਭਾਲੇ ਜਵਾਬ ਨਾਲ ਮੇਲ ਨਹੀਂ ਖਾਂਦਾ।',
 'Cache miss: saved response is incomplete or invalid.':
   'ਕੈਸ਼ ਮਿਸ: ਸੰਭਾਲਿਆ ਜਵਾਬ ਅਧੂਰਾ ਜਾਂ ਅਵੈਧ ਹੈ।',
 'Cache miss: saved response is older than {days} days.':
   'ਕੈਸ਼ ਮਿਸ: ਸੰਭਾਲਿਆ ਜਵਾਬ {days} ਦਿਨਾਂ ਤੋਂ ਪੁਰਾਣਾ ਹੈ।',
 'Cache miss: saved response uses an unsupported cache format.':
   'ਕੈਸ਼ ਮਿਸ: ਸੰਭਾਲਿਆ ਜਵਾਬ ਗੈਰ-ਸਮਰਥਿਤ ਕੈਸ਼ ਫਾਰਮੈਟ ਵਰਤਦਾ ਹੈ।',
 'Cached Overpass response:': 'ਕੈਸ਼ ਕੀਤਾ Overpass ਜਵਾਬ:',
 'Cancel': 'ਰੱਦ ਕਰੋ',
 'Cancellation has already been requested.': 'ਰੱਦ ਕਰਨ ਦੀ ਬੇਨਤੀ ਪਹਿਲਾਂ ਹੀ ਕੀਤੀ ਜਾ ਚੁੱਕੀ ਹੈ।',
 'Cancellation requested': 'ਰੱਦ ਕਰਨ ਦੀ ਬੇਨਤੀ ਕੀਤੀ',
 'Cancellation requested. If an HTTP request is already active, the downloader will stop when that request returns or times out.':
   'ਰੱਦ ਕਰਨ ਦੀ ਬੇਨਤੀ ਕੀਤੀ। ਜੇ HTTP ਬੇਨਤੀ ਪਹਿਲਾਂ ਹੀ ਸਰਗਰਮ ਹੈ, ਤਾਂ ਡਾਊਨਲੋਡਰ ਉਸ ਬੇਨਤੀ ਦੇ ਵਾਪਸ ਆਉਣ ਜਾਂ ਸਮਾਂ-ਸੀਮਾ ਖਤਮ ਹੋਣ \'ਤੇ ਰੁਕ ਜਾਵੇਗਾ।',
 'Cancellation requested; waiting for the current request to finish...':
   'ਰੱਦ ਕਰਨ ਦੀ ਬੇਨਤੀ ਕੀਤੀ; ਮੌਜੂਦਾ ਬੇਨਤੀ ਪੂਰੀ ਹੋਣ ਦੀ ਉਡੀਕ…',
 'Cannot draw AOI because the QGIS interface is unavailable.':
   'AOI ਨਹੀਂ ਖਿੱਚ ਸਕਦੇ ਕਿਉਂਕਿ QGIS ਇੰਟਰਫੇਸ ਉਪਲਬਧ ਨਹੀਂ ਹੈ।',
 'Cannot resolve active-layer extent because QGIS is unavailable.':
   'ਸਰਗਰਮ ਲੇਅਰ ਸੀਮਾ ਨਿਰਧਾਰਿਤ ਨਹੀਂ ਕਰ ਸਕਦੇ ਕਿਉਂਕਿ QGIS ਉਪਲਬਧ ਨਹੀਂ ਹੈ।',
 'Cannot resolve current map extent because QGIS is unavailable.':
   'ਮੌਜੂਦਾ ਨਕਸ਼ਾ ਸੀਮਾ ਨਿਰਧਾਰਿਤ ਨਹੀਂ ਕਰ ਸਕਦੇ ਕਿਉਂਕਿ QGIS ਉਪਲਬਧ ਨਹੀਂ ਹੈ।',
 'Cannot resolve selected-feature AOI because QGIS is unavailable.':
   'ਚੁਣੀਆਂ-ਵਿਸ਼ੇਸ਼ਤਾ AOI ਨਿਰਧਾਰਿਤ ਨਹੀਂ ਕਰ ਸਕਦੇ ਕਿਉਂਕਿ QGIS ਉਪਲਬਧ ਨਹੀਂ ਹੈ।',
 'Cannot transform an empty geometry.':
   'ਖਾਲੀ ਜਿਓਮੈਟਰੀ ਨੂੰ ਬਦਲਿਆ ਨਹੀਂ ਜਾ ਸਕਦਾ।',
 'Capture the current QGIS map canvas extent.':
   'ਮੌਜੂਦਾ QGIS ਨਕਸ਼ਾ ਕੈਨਵਸ ਸੀਮਾ ਕੈਪਚਰ ਕਰੋ।',
 'Choose all available levels, or select one or more levels to download (for example, 5–8 or level 5).':
   'ਸਾਰੇ ਉਪਲਬਧ ਪੱਧਰ ਚੁਣੋ, ਜਾਂ ਡਾਊਨਲੋਡ ਕਰਨ ਲਈ ਇੱਕ ਜਾਂ ਵੱਧ ਪੱਧਰ ਚੁਣੋ (ਜਿਵੇਂ 5–8 ਜਾਂ ਪੱਧਰ 5)।',
 'Choose an output directory before downloading.':
   'ਡਾਊਨਲੋਡ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਆਉਟਪੁੱਟ ਡਾਇਰੈਕਟਰੀ ਚੁਣੋ।',
 'City name': 'ਸ਼ਹਿਰ ਦਾ ਨਾਮ',
 'Classifying OSM elements and preparing GeoPackage layers.':
   'OSM ਤੱਤਾਂ ਦਾ ਵਰਗੀਕਰਨ ਅਤੇ GeoPackage ਲੇਅਰਾਂ ਤਿਆਰ ਕੀਤੀਆਂ ਜਾ ਰਹੀਆਂ ਹਨ।',
 'Classifying OSM elements and preparing Shapefile outputs.':
   'OSM ਤੱਤਾਂ ਦਾ ਵਰਗੀਕਰਨ ਅਤੇ Shapefile ਆਉਟਪੁੱਟ ਤਿਆਰ ਕੀਤੇ ਜਾ ਰਹੇ ਹਨ।',
 'Clear all': 'ਸਭ ਸਾਫ਼ ਕਰੋ',
 'Clear log': 'ਲੌਗ ਸਾਫ਼ ਕਰੋ',
 'Clear only the visible log, without changing processing settings.':
   'ਸਿਰਫ਼ ਦਿਖਣ ਵਾਲਾ ਲੌਗ ਸਾਫ਼ ਕਰੋ, ਪ੍ਰੋਸੈਸਿੰਗ ਸੈਟਿੰਗਾਂ ਬਦਲੇ ਬਿਨਾਂ।',
 'Clear selected levels so the user can make a narrower selection.':
   'ਚੁਣੇ ਪੱਧਰ ਸਾਫ਼ ਕਰੋ ਤਾਂ ਜੋ ਵਰਤੋਂਕਾਰ ਸੌਖੀ ਚੋਣ ਕਰ ਸਕੇ।',
 'Clear the messages currently shown in the Processing Log.':
   'ਪ੍ਰੋਸੈਸਿੰਗ ਲੌਗ ਵਿੱਚ ਇਸ ਵੇਲੇ ਦਿਖ ਰਹੇ ਸੁਨੇਹੇ ਸਾਫ਼ ਕਰੋ।',
 'Clear the previous AOI and display guidance for the chosen method.':
   'ਪਿਛਲੀ AOI ਸਾਫ਼ ਕਰੋ ਅਤੇ ਚੁਣੀ ਵਿਧੀ ਲਈ ਮਾਰਗਦਰਸ਼ਨ ਦਿਖਾਓ।',
 'Close': 'ਬੰਦ ਕਰੋ',
 'Collect optional filename components before exporting OSM data.':
   'OSM ਡੇਟਾ ਨਿਰਯਾਤ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਲੋੜੀਂਦੇ ਫਾਈਲਨਾਮ ਹਿੱਸੇ ਇਕੱਠੇ ਕਰੋ।',
 'Compact product header above the scrollable workflow.':
   'ਸਕ੍ਰੋਲ ਕਰਨ ਯੋਗ ਵਰਕਫਲੋ ਉੱਤੇ ਸੰਖੇਪ ਉਤਪਾਦ ਹੈਡਰ।',
 'Connection error on server ': 'ਸਰਵਰ \'ਤੇ ਕਨੈਕਸ਼ਨ ਗਲਤੀ: ',
 'Continue to Download': 'ਡਾਊਨਲੋਡ \'ਤੇ ਜਾਰੀ ਰੱਖੋ',
 'Convert a name component into a Windows-safe filename token.':
   'ਨਾਮ ਹਿੱਸੇ ਨੂੰ Windows-ਸੁਰੱਖਿਅਤ ਫਾਈਲਨਾਮ ਟੋਕਨ ਵਿੱਚ ਬਦਲੋ।',
 'Convert the drawn rectangle into the standard AOI object.':
   'ਖਿੱਚੀ ਆਇਤ ਨੂੰ ਮਿਆਰੀ AOI ਆਬਜੈਕਟ ਵਿੱਚ ਬਦਲੋ।',
 'Converting OSM response to GeoPackage...':
   'OSM ਜਵਾਬ ਨੂੰ GeoPackage ਵਿੱਚ ਬਦਲ ਰਿਹਾ ਹੈ…',
 'Converting OSM response to Shapefiles...':
   'OSM ਜਵਾਬ ਨੂੰ Shapefiles ਵਿੱਚ ਬਦਲ ਰਿਹਾ ਹੈ…',
 'Could not combine the selected feature geometries.':
   'ਚੁਣੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾ ਜਿਓਮੈਟਰੀਆਂ ਨੂੰ ਜੋੜਿਆ ਨਹੀਂ ਜਾ ਸਕਿਆ।',
 "Could not create Shapefile staging layer '{layer_name}'.":
   'Shapefile ਸਟੇਜਿੰਗ ਲੇਅਰ "{layer_name}" ਨਹੀਂ ਬਣਾ ਸਕੇ।',
 'Could not create an empty bus_stops_points layer.':
   'ਖਾਲੀ bus_stops_points ਲੇਅਰ ਨਹੀਂ ਬਣਾ ਸਕੇ।',
 "Could not create temporary QGIS layer '{layer_name}'.":
   'ਅਸਥਾਈ QGIS ਲੇਅਰ "{layer_name}" ਨਹੀਂ ਬਣਾ ਸਕੇ।',
 'Could not create temporary layer for admin_level {admin_level}.':
   'admin_level {admin_level} ਲਈ ਅਸਥਾਈ ਲੇਅਰ ਨਹੀਂ ਬਣਾ ਸਕੇ।',
 'Could not create the merged bus_stops_points layer.':
   'ਮਿਲਾਈ bus_stops_points ਲੇਅਰ ਨਹੀਂ ਬਣਾ ਸਕੇ।',
 'Could not delete temporary file': 'ਅਸਥਾਈ ਫਾਈਲ ਨਹੀਂ ਮਿਟਾ ਸਕੇ',
 "Could not load feature definition '{feature_key}': {error}":
   'ਵਿਸ਼ੇਸ਼ਤਾ ਪਰਿਭਾਸ਼ਾ "{feature_key}" ਲੋਡ ਨਹੀਂ ਕਰ ਸਕੇ: {error}',
 'Could not merge bus-station centroids into bus-stop points.':
   'ਬੱਸ-ਸਟੇਸ਼ਨ ਕੇਂਦਰਬਿੰਦੂ ਬੱਸ-ਸਟਾਪ ਬਿੰਦੂਆਂ ਵਿੱਚ ਨਹੀਂ ਮਿਲਾ ਸਕੇ।',
 'Could not overwrite existing output file: {error}':
   'ਮੌਜੂਦਾ ਆਉਟਪੁੱਟ ਫਾਈਲ ਉੱਤੇ ਨਹੀਂ ਲਿਖ ਸਕੇ: {error}',
 'Could not populate Shapefile for admin_level {admin_level}.':
   'admin_level {admin_level} ਲਈ Shapefile ਨਹੀਂ ਭਰ ਸਕੇ।',
 "Could not populate temporary layer '{layer_name}'.":
   'ਅਸਥਾਈ ਲੇਅਰ "{layer_name}" ਨਹੀਂ ਭਰ ਸਕੇ।',
 'Could not prepare the Overpass query:': 'Overpass ਕਵੈਰੀ ਤਿਆਰ ਨਹੀਂ ਕਰ ਸਕੇ:',
 "Could not reopen intermediate GeoPackage layer '{layer_name}'.":
   'ਵਿਚਕਾਰਲੀ GeoPackage ਲੇਅਰ "{layer_name}" ਦੁਬਾਰਾ ਨਹੀਂ ਖੋਲ੍ਹ ਸਕੇ।',
 'Could not restore previous QGIS map tool:':
   'ਪਿਛਲਾ QGIS ਨਕਸ਼ਾ ਸਾਧਨ ਬਹਾਲ ਨਹੀਂ ਕਰ ਸਕੇ:',
 'Could not search for temporary GeoPackages:':
   'ਅਸਥਾਈ GeoPackages ਖੋਜ ਨਹੀਂ ਸਕੇ:',
 'Country name': 'ਦੇਸ਼ ਦਾ ਨਾਮ',
 'Create one section panel and return it with its body layout.':
   'ਇੱਕ ਸੈਕਸ਼ਨ ਪੈਨਲ ਬਣਾਓ ਅਤੇ ਇਸਨੂੰ ਇਸਦੇ ਬਾਡੀ ਲੇਆਉਟ ਨਾਲ ਵਾਪਸ ਕਰੋ।',
 'Created bus_stops_points from bus-station polygon centroids.':
   'ਬੱਸ-ਸਟੇਸ਼ਨ ਬਹੁਭੁਜ ਕੇਂਦਰਬਿੰਦੂਆਂ ਤੋਂ bus_stops_points ਬਣਾਇਆ।',
 'Current QGIS map extent': 'ਮੌਜੂਦਾ QGIS ਨਕਸ਼ਾ ਸੀਮਾ',
 'Current QGIS map extent resolved.':
   'ਮੌਜੂਦਾ QGIS ਨਕਸ਼ਾ ਸੀਮਾ ਨਿਰਧਾਰਿਤ ਕੀਤੀ ਗਈ।',
 'Data © <a href="': 'ਡੇਟਾ © <a href="',
 'Deleted temporary workspace file:': 'ਅਸਥਾਈ ਵਰਕਸਪੇਸ ਫਾਈਲ ਮਿਟਾਈ:',
 'Details:': 'ਵੇਰਵੇ:',
 'Download': 'ਡਾਊਨਲੋਡ ਕਰੋ',
 'Download OSM Data': 'OSM ਡੇਟਾ ਡਾਊਨਲੋਡ ਕਰੋ',
 'Download OpenStreetMap data for any area and load it straight into QGIS.':
   'ਕਿਸੇ ਵੀ ਖੇਤਰ ਲਈ OpenStreetMap ਡੇਟਾ ਡਾਊਨਲੋਡ ਕਰੋ ਅਤੇ ਸਿੱਧਾ QGIS ਵਿੱਚ ਲੋਡ ਕਰੋ।',
 'Download cancelled because existing output files were not approved for overwrite.':
   'ਡਾਊਨਲੋਡ ਰੱਦ ਕੀਤਾ ਕਿਉਂਕਿ ਮੌਜੂਦਾ ਆਉਟਪੁੱਟ ਫਾਈਲਾਂ ਨੂੰ ਉੱਤੇ ਲਿਖਣ ਦੀ ਮਨਜ਼ੂਰੀ ਨਹੀਂ ਦਿੱਤੀ ਗਈ।',
 'Download cancelled before it started.':
   'ਸ਼ੁਰੂ ਹੋਣ ਤੋਂ ਪਹਿਲਾਂ ਡਾਊਨਲੋਡ ਰੱਦ ਕੀਤਾ।',
 'Download cancelled before results were returned.':
   'ਨਤੀਜੇ ਵਾਪਸ ਆਉਣ ਤੋਂ ਪਹਿਲਾਂ ਡਾਊਨਲੋਡ ਰੱਦ ਕੀਤਾ।',
 'Download cancelled before starting.':
   'ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਡਾਊਨਲੋਡ ਰੱਦ ਕੀਤਾ।',
 'Download cancelled in the output-naming dialog.':
   'ਆਉਟਪੁੱਟ-ਨਾਮਕਰਨ ਡਾਇਲਾਗ ਵਿੱਚ ਡਾਊਨਲੋਡ ਰੱਦ ਕੀਤਾ।',
 'Download cancelled.': 'ਡਾਊਨਲੋਡ ਰੱਦ ਕੀਤਾ।',
 'Download cancelled; existing files preserved.':
   'ਡਾਊਨਲੋਡ ਰੱਦ ਕੀਤਾ; ਮੌਜੂਦਾ ਫਾਈਲਾਂ ਬਚਾਈਆਂ ਗਈਆਂ।',
 'Download stopped.': 'ਡਾਊਨਲੋਡ ਰੁਕਿਆ।',
 'Download succeeded, but export failed.':
   'ਡਾਊਨਲੋਡ ਸਫਲ, ਪਰ ਨਿਰਯਾਤ ਅਸਫਲ।',
 'Downloading OSM data from Overpass...':
   'Overpass ਤੋਂ OSM ਡੇਟਾ ਡਾਊਨਲੋਡ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ…',
 'Draw AOI': 'AOI ਖਿੱਚੋ',
 'Draw a rectangle on the QGIS map to define the AOI.':
   'AOI ਪਰਿਭਾਸ਼ਿਤ ਕਰਨ ਲਈ QGIS ਨਕਸ਼ੇ \'ਤੇ ਆਇਤ ਖਿੱਚੋ।',
 'Draw rectangle on map': 'ਨਕਸ਼ੇ \'ਤੇ ਆਇਤ ਖਿੱਚੋ',
 'Draw the AOI rectangle on the QGIS map.':
   'QGIS ਨਕਸ਼ੇ \'ਤੇ AOI ਆਇਤ ਖਿੱਚੋ।',
 'Drawn AOI validation failed:': 'ਖਿੱਚੀ AOI ਪ੍ਰਮਾਣਿਕਤਾ ਅਸਫਲ:',
 'Drawn rectangle': 'ਖਿੱਚੀ ਆਇਤ',
 'Drawn rectangle AOI captured successfully.':
   'ਖਿੱਚੀ ਆਇਤ AOI ਸਫਲਤਾਪੂਰਵਕ ਕੈਪਚਰ ਕੀਤੀ ਗਈ।',
 'ERROR:': 'ਗਲਤੀ:',
 'East:': 'ਪੂਰਬ:',
 'Enable level checkboxes only when a specific selection is active.':
   'ਪੱਧਰ ਚੈੱਕਬਾਕਸ ਸਿਰਫ਼ ਤਦ ਸਮਰੱਥ ਕਰੋ ਜਦੋਂ ਖਾਸ ਚੋਣ ਸਰਗਰਮ ਹੋਵੇ।',
 'Enable only the AOI action button for the selected method.':
   'ਚੁਣੀ ਵਿਧੀ ਲਈ ਸਿਰਫ਼ AOI ਕਿਰਿਆ ਬਟਨ ਸਮਰੱਥ ਕਰੋ।',
 'Enable or disable controls while a download is running.':
   'ਡਾਊਨਲੋਡ ਚੱਲਦੇ ਸਮੇਂ ਨਿਯੰਤਰਣ ਸਮਰੱਥ ਜਾਂ ਅਸਮਰੱਥ ਕਰੋ।',
 'Enter at least one name (City, Country, Region, or AOI).':
   'ਘੱਟੋ-ਘੱਟ ਇੱਕ ਨਾਮ ਦਰਜ ਕਰੋ (ਸ਼ਹਿਰ, ਦੇਸ਼, ਖੇਤਰ ਜਾਂ AOI)।',
 'Enter one or more name components. Blank fields will be skipped, and the remaining names will be joined with underscores. The selected output format will be retained.':
   'ਇੱਕ ਜਾਂ ਵੱਧ ਨਾਮ ਹਿੱਸੇ ਦਰਜ ਕਰੋ। ਖਾਲੀ ਖੇਤਰ ਛੱਡ ਦਿੱਤੇ ਜਾਣਗੇ, ਅਤੇ ਬਾਕੀ ਨਾਮ ਅੰਡਰਸਕੋਰ ਨਾਲ ਜੋੜੇ ਜਾਣਗੇ। ਚੁਣਿਆ ਆਉਟਪੁੱਟ ਫਾਰਮੈਟ ਬਰਕਰਾਰ ਰਹੇਗਾ।',
 'Enter_a_name_to_preview': 'ਝਲਕ_ਲਈ_ਨਾਮ_ਦਰਜ_ਕਰੋ',
 'Export cancelled: output name is missing.':
   'ਨਿਰਯਾਤ ਰੱਦ: ਆਉਟਪੁੱਟ ਨਾਮ ਗੁੰਮ ਹੈ।',
 'Export complete:': 'ਨਿਰਯਾਤ ਪੂਰਾ:',
 'Export the downloaded response and optionally load its layers.':
   'ਡਾਊਨਲੋਡ ਕੀਤਾ ਜਵਾਬ ਨਿਰਯਾਤ ਕਰੋ ਅਤੇ ਲੋੜ ਪੈਣ \'ਤੇ ਇਸਦੀਆਂ ਲੇਅਰਾਂ ਲੋਡ ਕਰੋ।',
 'Failed to activate rectangle AOI tool:':
   'ਆਇਤ AOI ਸਾਧਨ ਸਰਗਰਮ ਕਰਨ ਵਿੱਚ ਅਸਫਲ:',
 'Failed to create AOI.': 'AOI ਬਣਾਉਣ ਵਿੱਚ ਅਸਫਲ।',
 'Failed to process drawn rectangle AOI:':
   'ਖਿੱਚੀ ਆਇਤ AOI ਦੀ ਪ੍ਰਕਿਰਿਆ ਕਰਨ ਵਿੱਚ ਅਸਫਲ:',
 'Failed to resolve active-layer extent.':
   'ਸਰਗਰਮ ਲੇਅਰ ਸੀਮਾ ਨਿਰਧਾਰਿਤ ਕਰਨ ਵਿੱਚ ਅਸਫਲ।',
 'Failed to resolve active-layer extent:':
   'ਸਰਗਰਮ ਲੇਅਰ ਸੀਮਾ ਨਿਰਧਾਰਿਤ ਕਰਨ ਵਿੱਚ ਅਸਫਲ:',
 'Failed to resolve current QGIS map extent:':
   'ਮੌਜੂਦਾ QGIS ਨਕਸ਼ਾ ਸੀਮਾ ਨਿਰਧਾਰਿਤ ਕਰਨ ਵਿੱਚ ਅਸਫਲ:',
 'Failed to resolve selected-feature AOI.':
   'ਚੁਣੀਆਂ-ਵਿਸ਼ੇਸ਼ਤਾ AOI ਨਿਰਧਾਰਿਤ ਕਰਨ ਵਿੱਚ ਅਸਫਲ।',
 'Failed to resolve selected-feature AOI:':
   'ਚੁਣੀਆਂ-ਵਿਸ਼ੇਸ਼ਤਾ AOI ਨਿਰਧਾਰਿਤ ਕਰਨ ਵਿੱਚ ਅਸਫਲ:',
 "Failed to write layer '{layer_name}' to '{output_path}': {error}":
   'ਲੇਅਰ "{layer_name}" ਨੂੰ "{output_path}" ਵਿੱਚ ਲਿਖਣ ਵਿੱਚ ਅਸਫਲ: {error}',
 "Feature '{feature_key}' has no tag definitions.":
   'ਵਿਸ਼ੇਸ਼ਤਾ "{feature_key}" ਵਿੱਚ ਕੋਈ ਟੈਗ ਪਰਿਭਾਸ਼ਾ ਨਹੀਂ।',
 'Feature specification  does not expose a tag-filter mapping.':
   'ਵਿਸ਼ੇਸ਼ਤਾ ਨਿਰਦੇਸ਼ ਟੈਗ-ਫਿਲਟਰ ਮੈਪਿੰਗ ਪ੍ਰਦਾਨ ਨਹੀਂ ਕਰਦਾ।',
 'Ferry stops': 'ਫੈਰੀ ਸਟਾਪ',
 'Filename preview': 'ਫਾਈਲਨਾਮ ਝਲਕ',
 'Full documentation': 'ਪੂਰੀ ਦਸਤਾਵੇਜ਼ੀਕਰਨ',
 'Generated Overpass query (': 'ਤਿਆਰ ਕੀਤੀ Overpass ਕਵੈਰੀ (',
 'GeoPackage': 'GeoPackage',
 'GeoPackage layer(s) to QGIS.': 'GeoPackage ਲੇਅਰ QGIS ਵਿੱਚ।',
 'GeoPackage saved:': 'GeoPackage ਸੰਭਾਲਿਆ:',
 'HTTP error on server ': 'ਸਰਵਰ \'ਤੇ HTTP ਗਲਤੀ: ',
 'HTTP error — ': 'HTTP ਗਲਤੀ — ',
 'HTTP {status} error on server {index}/{total}.':
   'ਸਰਵਰ {index}/{total} \'ਤੇ HTTP {status} ਗਲਤੀ।',
 'Handle a drawing tool deactivation initiated outside this dialog.':
   'ਇਸ ਡਾਇਲਾਗ ਤੋਂ ਬਾਹਰ ਸ਼ੁਰੂ ਹੋਏ ਡਰਾਇੰਗ ਸਾਧਨ ਦੀ ਅਸਮਰੱਥਾ ਨੂੰ ਸੰਭਾਲੋ।',
 'Help': 'ਮਦਦ',
 'Invalid east longitude: {value}': 'ਅਵੈਧ ਪੂਰਬੀ ਲੰਬਕਾਰ: {value}',
 'Invalid north latitude: {value}': 'ਅਵੈਧ ਉੱਤਰੀ ਅਕਸ਼ਾਂਸ਼: {value}',
 'Invalid response from server ': 'ਸਰਵਰ ਤੋਂ ਅਵੈਧ ਜਵਾਬ: ',
 'Invalid south latitude: {value}': 'ਅਵੈਧ ਦੱਖਣੀ ਅਕਸ਼ਾਂਸ਼: {value}',
 'Invalid west longitude: {value}': 'ਅਵੈਧ ਪੱਛਮੀ ਲੰਬਕਾਰ: {value}',
 'Keep the numeric readout in step with the progress bar.':
   'ਸੰਖਿਆਤਮਕ ਰੀਡਆਊਟ ਨੂੰ ਪ੍ਰਗਤੀ ਪੱਟੀ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਰੱਖੋ।',
 'Land & built environment': 'ਜ਼ਮੀਨ ਅਤੇ ਬਣਿਆ ਵਾਤਾਵਰਣ',
 'Landuse': 'ਜ਼ਮੀਨ ਵਰਤੋਂ',
 'Language:': 'ਭਾਸ਼ਾ:',
 'Linear features': 'ਰੇਖਿਕ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ',
 'Load the saved interface language and translate visible UI strings.':
   'ਸੰਭਾਲੀ ਇੰਟਰਫੇਸ ਭਾਸ਼ਾ ਲੋਡ ਕਰੋ ਅਤੇ ਦਿਖਣ ਵਾਲੀਆਂ UI ਸਤਰਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰੋ।',
 'Local response cache is disabled.': 'ਸਥਾਨਕ ਜਵਾਬ ਕੈਸ਼ ਅਸਮਰੱਥ ਹੈ।',
 'Main OSM Data Toolkit window.': 'ਮੁੱਖ OSM Data Toolkit ਵਿੰਡੋ।',
 'Manually capture the map extent after the user pans or zooms.':
   'ਵਰਤੋਂਕਾਰ ਦੁਆਰਾ ਪੈਨ ਜਾਂ ਜ਼ੂਮ ਕਰਨ ਤੋਂ ਬਾਅਦ ਨਕਸ਼ਾ ਸੀਮਾ ਹੱਥੀਂ ਕੈਪਚਰ ਕਰੋ।',
 'Merged bus-station polygon centroids into bus_stops_points.':
   'ਬੱਸ-ਸਟੇਸ਼ਨ ਬਹੁਭੁਜ ਕੇਂਦਰਬਿੰਦੂ bus_stops_points ਵਿੱਚ ਮਿਲਾਏ।',
 'No Overpass selectors were generated.':
   'ਕੋਈ Overpass ਚੋਣਕਾਰ ਤਿਆਰ ਨਹੀਂ ਕੀਤੇ ਗਏ।',
 'No active QGIS layer is available.':
   'ਕੋਈ ਸਰਗਰਮ QGIS ਲੇਅਰ ਉਪਲਬਧ ਨਹੀਂ ਹੈ।',
 'No active layer is available.': 'ਕੋਈ ਸਰਗਰਮ ਲੇਅਰ ਉਪਲਬਧ ਨਹੀਂ ਹੈ।',
 'No exportable features matched the selected categories. Try another AOI or select additional OSM feature categories.':
   'ਚੁਣੀਆਂ ਸ਼੍ਰੇਣੀਆਂ ਨਾਲ ਕੋਈ ਨਿਰਯਾਤਯੋਗ ਵਿਸ਼ੇਸ਼ਤਾ ਨਹੀਂ ਮਿਲੀ। ਕੋਈ ਹੋਰ AOI ਵਰਤੋ ਜਾਂ ਹੋਰ OSM ਵਿਸ਼ੇਸ਼ਤਾ ਸ਼੍ਰੇਣੀਆਂ ਚੁਣੋ।',
 'No features are selected in the active layer.':
   'ਸਰਗਰਮ ਲੇਅਰ ਵਿੱਚ ਕੋਈ ਵਿਸ਼ੇਸ਼ਤਾ ਚੁਣੀ ਨਹੀਂ ਗਈ।',
 'No levels selected. Select at least one level to continue.':
   'ਕੋਈ ਪੱਧਰ ਚੁਣਿਆ ਨਹੀਂ। ਜਾਰੀ ਰੱਖਣ ਲਈ ਘੱਟੋ-ਘੱਟ ਇੱਕ ਪੱਧਰ ਚੁਣੋ।',
 'No selected features found.': 'ਕੋਈ ਚੁਣੀ ਵਿਸ਼ੇਸ਼ਤਾ ਨਹੀਂ ਮਿਲੀ।',
 'No valid Area of Interest is available. Select an AOI method and resolve the AOI before downloading.':
   'ਕੋਈ ਵੈਧ ਦਿਲਚਸਪੀ ਦਾ ਖੇਤਰ ਉਪਲਬਧ ਨਹੀਂ ਹੈ। ਡਾਊਨਲੋਡ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ AOI ਵਿਧੀ ਚੁਣੋ ਅਤੇ AOI ਨਿਰਧਾਰਿਤ ਕਰੋ।',
 'North:': 'ਉੱਤਰ:',
 'Note: {layer_name} has too many tag columns for one Shapefile (DBF size limit); {count} rarely-used columns were left out.':
   'ਨੋਟ: {layer_name} ਵਿੱਚ ਇੱਕ Shapefile ਲਈ ਬਹੁਤ ਜ਼ਿਆਦਾ ਟੈਗ ਕਾਲਮ ਹਨ (DBF ਆਕਾਰ ਸੀਮਾ); {count} ਘੱਟ ਵਰਤੇ ਜਾਣ ਵਾਲੇ ਕਾਲਮ ਛੱਡ ਦਿੱਤੇ ਗਏ।',
 'OSM Data Toolkit': 'OSM Data Toolkit',
 'OSM Data Toolkit initialised.': 'OSM Data Toolkit ਸ਼ੁਰੂ ਕੀਤਾ ਗਿਆ।',
 'OSM Feature Categories': 'OSM ਵਿਸ਼ੇਸ਼ਤਾ ਸ਼੍ਰੇਣੀਆਂ',
 'OSM export completed successfully.': 'OSM ਨਿਰਯਾਤ ਸਫਲਤਾਪੂਰਵਕ ਪੂਰਾ ਹੋਇਆ।',
 'One or more output files with this name already exist. Do you want to overwrite the matching output files?':
   'ਇਸ ਨਾਮ ਨਾਲ ਇੱਕ ਜਾਂ ਵੱਧ ਆਉਟਪੁੱਟ ਫਾਈਲਾਂ ਪਹਿਲਾਂ ਹੀ ਮੌਜੂਦ ਹਨ। ਕੀ ਤੁਸੀਂ ਮੇਲ ਖਾਂਦੀਆਂ ਆਉਟਪੁੱਟ ਫਾਈਲਾਂ \'ਤੇ ਲਿਖਣਾ ਚਾਹੁੰਦੇ ਹੋ?',
 'Only the selected levels': 'ਸਿਰਫ਼ ਚੁਣੇ ਪੱਧਰ',
 'Only validated Overpass responses can be cached.':
   'ਸਿਰਫ਼ ਪ੍ਰਮਾਣਿਤ Overpass ਜਵਾਬ ਕੈਸ਼ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ।',
 'Open public spaces': 'ਖੁੱਲ੍ਹੀਆਂ ਜਨਤਕ ਥਾਵਾਂ',
 'Open the in-plugin help with links to the online documentation.':
   'ਔਨਲਾਈਨ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਦੇ ਲਿੰਕਾਂ ਨਾਲ ਪਲੱਗਇਨ-ਅੰਦਰੂਨੀ ਮਦਦ ਖੋਲ੍ਹੋ।',
 'Output Settings': 'ਆਉਟਪੁੱਟ ਸੈਟਿੰਗਾਂ',
 'Output directory': 'ਆਉਟਪੁੱਟ ਡਾਇਰੈਕਟਰੀ',
 'Output directory selected:': 'ਆਉਟਪੁੱਟ ਡਾਇਰੈਕਟਰੀ ਚੁਣੀ:',
 'Output format': 'ਆਉਟਪੁੱਟ ਫਾਰਮੈਟ',
 'Output settings': 'ਆਉਟਪੁੱਟ ਸੈਟਿੰਗਾਂ',
 'Overpass download cancelled.': 'Overpass ਡਾਊਨਲੋਡ ਰੱਦ ਕੀਤਾ।',
 'Overpass download completed:': 'Overpass ਡਾਊਨਲੋਡ ਪੂਰਾ:',
 'Overpass download failed.': 'Overpass ਡਾਊਨਲੋਡ ਅਸਫਲ।',
 'Overpass download failed:': 'Overpass ਡਾਊਨਲੋਡ ਅਸਫਲ:',
 'Overpass download running...': 'Overpass ਡਾਊਨਲੋਡ ਚੱਲ ਰਿਹਾ ਹੈ…',
 'Overpass download was cancelled by the caller.':
   'ਕਾਲਰ ਦੁਆਰਾ Overpass ਡਾਊਨਲੋਡ ਰੱਦ ਕੀਤਾ ਗਿਆ।',
 'Overpass query must be a non-empty string.':
   'Overpass ਕਵੈਰੀ ਖਾਲੀ ਨਾ ਹੋਣ ਵਾਲੀ ਸਤਰ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ।',
 "Overpass response 'elements' field is not a list.":
   'Overpass ਜਵਾਬ ਦਾ "elements" ਖੇਤਰ ਸੂਚੀ ਨਹੀਂ ਹੈ।',
 "Overpass response does not contain an 'elements' field.":
   'Overpass ਜਵਾਬ ਵਿੱਚ "elements" ਖੇਤਰ ਨਹੀਂ ਹੈ।',
 'Overpass response is not a JSON object.':
   'Overpass ਜਵਾਬ JSON ਆਬਜੈਕਟ ਨਹੀਂ ਹੈ।',
 'Overpass response received successfully:':
   'Overpass ਜਵਾਬ ਸਫਲਤਾਪੂਰਵਕ ਪ੍ਰਾਪਤ ਹੋਇਆ:',
 'Overpass server ': 'Overpass ਸਰਵਰ ',
 'Overpass server returned invalid JSON. Response preview: ':
   'Overpass ਸਰਵਰ ਨੇ ਅਵੈਧ JSON ਵਾਪਸ ਕੀਤਾ। ਜਵਾਬ ਝਲਕ: ',
 'Overpass servers available:': 'ਉਪਲਬਧ Overpass ਸਰਵਰ:',
 'Overpass timeout must be greater than zero.':
   'Overpass ਸਮਾਂ-ਸੀਮਾ ਜ਼ੀਰੋ ਤੋਂ ਵੱਧ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ।',
 'Plugin version': 'ਪਲੱਗਇਨ ਸੰਸਕਰਣ',
 'Points of interest (POI)': 'ਦਿਲਚਸਪੀ ਦੇ ਬਿੰਦੂ (POI)',
 'Prepared {index:,} of {total:,} OSM elements for export...':
   'ਨਿਰਯਾਤ ਲਈ {total:,} ਵਿੱਚੋਂ {index:,} OSM ਤੱਤ ਤਿਆਰ ਕੀਤੇ…',
 'Preparing Overpass download...': 'Overpass ਡਾਊਨਲੋਡ ਤਿਆਰ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ…',
 'Preparing Overpass query.': 'Overpass ਕਵੈਰੀ ਤਿਆਰ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ।',
 'Processing Options': 'ਪ੍ਰੋਸੈਸਿੰਗ ਵਿਕਲਪ',
 'Processing log': 'ਪ੍ਰੋਸੈਸਿੰਗ ਲੌਗ',
 'Processing messages will appear here...':
   'ਪ੍ਰੋਸੈਸਿੰਗ ਸੁਨੇਹੇ ਇੱਥੇ ਦਿਖਾਈ ਦੇਣਗੇ…',
 'Processing options': 'ਪ੍ਰੋਸੈਸਿੰਗ ਵਿਕਲਪ',
 'Public transport & places': 'ਜਨਤਕ ਆਵਾਜਾਈ ਅਤੇ ਥਾਵਾਂ',
 'QGIS interface object was not detected. Canvas-dependent AOI tools are disabled.':
   'QGIS ਇੰਟਰਫੇਸ ਆਬਜੈਕਟ ਨਹੀਂ ਲੱਭਿਆ। ਕੈਨਵਸ-ਨਿਰਭਰ AOI ਸਾਧਨ ਅਸਮਰੱਥ ਹਨ।',
 'QGIS map canvas could not be accessed.':
   'QGIS ਨਕਸ਼ਾ ਕੈਨਵਸ ਤੱਕ ਪਹੁੰਚ ਨਹੀਂ ਹੋ ਸਕੀ।',
 'QGIS map canvas is unavailable.': 'QGIS ਨਕਸ਼ਾ ਕੈਨਵਸ ਉਪਲਬਧ ਨਹੀਂ ਹੈ।',
 'Rail stops': 'ਰੇਲ ਸਟਾਪ',
 'Railways': 'ਰੇਲਵੇ',
 'Read the plugin version from metadata.txt (empty string if absent).':
   'metadata.txt ਤੋਂ ਪਲੱਗਇਨ ਸੰਸਕਰਣ ਪੜ੍ਹੋ (ਨਾ ਹੋਣ \'ਤੇ ਖਾਲੀ ਸਤਰ)।',
 'Read, validate and store the current QGIS map canvas extent.':
   'ਮੌਜੂਦਾ QGIS ਨਕਸ਼ਾ ਕੈਨਵਸ ਸੀਮਾ ਪੜ੍ਹੋ, ਪ੍ਰਮਾਣਿਤ ਕਰੋ ਅਤੇ ਸੰਭਾਲੋ।',
 'Ready.': 'ਤਿਆਰ।',
 'Rectangle AOI drawing tool activated.':
   'ਆਇਤ AOI ਡਰਾਇੰਗ ਸਾਧਨ ਸਰਗਰਮ ਕੀਤਾ ਗਿਆ।',
 'Rectangle AOI drawing was cancelled.':
   'ਆਇਤ AOI ਡਰਾਇੰਗ ਰੱਦ ਕੀਤੀ ਗਈ।',
 'Region name': 'ਖੇਤਰ ਦਾ ਨਾਮ',
 'Report an issue': 'ਸਮੱਸਿਆ ਦੀ ਰਿਪੋਰਟ ਕਰੋ',
 'Request cooperative cancellation of the background worker.':
   'ਬੈਕਗ੍ਰਾਊਂਡ ਵਰਕਰ ਦੀ ਸਹਿਯੋਗੀ ਰੱਦੀਕਰਨ ਦੀ ਬੇਨਤੀ ਕਰੋ।',
 'Request error on server ': 'ਸਰਵਰ \'ਤੇ ਬੇਨਤੀ ਗਲਤੀ: ',
 'Restore default GUI settings when the dialog closes.':
   'ਡਾਇਲਾਗ ਬੰਦ ਹੋਣ \'ਤੇ ਡਿਫ਼ਾਲਟ GUI ਸੈਟਿੰਗਾਂ ਬਹਾਲ ਕਰੋ।',
 'Restore the GUI once the background thread has stopped.':
   'ਬੈਕਗ੍ਰਾਊਂਡ ਥ੍ਰੈਡ ਰੁਕਣ \'ਤੇ GUI ਬਹਾਲ ਕਰੋ।',
 'Restore the QGIS map tool active before rectangle drawing.':
   'ਆਇਤ ਖਿੱਚਣ ਤੋਂ ਪਹਿਲਾਂ ਸਰਗਰਮ QGIS ਨਕਸ਼ਾ ਸਾਧਨ ਬਹਾਲ ਕਰੋ।',
 'Restore the map tool and reset state before hiding the dialog.':
   'ਡਾਇਲਾਗ ਲੁਕਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਨਕਸ਼ਾ ਸਾਧਨ ਬਹਾਲ ਕਰੋ ਅਤੇ ਸਥਿਤੀ ਰੀਸੈੱਟ ਕਰੋ।',
 'Retrying in ': 'ਮੁੜ ਕੋਸ਼ਿਸ਼ ',
 'Return selected levels, or None when all levels are requested.':
   'ਚੁਣੇ ਪੱਧਰ ਵਾਪਸ ਕਰੋ, ਜਾਂ ਜਦੋਂ ਸਾਰੇ ਪੱਧਰ ਮੰਗੇ ਗਏ ਹੋਣ ਤਾਂ None।',
 'Return the combined, sanitized filename prefix.':
   'ਜੋੜਿਆ, ਸਾਫ਼ ਕੀਤਾ ਫਾਈਲਨਾਮ ਪ੍ਰੀਫਿਕਸ ਵਾਪਸ ਕਰੋ।',
 'Return the mapping between feature keys and GUI checkboxes.':
   'ਵਿਸ਼ੇਸ਼ਤਾ ਕੁੰਜੀਆਂ ਅਤੇ GUI ਚੈੱਕਬਾਕਸਾਂ ਵਿਚਕਾਰ ਮੈਪਿੰਗ ਵਾਪਸ ਕਰੋ।',
 'Return the selected GUI feature keys.':
   'ਚੁਣੀਆਂ GUI ਵਿਸ਼ੇਸ਼ਤਾ ਕੁੰਜੀਆਂ ਵਾਪਸ ਕਰੋ।',
 'Roads': 'ਸੜਕਾਂ',
 'Run a modal dialog on both Qt5 and Qt6.':
   'Qt5 ਅਤੇ Qt6 ਦੋਵਾਂ \'ਤੇ ਮੋਡਲ ਡਾਇਲਾਗ ਚਲਾਓ।',
 'Select Output Directory': 'ਆਉਟਪੁੱਟ ਡਾਇਰੈਕਟਰੀ ਚੁਣੋ',
 'Select a vector layer with selected features.':
   'ਚੁਣੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਵਾਲੀ ਵੈਕਟਰ ਲੇਅਰ ਚੁਣੋ।',
 'Select all': 'ਸਭ ਚੁਣੋ',
 'Select an active QGIS layer.': 'ਸਰਗਰਮ QGIS ਲੇਅਰ ਚੁਣੋ।',
 'Select at least one OSM feature category before downloading.':
   'ਡਾਊਨਲੋਡ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਘੱਟੋ-ਘੱਟ ਇੱਕ OSM ਵਿਸ਼ੇਸ਼ਤਾ ਸ਼੍ਰੇਣੀ ਚੁਣੋ।',
 'Select at least one administrative level, or choose All levels.':
   'ਘੱਟੋ-ਘੱਟ ਇੱਕ ਪ੍ਰਸ਼ਾਸਕੀ ਪੱਧਰ ਚੁਣੋ, ਜਾਂ "ਸਾਰੇ ਪੱਧਰ" ਚੁਣੋ।',
 'Select at least one administrative level, or use None to retrieve all levels.':
   'ਘੱਟੋ-ਘੱਟ ਇੱਕ ਪ੍ਰਸ਼ਾਸਕੀ ਪੱਧਰ ਚੁਣੋ, ਜਾਂ ਸਾਰੇ ਪੱਧਰ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ None ਵਰਤੋ।',
 'Select levels 0–15 and switch to specific-level mode.':
   'ਪੱਧਰ 0–15 ਚੁਣੋ ਅਤੇ ਖਾਸ-ਪੱਧਰ ਮੋਡ \'ਤੇ ਜਾਓ।',
 'Select one or more features in the active layer.':
   'ਸਰਗਰਮ ਲੇਅਰ ਵਿੱਚ ਇੱਕ ਜਾਂ ਵੱਧ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਚੁਣੋ।',
 'Select output directory...': 'ਆਉਟਪੁੱਟ ਡਾਇਰੈਕਟਰੀ ਚੁਣੋ…',
 'Selected administrative levels:': 'ਚੁਣੇ ਪ੍ਰਸ਼ਾਸਕੀ ਪੱਧਰ:',
 'Selected feature IDs:': 'ਚੁਣੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦੇ ID:',
 'Selected feature(s) in active layer':
   'ਸਰਗਰਮ ਲੇਅਰ ਵਿੱਚ ਚੁਣੀ ਵਿਸ਼ੇਸ਼ਤਾ(ਵਾਂ)',
 'Selected features (': 'ਚੁਣੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ (',
 'Selected-feature AOI captured successfully (':
   'ਚੁਣੀਆਂ-ਵਿਸ਼ੇਸ਼ਤਾ AOI ਸਫਲਤਾਪੂਰਵਕ ਕੈਪਚਰ ਕੀਤੀ ਗਈ (',
 'Selected-feature AOI captured successfully.':
   'ਚੁਣੀਆਂ-ਵਿਸ਼ੇਸ਼ਤਾ AOI ਸਫਲਤਾਪੂਰਵਕ ਕੈਪਚਰ ਕੀਤੀ ਗਈ।',
 'Selected-feature AOI is invalid.': 'ਚੁਣੀਆਂ-ਵਿਸ਼ੇਸ਼ਤਾ AOI ਅਵੈਧ ਹੈ।',
 'Selected-feature AOI requires a vector layer.':
   'ਚੁਣੀਆਂ-ਵਿਸ਼ੇਸ਼ਤਾ AOI ਲਈ ਵੈਕਟਰ ਲੇਅਰ ਲੋੜੀਂਦੀ ਹੈ।',
 'Selected-feature AOI validation failed:':
   'ਚੁਣੀਆਂ-ਵਿਸ਼ੇਸ਼ਤਾ AOI ਪ੍ਰਮਾਣਿਕਤਾ ਅਸਫਲ:',
 'Sending query to Overpass...': 'Overpass ਨੂੰ ਕਵੈਰੀ ਭੇਜੀ ਜਾ ਰਹੀ ਹੈ…',
 'Server ': 'ਸਰਵਰ ',
 'Shapefile': 'Shapefile',
 'Shapefile export completed in:': 'Shapefile ਨਿਰਯਾਤ ਪੂਰਾ ਹੋਇਆ:',
 'Shapefile field names shortened for':
   'ਲਈ Shapefile ਖੇਤਰ ਨਾਮ ਛੋਟੇ ਕੀਤੇ',
 'Shapefile layer(s) to QGIS.': 'Shapefile ਲੇਅਰ QGIS ਵਿੱਚ।',
 'Short in-plugin help with links to the full online documentation.':
   'ਪੂਰੀ ਔਨਲਾਈਨ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਦੇ ਲਿੰਕਾਂ ਨਾਲ ਸੰਖੇਪ ਪਲੱਗਇਨ-ਅੰਦਰੂਨੀ ਮਦਦ।',
 'Show AOI coordinates and source CRS in the dialog.':
   'ਡਾਇਲਾਗ ਵਿੱਚ AOI ਕੋਆਰਡੀਨੇਟ ਅਤੇ ਸਰੋਤ CRS ਦਿਖਾਓ।',
 'Show a concise description of the active administrative filter.':
   'ਸਰਗਰਮ ਪ੍ਰਸ਼ਾਸਕੀ ਫਿਲਟਰ ਦਾ ਸੰਖੇਪ ਵੇਰਵਾ ਦਿਖਾਓ।',
 'Source CRS is invalid.': 'ਸਰੋਤ CRS ਅਵੈਧ ਹੈ।',
 'South latitude cannot be greater than north latitude.':
   'ਦੱਖਣੀ ਅਕਸ਼ਾਂਸ਼ ਉੱਤਰੀ ਅਕਸ਼ਾਂਸ਼ ਤੋਂ ਵੱਧ ਨਹੀਂ ਹੋ ਸਕਦਾ।',
 'South:': 'ਦੱਖਣ:',
 'Starting Overpass download...': 'Overpass ਡਾਊਨਲੋਡ ਸ਼ੁਰੂ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ…',
 'Supporting copy: muted, wrapped and visually quiet.':
   'ਸਹਾਇਕ ਟੈਕਸਟ: ਧੀਮਾ, ਲਪੇਟਿਆ ਅਤੇ ਦ੍ਰਿਸ਼ਟੀਗਤ ਤੌਰ \'ਤੇ ਸ਼ਾਂਤ।',
 "Tag '{tag}' contains an empty value list.":
   'ਟੈਗ "{tag}" ਵਿੱਚ ਖਾਲੀ ਮੁੱਲ ਸੂਚੀ ਹੈ।',
 'Temporary workspace cleanup complete:':
   'ਅਸਥਾਈ ਵਰਕਸਪੇਸ ਸਫ਼ਾਈ ਪੂਰੀ:',
 'Temporary workspace cleanup complete: no matching files found.':
   'ਅਸਥਾਈ ਵਰਕਸਪੇਸ ਸਫ਼ਾਈ ਪੂਰੀ: ਕੋਈ ਮੇਲ ਖਾਂਦੀ ਫਾਈਲ ਨਹੀਂ ਮਿਲੀ।',
 'Temporary-file cleanup skipped: workspace directory is invalid.':
   'ਅਸਥਾਈ-ਫਾਈਲ ਸਫ਼ਾਈ ਛੱਡੀ ਗਈ: ਵਰਕਸਪੇਸ ਡਾਇਰੈਕਟਰੀ ਅਵੈਧ ਹੈ।',
 'The OSM download succeeded, but the output could not be created.':
   'OSM ਡਾਊਨਲੋਡ ਸਫਲ, ਪਰ ਆਉਟਪੁੱਟ ਨਹੀਂ ਬਣਾਈ ਜਾ ਸਕੀ।',
 "The Overpass response must be a JSON object with an 'elements' list.":
   'Overpass ਜਵਾਬ "elements" ਸੂਚੀ ਵਾਲਾ JSON ਆਬਜੈਕਟ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।',
 'The QGIS map canvas CRS is invalid.':
   'QGIS ਨਕਸ਼ਾ ਕੈਨਵਸ CRS ਅਵੈਧ ਹੈ।',
 'The active layer CRS is invalid.': 'ਸਰਗਰਮ ਲੇਅਰ CRS ਅਵੈਧ ਹੈ।',
 'The active layer extent is empty.': 'ਸਰਗਰਮ ਲੇਅਰ ਸੀਮਾ ਖਾਲੀ ਹੈ।',
 'The active layer must be a vector layer.':
   'ਸਰਗਰਮ ਲੇਅਰ ਵੈਕਟਰ ਲੇਅਰ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ।',
 'The combined name is too long. Shorten one or more components.':
   'ਜੋੜਿਆ ਨਾਮ ਬਹੁਤ ਲੰਬਾ ਹੈ। ਇੱਕ ਜਾਂ ਵੱਧ ਹਿੱਸੇ ਛੋਟੇ ਕਰੋ।',
 'The combined selected-feature geometry is empty.':
   'ਜੋੜੀ ਚੁਣੀਆਂ-ਵਿਸ਼ੇਸ਼ਤਾ ਜਿਓਮੈਟਰੀ ਖਾਲੀ ਹੈ।',
 'The current AOI is invalid:': 'ਮੌਜੂਦਾ AOI ਅਵੈਧ ਹੈ:',
 'The current QGIS map extent is empty.':
   'ਮੌਜੂਦਾ QGIS ਨਕਸ਼ਾ ਸੀਮਾ ਖਾਲੀ ਹੈ।',
 'The dialog cannot close while a download thread is running. Cancellation has been requested; close the dialog after it stops.':
   'ਡਾਊਨਲੋਡ ਥ੍ਰੈਡ ਚੱਲਦੇ ਸਮੇਂ ਡਾਇਲਾਗ ਬੰਦ ਨਹੀਂ ਹੋ ਸਕਦਾ। ਰੱਦ ਕਰਨ ਦੀ ਬੇਨਤੀ ਕੀਤੀ ਗਈ ਹੈ; ਰੁਕਣ ਤੋਂ ਬਾਅਦ ਡਾਇਲਾਗ ਬੰਦ ਕਰੋ।',
 'The download completed, but no confirmed output name was available.':
   'ਡਾਊਨਲੋਡ ਪੂਰਾ ਹੋਇਆ, ਪਰ ਕੋਈ ਪੁਸ਼ਟੀ ਕੀਤਾ ਆਉਟਪੁੱਟ ਨਾਮ ਉਪਲਬਧ ਨਹੀਂ ਸੀ।',
 "The exported Shapefile '{path}' could not be opened in QGIS.":
   'ਨਿਰਯਾਤ ਕੀਤੀ Shapefile "{path}" QGIS ਵਿੱਚ ਨਹੀਂ ਖੋਲ੍ਹੀ ਜਾ ਸਕੀ।',
 "The exported layer '{layer_name}' could not be opened in QGIS.":
   'ਨਿਰਯਾਤ ਕੀਤੀ ਲੇਅਰ "{layer_name}" QGIS ਵਿੱਚ ਨਹੀਂ ਖੋਲ੍ਹੀ ਜਾ ਸਕੀ।',
 'The output name does not contain any valid filename characters.':
   'ਆਉਟਪੁੱਟ ਨਾਮ ਵਿੱਚ ਫਾਈਲਨਾਮ ਲਈ ਕੋਈ ਵੈਧ ਅੱਖਰ ਨਹੀਂ ਹਨ।',
 'The output name is empty after filename validation.':
   'ਫਾਈਲਨਾਮ ਪ੍ਰਮਾਣਿਕਤਾ ਤੋਂ ਬਾਅਦ ਆਉਟਪੁੱਟ ਨਾਮ ਖਾਲੀ ਹੈ।',
 'The selected features contain no valid geometry.':
   'ਚੁਣੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਵਿੱਚ ਕੋਈ ਵੈਧ ਜਿਓਮੈਟਰੀ ਨਹੀਂ ਹੈ।',
 'The selected output directory does not exist. Choose an existing folder.':
   'ਚੁਣੀ ਆਉਟਪੁੱਟ ਡਾਇਰੈਕਟਰੀ ਮੌਜੂਦ ਨਹੀਂ ਹੈ। ਮੌਜੂਦਾ ਫੋਲਡਰ ਚੁਣੋ।',
 'There is no active download to cancel.':
   'ਰੱਦ ਕਰਨ ਲਈ ਕੋਈ ਸਰਗਰਮ ਡਾਊਨਲੋਡ ਨਹੀਂ ਹੈ।',
 'Timeout on server ': 'ਸਰਵਰ \'ਤੇ ਸਮਾਂ-ਸੀਮਾ: ',
 'Translate widget labels while preserving each original English string.':
   'ਹਰ ਮੂਲ ਅੰਗਰੇਜ਼ੀ ਸਤਰ ਨੂੰ ਬਰਕਰਾਰ ਰੱਖਦੇ ਹੋਏ ਵਿਜੈਟ ਲੇਬਲਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰੋ।',
 'Trying Overpass server ': 'Overpass ਸਰਵਰ ਅਜ਼ਮਾਇਆ ਜਾ ਰਿਹਾ ਹੈ: ',
 'Unable to start AOI drawing:': 'AOI ਡਰਾਇੰਗ ਸ਼ੁਰੂ ਨਹੀਂ ਕਰ ਸਕੇ:',
 'Unclassified OSM elements not written to feature layers:':
   'ਵਿਸ਼ੇਸ਼ਤਾ ਲੇਅਰਾਂ ਵਿੱਚ ਨਾ ਲਿਖੇ ਅਵਰਗੀਕ੍ਰਿਤ OSM ਤੱਤ:',
 'Unsupported geometry family: {geometry_family}':
   'ਗੈਰ-ਸਮਰਥਿਤ ਜਿਓਮੈਟਰੀ ਪਰਿਵਾਰ: {geometry_family}',
 "Unsupported geometry type '{geometry_type}' for feature '{feature_key}'.":
   'ਵਿਸ਼ੇਸ਼ਤਾ "{feature_key}" ਲਈ ਗੈਰ-ਸਮਰਥਿਤ ਜਿਓਮੈਟਰੀ ਕਿਸਮ "{geometry_type}"।',
 'Unsupported geometry type for Shapefile export: {geometry_type}':
   'Shapefile ਨਿਰਯਾਤ ਲਈ ਗੈਰ-ਸਮਰਥਿਤ ਜਿਓਮੈਟਰੀ ਕਿਸਮ: {geometry_type}',
 "Unsupported match mode '{mode}' for feature '{feature_key}'.":
   'ਵਿਸ਼ੇਸ਼ਤਾ "{feature_key}" ਲਈ ਗੈਰ-ਸਮਰਥਿਤ ਮੇਲ ਮੋਡ "{mode}"।',
 'Unsupported output format:': 'ਗੈਰ-ਸਮਰਥਿਤ ਆਉਟਪੁੱਟ ਫਾਰਮੈਟ:',
 "Unsupported tag value type for '{feature_key}': {value_type}":
   '"{feature_key}" ਲਈ ਗੈਰ-ਸਮਰਥਿਤ ਟੈਗ ਮੁੱਲ ਕਿਸਮ: {value_type}',
 'Update Current QGIS Map Extent':
   'ਮੌਜੂਦਾ QGIS ਨਕਸ਼ਾ ਸੀਮਾ ਅੱਪਡੇਟ ਕਰੋ',
 'Update the "N selected" count next to the category heading.':
   'ਸ਼੍ਰੇਣੀ ਸਿਰਲੇਖ ਅੱਗੇ "N ਚੁਣੇ" ਗਿਣਤੀ ਅੱਪਡੇਟ ਕਰੋ।',
 'Update the filename preview as the user edits the components.':
   'ਵਰਤੋਂਕਾਰ ਦੁਆਰਾ ਹਿੱਸੇ ਸੋਧਦੇ ਸਮੇਂ ਫਾਈਲਨਾਮ ਝਲਕ ਅੱਪਡੇਟ ਕਰੋ।',
 'Use Layer Extent': 'ਲੇਅਰ ਸੀਮਾ ਵਰਤੋ',
 'Use Selected Features': 'ਚੁਣੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਵਰਤੋ',
 'Use local cache where available': 'ਜਿੱਥੇ ਉਪਲਬਧ ਹੋਵੇ ਸਥਾਨਕ ਕੈਸ਼ ਵਰਤੋ',
 'Use selected features in the active vector layer as the AOI.':
   'ਸਰਗਰਮ ਵੈਕਟਰ ਲੇਅਰ ਵਿੱਚ ਚੁਣੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਨੂੰ AOI ਵਜੋਂ ਵਰਤੋ।',
 'Use the full extent of the active QGIS layer as the AOI.':
   'ਸਰਗਰਮ QGIS ਲੇਅਰ ਦੀ ਪੂਰੀ ਸੀਮਾ ਨੂੰ AOI ਵਜੋਂ ਵਰਤੋ।',
 'Use the full extent of the active QGIS layer.':
   'ਸਰਗਰਮ QGIS ਲੇਅਰ ਦੀ ਪੂਰੀ ਸੀਮਾ ਵਰਤੋ।',
 'Use the selected features of the active vector layer as the AOI.':
   'ਸਰਗਰਮ ਵੈਕਟਰ ਲੇਅਰ ਦੀਆਂ ਚੁਣੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਨੂੰ AOI ਵਜੋਂ ਵਰਤੋ।',
 'Using cached data; no Overpass network request was needed.':
   'ਕੈਸ਼ ਕੀਤਾ ਡੇਟਾ ਵਰਤਿਆ ਜਾ ਰਿਹਾ ਹੈ; ਕੋਈ Overpass ਨੈੱਟਵਰਕ ਬੇਨਤੀ ਦੀ ਲੋੜ ਨਹੀਂ ਸੀ।',
 'Validate filename and any explicitly selected admin levels.':
   'ਫਾਈਲਨਾਮ ਅਤੇ ਸਪੱਸ਼ਟ ਤੌਰ \'ਤੇ ਚੁਣੇ ਪ੍ਰਸ਼ਾਸਕੀ ਪੱਧਰਾਂ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ।',
 'Validate inputs and start the background Overpass download.':
   'ਇਨਪੁੱਟਾਂ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ ਅਤੇ ਬੈਕਗ੍ਰਾਊਂਡ Overpass ਡਾਊਨਲੋਡ ਸ਼ੁਰੂ ਕਰੋ।',
 'WGS84 AOI bbox: south=': 'WGS84 AOI ਬਾਊਂਡਿੰਗ ਬਾਕਸ: ਦੱਖਣ=',
 'WGS84 AOI geometry is not available.':
   'WGS84 AOI ਜਿਓਮੈਟਰੀ ਉਪਲਬਧ ਨਹੀਂ ਹੈ।',
 'Warning: download succeeded, but the response could not be cached:':
   'ਚੇਤਾਵਨੀ: ਡਾਊਨਲੋਡ ਸਫਲ, ਪਰ ਜਵਾਬ ਕੈਸ਼ ਨਹੀਂ ਕੀਤਾ ਜਾ ਸਕਿਆ:',
 'Waterways': 'ਜਲਮਾਰਗ',
 'West longitude cannot be greater than east longitude.':
   'ਪੱਛਮੀ ਲੰਬਕਾਰ ਪੂਰਬੀ ਲੰਬਕਾਰ ਤੋਂ ਵੱਧ ਨਹੀਂ ਹੋ ਸਕਦਾ।',
 'West:': 'ਪੱਛਮ:',
 'Writing Shapefile {layer_index}/{total}: {layer_name}...':
   'Shapefile {layer_index}/{total} ਲਿਖੀ ਜਾ ਰਹੀ ਹੈ: {layer_name}…',
 'Writing layer {layer_index}/{total}: {layer_name} ({count:,} features)...':
   'ਲੇਅਰ {layer_index}/{total} ਲਿਖੀ ਜਾ ਰਹੀ ਹੈ: {layer_name} ({count:,} ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ)…',
 'attempt ': 'ਕੋਸ਼ਿਸ਼ ',
 'characters).': 'ਅੱਖਰ)।',
 'connection error — ': 'ਕਨੈਕਸ਼ਨ ਗਲਤੀ — ',
 'e.g. CBD': 'ਜਿਵੇਂ CBD',
 'e.g. Kenya': 'ਜਿਵੇਂ ਕੀਨੀਆ',
 'e.g. Nairobi': 'ਜਿਵੇਂ ਨੈਰੋਬੀ',
 'e.g. NairobiCounty': 'ਜਿਵੇਂ NairobiCounty',
 'elements (': 'ਤੱਤ (',
 'export failed:': 'ਨਿਰਯਾਤ ਅਸਫਲ:',
 'feature records).': 'ਵਿਸ਼ੇਸ਼ਤਾ ਰਿਕਾਰਡ)।',
 'feature(s)).': 'ਵਿਸ਼ੇਸ਼ਤਾ(ਵਾਂ))।',
 'features written.': 'ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਲਿਖੀਆਂ ਗਈਆਂ।',
 'file(s) deleted.': 'ਫਾਈਲ(ਾਂ) ਮਿਟਾਈਆਂ ਗਈਆਂ।',
 'relation geometry assignment(s); relation-member geometry assembly is not implemented yet.':
   'ਰਿਲੇਸ਼ਨ ਜਿਓਮੈਟਰੀ ਅਸਾਈਨਮੈਂਟ; ਰਿਲੇਸ਼ਨ-ਮੈਂਬਰ ਜਿਓਮੈਟਰੀ ਅਸੈਂਬਲੀ ਅਜੇ ਲਾਗੂ ਨਹੀਂ ਕੀਤੀ ਗਈ।',
 'relations).': 'ਰਿਲੇਸ਼ਨ)।',
 'response_data must be a dictionary.':
   'response_data ਇੱਕ ਡਿਕਸ਼ਨਰੀ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।',
 "response_data['elements'] must be a list.":
   "response_data['elements'] ਇੱਕ ਸੂਚੀ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ।",
 'temporary file(s) could not be deleted. They may still be in use by QGIS or another process.':
   'ਅਸਥਾਈ ਫਾਈਲ(ਾਂ) ਮਿਟਾਈਆਂ ਨਹੀਂ ਜਾ ਸਕੀਆਂ। ਉਹ QGIS ਜਾਂ ਕਿਸੇ ਹੋਰ ਪ੍ਰਕਿਰਿਆ ਦੁਆਰਾ ਅਜੇ ਵੀ ਵਰਤੋਂ ਵਿੱਚ ਹੋ ਸਕਦੀਆਂ ਹਨ।',
 'timeout — ': 'ਸਮਾਂ-ਸੀਮਾ — ',
 '{output_format} export failed: {error}':
   '{output_format} ਨਿਰਯਾਤ ਅਸਫਲ: {error}',
 '— Confirm Overwrite': '— ਉੱਤੇ ਲਿਖਣ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ',
 '— Export Error': '— ਨਿਰਯਾਤ ਗਲਤੀ',
 '— Help': '— ਮਦਦ',
 '— Output Naming': '— ਆਉਟਪੁੱਟ ਨਾਮਕਰਨ',
}