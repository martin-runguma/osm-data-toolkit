"""Swahili (Kiswahili) translation pack for the OSM Data Toolkit plugin.
Keys remain the English source strings; preserve placeholders and HTML."""
TEXT = {
 '\n<h3>Quick start</h3>\n<ol>\n  <li><b>Choose an area.</b> Use the current map extent, draw a rectangle\n      on the map, or use the bounding box of selected features or a\n      layer\'s extent.</li>\n  <li><b>Tick the OSM categories</b> you need (POI, stops, roads,\n      buildings, boundaries, landuse, ...).</li>\n  <li><b>Choose an output format and folder</b>, then click\n      <b>Download OSM Data</b>.</li>\n</ol>\n\n<h3>Good to know</h3>\n<ul>\n  <li><b>GeoPackage is recommended.</b> A Shapefile cannot hold very many\n      attribute columns, so on large areas some rarely used tag columns\n      may be left out (the log tells you when this happens).</li>\n  <li><b>Keep the area focused.</b> Very large areas produce huge Overpass\n      responses and can be slow or rejected by the public servers.</li>\n  <li><b>The cache</b> lets repeat downloads of the same query reuse\n      earlier results.</li>\n  <li><b>"Unclassified OSM elements"</b> in the log is informational: they\n      are mostly untagged vertices of lines and polygons that do not belong\n      to any selected category.</li>\n</ul>\n\n<p>Data &copy; OpenStreetMap contributors, available under the\n<a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a>.</p>\n<p><i>This plugin is not endorsed by or affiliated with the\nOpenStreetMap Foundation.</i></p>\n':
 '\n<h3>Anza haraka</h3>\n<ol>\n  <li><b>Chagua eneo.</b> Tumia eneo la sasa la ramani, chora mstatili\n      kwenye ramani, au tumia kisanduku cha mipaka cha vipengele\n      vilivyochaguliwa au eneo la tabaka.</li>\n  <li><b>Weka tiki kwenye kategoria za OSM</b> unazohitaji (POI, vituo,\n      barabara, majengo, mipaka, matumizi ya ardhi, ...).</li>\n  <li><b>Chagua umbizo la pato na folda</b>, kisha bofya\n      <b>Pakua Data ya OSM</b>.</li>\n</ol>\n\n<h3>Vizuri kujua</h3>\n<ul>\n  <li><b>GeoPackage inashauriwa.</b> Shapefile haiwezi kubeba safu nyingi\n      sana za sifa, kwa hivyo kwenye maeneo makubwa baadhi ya safu za\n      lebo zinazotumika mara chache zinaweza kuachwa (kumbukumbu\n      inakuambia hili linapotokea).</li>\n  <li><b>Weka eneo lililolengwa.</b> Maeneo makubwa sana huzalisha majibu\n      makubwa ya Overpass na yanaweza kuwa ya polepole au kukataliwa na\n      seva za umma.</li>\n  <li><b>Akiba</b> huruhusu upakuaji wa mara kwa mara wa swali moja\n      kutumia matokeo ya awali.</li>\n  <li><b>"Vipengele vya OSM visivyoainishwa"</b> kwenye kumbukumbu ni\n      taarifa: mara nyingi ni vituo visivyo na lebo vya mistari na\n      poligoni ambavyo haviingii katika kategoria yoyote\n      iliyochaguliwa.</li>\n</ul>\n\n<p>Data &copy; wachangiaji wa OpenStreetMap, inapatikana chini ya\n<a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a>.</p>\n<p><i>Programu-jalizi hii haikuidhinishwa na wala haihusiani na\nOpenStreetMap Foundation.</i></p>\n',
 ' responded successfully.': ' ilijibu kwa mafanikio.',
 ' seconds...': ' sekunde…',
 '" style="color:#0B5E8E; text-decoration:none;">OpenStreetMap contributors</a> (ODbL)':
   '" style="color:#0B5E8E; text-decoration:none;">Wachangiaji wa OpenStreetMap</a> (ODbL)',
 ', east=': ', mashariki=',
 ', north=': ', kaskazini=',
 ', west=': ', magharibi=',
 '0 selected': '0 zimechaguliwa',
 '<p>Plugin version': '<p>Toleo la programu-jalizi',
 'A download is already running.': 'Upakuaji tayari unaendelea.',
 'A labelled column of feature checkboxes.':
   'Safu yenye lebo ya visanduku vya kuchagua vya vipengele.',
 'AOI drawing cancelled.': 'Uchoraji wa AOI umeghairiwa.',
 'AOI geometry is empty.': 'Jiometri ya AOI ni tupu.',
 'AOI geometry is missing.': 'Jiometri ya AOI haipo.',
 'AOI name': 'Jina la AOI',
 'AOI rectangle captured successfully.':
   'Mstatili wa AOI umenaswa kwa mafanikio.',
 'AOI source CRS is invalid.': 'CRS chanzo cha AOI si sahihi.',
 'AOI validation failed:': 'Uthibitishaji wa AOI umeshindikana:',
 'AOI:': 'AOI:',
 'AOI: QGIS interface is not available.':
   'AOI: kiolesura cha QGIS hakipatikani.',
 "AOI: click 'Draw AOI', then drag a rectangle on the QGIS map.":
   'AOI: bofya "Chora AOI", kisha buruta mstatili kwenye ramani ya QGIS.',
 "AOI: click 'Use Layer Extent' to use the full extent of the active QGIS layer.":
   'AOI: bofya "Tumia Eneo la Tabaka" ili kutumia eneo kamili la tabaka amilifu la QGIS.',
 'AOI: click and drag on the QGIS map.':
   'AOI: bofya na buruta kwenye ramani ya QGIS.',
 'AOI: failed to resolve active layer extent':
   'AOI: imeshindwa kubaini eneo la tabaka amilifu',
 'AOI: failed to resolve selected features':
   'AOI: imeshindwa kubaini vipengele vilivyochaguliwa',
 'AOI: invalid': 'AOI: si sahihi',
 'AOI: no active QGIS layer.': 'AOI: hakuna tabaka amilifu la QGIS.',
 'AOI: no feature(s) selected in the active layer.':
   'AOI: hakuna kipengele kilichochaguliwa katika tabaka amilifu.',
 'AOI: not yet resolved': 'AOI: bado haijabainishwa',
 "AOI: select feature(s) in the active QGIS layer, then click 'Use Selected Features'.":
   'AOI: chagua kipengele/vipengele katika tabaka amilifu la QGIS, kisha bofya "Tumia Vipengele Vilivyochaguliwa".',
 'AOI: the active layer is not a vector layer.':
   'AOI: tabaka amilifu si tabaka la vekta.',
 'AOI: unable to create': 'AOI: imeshindwa kuunda',
 'AOI: unable to resolve': 'AOI: imeshindwa kubaini',
 'Activate the interactive rectangle AOI map tool.':
   'Washa zana shirikishi ya mstatili wa AOI kwenye ramani.',
 'Active layer extent': 'Eneo la tabaka amilifu',
 'Active-layer extent AOI is invalid.':
   'AOI ya eneo la tabaka amilifu si sahihi.',
 'Active-layer extent captured successfully.':
   'Eneo la tabaka amilifu limenaswa kwa mafanikio.',
 'Active-layer extent validation failed:':
   'Uthibitishaji wa eneo la tabaka amilifu umeshindikana:',
 'Administrative boundaries': 'Mipaka ya kiutawala',
 'Administrative boundary filter: all levels (no admin_level filter).':
   'Kichujio cha mipaka ya kiutawala: ngazi zote (hakuna kichujio cha admin_level).',
 'Administrative boundary levels': 'Ngazi za mipaka ya kiutawala',
 'Administrative boundary levels:': 'Ngazi za mipaka ya kiutawala:',
 'Administrative levels must be an integer, a numeric string, a sequence of levels, or None.':
   'Ngazi za kiutawala lazima ziwe nambari kamili, mfuatano wa nambari, mfuatano wa ngazi, au None.',
 'All OSM feature categories cleared.': 'Kategoria zote za vipengele vya OSM zimefutwa.',
 'All OSM feature categories selected.': 'Kategoria zote za vipengele vya OSM zimechaguliwa.',
 'All Overpass server URLs must be non-empty strings.':
   'URL zote za seva za Overpass lazima ziwe mifuatano isiyo tupu.',
 'All Overpass servers and retry attempts failed.':
   'Seva zote za Overpass na majaribio ya kurudia yameshindikana.',
 'All administrative levels will be included.':
   'Ngazi zote za kiutawala zitajumuishwa.',
 'All administrative levels will be included; no admin_level filter will be added to the query.':
   'Ngazi zote za kiutawala zitajumuishwa; hakuna kichujio cha admin_level kitakachoongezwa kwenye swali.',
 'All attempts failed for server ': 'Majaribio yote yameshindikana kwa seva ',
 'All levels (0–15; no admin_level filter)':
   'Ngazi zote (0–15; hakuna kichujio cha admin_level)',
 'An existing output directory is required for Shapefile export.':
   'Folda ya pato iliyopo inahitajika kwa uhamishaji wa Shapefile.',
 'An output GeoPackage path is required.':
   'Njia ya pato ya GeoPackage inahitajika.',
 'An output name is required for Shapefile export.':
   'Jina la pato linahitajika kwa uhamishaji wa Shapefile.',
 'Append a timestamped message to the processing log.':
   'Ongeza ujumbe wenye muhuri wa muda kwenye kumbukumbu ya uchakataji.',
 'Append an exported feature count to the processing log.':
   'Ongeza idadi ya vipengele vilivyohamishwa kwenye kumbukumbu ya uchakataji.',
 'Area of Interest': 'Eneo la Kuvutiwa',
 'At least one OSM feature must be selected.':
   'Angalau kipengele kimoja cha OSM lazima kichaguliwe.',
 'At least one OSM feature must be supplied.':
   'Angalau kipengele kimoja cha OSM lazima kitolewe.',
 'At least one Overpass server must be provided.':
   'Angalau seva moja ya Overpass lazima itolewe.',
 'Attempt details:': 'Maelezo ya majaribio:',
 'Automatically add downloaded layers to QGIS':
   'Ongeza tabaka zilizopakuliwa kwenye QGIS kiotomatiki',
 'Background Overpass download started.':
   'Upakuaji wa Overpass wa nyuma umeanza.',
 'Browse': 'Vinjari',
 'Browse…': 'Vinjari…',
 'Buildings': 'Majengo',
 'Bus stops': 'Vituo vya mabasi',
 'CRS:': 'CRS:',
 'Cache hit:': 'Akiba imepatikana:',
 'Cache hit: using saved Overpass response ({age} day(s) old).':
   'Akiba imepatikana: inatumia jibu la Overpass lililohifadhiwa (siku {age} za zamani).',
 'Cache miss:': 'Akiba haijapatikana:',
 'Cache miss: could not read saved response ({error}).':
   'Akiba haijapatikana: imeshindwa kusoma jibu lililohifadhiwa ({error}).',
 'Cache miss: query hash does not match the saved response.':
   'Akiba haijapatikana: hashi ya swali hailingani na jibu lililohifadhiwa.',
 'Cache miss: saved response is incomplete or invalid.':
   'Akiba haijapatikana: jibu lililohifadhiwa halijakamilika au si sahihi.',
 'Cache miss: saved response is older than {days} days.':
   'Akiba haijapatikana: jibu lililohifadhiwa ni la zamani zaidi ya siku {days}.',
 'Cache miss: saved response uses an unsupported cache format.':
   'Akiba haijapatikana: jibu lililohifadhiwa linatumia umbizo la akiba lisilotumika.',
 'Cached Overpass response:': 'Jibu la Overpass lililohifadhiwa kwenye akiba:',
 'Cancel': 'Ghairi',
 'Cancellation has already been requested.': 'Ombi la kughairi limeshatolewa.',
 'Cancellation requested': 'Ombi la kughairi limetolewa',
 'Cancellation requested. If an HTTP request is already active, the downloader will stop when that request returns or times out.':
   'Ombi la kughairi limetolewa. Ikiwa ombi la HTTP tayari linaendelea, kipakuzi kitasimama ombi hilo linaporejea au muda wake unapoisha.',
 'Cancellation requested; waiting for the current request to finish...':
   'Ombi la kughairi limetolewa; tunasubiri ombi la sasa likamilike…',
 'Cannot draw AOI because the QGIS interface is unavailable.':
   'Haiwezi kuchora AOI kwa sababu kiolesura cha QGIS hakipatikani.',
 'Cannot resolve active-layer extent because QGIS is unavailable.':
   'Haiwezi kubaini eneo la tabaka amilifu kwa sababu QGIS haipatikani.',
 'Cannot resolve current map extent because QGIS is unavailable.':
   'Haiwezi kubaini eneo la sasa la ramani kwa sababu QGIS haipatikani.',
 'Cannot resolve selected-feature AOI because QGIS is unavailable.':
   'Haiwezi kubaini AOI ya vipengele vilivyochaguliwa kwa sababu QGIS haipatikani.',
 'Cannot transform an empty geometry.':
   'Haiwezi kubadilisha jiometri tupu.',
 'Capture the current QGIS map canvas extent.':
   'Nasa eneo la sasa la turubai ya ramani ya QGIS.',
 'Choose all available levels, or select one or more levels to download (for example, 5–8 or level 5).':
   'Chagua ngazi zote zinazopatikana, au chagua ngazi moja au zaidi kupakua (kwa mfano, 5–8 au ngazi 5).',
 'Choose an output directory before downloading.':
   'Chagua folda ya pato kabla ya kupakua.',
 'City name': 'Jina la jiji',
 'Classifying OSM elements and preparing GeoPackage layers.':
   'Inaainisha vipengele vya OSM na kuandaa tabaka za GeoPackage.',
 'Classifying OSM elements and preparing Shapefile outputs.':
   'Inaainisha vipengele vya OSM na kuandaa matokeo ya Shapefile.',
 'Clear all': 'Futa zote',
 'Clear log': 'Futa kumbukumbu',
 'Clear only the visible log, without changing processing settings.':
   'Futa tu kumbukumbu inayoonekana, bila kubadilisha mipangilio ya uchakataji.',
 'Clear selected levels so the user can make a narrower selection.':
   'Futa ngazi zilizochaguliwa ili mtumiaji aweze kufanya uchaguzi mwembamba zaidi.',
 'Clear the messages currently shown in the Processing Log.':
   'Futa ujumbe unaoonyeshwa sasa kwenye Kumbukumbu ya Uchakataji.',
 'Clear the previous AOI and display guidance for the chosen method.':
   'Futa AOI ya awali na uonyeshe mwongozo wa njia iliyochaguliwa.',
 'Close': 'Funga',
 'Collect optional filename components before exporting OSM data.':
   'Kusanya sehemu za hiari za jina la faili kabla ya kuhamisha data ya OSM.',
 'Compact product header above the scrollable workflow.':
   'Kichwa kifupi cha bidhaa juu ya mtiririko wa kazi unaosogeza.',
 'Connection error on server ': 'Hitilafu ya muunganisho kwenye seva ',
 'Continue to Download': 'Endelea kupakua',
 'Convert a name component into a Windows-safe filename token.':
   'Badilisha sehemu ya jina kuwa tokeni ya jina la faili salama kwa Windows.',
 'Convert the drawn rectangle into the standard AOI object.':
   'Badilisha mstatili uliochorwa kuwa kipengele cha kawaida cha AOI.',
 'Converting OSM response to GeoPackage...':
   'Inabadilisha jibu la OSM kuwa GeoPackage…',
 'Converting OSM response to Shapefiles...':
   'Inabadilisha jibu la OSM kuwa Shapefiles…',
 'Could not combine the selected feature geometries.':
   'Imeshindwa kuchanganya jiometri za vipengele vilivyochaguliwa.',
 "Could not create Shapefile staging layer '{layer_name}'.":
   'Imeshindwa kuunda tabaka la maandalizi la Shapefile "{layer_name}".',
 'Could not create an empty bus_stops_points layer.':
   'Imeshindwa kuunda tabaka tupu la bus_stops_points.',
 "Could not create temporary QGIS layer '{layer_name}'.":
   'Imeshindwa kuunda tabaka la muda la QGIS "{layer_name}".',
 'Could not create temporary layer for admin_level {admin_level}.':
   'Imeshindwa kuunda tabaka la muda kwa admin_level {admin_level}.',
 'Could not create the merged bus_stops_points layer.':
   'Imeshindwa kuunda tabaka la bus_stops_points lililounganishwa.',
 'Could not delete temporary file':
   'Imeshindwa kufuta faili ya muda',
 "Could not load feature definition '{feature_key}': {error}":
   'Imeshindwa kupakia ufafanuzi wa kipengele "{feature_key}": {error}',
 'Could not merge bus-station centroids into bus-stop points.':
   'Imeshindwa kuunganisha vituo vya poligoni za vituo vya mabasi kwenye pointi za vituo vya mabasi.',
 'Could not overwrite existing output file: {error}':
   'Imeshindwa kuandika juu ya faili ya pato iliyopo: {error}',
 'Could not populate Shapefile for admin_level {admin_level}.':
   'Imeshindwa kujaza Shapefile kwa admin_level {admin_level}.',
 "Could not populate temporary layer '{layer_name}'.":
   'Imeshindwa kujaza tabaka la muda "{layer_name}".',
 'Could not prepare the Overpass query:':
   'Imeshindwa kuandaa swali la Overpass:',
 "Could not reopen intermediate GeoPackage layer '{layer_name}'.":
   'Imeshindwa kufungua tena tabaka la GeoPackage la kati "{layer_name}".',
 'Could not restore previous QGIS map tool:':
   'Imeshindwa kurejesha zana ya awali ya ramani ya QGIS:',
 'Could not search for temporary GeoPackages:':
   'Imeshindwa kutafuta GeoPackages za muda:',
 'Country name': 'Jina la nchi',
 'Create one section panel and return it with its body layout.':
   'Unda paneli moja ya sehemu na uirudishe pamoja na mpangilio wa mwili wake.',
 'Created bus_stops_points from bus-station polygon centroids.':
   'Imeunda bus_stops_points kutoka vituo vya poligoni za vituo vya mabasi.',
 'Current QGIS map extent': 'Eneo la sasa la ramani ya QGIS',
 'Current QGIS map extent resolved.':
   'Eneo la sasa la ramani ya QGIS limebainishwa.',
 'Data © <a href="': 'Data © <a href="',
 'Deleted temporary workspace file:':
   'Faili ya muda ya nafasi ya kazi imefutwa:',
 'Details:': 'Maelezo:',
 'Download': 'Pakua',
 'Download OSM Data': 'Pakua Data ya OSM',
 'Download OpenStreetMap data for any area and load it straight into QGIS.':
   'Pakua data ya OpenStreetMap kwa eneo lolote na uipakishe moja kwa moja kwenye QGIS.',
 'Download cancelled because existing output files were not approved for overwrite.':
   'Upakuaji umeghairiwa kwa sababu faili za pato zilizopo hazikuidhinishwa kuandikwa juu.',
 'Download cancelled before it started.':
   'Upakuaji umeghairiwa kabla ya kuanza.',
 'Download cancelled before results were returned.':
   'Upakuaji umeghairiwa kabla ya matokeo kurejeshwa.',
 'Download cancelled before starting.':
   'Upakuaji umeghairiwa kabla ya kuanza.',
 'Download cancelled in the output-naming dialog.':
   'Upakuaji umeghairiwa kwenye kidirisha cha kutaja jina la pato.',
 'Download cancelled.': 'Upakuaji umeghairiwa.',
 'Download cancelled; existing files preserved.':
   'Upakuaji umeghairiwa; faili zilizopo zimehifadhiwa.',
 'Download stopped.': 'Upakuaji umesimama.',
 'Download succeeded, but export failed.':
   'Upakuaji umefanikiwa, lakini uhamishaji umeshindikana.',
 'Downloading OSM data from Overpass...':
   'Inapakua data ya OSM kutoka Overpass…',
 'Draw AOI': 'Chora AOI',
 'Draw a rectangle on the QGIS map to define the AOI.':
   'Chora mstatili kwenye ramani ya QGIS ili kufafanua AOI.',
 'Draw rectangle on map': 'Chora mstatili kwenye ramani',
 'Draw the AOI rectangle on the QGIS map.':
   'Chora mstatili wa AOI kwenye ramani ya QGIS.',
 'Drawn AOI validation failed:':
   'Uthibitishaji wa AOI iliyochorwa umeshindikana:',
 'Drawn rectangle': 'Mstatili uliochorwa',
 'Drawn rectangle AOI captured successfully.':
   'Mstatili wa AOI uliochorwa umenaswa kwa mafanikio.',
 'ERROR:': 'HITILAFU:',
 'East:': 'Mashariki:',
 'Enable level checkboxes only when a specific selection is active.':
   'Washa visanduku vya ngazi tu wakati uchaguzi mahususi unaendelea.',
 'Enable only the AOI action button for the selected method.':
   'Washa tu kitufe cha kitendo cha AOI kwa njia iliyochaguliwa.',
 'Enable or disable controls while a download is running.':
   'Washa au zima vidhibiti wakati upakuaji unaendelea.',
 'Enter at least one name (City, Country, Region, or AOI).':
   'Weka angalau jina moja (jiji, nchi, mkoa, au AOI).',
 'Enter one or more name components. Blank fields will be skipped, and the remaining names will be joined with underscores. The selected output format will be retained.':
   'Weka sehemu moja au zaidi za jina. Sehemu tupu zitarukwa, na majina yaliyobaki yataunganishwa kwa alama za chini. Umbizo la pato lililochaguliwa litahifadhiwa.',
 'Enter_a_name_to_preview': 'Weka_jina_ili_kuona_hakiki',
 'Export cancelled: output name is missing.':
   'Uhamishaji umeghairiwa: jina la pato halipo.',
 'Export complete:': 'Uhamishaji umekamilika:',
 'Export the downloaded response and optionally load its layers.':
   'Hamisha jibu lililopakuliwa na hiari pakia tabaka zake.',
 'Failed to activate rectangle AOI tool:':
   'Imeshindwa kuwasha zana ya mstatili wa AOI:',
 'Failed to create AOI.': 'Imeshindwa kuunda AOI.',
 'Failed to process drawn rectangle AOI:':
   'Imeshindwa kuchakata mstatili wa AOI uliochorwa:',
 'Failed to resolve active-layer extent.':
   'Imeshindwa kubaini eneo la tabaka amilifu.',
 'Failed to resolve active-layer extent:':
   'Imeshindwa kubaini eneo la tabaka amilifu:',
 'Failed to resolve current QGIS map extent:':
   'Imeshindwa kubaini eneo la sasa la ramani ya QGIS:',
 'Failed to resolve selected-feature AOI.':
   'Imeshindwa kubaini AOI ya vipengele vilivyochaguliwa.',
 'Failed to resolve selected-feature AOI:':
   'Imeshindwa kubaini AOI ya vipengele vilivyochaguliwa:',
 "Failed to write layer '{layer_name}' to '{output_path}': {error}":
   'Imeshindwa kuandika tabaka "{layer_name}" kwenye "{output_path}": {error}',
 "Feature '{feature_key}' has no tag definitions.":
   'Kipengele "{feature_key}" hakina ufafanuzi wa lebo.',
 'Feature specification  does not expose a tag-filter mapping.':
   'Vipimo vya kipengele havitoi ramani ya kichujio cha lebo.',
 'Ferry stops': 'Vituo vya feri',
 'Filename preview': 'Hakiki ya jina la faili',
 'Full documentation': 'Nyaraka kamili',
 'Generated Overpass query (': 'Swali la Overpass lililozalishwa (',
 'GeoPackage': 'GeoPackage',
 'GeoPackage layer(s) to QGIS.': 'tabaka za GeoPackage kwenye QGIS.',
 'GeoPackage saved:': 'GeoPackage imehifadhiwa:',
 'HTTP error on server ': 'Hitilafu ya HTTP kwenye seva ',
 'HTTP error — ': 'hitilafu ya HTTP — ',
 'HTTP {status} error on server {index}/{total}.':
   'Hitilafu ya HTTP {status} kwenye seva {index}/{total}.',
 'Handle a drawing tool deactivation initiated outside this dialog.':
   'Shughulikia kuzimwa kwa zana ya kuchora kulikoanzishwa nje ya kidirisha hiki.',
 'Help': 'Msaada',
 'Invalid east longitude: {value}':
   'Longitudo ya mashariki si sahihi: {value}',
 'Invalid north latitude: {value}':
   'Latitudo ya kaskazini si sahihi: {value}',
 'Invalid response from server ': 'Jibu si sahihi kutoka seva ',
 'Invalid south latitude: {value}':
   'Latitudo ya kusini si sahihi: {value}',
 'Invalid west longitude: {value}':
   'Longitudo ya magharibi si sahihi: {value}',
 'Keep the numeric readout in step with the progress bar.':
   'Weka usomaji wa nambari sambamba na upau wa maendeleo.',
 'Land & built environment': 'Ardhi na mazingira yaliyojengwa',
 'Landuse': 'Matumizi ya ardhi',
 'Language:': 'Lugha:',
 'Linear features': 'Vipengele vya mstari',
 'Load the saved interface language and translate visible UI strings.':
   'Pakia lugha ya kiolesura iliyohifadhiwa na utafsiri mifuatano inayoonekana ya UI.',
 'Local response cache is disabled.':
   'Akiba ya majibu ya ndani imezimwa.',
 'Main OSM Data Toolkit window.': 'Dirisha kuu la OSM Data Toolkit.',
 'Manually capture the map extent after the user pans or zooms.':
   'Nasa eneo la ramani kwa mkono baada ya mtumiaji kusogeza au kukuza.',
 'Merged bus-station polygon centroids into bus_stops_points.':
   'Vituo vya poligoni za vituo vya mabasi vimeunganishwa kwenye bus_stops_points.',
 'No Overpass selectors were generated.':
   'Hakuna kichaguzi cha Overpass kilichozalishwa.',
 'No active QGIS layer is available.':
   'Hakuna tabaka amilifu la QGIS linalopatikana.',
 'No active layer is available.':
   'Hakuna tabaka amilifu linalopatikana.',
 'No exportable features matched the selected categories. Try another AOI or select additional OSM feature categories.':
   'Hakuna kipengele kinachoweza kuhamishwa kilicholingana na kategoria zilizochaguliwa. Jaribu AOI nyingine au chagua kategoria za ziada za vipengele vya OSM.',
 'No features are selected in the active layer.':
   'Hakuna vipengele vilivyochaguliwa katika tabaka amilifu.',
 'No levels selected. Select at least one level to continue.':
   'Hakuna ngazi zilizochaguliwa. Chagua angalau ngazi moja ili kuendelea.',
 'No selected features found.':
   'Hakuna vipengele vilivyochaguliwa vilivyopatikana.',
 'No valid Area of Interest is available. Select an AOI method and resolve the AOI before downloading.':
   'Hakuna Eneo la Kuvutiwa halali linalopatikana. Chagua njia ya AOI na ubaini AOI kabla ya kupakua.',
 'North:': 'Kaskazini:',
 'Note: {layer_name} has too many tag columns for one Shapefile (DBF size limit); {count} rarely-used columns were left out.':
   'Kumbuka: {layer_name} ina safu nyingi mno za lebo kwa Shapefile moja (kikomo cha ukubwa wa DBF); safu {count} zinazotumika mara chache ziliachwa.',
 'OSM Data Toolkit': 'OSM Data Toolkit',
 'OSM Data Toolkit initialised.':
   'OSM Data Toolkit imeanzishwa.',
 'OSM Feature Categories': 'Kategoria za Vipengele vya OSM',
 'OSM export completed successfully.':
   'Uhamishaji wa OSM umekamilika kwa mafanikio.',
 'One or more output files with this name already exist. Do you want to overwrite the matching output files?':
   'Faili moja au zaidi za pato zenye jina hili tayari zipo. Je, unataka kuandika juu ya faili za pato zinazolingana?',
 'Only the selected levels': 'Ngazi zilizochaguliwa pekee',
 'Only validated Overpass responses can be cached.':
   'Majibu ya Overpass yaliyothibitishwa pekee yanaweza kuhifadhiwa kwenye akiba.',
 'Open public spaces': 'Nafasi za umma zilizo wazi',
 'Open the in-plugin help with links to the online documentation.':
   'Fungua msaada ndani ya programu-jalizi wenye viungo vya nyaraka za mtandaoni.',
 'Output Settings': 'Mipangilio ya Pato',
 'Output directory': 'Folda ya pato',
 'Output directory selected:': 'Folda ya pato imechaguliwa:',
 'Output format': 'Umbizo la pato',
 'Output settings': 'Mipangilio ya pato',
 'Overpass download cancelled.': 'Upakuaji wa Overpass umeghairiwa.',
 'Overpass download completed:': 'Upakuaji wa Overpass umekamilika:',
 'Overpass download failed.': 'Upakuaji wa Overpass umeshindikana.',
 'Overpass download failed:': 'Upakuaji wa Overpass umeshindikana:',
 'Overpass download running...': 'Upakuaji wa Overpass unaendelea…',
 'Overpass download was cancelled by the caller.':
   'Upakuaji wa Overpass ulighairiwa na mwitaji.',
 'Overpass query must be a non-empty string.':
   'Swali la Overpass lazima liwe mfuatano usio tupu.',
 "Overpass response 'elements' field is not a list.":
   'Sehemu ya "elements" ya jibu la Overpass si orodha.',
 "Overpass response does not contain an 'elements' field.":
   'Jibu la Overpass halina sehemu ya "elements".',
 'Overpass response is not a JSON object.':
   'Jibu la Overpass si kipengele cha JSON.',
 'Overpass response received successfully:':
   'Jibu la Overpass limepokelewa kwa mafanikio:',
 'Overpass server ': 'Seva ya Overpass ',
 'Overpass server returned invalid JSON. Response preview: ':
   'Seva ya Overpass ilirudisha JSON si sahihi. Hakiki ya jibu: ',
 'Overpass servers available:': 'Seva za Overpass zinazopatikana:',
 'Overpass timeout must be greater than zero.':
   'Muda wa kusubiri wa Overpass lazima uwe mkubwa kuliko sufuri.',
 'Plugin version': 'Toleo la programu-jalizi',
 'Points of interest (POI)': 'Pointi za kuvutiwa (POI)',
 'Prepared {index:,} of {total:,} OSM elements for export...':
   'Imeandaa {index:,} kati ya {total:,} vipengele vya OSM kwa uhamishaji…',
 'Preparing Overpass download...':
   'Inaandaa upakuaji wa Overpass…',
 'Preparing Overpass query.': 'Inaandaa swali la Overpass.',
 'Processing Options': 'Chaguo za Uchakataji',
 'Processing log': 'Kumbukumbu ya uchakataji',
 'Processing messages will appear here...':
   'Ujumbe wa uchakataji utaonekana hapa…',
 'Processing options': 'Chaguo za uchakataji',
 'Public transport & places': 'Usafiri wa umma na maeneo',
 'QGIS interface object was not detected. Canvas-dependent AOI tools are disabled.':
   'Kipengele cha kiolesura cha QGIS hakijagunduliwa. Zana za AOI zinazotegemea turubai zimezimwa.',
 'QGIS map canvas could not be accessed.':
   'Turubai ya ramani ya QGIS haikuweza kufikiwa.',
 'QGIS map canvas is unavailable.':
   'Turubai ya ramani ya QGIS haipatikani.',
 'Rail stops': 'Vituo vya reli',
 'Railways': 'Reli',
 'Read the plugin version from metadata.txt (empty string if absent).':
   'Soma toleo la programu-jalizi kutoka metadata.txt (mfuatano tupu ikiwa haipo).',
 'Read, validate and store the current QGIS map canvas extent.':
   'Soma, thibitisha na hifadhi eneo la sasa la turubai ya ramani ya QGIS.',
 'Ready.': 'Tayari.',
 'Rectangle AOI drawing tool activated.':
   'Zana ya kuchora mstatili wa AOI imewashwa.',
 'Rectangle AOI drawing was cancelled.':
   'Uchoraji wa mstatili wa AOI ulighairiwa.',
 'Region name': 'Jina la mkoa',
 'Report an issue': 'Ripoti tatizo',
 'Request cooperative cancellation of the background worker.':
   'Omba ughairi wa kushirikiana wa mfanyakazi wa nyuma.',
 'Request error on server ': 'Hitilafu ya ombi kwenye seva ',
 'Restore default GUI settings when the dialog closes.':
   'Rejesha mipangilio chaguo-msingi ya GUI kidirisha kinapofungwa.',
 'Restore the GUI once the background thread has stopped.':
   'Rejesha GUI uzi wa nyuma unaposimama.',
 'Restore the QGIS map tool active before rectangle drawing.':
   'Rejesha zana ya ramani ya QGIS iliyokuwa amilifu kabla ya kuchora mstatili.',
 'Restore the map tool and reset state before hiding the dialog.':
   'Rejesha zana ya ramani na uweke upya hali kabla ya kuficha kidirisha.',
 'Retrying in ': 'Inajaribu tena baada ya ',
 'Return selected levels, or None when all levels are requested.':
   'Rudisha ngazi zilizochaguliwa, au None wakati ngazi zote zinaombwa.',
 'Return the combined, sanitized filename prefix.':
   'Rudisha kiambishi awali cha jina la faili kilichounganishwa na kusafishwa.',
 'Return the mapping between feature keys and GUI checkboxes.':
   'Rudisha ramani kati ya funguo za vipengele na visanduku vya kuchagua vya GUI.',
 'Return the selected GUI feature keys.':
   'Rudisha funguo za vipengele vya GUI zilizochaguliwa.',
 'Roads': 'Barabara',
 'Run a modal dialog on both Qt5 and Qt6.':
   'Endesha kidirisha cha modal kwenye Qt5 na Qt6.',
 'Select Output Directory': 'Chagua Folda ya Pato',
 'Select a vector layer with selected features.':
   'Chagua tabaka la vekta lenye vipengele vilivyochaguliwa.',
 'Select all': 'Chagua zote',
 'Select an active QGIS layer.': 'Chagua tabaka amilifu la QGIS.',
 'Select at least one OSM feature category before downloading.':
   'Chagua angalau kategoria moja ya kipengele cha OSM kabla ya kupakua.',
 'Select at least one administrative level, or choose All levels.':
   'Chagua angalau ngazi moja ya kiutawala, au chagua Ngazi zote.',
 'Select at least one administrative level, or use None to retrieve all levels.':
   'Chagua angalau ngazi moja ya kiutawala, au tumia None kupata ngazi zote.',
 'Select levels 0–15 and switch to specific-level mode.':
   'Chagua ngazi 0–15 na ubadilishe kwenda hali ya ngazi mahususi.',
 'Select one or more features in the active layer.':
   'Chagua kipengele kimoja au zaidi katika tabaka amilifu.',
 'Select output directory...': 'Chagua folda ya pato…',
 'Selected administrative levels:': 'Ngazi za kiutawala zilizochaguliwa:',
 'Selected feature IDs:': 'Vitambulisho vya vipengele vilivyochaguliwa:',
 'Selected feature(s) in active layer':
   'Kipengele/vipengele vilivyochaguliwa katika tabaka amilifu',
 'Selected features (': 'Vipengele vilivyochaguliwa (',
 'Selected-feature AOI captured successfully (':
   'AOI ya vipengele vilivyochaguliwa imenaswa kwa mafanikio (',
 'Selected-feature AOI captured successfully.':
   'AOI ya vipengele vilivyochaguliwa imenaswa kwa mafanikio.',
 'Selected-feature AOI is invalid.':
   'AOI ya vipengele vilivyochaguliwa si sahihi.',
 'Selected-feature AOI requires a vector layer.':
   'AOI ya vipengele vilivyochaguliwa inahitaji tabaka la vekta.',
 'Selected-feature AOI validation failed:':
   'Uthibitishaji wa AOI ya vipengele vilivyochaguliwa umeshindikana:',
 'Sending query to Overpass...': 'Inatuma swali kwa Overpass…',
 'Server ': 'Seva ',
 'Shapefile': 'Shapefile',
 'Shapefile export completed in:':
   'Uhamishaji wa Shapefile umekamilika kwa:',
 'Shapefile field names shortened for':
   'Majina ya sehemu za Shapefile yamefupishwa kwa',
 'Shapefile layer(s) to QGIS.': 'tabaka za Shapefile kwenye QGIS.',
 'Short in-plugin help with links to the full online documentation.':
   'Msaada mfupi ndani ya programu-jalizi wenye viungo vya nyaraka kamili za mtandaoni.',
 'Show AOI coordinates and source CRS in the dialog.':
   'Onyesha viwianishi vya AOI na CRS chanzo kwenye kidirisha.',
 'Show a concise description of the active administrative filter.':
   'Onyesha maelezo mafupi ya kichujio cha kiutawala kinachoendelea.',
 'Source CRS is invalid.': 'CRS chanzo si sahihi.',
 'South latitude cannot be greater than north latitude.':
   'Latitudo ya kusini haiwezi kuwa kubwa kuliko latitudo ya kaskazini.',
 'South:': 'Kusini:',
 'Starting Overpass download...':
   'Inaanza upakuaji wa Overpass…',
 'Supporting copy: muted, wrapped and visually quiet.':
   'Nakala saidizi: isiyo na sauti, imefungwa na kimya kimtazamo.',
 "Tag '{tag}' contains an empty value list.":
   'Lebo "{tag}" ina orodha tupu ya thamani.',
 'Temporary workspace cleanup complete:':
   'Usafishaji wa nafasi ya kazi ya muda umekamilika:',
 'Temporary workspace cleanup complete: no matching files found.':
   'Usafishaji wa nafasi ya kazi ya muda umekamilika: hakuna faili zinazolingana zilizopatikana.',
 'Temporary-file cleanup skipped: workspace directory is invalid.':
   'Usafishaji wa faili za muda umerukwa: folda ya nafasi ya kazi si sahihi.',
 'The OSM download succeeded, but the output could not be created.':
   'Upakuaji wa OSM umefanikiwa, lakini pato halikuweza kuundwa.',
 "The Overpass response must be a JSON object with an 'elements' list.":
   'Jibu la Overpass lazima liwe kipengele cha JSON chenye orodha ya "elements".',
 'The QGIS map canvas CRS is invalid.':
   'CRS ya turubai ya ramani ya QGIS si sahihi.',
 'The active layer CRS is invalid.':
   'CRS ya tabaka amilifu si sahihi.',
 'The active layer extent is empty.':
   'Eneo la tabaka amilifu ni tupu.',
 'The active layer must be a vector layer.':
   'Tabaka amilifu lazima liwe tabaka la vekta.',
 'The combined name is too long. Shorten one or more components.':
   'Jina lililounganishwa ni refu mno. Fupisha sehemu moja au zaidi.',
 'The combined selected-feature geometry is empty.':
   'Jiometri iliyounganishwa ya vipengele vilivyochaguliwa ni tupu.',
 'The current AOI is invalid:': 'AOI ya sasa si sahihi:',
 'The current QGIS map extent is empty.':
   'Eneo la sasa la ramani ya QGIS ni tupu.',
 'The dialog cannot close while a download thread is running. Cancellation has been requested; close the dialog after it stops.':
   'Kidirisha hakiwezi kufungwa wakati uzi wa upakuaji unaendelea. Ombi la kughairi limetolewa; funga kidirisha baada ya kusimama.',
 'The download completed, but no confirmed output name was available.':
   'Upakuaji umekamilika, lakini hakuna jina la pato lililothibitishwa lililokuwa linapatikana.',
 "The exported Shapefile '{path}' could not be opened in QGIS.":
   'Shapefile iliyohamishwa "{path}" haikuweza kufunguliwa kwenye QGIS.',
 "The exported layer '{layer_name}' could not be opened in QGIS.":
   'Tabaka lililohamishwa "{layer_name}" halikuweza kufunguliwa kwenye QGIS.',
 'The output name does not contain any valid filename characters.':
   'Jina la pato halina herufi yoyote halali ya jina la faili.',
 'The output name is empty after filename validation.':
   'Jina la pato ni tupu baada ya uthibitishaji wa jina la faili.',
 'The selected features contain no valid geometry.':
   'Vipengele vilivyochaguliwa havina jiometri halali.',
 'The selected output directory does not exist. Choose an existing folder.':
   'Folda ya pato iliyochaguliwa haipo. Chagua folda iliyopo.',
 'There is no active download to cancel.':
   'Hakuna upakuaji unaoendelea wa kughairi.',
 'Timeout on server ': 'Muda umeisha kwenye seva ',
 'Translate widget labels while preserving each original English string.':
   'Tafsiri lebo za wijeti huku ukihifadhi kila mfuatano halisi wa Kiingereza.',
 'Trying Overpass server ': 'Inajaribu seva ya Overpass ',
 'Unable to start AOI drawing:': 'Imeshindwa kuanza uchoraji wa AOI:',
 'Unclassified OSM elements not written to feature layers:':
   'Vipengele vya OSM visivyoainishwa ambavyo havikuandikwa kwenye tabaka za vipengele:',
 'Unsupported geometry family: {geometry_family}':
   'Familia ya jiometri isiyotumika: {geometry_family}',
 "Unsupported geometry type '{geometry_type}' for feature '{feature_key}'.":
   'Aina ya jiometri "{geometry_type}" isiyotumika kwa kipengele "{feature_key}".',
 'Unsupported geometry type for Shapefile export: {geometry_type}':
   'Aina ya jiometri isiyotumika kwa uhamishaji wa Shapefile: {geometry_type}',
 "Unsupported match mode '{mode}' for feature '{feature_key}'.":
   'Hali ya ulinganifu "{mode}" isiyotumika kwa kipengele "{feature_key}".',
 'Unsupported output format:': 'Umbizo la pato lisilotumika:',
 "Unsupported tag value type for '{feature_key}': {value_type}":
   'Aina ya thamani ya lebo isiyotumika kwa "{feature_key}": {value_type}',
 'Update Current QGIS Map Extent':
   'Sasisha Eneo la Sasa la Ramani ya QGIS',
 'Update the "N selected" count next to the category heading.':
   'Sasisha hesabu ya "N zimechaguliwa" kando ya kichwa cha kategoria.',
 'Update the filename preview as the user edits the components.':
   'Sasisha hakiki ya jina la faili mtumiaji anapohariri sehemu.',
 'Use Layer Extent': 'Tumia Eneo la Tabaka',
 'Use Selected Features': 'Tumia Vipengele Vilivyochaguliwa',
 'Use local cache where available':
   'Tumia akiba ya ndani inapopatikana',
 'Use selected features in the active vector layer as the AOI.':
   'Tumia vipengele vilivyochaguliwa katika tabaka la vekta amilifu kama AOI.',
 'Use the full extent of the active QGIS layer as the AOI.':
   'Tumia eneo kamili la tabaka amilifu la QGIS kama AOI.',
 'Use the full extent of the active QGIS layer.':
   'Tumia eneo kamili la tabaka amilifu la QGIS.',
 'Use the selected features of the active vector layer as the AOI.':
   'Tumia vipengele vilivyochaguliwa vya tabaka la vekta amilifu kama AOI.',
 'Using cached data; no Overpass network request was needed.':
   'Inatumia data iliyohifadhiwa kwenye akiba; hakuna ombi la mtandao la Overpass lililohitajika.',
 'Validate filename and any explicitly selected admin levels.':
   'Thibitisha jina la faili na ngazi zozote za admin zilizochaguliwa kwa uwazi.',
 'Validate inputs and start the background Overpass download.':
   'Thibitisha maingizo na uanze upakuaji wa Overpass wa nyuma.',
 'WGS84 AOI bbox: south=': 'Kisanduku cha mipaka cha AOI cha WGS84: kusini=',
 'WGS84 AOI geometry is not available.':
   'Jiometri ya AOI ya WGS84 haipatikani.',
 'Warning: download succeeded, but the response could not be cached:':
   'Onyo: upakuaji umefanikiwa, lakini jibu halikuweza kuhifadhiwa kwenye akiba:',
 'Waterways': 'Njia za maji',
 'West longitude cannot be greater than east longitude.':
   'Longitudo ya magharibi haiwezi kuwa kubwa kuliko longitudo ya mashariki.',
 'West:': 'Magharibi:',
 'Writing Shapefile {layer_index}/{total}: {layer_name}...':
   'Inaandika Shapefile {layer_index}/{total}: {layer_name}…',
 'Writing layer {layer_index}/{total}: {layer_name} ({count:,} features)...':
   'Inaandika tabaka {layer_index}/{total}: {layer_name} ({count:,} vipengele)…',
 'attempt ': 'jaribio ',
 'characters).': 'herufi).',
 'connection error — ': 'hitilafu ya muunganisho — ',
 'e.g. CBD': 'k.m. CBD',
 'e.g. Kenya': 'k.m. Kenya',
 'e.g. Nairobi': 'k.m. Nairobi',
 'e.g. NairobiCounty': 'k.m. NairobiCounty',
 'elements (': 'vipengele (',
 'export failed:': 'uhamishaji umeshindikana:',
 'feature records).': 'rekodi za vipengele).',
 'feature(s)).': 'kipengele/vipengele)).',
 'features written.': 'vipengele vimeandikwa.',
 'file(s) deleted.': 'faili zimefutwa.',
 'relation geometry assignment(s); relation-member geometry assembly is not implemented yet.':
   'mgao wa jiometri ya uhusiano; uunganishaji wa jiometri ya mwanachama wa uhusiano bado hautekelezwi.',
 'relations).': 'uhusiano).',
 'response_data must be a dictionary.':
   'response_data lazima iwe kamusi.',
 "response_data['elements'] must be a list.":
   "response_data['elements'] lazima iwe orodha.",
 'temporary file(s) could not be deleted. They may still be in use by QGIS or another process.':
   'faili za muda hazikuweza kufutwa. Zinaweza kuwa bado zinatumika na QGIS au mchakato mwingine.',
 'timeout — ': 'muda umeisha — ',
 '{output_format} export failed: {error}':
   'Uhamishaji wa {output_format} umeshindikana: {error}',
 '— Confirm Overwrite': '— Thibitisha Kuandika Juu',
 '— Export Error': '— Hitilafu ya Uhamishaji',
 '— Help': '— Msaada',
 '— Output Naming': '— Utajaji wa Pato',
}