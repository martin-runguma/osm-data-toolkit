"""Tamil (தமிழ்) translation pack for the OSM Data Toolkit plugin.
Keys remain the English source strings; preserve placeholders and HTML."""
TEXT = {
 '\n<h3>Quick start</h3>\n<ol>\n  <li><b>Choose an area.</b> Use the current map extent, draw a rectangle\n      on the map, or use the bounding box of selected features or a\n      layer\'s extent.</li>\n  <li><b>Tick the OSM categories</b> you need (POI, stops, roads,\n      buildings, boundaries, landuse, ...).</li>\n  <li><b>Choose an output format and folder</b>, then click\n      <b>Download OSM Data</b>.</li>\n</ol>\n\n<h3>Good to know</h3>\n<ul>\n  <li><b>GeoPackage is recommended.</b> A Shapefile cannot hold very many\n      attribute columns, so on large areas some rarely used tag columns\n      may be left out (the log tells you when this happens).</li>\n  <li><b>Keep the area focused.</b> Very large areas produce huge Overpass\n      responses and can be slow or rejected by the public servers.</li>\n  <li><b>The cache</b> lets repeat downloads of the same query reuse\n      earlier results.</li>\n  <li><b>"Unclassified OSM elements"</b> in the log is informational: they\n      are mostly untagged vertices of lines and polygons that do not belong\n      to any selected category.</li>\n</ul>\n\n<p>Data &copy; OpenStreetMap contributors, available under the\n<a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a>.</p>\n<p><i>This plugin is not endorsed by or affiliated with the\nOpenStreetMap Foundation.</i></p>\n':
 '\n<h3>விரைவு தொடக்கம்</h3>\n<ol>\n  <li><b>ஒரு பகுதியைத் தேர்ந்தெடுக்கவும்.</b> தற்போதைய வரைபட எல்லையைப் பயன்படுத்தவும்,\n      வரைபடத்தில் ஒரு செவ்வகத்தை வரையவும், அல்லது தேர்ந்தெடுக்கப்பட்ட\n      அம்சங்கள் அல்லது அடுக்கின் எல்லையின் எல்லைப்பெட்டியைப்\n      பயன்படுத்தவும்.</li>\n  <li><b>உங்களுக்குத் தேவையான OSM வகைகளைத் தேர்ந்தெடுக்கவும்</b> (POI, நிறுத்தங்கள்,\n      சாலைகள், கட்டிடங்கள், எல்லைகள், நிலப் பயன்பாடு, ...).</li>\n  <li><b>வெளியீட்டு வடிவமைப்பு மற்றும் கோப்புறையைத் தேர்ந்தெடுக்கவும்</b>, பின்னர்\n      <b>OSM தரவைப் பதிவிறக்கு</b> என்பதைக் கிளிக் செய்யவும்.</li>\n</ol>\n\n<h3>தெரிந்து கொள்ள வேண்டியவை</h3>\n<ul>\n  <li><b>GeoPackage பரிந்துரைக்கப்படுகிறது.</b> Shapefile-ஆல் மிக அதிகமான\n      பண்புக்கூறு நெடுவரிசைகளை வைத்திருக்க முடியாது, எனவே பெரிய பகுதிகளில்\n      சில அரிதாகப் பயன்படுத்தப்படும் குறிச்சொல் நெடுவரிசைகள் விடுபடலாம்\n      (இது நிகழும்போது பதிவு உங்களுக்குத் தெரிவிக்கும்).</li>\n  <li><b>பகுதியைக் கவனம் செலுத்தி வைத்திருங்கள்.</b> மிகப் பெரிய பகுதிகள்\n      பெரிய Overpass பதில்களை உருவாக்கும், மேலும் பொது சேவையகங்களால்\n      மெதுவாக்கப்படலாம் அல்லது நிராகரிக்கப்படலாம்.</li>\n  <li><b>தற்காலிகச் சேமிப்பு</b> ஒரே வினவலின் மீள்பதிவிறக்கங்கள்\n      முந்தைய முடிவுகளை மீண்டும் பயன்படுத்த அனுமதிக்கிறது.</li>\n  <li>பதிவில் உள்ள <b>"வகைப்படுத்தப்படாத OSM கூறுகள்"</b> என்பது தகவலுக்கானது:\n      அவை பெரும்பாலும் எந்தத் தேர்ந்தெடுக்கப்பட்ட வகைக்கும் சொந்தமில்லாத\n      குறிச்சொல் இல்லாத கோடுகள் மற்றும் பலகோணங்களின் முனைகளாகும்.</li>\n</ul>\n\n<p>தரவு &copy; OpenStreetMap பங்களிப்பாளர்கள், <a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a> கீழ் கிடைக்கிறது.</p>\n<p><i>இந்தச் செருகல் OpenStreetMap Foundation ஆல் அங்கீகரிக்கப்படவில்லை அல்லது அதனுடன் இணைக்கப்படவில்லை.</i></p>\n',
 ' responded successfully.': ' வெற்றிகரமாக பதிலளித்தது.',
 ' seconds...': ' வினாடிகள்…',
 '" style="color:#0B5E8E; text-decoration:none;">OpenStreetMap contributors</a> (ODbL)':
   '" style="color:#0B5E8E; text-decoration:none;">OpenStreetMap பங்களிப்பாளர்கள்</a> (ODbL)',
 ', east=': ', கிழக்கு=',
 ', north=': ', வடக்கு=',
 ', west=': ', மேற்கு=',
 '0 selected': '0 தேர்ந்தெடுக்கப்பட்டது',
 '<p>Plugin version': '<p>செருகல் பதிப்பு',
 'A download is already running.': 'ஒரு பதிவிறக்கம் ஏற்கனவே இயங்குகிறது.',
 'A labelled column of feature checkboxes.':
   'அம்ச தேர்வுப்பெட்டிகளின் லேபிளிடப்பட்ட நெடுவரிசை.',
 'AOI drawing cancelled.': 'AOI வரைதல் ரத்து செய்யப்பட்டது.',
 'AOI geometry is empty.': 'AOI வடிவியல் காலியாக உள்ளது.',
 'AOI geometry is missing.': 'AOI வடிவியல் இல்லை.',
 'AOI name': 'AOI பெயர்',
 'AOI rectangle captured successfully.':
   'AOI செவ்வகம் வெற்றிகரமாகப் பிடிக்கப்பட்டது.',
 'AOI source CRS is invalid.': 'AOI மூல CRS தவறானது.',
 'AOI validation failed:': 'AOI சரிபார்ப்பு தோல்வியடைந்தது:',
 'AOI:': 'AOI:',
 'AOI: QGIS interface is not available.':
   'AOI: QGIS இடைமுகம் கிடைக்கவில்லை.',
 "AOI: click 'Draw AOI', then drag a rectangle on the QGIS map.":
   'AOI: "AOI வரையவும்" என்பதைக் கிளிக் செய்து, QGIS வரைபடத்தில் ஒரு செவ்வகத்தை இழுக்கவும்.',
 "AOI: click 'Use Layer Extent' to use the full extent of the active QGIS layer.":
   'AOI: செயலில் உள்ள QGIS அடுக்கின் முழு எல்லையைப் பயன்படுத்த "அடுக்கு எல்லையைப் பயன்படுத்து" என்பதைக் கிளிக் செய்யவும்.',
 'AOI: click and drag on the QGIS map.':
   'AOI: QGIS வரைபடத்தில் கிளிக் செய்து இழுக்கவும்.',
 'AOI: failed to resolve active layer extent':
   'AOI: செயலில் உள்ள அடுக்கு எல்லையைத் தீர்மானிக்க முடியவில்லை',
 'AOI: failed to resolve selected features':
   'AOI: தேர்ந்தெடுக்கப்பட்ட அம்சங்களைத் தீர்மானிக்க முடியவில்லை',
 'AOI: invalid': 'AOI: தவறானது',
 'AOI: no active QGIS layer.': 'AOI: செயலில் உள்ள QGIS அடுக்கு இல்லை.',
 'AOI: no feature(s) selected in the active layer.':
   'AOI: செயலில் உள்ள அடுக்கில் எந்த அம்சமும் தேர்ந்தெடுக்கப்படவில்லை.',
 'AOI: not yet resolved': 'AOI: இன்னும் தீர்மானிக்கப்படவில்லை',
 "AOI: select feature(s) in the active QGIS layer, then click 'Use Selected Features'.":
   'AOI: செயலில் உள்ள QGIS அடுக்கில் அம்சங்களைத் தேர்ந்தெடுத்து, பின்னர் "தேர்ந்தெடுத்த அம்சங்களைப் பயன்படுத்து" என்பதைக் கிளிக் செய்யவும்.',
 'AOI: the active layer is not a vector layer.':
   'AOI: செயலில் உள்ள அடுக்கு திசையன் அடுக்கு அல்ல.',
 'AOI: unable to create': 'AOI: உருவாக்க முடியவில்லை',
 'AOI: unable to resolve': 'AOI: தீர்மானிக்க முடியவில்லை',
 'Activate the interactive rectangle AOI map tool.':
   'ஊடாடும் செவ்வக AOI வரைபடக் கருவியை இயக்கவும்.',
 'Active layer extent': 'செயலில் உள்ள அடுக்கு எல்லை',
 'Active-layer extent AOI is invalid.':
   'செயலில் உள்ள அடுக்கு எல்லை AOI தவறானது.',
 'Active-layer extent captured successfully.':
   'செயலில் உள்ள அடுக்கு எல்லை வெற்றிகரமாகப் பிடிக்கப்பட்டது.',
 'Active-layer extent validation failed:':
   'செயலில் உள்ள அடுக்கு எல்லை சரிபார்ப்பு தோல்வியடைந்தது:',
 'Administrative boundaries': 'நிர்வாக எல்லைகள்',
 'Administrative boundary filter: all levels (no admin_level filter).':
   'நிர்வாக எல்லை வடிகட்டி: அனைத்து நிலைகளும் (admin_level வடிகட்டி இல்லை).',
 'Administrative boundary levels': 'நிர்வாக எல்லை நிலைகள்',
 'Administrative boundary levels:': 'நிர்வாக எல்லை நிலைகள்:',
 'Administrative levels must be an integer, a numeric string, a sequence of levels, or None.':
   'நிர்வாக நிலைகள் முழு எண், எண்ணியல் சரம், நிலைகளின் வரிசை அல்லது None ஆக இருக்க வேண்டும்.',
 'All OSM feature categories cleared.': 'அனைத்து OSM அம்ச வகைகளும் அழிக்கப்பட்டன.',
 'All OSM feature categories selected.': 'அனைத்து OSM அம்ச வகைகளும் தேர்ந்தெடுக்கப்பட்டன.',
 'All Overpass server URLs must be non-empty strings.':
   'அனைத்து Overpass சேவையக URL-களும் காலியாக இல்லாத சரங்களாக இருக்க வேண்டும்.',
 'All Overpass servers and retry attempts failed.':
   'அனைத்து Overpass சேவையகங்களும் மறுமுயற்சிகளும் தோல்வியடைந்தன.',
 'All administrative levels will be included.':
   'அனைத்து நிர்வாக நிலைகளும் சேர்க்கப்படும்.',
 'All administrative levels will be included; no admin_level filter will be added to the query.':
   'அனைத்து நிர்வாக நிலைகளும் சேர்க்கப்படும்; வினவலில் admin_level வடிகட்டி சேர்க்கப்படாது.',
 'All attempts failed for server ': 'சேவையகத்திற்கான அனைத்து முயற்சிகளும் தோல்வியடைந்தன ',
 'All levels (0–15; no admin_level filter)':
   'அனைத்து நிலைகளும் (0–15; admin_level வடிகட்டி இல்லை)',
 'An existing output directory is required for Shapefile export.':
   'Shapefile ஏற்றுமதிக்கு இருக்கும் வெளியீட்டு கோப்புறை தேவை.',
 'An output GeoPackage path is required.':
   'வெளியீட்டு GeoPackage பாதை தேவை.',
 'An output name is required for Shapefile export.':
   'Shapefile ஏற்றுமதிக்கு வெளியீட்டு பெயர் தேவை.',
 'Append a timestamped message to the processing log.':
   'செயலாக்கப் பதிவில் நேரமுத்திரையுடன் ஒரு செய்தியைச் சேர்க்கவும்.',
 'Append an exported feature count to the processing log.':
   'செயலாக்கப் பதிவில் ஏற்றுமதி செய்யப்பட்ட அம்சங்களின் எண்ணிக்கையைச் சேர்க்கவும்.',
 'Area of Interest': 'ஆர்வப் பகுதி',
 'At least one OSM feature must be selected.':
   'குறைந்தது ஒரு OSM அம்சம் தேர்ந்தெடுக்கப்பட வேண்டும்.',
 'At least one OSM feature must be supplied.':
   'குறைந்தது ஒரு OSM அம்சம் வழங்கப்பட வேண்டும்.',
 'At least one Overpass server must be provided.':
   'குறைந்தது ஒரு Overpass சேவையகம் வழங்கப்பட வேண்டும்.',
 'Attempt details:': 'முயற்சி விவரங்கள்:',
 'Automatically add downloaded layers to QGIS':
   'பதிவிறக்கப்பட்ட அடுக்குகளை QGIS-ல் தானாகச் சேர்க்கவும்',
 'Background Overpass download started.':
   'பின்னணி Overpass பதிவிறக்கம் தொடங்கியது.',
 'Browse': 'உலாவு',
 'Browse…': 'உலாவு…',
 'Buildings': 'கட்டிடங்கள்',
 'Bus stops': 'பேருந்து நிறுத்தங்கள்',
 'CRS:': 'CRS:',
 'Cache hit:': 'தற்காலிகச் சேமிப்பு இணக்கம்:',
 'Cache hit: using saved Overpass response ({age} day(s) old).':
   'தற்காலிகச் சேமிப்பு இணக்கம்: சேமிக்கப்பட்ட Overpass பதிலைப் பயன்படுத்துகிறது ({age} நாள்(கள்) பழையது).',
 'Cache miss:': 'தற்காலிகச் சேமிப்பு தவறவிட்டது:',
 'Cache miss: could not read saved response ({error}).':
   'தற்காலிகச் சேமிப்பு தவறவிட்டது: சேமிக்கப்பட்ட பதிலைப் படிக்க முடியவில்லை ({error}).',
 'Cache miss: query hash does not match the saved response.':
   'தற்காலிகச் சேமிப்பு தவறவிட்டது: வினவல் ஹாஷ் சேமிக்கப்பட்ட பதிலுடன் பொருந்தவில்லை.',
 'Cache miss: saved response is incomplete or invalid.':
   'தற்காலிகச் சேமிப்பு தவறவிட்டது: சேமிக்கப்பட்ட பதில் முழுமையற்றது அல்லது தவறானது.',
 'Cache miss: saved response is older than {days} days.':
   'தற்காலிகச் சேமிப்பு தவறவிட்டது: சேமிக்கப்பட்ட பதில் {days} நாட்களுக்கு மேல் பழையது.',
 'Cache miss: saved response uses an unsupported cache format.':
   'தற்காலிகச் சேமிப்பு தவறவிட்டது: சேமிக்கப்பட்ட பதில் ஆதரிக்கப்படாத தற்காலிகச் சேமிப்பு வடிவமைப்பைப் பயன்படுத்துகிறது.',
 'Cached Overpass response:': 'தற்காலிகச் சேமிப்பில் உள்ள Overpass பதில்:',
 'Cancel': 'ரத்து செய்',
 'Cancellation has already been requested.': 'ரத்து செய்யும் கோரிக்கை ஏற்கனவே அனுப்பப்பட்டுள்ளது.',
 'Cancellation requested': 'ரத்து செய்யக் கோரப்பட்டது',
 'Cancellation requested. If an HTTP request is already active, the downloader will stop when that request returns or times out.':
   'ரத்து செய்யக் கோரப்பட்டது. HTTP கோரிக்கை ஏற்கனவே செயலில் இருந்தால், அந்தக் கோரிக்கை திரும்பும்போது அல்லது நேரம் முடிவடையும்போது பதிவிறக்கி நிற்கும்.',
 'Cancellation requested; waiting for the current request to finish...':
   'ரத்து செய்யக் கோரப்பட்டது; தற்போதைய கோரிக்கை முடியும் வரை காத்திருக்கிறது…',
 'Cannot draw AOI because the QGIS interface is unavailable.':
   'QGIS இடைமுகம் கிடைக்காததால் AOI வரைய முடியவில்லை.',
 'Cannot resolve active-layer extent because QGIS is unavailable.':
   'QGIS கிடைக்காததால் செயலில் உள்ள அடுக்கு எல்லையைத் தீர்மானிக்க முடியவில்லை.',
 'Cannot resolve current map extent because QGIS is unavailable.':
   'QGIS கிடைக்காததால் தற்போதைய வரைபட எல்லையைத் தீர்மானிக்க முடியவில்லை.',
 'Cannot resolve selected-feature AOI because QGIS is unavailable.':
   'QGIS கிடைக்காததால் தேர்ந்தெடுத்த அம்ச AOI-ஐத் தீர்மானிக்க முடியவில்லை.',
 'Cannot transform an empty geometry.':
   'காலியான வடிவியலை மாற்ற முடியாது.',
 'Capture the current QGIS map canvas extent.':
   'தற்போதைய QGIS வரைபட கேன்வாஸ் எல்லையைப் பிடிக்கவும்.',
 'Choose all available levels, or select one or more levels to download (for example, 5–8 or level 5).':
   'கிடைக்கக்கூடிய அனைத்து நிலைகளையும் தேர்ந்தெடுக்கவும் அல்லது பதிவிறக்க ஒன்று அல்லது அதற்கு மேற்பட்ட நிலைகளைத் தேர்ந்தெடுக்கவும் (எடுத்துக்காட்டாக, 5–8 அல்லது நிலை 5).',
 'Choose an output directory before downloading.':
   'பதிவிறக்குவதற்கு முன் வெளியீட்டு கோப்புறையைத் தேர்ந்தெடுக்கவும்.',
 'City name': 'நகரப் பெயர்',
 'Classifying OSM elements and preparing GeoPackage layers.':
   'OSM கூறுகளை வகைப்படுத்தி GeoPackage அடுக்குகளைத் தயார் செய்கிறது.',
 'Classifying OSM elements and preparing Shapefile outputs.':
   'OSM கூறுகளை வகைப்படுத்தி Shapefile வெளியீடுகளைத் தயார் செய்கிறது.',
 'Clear all': 'அனைத்தையும் அழி',
 'Clear log': 'பதிவை அழி',
 'Clear only the visible log, without changing processing settings.':
   'செயலாக்க அமைப்புகளை மாற்றாமல் தெரியும் பதிவை மட்டும் அழிக்கவும்.',
 'Clear selected levels so the user can make a narrower selection.':
   'பயனர் குறுகிய தேர்வைச் செய்ய, தேர்ந்தெடுக்கப்பட்ட நிலைகளை அழிக்கவும்.',
 'Clear the messages currently shown in the Processing Log.':
   'செயலாக்கப் பதிவில் தற்போது காட்டப்படும் செய்திகளை அழிக்கவும்.',
 'Clear the previous AOI and display guidance for the chosen method.':
   'முந்தைய AOI-ஐ அழித்து தேர்ந்தெடுத்த முறைக்கான வழிகாட்டலைக் காட்டவும்.',
 'Close': 'மூடு',
 'Collect optional filename components before exporting OSM data.':
   'OSM தரவை ஏற்றுமதி செய்வதற்கு முன் விருப்பமான கோப்புப்பெயர் கூறுகளைச் சேகரிக்கவும்.',
 'Compact product header above the scrollable workflow.':
   'ஸ்க்ரோல் செய்யக்கூடிய பணிப்பாய்வுக்கு மேலே சுருக்கமான தயாரிப்பு தலைப்பு.',
 'Connection error on server ': 'சேவையகத்தில் இணைப்புப் பிழை ',
 'Continue to Download': 'பதிவிறக்கத்திற்குத் தொடரவும்',
 'Convert a name component into a Windows-safe filename token.':
   'பெயர் கூறை Windows-பாதுகாப்பான கோப்புப்பெயர் டோக்கனாக மாற்றவும்.',
 'Convert the drawn rectangle into the standard AOI object.':
   'வரையப்பட்ட செவ்வகத்தை நிலையான AOI பொருளாக மாற்றவும்.',
 'Converting OSM response to GeoPackage...':
   'OSM பதிலை GeoPackage ஆக மாற்றுகிறது…',
 'Converting OSM response to Shapefiles...':
   'OSM பதிலை Shapefile ஆக மாற்றுகிறது…',
 'Could not combine the selected feature geometries.':
   'தேர்ந்தெடுத்த அம்ச வடிவியல்களை இணைக்க முடியவில்லை.',
 "Could not create Shapefile staging layer '{layer_name}'.":
   'Shapefile இடைநிலை அடுக்கு "{layer_name}"-ஐ உருவாக்க முடியவில்லை.',
 'Could not create an empty bus_stops_points layer.':
   'காலியான bus_stops_points அடுக்கை உருவாக்க முடியவில்லை.',
 "Could not create temporary QGIS layer '{layer_name}'.":
   'தற்காலிக QGIS அடுக்கு "{layer_name}"-ஐ உருவாக்க முடியவில்லை.',
 'Could not create temporary layer for admin_level {admin_level}.':
   'admin_level {admin_level} க்கான தற்காலிக அடுக்கை உருவாக்க முடியவில்லை.',
 'Could not create the merged bus_stops_points layer.':
   'இணைக்கப்பட்ட bus_stops_points அடுக்கை உருவாக்க முடியவில்லை.',
 'Could not delete temporary file': 'தற்காலிக கோப்பை நீக்க முடியவில்லை',
 "Could not load feature definition '{feature_key}': {error}":
   'அம்ச வரையறை "{feature_key}"-ஐ ஏற்ற முடியவில்லை: {error}',
 'Could not merge bus-station centroids into bus-stop points.':
   'பேருந்து நிலைய மையப்புள்ளிகளை பேருந்து நிறுத்தப் புள்ளிகளில் இணைக்க முடியவில்லை.',
 'Could not overwrite existing output file: {error}':
   'இருக்கும் வெளியீட்டு கோப்பை மேலெழுத முடியவில்லை: {error}',
 'Could not populate Shapefile for admin_level {admin_level}.':
   'admin_level {admin_level} க்கான Shapefile-ஐ நிரப்ப முடியவில்லை.',
 "Could not populate temporary layer '{layer_name}'.":
   'தற்காலிக அடுக்கு "{layer_name}"-ஐ நிரப்ப முடியவில்லை.',
 'Could not prepare the Overpass query:':
   'Overpass வினவலைத் தயார் செய்ய முடியவில்லை:',
 "Could not reopen intermediate GeoPackage layer '{layer_name}'.":
   'இடைநிலை GeoPackage அடுக்கு "{layer_name}"-ஐ மீண்டும் திறக்க முடியவில்லை.',
 'Could not restore previous QGIS map tool:':
   'முந்தைய QGIS வரைபடக் கருவியை மீட்டெடுக்க முடியவில்லை:',
 'Could not search for temporary GeoPackages:':
   'தற்காலிக GeoPackage-களைத் தேட முடியவில்லை:',
 'Country name': 'நாட்டின் பெயர்',
 'Create one section panel and return it with its body layout.':
   'ஒரு பிரிவு பேனலை உருவாக்கி அதன் உள்ளடக்க தளவமைப்புடன் திருப்பித் தரவும்.',
 'Created bus_stops_points from bus-station polygon centroids.':
   'பேருந்து நிலைய பலகோண மையப்புள்ளிகளிலிருந்து bus_stops_points உருவாக்கப்பட்டது.',
 'Current QGIS map extent': 'தற்போதைய QGIS வரைபட எல்லை',
 'Current QGIS map extent resolved.':
   'தற்போதைய QGIS வரைபட எல்லை தீர்மானிக்கப்பட்டது.',
 'Data © <a href="': 'தரவு © <a href="',
 'Deleted temporary workspace file:':
   'தற்காலிக பணியிடக் கோப்பு நீக்கப்பட்டது:',
 'Details:': 'விவரங்கள்:',
 'Download': 'பதிவிறக்கு',
 'Download OSM Data': 'OSM தரவைப் பதிவிறக்கு',
 'Download OpenStreetMap data for any area and load it straight into QGIS.':
   'எந்தப் பகுதிக்கும் OpenStreetMap தரவைப் பதிவிறக்கி நேரடியாக QGIS-ல் ஏற்றவும்.',
 'Download cancelled because existing output files were not approved for overwrite.':
   'இருக்கும் வெளியீட்டு கோப்புகள் மேலெழுத அனுமதிக்கப்படாததால் பதிவிறக்கம் ரத்து செய்யப்பட்டது.',
 'Download cancelled before it started.':
   'தொடங்குவதற்கு முன் பதிவிறக்கம் ரத்து செய்யப்பட்டது.',
 'Download cancelled before results were returned.':
   'முடிவுகள் திரும்பும் முன் பதிவிறக்கம் ரத்து செய்யப்பட்டது.',
 'Download cancelled before starting.':
   'தொடங்குவதற்கு முன் பதிவிறக்கம் ரத்து செய்யப்பட்டது.',
 'Download cancelled in the output-naming dialog.':
   'வெளியீட்டு பெயரிடல் உரையாடலில் பதிவிறக்கம் ரத்து செய்யப்பட்டது.',
 'Download cancelled.': 'பதிவிறக்கம் ரத்து செய்யப்பட்டது.',
 'Download cancelled; existing files preserved.':
   'பதிவிறக்கம் ரத்து செய்யப்பட்டது; இருக்கும் கோப்புகள் பாதுகாக்கப்பட்டன.',
 'Download stopped.': 'பதிவிறக்கம் நிறுத்தப்பட்டது.',
 'Download succeeded, but export failed.':
   'பதிவிறக்கம் வெற்றிகரமானது, ஆனால் ஏற்றுமதி தோல்வியடைந்தது.',
 'Downloading OSM data from Overpass...':
   'Overpass-இலிருந்து OSM தரவைப் பதிவிறக்குகிறது…',
 'Draw AOI': 'AOI வரையவும்',
 'Draw a rectangle on the QGIS map to define the AOI.':
   'AOI-ஐ வரையறுக்க QGIS வரைபடத்தில் ஒரு செவ்வகத்தை வரையவும்.',
 'Draw rectangle on map': 'வரைபடத்தில் செவ்வகம் வரையவும்',
 'Draw the AOI rectangle on the QGIS map.':
   'QGIS வரைபடத்தில் AOI செவ்வகத்தை வரையவும்.',
 'Drawn AOI validation failed:':
   'வரையப்பட்ட AOI சரிபார்ப்பு தோல்வியடைந்தது:',
 'Drawn rectangle': 'வரையப்பட்ட செவ்வகம்',
 'Drawn rectangle AOI captured successfully.':
   'வரையப்பட்ட செவ்வக AOI வெற்றிகரமாகப் பிடிக்கப்பட்டது.',
 'ERROR:': 'பிழை:',
 'East:': 'கிழக்கு:',
 'Enable level checkboxes only when a specific selection is active.':
   'குறிப்பிட்ட தேர்வு செயலில் இருக்கும்போது மட்டும் நிலை தேர்வுப்பெட்டிகளை இயக்கவும்.',
 'Enable only the AOI action button for the selected method.':
   'தேர்ந்தெடுத்த முறைக்கு AOI செயல் பொத்தானை மட்டும் இயக்கவும்.',
 'Enable or disable controls while a download is running.':
   'பதிவிறக்கம் இயங்கும்போது கட்டுப்பாடுகளை இயக்கவும் அல்லது முடக்கவும்.',
 'Enter at least one name (City, Country, Region, or AOI).':
   'குறைந்தது ஒரு பெயரை உள்ளிடவும் (நகரம், நாடு, பிராந்தியம் அல்லது AOI).',
 'Enter one or more name components. Blank fields will be skipped, and the remaining names will be joined with underscores. The selected output format will be retained.':
   'ஒன்று அல்லது அதற்கு மேற்பட்ட பெயர் கூறுகளை உள்ளிடவும். காலியான புலங்கள் தவிர்க்கப்படும், மீதமுள்ள பெயர்கள் அடிக்கோடுகளுடன் இணைக்கப்படும். தேர்ந்தெடுத்த வெளியீட்டு வடிவமைப்பு தக்கவைக்கப்படும்.',
 'Enter_a_name_to_preview': 'முன்னோட்டத்திற்கு_ஒரு_பெயரை_உள்ளிடவும்',
 'Export cancelled: output name is missing.':
   'ஏற்றுமதி ரத்து: வெளியீட்டு பெயர் இல்லை.',
 'Export complete:': 'ஏற்றுமதி முடிந்தது:',
 'Export the downloaded response and optionally load its layers.':
   'பதிவிறக்கப்பட்ட பதிலை ஏற்றுமதி செய்து விருப்பமாக அதன் அடுக்குகளை ஏற்றவும்.',
 'Failed to activate rectangle AOI tool:':
   'செவ்வக AOI கருவியை இயக்கத் தவறியது:',
 'Failed to create AOI.': 'AOI உருவாக்கத் தவறியது.',
 'Failed to process drawn rectangle AOI:':
   'வரையப்பட்ட செவ்வக AOI-ஐச் செயலாக்கத் தவறியது:',
 'Failed to resolve active-layer extent.':
   'செயலில் உள்ள அடுக்கு எல்லையைத் தீர்மானிக்கத் தவறியது.',
 'Failed to resolve active-layer extent:':
   'செயலில் உள்ள அடுக்கு எல்லையைத் தீர்மானிக்கத் தவறியது:',
 'Failed to resolve current QGIS map extent:':
   'தற்போதைய QGIS வரைபட எல்லையைத் தீர்மானிக்கத் தவறியது:',
 'Failed to resolve selected-feature AOI.':
   'தேர்ந்தெடுத்த-அம்ச AOI-ஐத் தீர்மானிக்கத் தவறியது.',
 'Failed to resolve selected-feature AOI:':
   'தேர்ந்தெடுத்த-அம்ச AOI-ஐத் தீர்மானிக்கத் தவறியது:',
 "Failed to write layer '{layer_name}' to '{output_path}': {error}":
   'அடுக்கு "{layer_name}"-ஐ "{output_path}"-ல் எழுதத் தவறியது: {error}',
 "Feature '{feature_key}' has no tag definitions.":
   'அம்சம் "{feature_key}"-ல் குறிச்சொல் வரையறைகள் இல்லை.',
 'Feature specification  does not expose a tag-filter mapping.':
   'அம்ச விவரக்குறிப்பு குறிச்சொல்-வடிகட்டி மேப்பிங்கை வெளிப்படுத்தவில்லை.',
 'Ferry stops': 'படகு நிறுத்தங்கள்',
 'Filename preview': 'கோப்புப்பெயர் முன்னோட்டம்',
 'Full documentation': 'முழு ஆவணங்கள்',
 'Generated Overpass query (': 'உருவாக்கப்பட்ட Overpass வினவல் (',
 'GeoPackage': 'GeoPackage',
 'GeoPackage layer(s) to QGIS.': 'GeoPackage அடுக்கு(கள்) QGIS-ல்.',
 'GeoPackage saved:': 'GeoPackage சேமிக்கப்பட்டது:',
 'HTTP error on server ': 'சேவையகத்தில் HTTP பிழை ',
 'HTTP error — ': 'HTTP பிழை — ',
 'HTTP {status} error on server {index}/{total}.':
   'சேவையகம் {index}/{total}-ல் HTTP {status} பிழை.',
 'Handle a drawing tool deactivation initiated outside this dialog.':
   'இந்த உரையாடலுக்கு வெளியே தொடங்கப்பட்ட வரைதல் கருவி முடக்கத்தைக் கையாளவும்.',
 'Help': 'உதவி',
 'Invalid east longitude: {value}':
   'தவறான கிழக்கு தீர்க்கரேகை: {value}',
 'Invalid north latitude: {value}':
   'தவறான வடக்கு அட்சரேகை: {value}',
 'Invalid response from server ': 'சேவையகத்திலிருந்து தவறான பதில் ',
 'Invalid south latitude: {value}':
   'தவறான தெற்கு அட்சரேகை: {value}',
 'Invalid west longitude: {value}':
   'தவறான மேற்கு தீர்க்கரேகை: {value}',
 'Keep the numeric readout in step with the progress bar.':
   'எண் அளவீட்டை முன்னேற்றப் பட்டியுடன் ஒத்திசைவாக வைத்திருங்கள்.',
 'Land & built environment': 'நிலம் மற்றும் கட்டப்பட்ட சூழல்',
 'Landuse': 'நிலப் பயன்பாடு',
 'Language:': 'மொழி:',
 'Linear features': 'நேரியல் அம்சங்கள்',
 'Load the saved interface language and translate visible UI strings.':
   'சேமிக்கப்பட்ட இடைமுக மொழியை ஏற்றி, தெரியும் UI சரங்களை மொழிபெயர்க்கவும்.',
 'Local response cache is disabled.':
   'உள்ளூர் பதில் தற்காலிகச் சேமிப்பு முடக்கப்பட்டுள்ளது.',
 'Main OSM Data Toolkit window.': 'முதன்மை OSM Data Toolkit சாளரம்.',
 'Manually capture the map extent after the user pans or zooms.':
   'பயனர் நகர்த்திய அல்லது பெரிதாக்கிய பிறகு வரைபட எல்லையை கைமுறையாகப் பிடிக்கவும்.',
 'Merged bus-station polygon centroids into bus_stops_points.':
   'பேருந்து நிலைய பலகோண மையப்புள்ளிகள் bus_stops_points-ல் இணைக்கப்பட்டன.',
 'No Overpass selectors were generated.':
   'Overpass தேர்வான்கள் எதுவும் உருவாக்கப்படவில்லை.',
 'No active QGIS layer is available.':
   'செயலில் உள்ள QGIS அடுக்கு எதுவும் கிடைக்கவில்லை.',
 'No active layer is available.':
   'செயலில் உள்ள அடுக்கு எதுவும் கிடைக்கவில்லை.',
 'No exportable features matched the selected categories. Try another AOI or select additional OSM feature categories.':
   'ஏற்றுமதி செய்யக்கூடிய அம்சங்கள் எதுவும் தேர்ந்தெடுத்த வகைகளுடன் பொருந்தவில்லை. வேறு AOI-ஐ முயற்சிக்கவும் அல்லது கூடுதல் OSM அம்ச வகைகளைத் தேர்ந்தெடுக்கவும்.',
 'No features are selected in the active layer.':
   'செயலில் உள்ள அடுக்கில் எந்த அம்சமும் தேர்ந்தெடுக்கப்படவில்லை.',
 'No levels selected. Select at least one level to continue.':
   'எந்த நிலையும் தேர்ந்தெடுக்கப்படவில்லை. தொடர குறைந்தது ஒரு நிலையைத் தேர்ந்தெடுக்கவும்.',
 'No selected features found.':
   'தேர்ந்தெடுக்கப்பட்ட அம்சங்கள் எதுவும் கிடைக்கவில்லை.',
 'No valid Area of Interest is available. Select an AOI method and resolve the AOI before downloading.':
   'சரியான ஆர்வப் பகுதி எதுவும் கிடைக்கவில்லை. பதிவிறக்குவதற்கு முன் AOI முறையைத் தேர்ந்தெடுத்து AOI-ஐத் தீர்மானிக்கவும்.',
 'North:': 'வடக்கு:',
 'Note: {layer_name} has too many tag columns for one Shapefile (DBF size limit); {count} rarely-used columns were left out.':
   'குறிப்பு: {layer_name}-ல் ஒரு Shapefile-க்கு மிக அதிகமான குறிச்சொல் நெடுவரிசைகள் உள்ளன (DBF அளவு வரம்பு); {count} அரிதாகப் பயன்படுத்தப்படும் நெடுவரிசைகள் விடுபட்டன.',
 'OSM Data Toolkit': 'OSM Data Toolkit',
 'OSM Data Toolkit initialised.':
   'OSM Data Toolkit தொடங்கப்பட்டது.',
 'OSM Feature Categories': 'OSM அம்ச வகைகள்',
 'OSM export completed successfully.':
   'OSM ஏற்றுமதி வெற்றிகரமாக முடிந்தது.',
 'One or more output files with this name already exist. Do you want to overwrite the matching output files?':
   'இந்தப் பெயரில் ஒன்று அல்லது அதற்கு மேற்பட்ட வெளியீட்டு கோப்புகள் ஏற்கனவே உள்ளன. பொருந்தும் வெளியீட்டு கோப்புகளை மேலெழுத விரும்புகிறீர்களா?',
 'Only the selected levels': 'தேர்ந்தெடுத்த நிலைகள் மட்டும்',
 'Only validated Overpass responses can be cached.':
   'சரிபார்க்கப்பட்ட Overpass பதில்களை மட்டுமே தற்காலிகச் சேமிப்பில் வைக்க முடியும்.',
 'Open public spaces': 'திறந்த பொது இடங்கள்',
 'Open the in-plugin help with links to the online documentation.':
   'ஆன்லைன் ஆவணங்களுக்கான இணைப்புகளுடன் பிளகின்-உள்ளே உதவியைத் திறக்கவும்.',
 'Output Settings': 'வெளியீட்டு அமைப்புகள்',
 'Output directory': 'வெளியீட்டு கோப்புறை',
 'Output directory selected:': 'வெளியீட்டு கோப்புறை தேர்ந்தெடுக்கப்பட்டது:',
 'Output format': 'வெளியீட்டு வடிவமைப்பு',
 'Output settings': 'வெளியீட்டு அமைப்புகள்',
 'Overpass download cancelled.': 'Overpass பதிவிறக்கம் ரத்து செய்யப்பட்டது.',
 'Overpass download completed:': 'Overpass பதிவிறக்கம் முடிந்தது:',
 'Overpass download failed.': 'Overpass பதிவிறக்கம் தோல்வியடைந்தது.',
 'Overpass download failed:': 'Overpass பதிவிறக்கம் தோல்வியடைந்தது:',
 'Overpass download running...': 'Overpass பதிவிறக்கம் இயங்குகிறது…',
 'Overpass download was cancelled by the caller.':
   'Overpass பதிவிறக்கம் அழைப்பவரால் ரத்து செய்யப்பட்டது.',
 'Overpass query must be a non-empty string.':
   'Overpass வினவல் காலியாக இல்லாத சரமாக இருக்க வேண்டும்.',
 "Overpass response 'elements' field is not a list.":
   'Overpass பதிலின் "elements" புலம் ஒரு பட்டியல் அல்ல.',
 "Overpass response does not contain an 'elements' field.":
   'Overpass பதிலில் "elements" புலம் இல்லை.',
 'Overpass response is not a JSON object.':
   'Overpass பதில் ஒரு JSON பொருள் அல்ல.',
 'Overpass response received successfully:':
   'Overpass பதில் வெற்றிகரமாகப் பெறப்பட்டது:',
 'Overpass server ': 'Overpass சேவையகம் ',
 'Overpass server returned invalid JSON. Response preview: ':
   'Overpass சேவையகம் தவறான JSON-ஐத் திருப்பியது. பதில் முன்னோட்டம்: ',
 'Overpass servers available:': 'கிடைக்கக்கூடிய Overpass சேவையகங்கள்:',
 'Overpass timeout must be greater than zero.':
   'Overpass நேர வரம்பு பூஜ்ஜியத்தை விட அதிகமாக இருக்க வேண்டும்.',
 'Plugin version': 'செருகல் பதிப்பு',
 'Points of interest (POI)': 'ஆர்வப் புள்ளிகள் (POI)',
 'Prepared {index:,} of {total:,} OSM elements for export...':
   '{total:,}-ல் {index:,} OSM கூறுகள் ஏற்றுமதிக்குத் தயார் செய்யப்பட்டன…',
 'Preparing Overpass download...':
   'Overpass பதிவிறக்கத்தைத் தயார் செய்கிறது…',
 'Preparing Overpass query.':
   'Overpass வினவலைத் தயார் செய்கிறது.',
 'Processing Options': 'செயலாக்க விருப்பங்கள்',
 'Processing log': 'செயலாக்கப் பதிவு',
 'Processing messages will appear here...':
   'செயலாக்கச் செய்திகள் இங்கே தோன்றும்…',
 'Processing options': 'செயலாக்க விருப்பங்கள்',
 'Public transport & places': 'பொது போக்குவரத்து மற்றும் இடங்கள்',
 'QGIS interface object was not detected. Canvas-dependent AOI tools are disabled.':
   'QGIS இடைமுகப் பொருள் கண்டறியப்படவில்லை. கேன்வாஸ் சார்ந்த AOI கருவிகள் முடக்கப்பட்டுள்ளன.',
 'QGIS map canvas could not be accessed.':
   'QGIS வரைபட கேன்வாஸை அணுக முடியவில்லை.',
 'QGIS map canvas is unavailable.':
   'QGIS வரைபட கேன்வாஸ் கிடைக்கவில்லை.',
 'Rail stops': 'ரயில் நிறுத்தங்கள்',
 'Railways': 'ரயில்பாதைகள்',
 'Read the plugin version from metadata.txt (empty string if absent).':
   'metadata.txt-இலிருந்து செருகல் பதிப்பைப் படிக்கவும் (இல்லையெனில் காலிச் சரம்).',
 'Read, validate and store the current QGIS map canvas extent.':
   'தற்போதைய QGIS வரைபட கேன்வாஸ் எல்லையைப் படித்து, சரிபார்த்து, சேமிக்கவும்.',
 'Ready.': 'தயார்.',
 'Rectangle AOI drawing tool activated.':
   'செவ்வக AOI வரைதல் கருவி இயக்கப்பட்டது.',
 'Rectangle AOI drawing was cancelled.':
   'செவ்வக AOI வரைதல் ரத்து செய்யப்பட்டது.',
 'Region name': 'பிராந்தியப் பெயர்',
 'Report an issue': 'சிக்கலைப் புகாரளிக்கவும்',
 'Request cooperative cancellation of the background worker.':
   'பின்னணி பணியாளரின் கூட்டு ரத்தைக் கோரவும்.',
 'Request error on server ': 'சேவையகத்தில் கோரிக்கைப் பிழை ',
 'Restore default GUI settings when the dialog closes.':
   'உரையாடல் மூடும்போது இயல்பு GUI அமைப்புகளை மீட்டெடுக்கவும்.',
 'Restore the GUI once the background thread has stopped.':
   'பின்னணி இழை நிற்கும்போது GUI-ஐ மீட்டெடுக்கவும்.',
 'Restore the QGIS map tool active before rectangle drawing.':
   'செவ்வகம் வரைவதற்கு முன் செயலில் இருந்த QGIS வரைபடக் கருவியை மீட்டெடுக்கவும்.',
 'Restore the map tool and reset state before hiding the dialog.':
   'உரையாடலை மறைப்பதற்கு முன் வரைபடக் கருவியை மீட்டெடுத்து நிலையை மீட்டமைக்கவும்.',
 'Retrying in ': 'மீண்டும் முயற்சிக்கிறது ',
 'Return selected levels, or None when all levels are requested.':
   'தேர்ந்தெடுத்த நிலைகளைத் திருப்பித் தரவும், அல்லது அனைத்து நிலைகளும் கோரப்படும்போது None.',
 'Return the combined, sanitized filename prefix.':
   'இணைக்கப்பட்ட, சுத்திகரிக்கப்பட்ட கோப்புப்பெயர் முன்னொட்டைத் திருப்பித் தரவும்.',
 'Return the mapping between feature keys and GUI checkboxes.':
   'அம்ச விசைகள் மற்றும் GUI தேர்வுப்பெட்டிகளுக்கு இடையிலான மேப்பிங்கைத் திருப்பித் தரவும்.',
 'Return the selected GUI feature keys.':
   'தேர்ந்தெடுத்த GUI அம்ச விசைகளைத் திருப்பித் தரவும்.',
 'Roads': 'சாலைகள்',
 'Run a modal dialog on both Qt5 and Qt6.':
   'Qt5 மற்றும் Qt6 இரண்டிலும் மாதிரி உரையாடலை இயக்கவும்.',
 'Select Output Directory': 'வெளியீட்டு கோப்புறையைத் தேர்ந்தெடுக்கவும்',
 'Select a vector layer with selected features.':
   'தேர்ந்தெடுத்த அம்சங்களுடன் ஒரு திசையன் அடுக்கைத் தேர்ந்தெடுக்கவும்.',
 'Select all': 'அனைத்தையும் தேர்ந்தெடு',
 'Select an active QGIS layer.': 'செயலில் உள்ள QGIS அடுக்கைத் தேர்ந்தெடுக்கவும்.',
 'Select at least one OSM feature category before downloading.':
   'பதிவிறக்குவதற்கு முன் குறைந்தது ஒரு OSM அம்ச வகையைத் தேர்ந்தெடுக்கவும்.',
 'Select at least one administrative level, or choose All levels.':
   'குறைந்தது ஒரு நிர்வாக நிலையைத் தேர்ந்தெடுக்கவும் அல்லது "அனைத்து நிலைகள்" தேர்ந்தெடுக்கவும்.',
 'Select at least one administrative level, or use None to retrieve all levels.':
   'குறைந்தது ஒரு நிர்வாக நிலையைத் தேர்ந்தெடுக்கவும் அல்லது அனைத்து நிலைகளையும் பெற None-ஐப் பயன்படுத்தவும்.',
 'Select levels 0–15 and switch to specific-level mode.':
   '0–15 நிலைகளைத் தேர்ந்தெடுத்து குறிப்பிட்ட-நிலை பயன்முறைக்கு மாறவும்.',
 'Select one or more features in the active layer.':
   'செயலில் உள்ள அடுக்கில் ஒன்று அல்லது அதற்கு மேற்பட்ட அம்சங்களைத் தேர்ந்தெடுக்கவும்.',
 'Select output directory...': 'வெளியீட்டு கோப்புறையைத் தேர்ந்தெடுக்கவும்…',
 'Selected administrative levels:': 'தேர்ந்தெடுத்த நிர்வாக நிலைகள்:',
 'Selected feature IDs:': 'தேர்ந்தெடுத்த அம்ச ID-கள்:',
 'Selected feature(s) in active layer':
   'செயலில் உள்ள அடுக்கில் தேர்ந்தெடுத்த அம்சம்(கள்)',
 'Selected features (': 'தேர்ந்தெடுத்த அம்சங்கள் (',
 'Selected-feature AOI captured successfully (':
   'தேர்ந்தெடுத்த-அம்ச AOI வெற்றிகரமாகப் பிடிக்கப்பட்டது (',
 'Selected-feature AOI captured successfully.':
   'தேர்ந்தெடுத்த-அம்ச AOI வெற்றிகரமாகப் பிடிக்கப்பட்டது.',
 'Selected-feature AOI is invalid.':
   'தேர்ந்தெடுத்த-அம்ச AOI தவறானது.',
 'Selected-feature AOI requires a vector layer.':
   'தேர்ந்தெடுத்த-அம்ச AOI-க்கு திசையன் அடுக்கு தேவை.',
 'Selected-feature AOI validation failed:':
   'தேர்ந்தெடுத்த-அம்ச AOI சரிபார்ப்பு தோல்வியடைந்தது:',
 'Sending query to Overpass...': 'Overpass-க்கு வினவலை அனுப்புகிறது…',
 'Server ': 'சேவையகம் ',
 'Shapefile': 'Shapefile',
 'Shapefile export completed in:':
   'Shapefile ஏற்றுமதி முடிந்தது:',
 'Shapefile field names shortened for':
   'Shapefile புலப் பெயர்கள் சுருக்கப்பட்டன',
 'Shapefile layer(s) to QGIS.': 'Shapefile அடுக்கு(கள்) QGIS-ல்.',
 'Short in-plugin help with links to the full online documentation.':
   'முழு ஆன்லைன் ஆவணங்களுக்கான இணைப்புகளுடன் சுருக்கமான பிளகின்-உள்ளே உதவி.',
 'Show AOI coordinates and source CRS in the dialog.':
   'உரையாடலில் AOI ஒருங்கிணைப்புகள் மற்றும் மூல CRS-ஐக் காட்டவும்.',
 'Show a concise description of the active administrative filter.':
   'செயலில் உள்ள நிர்வாக வடிகட்டியின் சுருக்கமான விவரத்தைக் காட்டவும்.',
 'Source CRS is invalid.': 'மூல CRS தவறானது.',
 'South latitude cannot be greater than north latitude.':
   'தெற்கு அட்சரேகை வடக்கு அட்சரேகையை விட அதிகமாக இருக்க முடியாது.',
 'South:': 'தெற்கு:',
 'Starting Overpass download...':
   'Overpass பதிவிறக்கத்தைத் தொடங்குகிறது…',
 'Supporting copy: muted, wrapped and visually quiet.':
   'துணை உரை: மென்மையான, மடக்கப்பட்ட மற்றும் காட்சி அமைதியான.',
 "Tag '{tag}' contains an empty value list.":
   'குறிச்சொல் "{tag}" காலியான மதிப்புப் பட்டியலைக் கொண்டுள்ளது.',
 'Temporary workspace cleanup complete:':
   'தற்காலிக பணியிடச் சுத்தம் முடிந்தது:',
 'Temporary workspace cleanup complete: no matching files found.':
   'தற்காலிக பணியிடச் சுத்தம் முடிந்தது: பொருந்தும் கோப்புகள் எதுவும் கிடைக்கவில்லை.',
 'Temporary-file cleanup skipped: workspace directory is invalid.':
   'தற்காலிக-கோப்பு சுத்தம் தவிர்க்கப்பட்டது: பணியிடக் கோப்புறை தவறானது.',
 'The OSM download succeeded, but the output could not be created.':
   'OSM பதிவிறக்கம் வெற்றிகரமானது, ஆனால் வெளியீட்டை உருவாக்க முடியவில்லை.',
 "The Overpass response must be a JSON object with an 'elements' list.":
   'Overpass பதில் "elements" பட்டியலுடன் ஒரு JSON பொருளாக இருக்க வேண்டும்.',
 'The QGIS map canvas CRS is invalid.':
   'QGIS வரைபட கேன்வாஸ் CRS தவறானது.',
 'The active layer CRS is invalid.':
   'செயலில் உள்ள அடுக்கு CRS தவறானது.',
 'The active layer extent is empty.':
   'செயலில் உள்ள அடுக்கு எல்லை காலியாக உள்ளது.',
 'The active layer must be a vector layer.':
   'செயலில் உள்ள அடுக்கு ஒரு திசையன் அடுக்காக இருக்க வேண்டும்.',
 'The combined name is too long. Shorten one or more components.':
   'இணைந்த பெயர் மிக நீளமாக உள்ளது. ஒன்று அல்லது அதற்கு மேற்பட்ட கூறுகளைச் சுருக்கவும்.',
 'The combined selected-feature geometry is empty.':
   'இணைந்த தேர்ந்தெடுத்த-அம்ச வடிவியல் காலியாக உள்ளது.',
 'The current AOI is invalid:': 'தற்போதைய AOI தவறானது:',
 'The current QGIS map extent is empty.':
   'தற்போதைய QGIS வரைபட எல்லை காலியாக உள்ளது.',
 'The dialog cannot close while a download thread is running. Cancellation has been requested; close the dialog after it stops.':
   'பதிவிறக்க இழை இயங்கும்போது உரையாடலை மூட முடியாது. ரத்து கோரப்பட்டுள்ளது; அது நிற்கும் பிறகு உரையாடலை மூடவும்.',
 'The download completed, but no confirmed output name was available.':
   'பதிவிறக்கம் முடிந்தது, ஆனால் உறுதி செய்யப்பட்ட வெளியீட்டுப் பெயர் எதுவும் கிடைக்கவில்லை.',
 "The exported Shapefile '{path}' could not be opened in QGIS.":
   'ஏற்றுமதி செய்யப்பட்ட Shapefile "{path}"-ஐ QGIS-ல் திறக்க முடியவில்லை.',
 "The exported layer '{layer_name}' could not be opened in QGIS.":
   'ஏற்றுமதி செய்யப்பட்ட அடுக்கு "{layer_name}"-ஐ QGIS-ல் திறக்க முடியவில்லை.',
 'The output name does not contain any valid filename characters.':
   'வெளியீட்டுப் பெயரில் சரியான கோப்புப்பெயர் எழுத்துகள் எதுவும் இல்லை.',
 'The output name is empty after filename validation.':
   'கோப்புப்பெயர் சரிபார்ப்புக்குப் பிறகு வெளியீட்டுப் பெயர் காலியாக உள்ளது.',
 'The selected features contain no valid geometry.':
   'தேர்ந்தெடுத்த அம்சங்களில் சரியான வடிவியல் எதுவும் இல்லை.',
 'The selected output directory does not exist. Choose an existing folder.':
   'தேர்ந்தெடுத்த வெளியீட்டு கோப்புறை இல்லை. இருக்கும் கோப்புறையைத் தேர்ந்தெடுக்கவும்.',
 'There is no active download to cancel.':
   'ரத்து செய்ய செயலில் உள்ள பதிவிறக்கம் எதுவும் இல்லை.',
 'Timeout on server ': 'சேவையகத்தில் நேரம் முடிந்தது ',
 'Translate widget labels while preserving each original English string.':
   'ஒவ்வொரு அசல் ஆங்கில சரத்தையும் பாதுகாத்து விட்ஜெட் லேபிள்களை மொழிபெயர்க்கவும்.',
 'Trying Overpass server ': 'Overpass சேவையகத்தை முயற்சிக்கிறது ',
 'Unable to start AOI drawing:': 'AOI வரைதலைத் தொடங்க முடியவில்லை:',
 'Unclassified OSM elements not written to feature layers:':
   'அம்ச அடுக்குகளில் எழுதப்படாத வகைப்படுத்தப்படாத OSM கூறுகள்:',
 'Unsupported geometry family: {geometry_family}':
   'ஆதரிக்கப்படாத வடிவியல் குடும்பம்: {geometry_family}',
 "Unsupported geometry type '{geometry_type}' for feature '{feature_key}'.":
   'அம்சம் "{feature_key}"-க்கு ஆதரிக்கப்படாத வடிவியல் வகை "{geometry_type}".',
 'Unsupported geometry type for Shapefile export: {geometry_type}':
   'Shapefile ஏற்றுமதிக்கு ஆதரிக்கப்படாத வடிவியல் வகை: {geometry_type}',
 "Unsupported match mode '{mode}' for feature '{feature_key}'.":
   'அம்சம் "{feature_key}"-க்கு ஆதரிக்கப்படாத பொருத்து முறை "{mode}".',
 'Unsupported output format:': 'ஆதரிக்கப்படாத வெளியீட்டு வடிவமைப்பு:',
 "Unsupported tag value type for '{feature_key}': {value_type}":
   '"{feature_key}"-க்கு ஆதரிக்கப்படாத குறிச்சொல் மதிப்பு வகை: {value_type}',
 'Update Current QGIS Map Extent':
   'தற்போதைய QGIS வரைபட எல்லையைப் புதுப்பிக்கவும்',
 'Update the "N selected" count next to the category heading.':
   'வகை தலைப்புக்கு அருகிலுள்ள "N தேர்ந்தெடுக்கப்பட்டது" எண்ணிக்கையைப் புதுப்பிக்கவும்.',
 'Update the filename preview as the user edits the components.':
   'பயனர் கூறுகளைத் திருத்தும்போது கோப்புப்பெயர் முன்னோட்டத்தைப் புதுப்பிக்கவும்.',
 'Use Layer Extent': 'அடுக்கு எல்லையைப் பயன்படுத்து',
 'Use Selected Features': 'தேர்ந்தெடுத்த அம்சங்களைப் பயன்படுத்து',
 'Use local cache where available':
   'கிடைக்கும்போது உள்ளூர் தற்காலிகச் சேமிப்பைப் பயன்படுத்தவும்',
 'Use selected features in the active vector layer as the AOI.':
   'செயலில் உள்ள திசையன் அடுக்கில் தேர்ந்தெடுத்த அம்சங்களை AOI ஆகப் பயன்படுத்தவும்.',
 'Use the full extent of the active QGIS layer as the AOI.':
   'செயலில் உள்ள QGIS அடுக்கின் முழு எல்லையை AOI ஆகப் பயன்படுத்தவும்.',
 'Use the full extent of the active QGIS layer.':
   'செயலில் உள்ள QGIS அடுக்கின் முழு எல்லையைப் பயன்படுத்தவும்.',
 'Use the selected features of the active vector layer as the AOI.':
   'செயலில் உள்ள திசையன் அடுக்கின் தேர்ந்தெடுத்த அம்சங்களை AOI ஆகப் பயன்படுத்தவும்.',
 'Using cached data; no Overpass network request was needed.':
   'தற்காலிகச் சேமிப்பில் உள்ள தரவைப் பயன்படுத்துகிறது; Overpass பிணையக் கோரிக்கை தேவைப்படவில்லை.',
 'Validate filename and any explicitly selected admin levels.':
   'கோப்புப்பெயர் மற்றும் வெளிப்படையாகத் தேர்ந்தெடுக்கப்பட்ட admin நிலைகளைச் சரிபார்க்கவும்.',
 'Validate inputs and start the background Overpass download.':
   'உள்ளீடுகளைச் சரிபார்த்து பின்னணி Overpass பதிவிறக்கத்தைத் தொடங்கவும்.',
 'WGS84 AOI bbox: south=': 'WGS84 AOI எல்லைப்பெட்டி: தெற்கு=',
 'WGS84 AOI geometry is not available.':
   'WGS84 AOI வடிவியல் கிடைக்கவில்லை.',
 'Warning: download succeeded, but the response could not be cached:':
   'எச்சரிக்கை: பதிவிறக்கம் வெற்றிகரமானது, ஆனால் பதிலைத் தற்காலிகச் சேமிப்பில் வைக்க முடியவில்லை:',
 'Waterways': 'நீர்வழிகள்',
 'West longitude cannot be greater than east longitude.':
   'மேற்கு தீர்க்கரேகை கிழக்கு தீர்க்கரேகையை விட அதிகமாக இருக்க முடியாது.',
 'West:': 'மேற்கு:',
 'Writing Shapefile {layer_index}/{total}: {layer_name}...':
   'Shapefile {layer_index}/{total} எழுதுகிறது: {layer_name}…',
 'Writing layer {layer_index}/{total}: {layer_name} ({count:,} features)...':
   'அடுக்கு {layer_index}/{total} எழுதுகிறது: {layer_name} ({count:,} அம்சங்கள்)…',
 'attempt ': 'முயற்சி ',
 'characters).': 'எழுத்துகள்).',
 'connection error — ': 'இணைப்புப் பிழை — ',
 'e.g. CBD': 'எ.கா. CBD',
 'e.g. Kenya': 'எ.கா. கென்யா',
 'e.g. Nairobi': 'எ.கா. நைரோபி',
 'e.g. NairobiCounty': 'எ.கா. NairobiCounty',
 'elements (': 'கூறுகள் (',
 'export failed:': 'ஏற்றுமதி தோல்வியடைந்தது:',
 'feature records).': 'அம்சப் பதிவுகள்).',
 'feature(s)).': 'அம்சம்(ங்கள்)).',
 'features written.': 'அம்சங்கள் எழுதப்பட்டன.',
 'file(s) deleted.': 'கோப்பு(கள்) நீக்கப்பட்டன.',
 'relation geometry assignment(s); relation-member geometry assembly is not implemented yet.':
   'தொடர்பு வடிவியல் ஒதுக்கீடு(கள்); தொடர்பு-உறுப்பு வடிவியல் சேர்க்கை இன்னும் செயல்படுத்தப்படவில்லை.',
 'relations).': 'தொடர்புகள்).',
 'response_data must be a dictionary.':
   'response_data ஒரு அகராதியாக இருக்க வேண்டும்.',
 "response_data['elements'] must be a list.":
   "response_data['elements'] ஒரு பட்டியலாக இருக்க வேண்டும்.",
 'temporary file(s) could not be deleted. They may still be in use by QGIS or another process.':
   'தற்காலிக கோப்பு(கள்) நீக்க முடியவில்லை. அவை QGIS அல்லது மற்றொரு செயல்முறையால் இன்னும் பயன்படுத்தப்படலாம்.',
 'timeout — ': 'நேரம் முடிந்தது — ',
 '{output_format} export failed: {error}':
   '{output_format} ஏற்றுமதி தோல்வியடைந்தது: {error}',
 '— Confirm Overwrite': '— மேலெழுதுவதை உறுதிப்படுத்து',
 '— Export Error': '— ஏற்றுமதிப் பிழை',
 '— Help': '— உதவி',
 '— Output Naming': '— வெளியீட்டுப் பெயரிடல்',
}