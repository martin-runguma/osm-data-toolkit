"""Telugu (తెలుగు) translation pack for the OSM Data Toolkit plugin.
Keys remain the English source strings; preserve placeholders and HTML."""
TEXT = {
 '\n<h3>Quick start</h3>\n<ol>\n  <li><b>Choose an area.</b> Use the current map extent, draw a rectangle\n      on the map, or use the bounding box of selected features or a\n      layer\'s extent.</li>\n  <li><b>Tick the OSM categories</b> you need (POI, stops, roads,\n      buildings, boundaries, landuse, ...).</li>\n  <li><b>Choose an output format and folder</b>, then click\n      <b>Download OSM Data</b>.</li>\n</ol>\n\n<h3>Good to know</h3>\n<ul>\n  <li><b>GeoPackage is recommended.</b> A Shapefile cannot hold very many\n      attribute columns, so on large areas some rarely used tag columns\n      may be left out (the log tells you when this happens).</li>\n  <li><b>Keep the area focused.</b> Very large areas produce huge Overpass\n      responses and can be slow or rejected by the public servers.</li>\n  <li><b>The cache</b> lets repeat downloads of the same query reuse\n      earlier results.</li>\n  <li><b>"Unclassified OSM elements"</b> in the log is informational: they\n      are mostly untagged vertices of lines and polygons that do not belong\n      to any selected category.</li>\n</ul>\n\n<p>Data &copy; OpenStreetMap contributors, available under the\n<a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a>.</p>\n<p><i>This plugin is not endorsed by or affiliated with the\nOpenStreetMap Foundation.</i></p>\n':
 '\n<h3>త్వరిత ప్రారంభం</h3>\n<ol>\n  <li><b>ఒక ప్రాంతాన్ని ఎంచుకోండి.</b> ప్రస్తుత మ్యాప్ పరిధిని ఉపయోగించండి, మ్యాప్‌పై\n      దీర్ఘచతురస్రాన్ని గీయండి, లేదా ఎంచుకున్న ఫీచర్ల బౌండింగ్ బాక్స్ లేదా\n      లేయర్ పరిధిని ఉపయోగించండి.</li>\n  <li><b>మీకు అవసరమైన OSM వర్గాలను టిక్ చేయండి</b> (POI, స్టాప్‌లు, రోడ్లు,\n      భవనాలు, సరిహద్దులు, భూవినియోగం, ...).</li>\n  <li><b>అవుట్‌పుట్ ఫార్మాట్ మరియు ఫోల్డర్‌ను ఎంచుకోండి</b>, ఆపై\n      <b>OSM డేటాను డౌన్‌లోడ్ చేయండి</b>పై క్లిక్ చేయండి.</li>\n</ol>\n\n<h3>తెలుసుకోవడం మంచిది</h3>\n<ul>\n  <li><b>GeoPackage సిఫార్సు చేయబడింది.</b> Shapefile చాలా ఎక్కువ\n      లక్షణ నిలువు వరుసలను ఉంచుకోలేదు, కాబట్టి పెద్ద ప్రాంతాలలో కొన్ని\n      అరుదుగా ఉపయోగించే ట్యాగ్ నిలువు వరుసలు విస్మరించబడవచ్చు\n      (ఇది జరిగినప్పుడు లాగ్ మీకు తెలియజేస్తుంది).</li>\n  <li><b>ప్రాంతాన్ని దృష్టిలో ఉంచుకోండి.</b> చాలా పెద్ద ప్రాంతాలు భారీ Overpass\n      ప్రతిస్పందనలను ఉత్పత్తి చేస్తాయి మరియు నెమ్మదిగా ఉండవచ్చు లేదా\n      పబ్లిక్ సర్వర్‌లు తిరస్కరించవచ్చు.</li>\n  <li><b>కాష్</b> ఒకే ప్రశ్న యొక్క పునరావృత డౌన్‌లోడ్‌లను గత\n      ఫలితాలను తిరిగి ఉపయోగించడానికి అనుమతిస్తుంది.</li>\n  <li>లాగ్‌లోని <b>"వర్గీకరించని OSM మూలకాలు"</b> సమాచారం మాత్రమే: అవి\n      ఎక్కువగా ఏ ఎంచుకున్న వర్గానికీ చెందని లైన్లు మరియు బహుభుజాల\n      ట్యాగ్ లేని శీర్షాలు.</li>\n</ul>\n\n<p>డేటా &copy; OpenStreetMap సహకారులు, <a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a> కింద అందుబాటులో ఉంది.</p>\n<p><i>ఈ ప్లగిన్ OpenStreetMap Foundation ఆమోదం పొందలేదు లేదా దానితో అనుబంధించబడలేదు.</i></p>\n',
 ' responded successfully.': ' విజయవంతంగా ప్రతిస్పందించింది.',
 ' seconds...': ' సెకన్లు…',
 '" style="color:#0B5E8E; text-decoration:none;">OpenStreetMap contributors</a> (ODbL)':
   '" style="color:#0B5E8E; text-decoration:none;">OpenStreetMap సహకారులు</a> (ODbL)',
 ', east=': ', తూర్పు=',
 ', north=': ', ఉత్తరం=',
 ', west=': ', పడమర=',
 '0 selected': '0 ఎంచుకోబడింది',
 '<p>Plugin version': '<p>ప్లగిన్ వెర్షన్',
 'A download is already running.': 'డౌన్‌లోడ్ ఇప్పటికే నడుస్తోంది.',
 'A labelled column of feature checkboxes.':
   'ఫీచర్ చెక్‌బాక్స్‌ల లేబుల్ చేసిన నిలువు వరుస.',
 'AOI drawing cancelled.': 'AOI గీయడం రద్దు చేయబడింది.',
 'AOI geometry is empty.': 'AOI జ్యామితి ఖాళీగా ఉంది.',
 'AOI geometry is missing.': 'AOI జ్యామితి లేదు.',
 'AOI name': 'AOI పేరు',
 'AOI rectangle captured successfully.':
   'AOI దీర్ఘచతురస్రం విజయవంతంగా క్యాప్చర్ చేయబడింది.',
 'AOI source CRS is invalid.': 'AOI మూల CRS చెల్లదు.',
 'AOI validation failed:': 'AOI ధృవీకరణ విఫలమైంది:',
 'AOI:': 'AOI:',
 'AOI: QGIS interface is not available.':
   'AOI: QGIS ఇంటర్‌ఫేస్ అందుబాటులో లేదు.',
 "AOI: click 'Draw AOI', then drag a rectangle on the QGIS map.":
   'AOI: "AOI గీయండి" క్లిక్ చేయండి, ఆపై QGIS మ్యాప్‌పై దీర్ఘచతురస్రాన్ని లాగండి.',
 "AOI: click 'Use Layer Extent' to use the full extent of the active QGIS layer.":
   'AOI: సక్రియ QGIS లేయర్ పూర్తి పరిధిని ఉపయోగించడానికి "లేయర్ పరిధిని ఉపయోగించు" క్లిక్ చేయండి.',
 'AOI: click and drag on the QGIS map.':
   'AOI: QGIS మ్యాప్‌పై క్లిక్ చేసి లాగండి.',
 'AOI: failed to resolve active layer extent':
   'AOI: సక్రియ లేయర్ పరిధిని నిర్ధారించడం విఫలమైంది',
 'AOI: failed to resolve selected features':
   'AOI: ఎంచుకున్న ఫీచర్‌లను నిర్ధారించడం విఫలమైంది',
 'AOI: invalid': 'AOI: చెల్లదు',
 'AOI: no active QGIS layer.': 'AOI: సక్రియ QGIS లేయర్ లేదు.',
 'AOI: no feature(s) selected in the active layer.':
   'AOI: సక్రియ లేయర్‌లో ఏ ఫీచర్ ఎంచుకోబడలేదు.',
 'AOI: not yet resolved': 'AOI: ఇంకా నిర్ధారించబడలేదు',
 "AOI: select feature(s) in the active QGIS layer, then click 'Use Selected Features'.":
   'AOI: సక్రియ QGIS లేయర్‌లో ఫీచర్(లు) ఎంచుకోండి, ఆపై "ఎంచుకున్న ఫీచర్‌లను ఉపయోగించు" క్లిక్ చేయండి.',
 'AOI: the active layer is not a vector layer.':
   'AOI: సక్రియ లేయర్ వెక్టర్ లేయర్ కాదు.',
 'AOI: unable to create': 'AOI: సృష్టించడం సాధ్యం కాదు',
 'AOI: unable to resolve': 'AOI: నిర్ధారించడం సాధ్యం కాదు',
 'Activate the interactive rectangle AOI map tool.':
   'ఇంటరాక్టివ్ దీర్ఘచతురస్ర AOI మ్యాప్ సాధనాన్ని సక్రియం చేయండి.',
 'Active layer extent': 'సక్రియ లేయర్ పరిధి',
 'Active-layer extent AOI is invalid.':
   'సక్రియ-లేయర్ పరిధి AOI చెల్లదు.',
 'Active-layer extent captured successfully.':
   'సక్రియ-లేయర్ పరిధి విజయవంతంగా క్యాప్చర్ చేయబడింది.',
 'Active-layer extent validation failed:':
   'సక్రియ-లేయర్ పరిధి ధృవీకరణ విఫలమైంది:',
 'Administrative boundaries': 'పరిపాలనా సరిహద్దులు',
 'Administrative boundary filter: all levels (no admin_level filter).':
   'పరిపాలనా సరిహద్దు ఫిల్టర్: అన్ని స్థాయిలు (admin_level ఫిల్టర్ లేదు).',
 'Administrative boundary levels': 'పరిపాలనా సరిహద్దు స్థాయిలు',
 'Administrative boundary levels:': 'పరిపాలనా సరిహద్దు స్థాయిలు:',
 'Administrative levels must be an integer, a numeric string, a sequence of levels, or None.':
   'పరిపాలనా స్థాయిలు పూర్ణాంకం, సంఖ్యా స్ట్రింగ్, స్థాయిల క్రమం లేదా None అయి ఉండాలి.',
 'All OSM feature categories cleared.': 'అన్ని OSM ఫీచర్ వర్గాలు క్లియర్ చేయబడ్డాయి.',
 'All OSM feature categories selected.': 'అన్ని OSM ఫీచర్ వర్గాలు ఎంచుకోబడ్డాయి.',
 'All Overpass server URLs must be non-empty strings.':
   'అన్ని Overpass సర్వర్ URLలు ఖాళీ కాని స్ట్రింగ్‌లు అయి ఉండాలి.',
 'All Overpass servers and retry attempts failed.':
   'అన్ని Overpass సర్వర్‌లు మరియు పునఃప్రయత్నాలు విఫలమయ్యాయి.',
 'All administrative levels will be included.':
   'అన్ని పరిపాలనా స్థాయిలు చేర్చబడతాయి.',
 'All administrative levels will be included; no admin_level filter will be added to the query.':
   'అన్ని పరిపాలనా స్థాయిలు చేర్చబడతాయి; ప్రశ్నకు admin_level ఫిల్టర్ జోడించబడదు.',
 'All attempts failed for server ': 'సర్వర్ కోసం అన్ని ప్రయత్నాలు విఫలమయ్యాయి ',
 'All levels (0–15; no admin_level filter)':
   'అన్ని స్థాయిలు (0–15; admin_level ఫిల్టర్ లేదు)',
 'An existing output directory is required for Shapefile export.':
   'Shapefile ఎగుమతికి ఇప్పటికే ఉన్న అవుట్‌పుట్ డైరెక్టరీ అవసరం.',
 'An output GeoPackage path is required.':
   'అవుట్‌పుట్ GeoPackage మార్గం అవసరం.',
 'An output name is required for Shapefile export.':
   'Shapefile ఎగుమతికి అవుట్‌పుట్ పేరు అవసరం.',
 'Append a timestamped message to the processing log.':
   'ప్రాసెసింగ్ లాగ్‌కు టైమ్‌స్టాంప్‌తో సందేశాన్ని జోడించండి.',
 'Append an exported feature count to the processing log.':
   'ప్రాసెసింగ్ లాగ్‌కు ఎగుమతి చేసిన ఫీచర్‌ల సంఖ్యను జోడించండి.',
 'Area of Interest': 'ఆసక్తి ప్రాంతం',
 'At least one OSM feature must be selected.':
   'కనీసం ఒక OSM ఫీచర్ ఎంచుకోవాలి.',
 'At least one OSM feature must be supplied.':
   'కనీసం ఒక OSM ఫీచర్ అందించాలి.',
 'At least one Overpass server must be provided.':
   'కనీసం ఒక Overpass సర్వర్ అందించాలి.',
 'Attempt details:': 'ప్రయత్నం వివరాలు:',
 'Automatically add downloaded layers to QGIS':
   'డౌన్‌లోడ్ చేసిన లేయర్‌లను స్వయంచాలకంగా QGISకి జోడించండి',
 'Background Overpass download started.':
   'నేపథ్య Overpass డౌన్‌లోడ్ ప్రారంభమైంది.',
 'Browse': 'బ్రౌజ్ చేయండి',
 'Browse…': 'బ్రౌజ్ చేయండి…',
 'Buildings': 'భవనాలు',
 'Bus stops': 'బస్ స్టాప్‌లు',
 'CRS:': 'CRS:',
 'Cache hit:': 'కాష్ హిట్:',
 'Cache hit: using saved Overpass response ({age} day(s) old).':
   'కాష్ హిట్: సేవ్ చేసిన Overpass ప్రతిస్పందనను ఉపయోగిస్తోంది ({age} రోజులు పాతది).',
 'Cache miss:': 'కాష్ మిస్:',
 'Cache miss: could not read saved response ({error}).':
   'కాష్ మిస్: సేవ్ చేసిన ప్రతిస్పందనను చదవలేకపోయింది ({error}).',
 'Cache miss: query hash does not match the saved response.':
   'కాష్ మిస్: క్వెరీ హాష్ సేవ్ చేసిన ప్రతిస్పందనతో సరిపోలలేదు.',
 'Cache miss: saved response is incomplete or invalid.':
   'కాష్ మిస్: సేవ్ చేసిన ప్రతిస్పందన అసంపూర్ణం లేదా చెల్లదు.',
 'Cache miss: saved response is older than {days} days.':
   'కాష్ మిస్: సేవ్ చేసిన ప్రతిస్పందన {days} రోజుల కంటే పాతది.',
 'Cache miss: saved response uses an unsupported cache format.':
   'కాష్ మిస్: సేవ్ చేసిన ప్రతిస్పందన మద్దతు లేని కాష్ ఫార్మాట్‌ను ఉపయోగిస్తోంది.',
 'Cached Overpass response:': 'కాష్ చేసిన Overpass ప్రతిస్పందన:',
 'Cancel': 'రద్దు చేయండి',
 'Cancellation has already been requested.': 'రద్దు అభ్యర్థన ఇప్పటికే పంపబడింది.',
 'Cancellation requested': 'రద్దు అభ్యర్థించబడింది',
 'Cancellation requested. If an HTTP request is already active, the downloader will stop when that request returns or times out.':
   'రద్దు అభ్యర్థించబడింది. HTTP అభ్యర్థన ఇప్పటికే సక్రియంగా ఉంటే, ఆ అభ్యర్థన తిరిగి వచ్చినప్పుడు లేదా సమయం ముగిసినప్పుడు డౌన్‌లోడర్ ఆగిపోతుంది.',
 'Cancellation requested; waiting for the current request to finish...':
   'రద్దు అభ్యర్థించబడింది; ప్రస్తుత అభ్యర్థన పూర్తయ్యే వరకు వేచి ఉంది…',
 'Cannot draw AOI because the QGIS interface is unavailable.':
   'QGIS ఇంటర్‌ఫేస్ అందుబాటులో లేకపోవడం వల్ల AOI గీయలేము.',
 'Cannot resolve active-layer extent because QGIS is unavailable.':
   'QGIS అందుబాటులో లేకపోవడం వల్ల సక్రియ-లేయర్ పరిధిని నిర్ధారించలేము.',
 'Cannot resolve current map extent because QGIS is unavailable.':
   'QGIS అందుబాటులో లేకపోవడం వల్ల ప్రస్తుత మ్యాప్ పరిధిని నిర్ధారించలేము.',
 'Cannot resolve selected-feature AOI because QGIS is unavailable.':
   'QGIS అందుబాటులో లేకపోవడం వల్ల ఎంచుకున్న-ఫీచర్ AOIని నిర్ధారించలేము.',
 'Cannot transform an empty geometry.':
   'ఖాళీ జ్యామితిని మార్చలేము.',
 'Capture the current QGIS map canvas extent.':
   'ప్రస్తుత QGIS మ్యాప్ కాన్వాస్ పరిధిని క్యాప్చర్ చేయండి.',
 'Choose all available levels, or select one or more levels to download (for example, 5–8 or level 5).':
   'అందుబాటులో ఉన్న అన్ని స్థాయిలను ఎంచుకోండి, లేదా డౌన్‌లోడ్ చేయడానికి ఒకటి లేదా అంతకంటే ఎక్కువ స్థాయిలను ఎంచుకోండి (ఉదాహరణకు, 5–8 లేదా స్థాయి 5).',
 'Choose an output directory before downloading.':
   'డౌన్‌లోడ్ చేయడానికి ముందు అవుట్‌పుట్ డైరెక్టరీని ఎంచుకోండి.',
 'City name': 'నగరం పేరు',
 'Classifying OSM elements and preparing GeoPackage layers.':
   'OSM మూలకాలను వర్గీకరిస్తోంది మరియు GeoPackage లేయర్‌లను సిద్ధం చేస్తోంది.',
 'Classifying OSM elements and preparing Shapefile outputs.':
   'OSM మూలకాలను వర్గీకరిస్తోంది మరియు Shapefile అవుట్‌పుట్‌లను సిద్ధం చేస్తోంది.',
 'Clear all': 'అన్నీ క్లియర్ చేయండి',
 'Clear log': 'లాగ్ క్లియర్ చేయండి',
 'Clear only the visible log, without changing processing settings.':
   'ప్రాసెసింగ్ సెట్టింగ్‌లను మార్చకుండా కనిపించే లాగ్‌ను మాత్రమే క్లియర్ చేయండి.',
 'Clear selected levels so the user can make a narrower selection.':
   'వినియోగదారు సన్నని ఎంపిక చేయగలిగేలా ఎంచుకున్న స్థాయిలను క్లియర్ చేయండి.',
 'Clear the messages currently shown in the Processing Log.':
   'ప్రాసెసింగ్ లాగ్‌లో ప్రస్తుతం చూపబడుతున్న సందేశాలను క్లియర్ చేయండి.',
 'Clear the previous AOI and display guidance for the chosen method.':
   'మునుపటి AOIని క్లియర్ చేసి ఎంచుకున్న పద్ధతికి మార్గదర్శకత్వాన్ని చూపండి.',
 'Close': 'మూసివేయండి',
 'Collect optional filename components before exporting OSM data.':
   'OSM డేటాను ఎగుమతి చేయడానికి ముందు ఐచ్ఛిక ఫైల్‌నేమ్ భాగాలను సేకరించండి.',
 'Compact product header above the scrollable workflow.':
   'స్క్రోల్ చేయగల వర్క్‌ఫ్లో పైన కాంపాక్ట్ ఉత్పత్తి హెడర్.',
 'Connection error on server ': 'సర్వర్‌పై కనెక్షన్ లోపం ',
 'Continue to Download': 'డౌన్‌లోడ్‌కు కొనసాగండి',
 'Convert a name component into a Windows-safe filename token.':
   'పేరు భాగాన్ని Windows-సురక్షిత ఫైల్‌నేమ్ టోకెన్‌గా మార్చండి.',
 'Convert the drawn rectangle into the standard AOI object.':
   'గీసిన దీర్ఘచతురస్రాన్ని ప్రామాణిక AOI ఆబ్జెక్ట్‌గా మార్చండి.',
 'Converting OSM response to GeoPackage...':
   'OSM ప్రతిస్పందనను GeoPackageగా మారుస్తోంది…',
 'Converting OSM response to Shapefiles...':
   'OSM ప్రతిస్పందనను Shapefileలుగా మారుస్తోంది…',
 'Could not combine the selected feature geometries.':
   'ఎంచుకున్న ఫీచర్ జ్యామితులను కలపలేకపోయింది.',
 "Could not create Shapefile staging layer '{layer_name}'.":
   'Shapefile స్టేజింగ్ లేయర్ "{layer_name}"ని సృష్టించలేకపోయింది.',
 'Could not create an empty bus_stops_points layer.':
   'ఖాళీ bus_stops_points లేయర్‌ను సృష్టించలేకపోయింది.',
 "Could not create temporary QGIS layer '{layer_name}'.":
   'తాత్కాలిక QGIS లేయర్ "{layer_name}"ని సృష్టించలేకపోయింది.',
 'Could not create temporary layer for admin_level {admin_level}.':
   'admin_level {admin_level} కోసం తాత్కాలిక లేయర్‌ను సృష్టించలేకపోయింది.',
 'Could not create the merged bus_stops_points layer.':
   'విలీనం చేసిన bus_stops_points లేయర్‌ను సృష్టించలేకపోయింది.',
 'Could not delete temporary file': 'తాత్కాలిక ఫైల్‌ను తొలగించలేకపోయింది',
 "Could not load feature definition '{feature_key}': {error}":
   'ఫీచర్ నిర్వచనం "{feature_key}"ని లోడ్ చేయలేకపోయింది: {error}',
 'Could not merge bus-station centroids into bus-stop points.':
   'బస్-స్టేషన్ సెంట్రాయిడ్‌లను బస్-స్టాప్ పాయింట్‌లలో విలీనం చేయలేకపోయింది.',
 'Could not overwrite existing output file: {error}':
   'ఇప్పటికే ఉన్న అవుట్‌పుట్ ఫైల్‌ను ఓవర్‌రైట్ చేయలేకపోయింది: {error}',
 'Could not populate Shapefile for admin_level {admin_level}.':
   'admin_level {admin_level} కోసం Shapefileని నింపలేకపోయింది.',
 "Could not populate temporary layer '{layer_name}'.":
   'తాత్కాలిక లేయర్ "{layer_name}"ని నింపలేకపోయింది.',
 'Could not prepare the Overpass query:':
   'Overpass క్వెరీని సిద్ధం చేయలేకపోయింది:',
 "Could not reopen intermediate GeoPackage layer '{layer_name}'.":
   'ఇంటర్మీడియట్ GeoPackage లేయర్ "{layer_name}"ని మళ్లీ తెరవలేకపోయింది.',
 'Could not restore previous QGIS map tool:':
   'మునుపటి QGIS మ్యాప్ సాధనాన్ని పునరుద్ధరించలేకపోయింది:',
 'Could not search for temporary GeoPackages:':
   'తాత్కాలిక GeoPackageలను శోధించలేకపోయింది:',
 'Country name': 'దేశం పేరు',
 'Create one section panel and return it with its body layout.':
   'ఒక విభాగం ప్యానెల్‌ను సృష్టించి దాని బాడీ లేఅవుట్‌తో తిరిగి ఇవ్వండి.',
 'Created bus_stops_points from bus-station polygon centroids.':
   'బస్-స్టేషన్ బహుభుజి సెంట్రాయిడ్‌ల నుండి bus_stops_points సృష్టించబడింది.',
 'Current QGIS map extent': 'ప్రస్తుత QGIS మ్యాప్ పరిధి',
 'Current QGIS map extent resolved.':
   'ప్రస్తుత QGIS మ్యాప్ పరిధి నిర్ధారించబడింది.',
 'Data © <a href="': 'డేటా © <a href="',
 'Deleted temporary workspace file:':
   'తాత్కాలిక వర్క్‌స్పేస్ ఫైల్ తొలగించబడింది:',
 'Details:': 'వివరాలు:',
 'Download': 'డౌన్‌లోడ్',
 'Download OSM Data': 'OSM డేటాను డౌన్‌లోడ్ చేయండి',
 'Download OpenStreetMap data for any area and load it straight into QGIS.':
   'ఏదైనా ప్రాంతం కోసం OpenStreetMap డేటాను డౌన్‌లోడ్ చేసి నేరుగా QGISలో లోడ్ చేయండి.',
 'Download cancelled because existing output files were not approved for overwrite.':
   'ఇప్పటికే ఉన్న అవుట్‌పుట్ ఫైల్‌లను ఓవర్‌రైట్ చేయడానికి ఆమోదం లేకపోవడం వల్ల డౌన్‌లోడ్ రద్దు చేయబడింది.',
 'Download cancelled before it started.':
   'ప్రారంభం కాకముందే డౌన్‌లోడ్ రద్దు చేయబడింది.',
 'Download cancelled before results were returned.':
   'ఫలితాలు తిరిగి రాకముందే డౌన్‌లోడ్ రద్దు చేయబడింది.',
 'Download cancelled before starting.':
   'ప్రారంభించకముందే డౌన్‌లోడ్ రద్దు చేయబడింది.',
 'Download cancelled in the output-naming dialog.':
   'అవుట్‌పుట్-నేమింగ్ డైలాగ్‌లో డౌన్‌లోడ్ రద్దు చేయబడింది.',
 'Download cancelled.': 'డౌన్‌లోడ్ రద్దు చేయబడింది.',
 'Download cancelled; existing files preserved.':
   'డౌన్‌లోడ్ రద్దు చేయబడింది; ఇప్పటికే ఉన్న ఫైల్‌లు భద్రపరచబడ్డాయి.',
 'Download stopped.': 'డౌన్‌లోడ్ ఆగిపోయింది.',
 'Download succeeded, but export failed.':
   'డౌన్‌లోడ్ విజయవంతమైంది, కానీ ఎగుమతి విఫలమైంది.',
 'Downloading OSM data from Overpass...':
   'Overpass నుండి OSM డేటాను డౌన్‌లోడ్ చేస్తోంది…',
 'Draw AOI': 'AOI గీయండి',
 'Draw a rectangle on the QGIS map to define the AOI.':
   'AOIని నిర్వచించడానికి QGIS మ్యాప్‌పై దీర్ఘచతురస్రాన్ని గీయండి.',
 'Draw rectangle on map': 'మ్యాప్‌పై దీర్ఘచతురస్రాన్ని గీయండి',
 'Draw the AOI rectangle on the QGIS map.':
   'QGIS మ్యాప్‌పై AOI దీర్ఘచతురస్రాన్ని గీయండి.',
 'Drawn AOI validation failed:':
   'గీసిన AOI ధృవీకరణ విఫలమైంది:',
 'Drawn rectangle': 'గీసిన దీర్ఘచతురస్రం',
 'Drawn rectangle AOI captured successfully.':
   'గీసిన దీర్ఘచతురస్ర AOI విజయవంతంగా క్యాప్చర్ చేయబడింది.',
 'ERROR:': 'లోపం:',
 'East:': 'తూర్పు:',
 'Enable level checkboxes only when a specific selection is active.':
   'నిర్దిష్ట ఎంపిక సక్రియంగా ఉన్నప్పుడు మాత్రమే స్థాయి చెక్‌బాక్స్‌లను ప్రారంభించండి.',
 'Enable only the AOI action button for the selected method.':
   'ఎంచుకున్న పద్ధతికి AOI చర్య బటన్‌ను మాత్రమే ప్రారంభించండి.',
 'Enable or disable controls while a download is running.':
   'డౌన్‌లోడ్ నడుస్తున్నప్పుడు నియంత్రణలను ప్రారంభించండి లేదా నిలిపివేయండి.',
 'Enter at least one name (City, Country, Region, or AOI).':
   'కనీసం ఒక పేరును నమోదు చేయండి (నగరం, దేశం, ప్రాంతం లేదా AOI).',
 'Enter one or more name components. Blank fields will be skipped, and the remaining names will be joined with underscores. The selected output format will be retained.':
   'ఒకటి లేదా అంతకంటే ఎక్కువ పేరు భాగాలను నమోదు చేయండి. ఖాళీ ఫీల్డ్‌లు దాటవేయబడతాయి మరియు మిగిలిన పేర్లు అండర్‌స్కోర్‌లతో కలపబడతాయి. ఎంచుకున్న అవుట్‌పుట్ ఫార్మాట్ నిలుపుకోబడుతుంది.',
 'Enter_a_name_to_preview': 'ప్రివ్యూ_కోసం_పేరు_నమోదు_చేయండి',
 'Export cancelled: output name is missing.':
   'ఎగుమతి రద్దు: అవుట్‌పుట్ పేరు లేదు.',
 'Export complete:': 'ఎగుమతి పూర్తయింది:',
 'Export the downloaded response and optionally load its layers.':
   'డౌన్‌లోడ్ చేసిన ప్రతిస్పందనను ఎగుమతి చేయండి మరియు ఐచ్ఛికంగా దాని లేయర్‌లను లోడ్ చేయండి.',
 'Failed to activate rectangle AOI tool:':
   'దీర్ఘచతురస్ర AOI సాధనాన్ని సక్రియం చేయడం విఫలమైంది:',
 'Failed to create AOI.': 'AOIని సృష్టించడం విఫలమైంది.',
 'Failed to process drawn rectangle AOI:':
   'గీసిన దీర్ఘచతురస్ర AOIని ప్రాసెస్ చేయడం విఫలమైంది:',
 'Failed to resolve active-layer extent.':
   'సక్రియ-లేయర్ పరిధిని నిర్ధారించడం విఫలమైంది.',
 'Failed to resolve active-layer extent:':
   'సక్రియ-లేయర్ పరిధిని నిర్ధారించడం విఫలమైంది:',
 'Failed to resolve current QGIS map extent:':
   'ప్రస్తుత QGIS మ్యాప్ పరిధిని నిర్ధారించడం విఫలమైంది:',
 'Failed to resolve selected-feature AOI.':
   'ఎంచుకున్న-ఫీచర్ AOIని నిర్ధారించడం విఫలమైంది.',
 'Failed to resolve selected-feature AOI:':
   'ఎంచుకున్న-ఫీచర్ AOIని నిర్ధారించడం విఫలమైంది:',
 "Failed to write layer '{layer_name}' to '{output_path}': {error}":
   'లేయర్ "{layer_name}"ని "{output_path}"కి రాయడం విఫలమైంది: {error}',
 "Feature '{feature_key}' has no tag definitions.":
   'ఫీచర్ "{feature_key}"కు ట్యాగ్ నిర్వచనాలు లేవు.',
 'Feature specification  does not expose a tag-filter mapping.':
   'ఫీచర్ స్పెసిఫికేషన్ ట్యాగ్-ఫిల్టర్ మ్యాపింగ్‌ను అందించదు.',
 'Ferry stops': 'ఫెర్రీ స్టాప్‌లు',
 'Filename preview': 'ఫైల్‌నేమ్ ప్రివ్యూ',
 'Full documentation': 'పూర్తి డాక్యుమెంటేషన్',
 'Generated Overpass query (': 'ఉత్పత్తి చేసిన Overpass క్వెరీ (',
 'GeoPackage': 'GeoPackage',
 'GeoPackage layer(s) to QGIS.': 'GeoPackage లేయర్(లు) QGISలో.',
 'GeoPackage saved:': 'GeoPackage సేవ్ చేయబడింది:',
 'HTTP error on server ': 'సర్వర్‌పై HTTP లోపం ',
 'HTTP error — ': 'HTTP లోపం — ',
 'HTTP {status} error on server {index}/{total}.':
   'సర్వర్ {index}/{total}పై HTTP {status} లోపం.',
 'Handle a drawing tool deactivation initiated outside this dialog.':
   'ఈ డైలాగ్ వెలుపల ప్రారంభించిన డ్రాయింగ్ సాధన నిష్క్రియత్వాన్ని నిర్వహించండి.',
 'Help': 'సహాయం',
 'Invalid east longitude: {value}':
   'చెల్లని తూర్పు రేఖాంశం: {value}',
 'Invalid north latitude: {value}':
   'చెల్లని ఉత్తర అక్షాంశం: {value}',
 'Invalid response from server ': 'సర్వర్ నుండి చెల్లని ప్రతిస్పందన ',
 'Invalid south latitude: {value}':
   'చెల్లని దక్షిణ అక్షాంశం: {value}',
 'Invalid west longitude: {value}':
   'చెల్లని పడమర రేఖాంశం: {value}',
 'Keep the numeric readout in step with the progress bar.':
   'సంఖ్యా పఠనాన్ని ప్రోగ్రెస్ బార్‌తో సమన్వయంగా ఉంచండి.',
 'Land & built environment': 'భూమి & నిర్మిత పర్యావరణం',
 'Landuse': 'భూవినియోగం',
 'Language:': 'భాష:',
 'Linear features': 'రేఖీయ ఫీచర్‌లు',
 'Load the saved interface language and translate visible UI strings.':
   'సేవ్ చేసిన ఇంటర్‌ఫేస్ భాషను లోడ్ చేసి కనిపించే UI స్ట్రింగ్‌లను అనువదించండి.',
 'Local response cache is disabled.':
   'స్థానిక ప్రతిస్పందన కాష్ నిలిపివేయబడింది.',
 'Main OSM Data Toolkit window.': 'ప్రధాన OSM Data Toolkit విండో.',
 'Manually capture the map extent after the user pans or zooms.':
   'వినియోగదారు పాన్ లేదా జూమ్ చేసిన తర్వాత మ్యాప్ పరిధిని మాన్యువల్‌గా క్యాప్చర్ చేయండి.',
 'Merged bus-station polygon centroids into bus_stops_points.':
   'బస్-స్టేషన్ బహుభుజి సెంట్రాయిడ్‌లను bus_stops_pointsలో విలీనం చేసింది.',
 'No Overpass selectors were generated.':
   'Overpass సెలెక్టర్‌లు ఏవీ ఉత్పత్తి చేయబడలేదు.',
 'No active QGIS layer is available.':
   'సక్రియ QGIS లేయర్ ఏదీ అందుబాటులో లేదు.',
 'No active layer is available.':
   'సక్రియ లేయర్ ఏదీ అందుబాటులో లేదు.',
 'No exportable features matched the selected categories. Try another AOI or select additional OSM feature categories.':
   'ఎంచుకున్న వర్గాలతో సరిపోలిన ఎగుమతి చేయగల ఫీచర్‌లు ఏవీ లేవు. మరొక AOI ప్రయత్నించండి లేదా అదనపు OSM ఫీచర్ వర్గాలను ఎంచుకోండి.',
 'No features are selected in the active layer.':
   'సక్రియ లేయర్‌లో ఏ ఫీచర్ ఎంచుకోబడలేదు.',
 'No levels selected. Select at least one level to continue.':
   'స్థాయిలు ఏవీ ఎంచుకోబడలేదు. కొనసాగడానికి కనీసం ఒక స్థాయిని ఎంచుకోండి.',
 'No selected features found.':
   'ఎంచుకున్న ఫీచర్‌లు ఏవీ కనుగొనబడలేదు.',
 'No valid Area of Interest is available. Select an AOI method and resolve the AOI before downloading.':
   'చెల్లుబాటు అయ్యే ఆసక్తి ప్రాంతం ఏదీ అందుబాటులో లేదు. డౌన్‌లోడ్ చేయడానికి ముందు AOI పద్ధతిని ఎంచుకోండి మరియు AOIని నిర్ధారించండి.',
 'North:': 'ఉత్తరం:',
 'Note: {layer_name} has too many tag columns for one Shapefile (DBF size limit); {count} rarely-used columns were left out.':
   'గమనిక: {layer_name}కు ఒక Shapefile కోసం చాలా ఎక్కువ ట్యాగ్ నిలువు వరుసలు ఉన్నాయి (DBF పరిమాణ పరిమితి); {count} అరుదుగా ఉపయోగించే నిలువు వరుసలు విస్మరించబడ్డాయి.',
 'OSM Data Toolkit': 'OSM Data Toolkit',
 'OSM Data Toolkit initialised.':
   'OSM Data Toolkit ప్రారంభించబడింది.',
 'OSM Feature Categories': 'OSM ఫీచర్ వర్గాలు',
 'OSM export completed successfully.':
   'OSM ఎగుమతి విజయవంతంగా పూర్తయింది.',
 'One or more output files with this name already exist. Do you want to overwrite the matching output files?':
   'ఈ పేరుతో ఒకటి లేదా అంతకంటే ఎక్కువ అవుట్‌పుట్ ఫైల్‌లు ఇప్పటికే ఉన్నాయి. సరిపోలే అవుట్‌పుట్ ఫైల్‌లను ఓవర్‌రైట్ చేయాలనుకుంటున్నారా?',
 'Only the selected levels': 'ఎంచుకున్న స్థాయిలు మాత్రమే',
 'Only validated Overpass responses can be cached.':
   'ధృవీకరించబడిన Overpass ప్రతిస్పందనలను మాత్రమే కాష్ చేయవచ్చు.',
 'Open public spaces': 'ఓపెన్ పబ్లిక్ స్పేస్‌లు',
 'Open the in-plugin help with links to the online documentation.':
   'ఆన్‌లైన్ డాక్యుమెంటేషన్ లింక్‌లతో ప్లగిన్-లోపలి సహాయాన్ని తెరవండి.',
 'Output Settings': 'అవుట్‌పుట్ సెట్టింగ్‌లు',
 'Output directory': 'అవుట్‌పుట్ డైరెక్టరీ',
 'Output directory selected:': 'అవుట్‌పుట్ డైరెక్టరీ ఎంచుకోబడింది:',
 'Output format': 'అవుట్‌పుట్ ఫార్మాట్',
 'Output settings': 'అవుట్‌పుట్ సెట్టింగ్‌లు',
 'Overpass download cancelled.': 'Overpass డౌన్‌లోడ్ రద్దు చేయబడింది.',
 'Overpass download completed:': 'Overpass డౌన్‌లోడ్ పూర్తయింది:',
 'Overpass download failed.': 'Overpass డౌన్‌లోడ్ విఫలమైంది.',
 'Overpass download failed:': 'Overpass డౌన్‌లోడ్ విఫలమైంది:',
 'Overpass download running...': 'Overpass డౌన్‌లోడ్ నడుస్తోంది…',
 'Overpass download was cancelled by the caller.':
   'Overpass డౌన్‌లోడ్ కాలర్ ద్వారా రద్దు చేయబడింది.',
 'Overpass query must be a non-empty string.':
   'Overpass క్వెరీ ఖాళీ కాని స్ట్రింగ్ అయి ఉండాలి.',
 "Overpass response 'elements' field is not a list.":
   'Overpass ప్రతిస్పందన "elements" ఫీల్డ్ జాబితా కాదు.',
 "Overpass response does not contain an 'elements' field.":
   'Overpass ప్రతిస్పందనలో "elements" ఫీల్డ్ లేదు.',
 'Overpass response is not a JSON object.':
   'Overpass ప్రతిస్పందన JSON ఆబ్జెక్ట్ కాదు.',
 'Overpass response received successfully:':
   'Overpass ప్రతిస్పందన విజయవంతంగా స్వీకరించబడింది:',
 'Overpass server ': 'Overpass సర్వర్ ',
 'Overpass server returned invalid JSON. Response preview: ':
   'Overpass సర్వర్ చెల్లని JSONని తిరిగి ఇచ్చింది. ప్రతిస్పందన ప్రివ్యూ: ',
 'Overpass servers available:': 'అందుబాటులో ఉన్న Overpass సర్వర్‌లు:',
 'Overpass timeout must be greater than zero.':
   'Overpass సమయ పరిమితి సున్నా కంటే ఎక్కువగా ఉండాలి.',
 'Plugin version': 'ప్లగిన్ వెర్షన్',
 'Points of interest (POI)': 'ఆసక్తి పాయింట్లు (POI)',
 'Prepared {index:,} of {total:,} OSM elements for export...':
   'ఎగుమతి కోసం {total:,}లో {index:,} OSM మూలకాలు సిద్ధం చేయబడ్డాయి…',
 'Preparing Overpass download...':
   'Overpass డౌన్‌లోడ్‌ను సిద్ధం చేస్తోంది…',
 'Preparing Overpass query.':
   'Overpass క్వెరీని సిద్ధం చేస్తోంది.',
 'Processing Options': 'ప్రాసెసింగ్ ఎంపికలు',
 'Processing log': 'ప్రాసెసింగ్ లాగ్',
 'Processing messages will appear here...':
   'ప్రాసెసింగ్ సందేశాలు ఇక్కడ కనిపిస్తాయి…',
 'Processing options': 'ప్రాసెసింగ్ ఎంపికలు',
 'Public transport & places': 'పబ్లిక్ రవాణా & స్థలాలు',
 'QGIS interface object was not detected. Canvas-dependent AOI tools are disabled.':
   'QGIS ఇంటర్‌ఫేస్ ఆబ్జెక్ట్ గుర్తించబడలేదు. కాన్వాస్-ఆధారిత AOI సాధనాలు నిలిపివేయబడ్డాయి.',
 'QGIS map canvas could not be accessed.':
   'QGIS మ్యాప్ కాన్వాస్‌ను యాక్సెస్ చేయలేకపోయింది.',
 'QGIS map canvas is unavailable.':
   'QGIS మ్యాప్ కాన్వాస్ అందుబాటులో లేదు.',
 'Rail stops': 'రైలు స్టాప్‌లు',
 'Railways': 'రైల్వేలు',
 'Read the plugin version from metadata.txt (empty string if absent).':
   'metadata.txt నుండి ప్లగిన్ వెర్షన్‌ను చదవండి (లేకపోతే ఖాళీ స్ట్రింగ్).',
 'Read, validate and store the current QGIS map canvas extent.':
   'ప్రస్తుత QGIS మ్యాప్ కాన్వాస్ పరిధిని చదవండి, ధృవీకరించండి మరియు నిల్వ చేయండి.',
 'Ready.': 'సిద్ధం.',
 'Rectangle AOI drawing tool activated.':
   'దీర్ఘచతురస్ర AOI డ్రాయింగ్ సాధనం సక్రియం చేయబడింది.',
 'Rectangle AOI drawing was cancelled.':
   'దీర్ఘచతురస్ర AOI డ్రాయింగ్ రద్దు చేయబడింది.',
 'Region name': 'ప్రాంతం పేరు',
 'Report an issue': 'సమస్యను నివేదించండి',
 'Request cooperative cancellation of the background worker.':
   'నేపథ్య వర్కర్ సహకార రద్దును అభ్యర్థించండి.',
 'Request error on server ': 'సర్వర్‌పై అభ్యర్థన లోపం ',
 'Restore default GUI settings when the dialog closes.':
   'డైలాగ్ మూసివేసినప్పుడు డిఫాల్ట్ GUI సెట్టింగ్‌లను పునరుద్ధరించండి.',
 'Restore the GUI once the background thread has stopped.':
   'నేపథ్య థ్రెడ్ ఆగిన తర్వాత GUIని పునరుద్ధరించండి.',
 'Restore the QGIS map tool active before rectangle drawing.':
   'దీర్ఘచతురస్రం గీయడానికి ముందు సక్రియంగా ఉన్న QGIS మ్యాప్ సాధనాన్ని పునరుద్ధరించండి.',
 'Restore the map tool and reset state before hiding the dialog.':
   'డైలాగ్‌ను దాచడానికి ముందు మ్యాప్ సాధనాన్ని పునరుద్ధరించి స్థితిని రీసెట్ చేయండి.',
 'Retrying in ': 'మళ్లీ ప్రయత్నిస్తోంది ',
 'Return selected levels, or None when all levels are requested.':
   'ఎంచుకున్న స్థాయిలను తిరిగి ఇవ్వండి, లేదా అన్ని స్థాయిలు అభ్యర్థించినప్పుడు None.',
 'Return the combined, sanitized filename prefix.':
   'కలిపిన, శుద్ధి చేసిన ఫైల్‌నేమ్ ప్రిఫిక్స్‌ను తిరిగి ఇవ్వండి.',
 'Return the mapping between feature keys and GUI checkboxes.':
   'ఫీచర్ కీలు మరియు GUI చెక్‌బాక్స్‌ల మధ్య మ్యాపింగ్‌ను తిరిగి ఇవ్వండి.',
 'Return the selected GUI feature keys.':
   'ఎంచుకున్న GUI ఫీచర్ కీలను తిరిగి ఇవ్వండి.',
 'Roads': 'రోడ్లు',
 'Run a modal dialog on both Qt5 and Qt6.':
   'Qt5 మరియు Qt6 రెండింటిపై మోడల్ డైలాగ్‌ను అమలు చేయండి.',
 'Select Output Directory': 'అవుట్‌పుట్ డైరెక్టరీని ఎంచుకోండి',
 'Select a vector layer with selected features.':
   'ఎంచుకున్న ఫీచర్‌లతో వెక్టర్ లేయర్‌ను ఎంచుకోండి.',
 'Select all': 'అన్నీ ఎంచుకోండి',
 'Select an active QGIS layer.': 'సక్రియ QGIS లేయర్‌ను ఎంచుకోండి.',
 'Select at least one OSM feature category before downloading.':
   'డౌన్‌లోడ్ చేయడానికి ముందు కనీసం ఒక OSM ఫీచర్ వర్గాన్ని ఎంచుకోండి.',
 'Select at least one administrative level, or choose All levels.':
   'కనీసం ఒక పరిపాలనా స్థాయిని ఎంచుకోండి, లేదా "అన్ని స్థాయిలు" ఎంచుకోండి.',
 'Select at least one administrative level, or use None to retrieve all levels.':
   'కనీసం ఒక పరిపాలనా స్థాయిని ఎంచుకోండి, లేదా అన్ని స్థాయిలను పొందడానికి None ఉపయోగించండి.',
 'Select levels 0–15 and switch to specific-level mode.':
   '0–15 స్థాయిలను ఎంచుకోండి మరియు నిర్దిష్ట-స్థాయి మోడ్‌కు మారండి.',
 'Select one or more features in the active layer.':
   'సక్రియ లేయర్‌లో ఒకటి లేదా అంతకంటే ఎక్కువ ఫీచర్‌లను ఎంచుకోండి.',
 'Select output directory...': 'అవుట్‌పుట్ డైరెక్టరీని ఎంచుకోండి…',
 'Selected administrative levels:': 'ఎంచుకున్న పరిపాలనా స్థాయిలు:',
 'Selected feature IDs:': 'ఎంచుకున్న ఫీచర్ IDలు:',
 'Selected feature(s) in active layer':
   'సక్రియ లేయర్‌లో ఎంచుకున్న ఫీచర్(లు)',
 'Selected features (': 'ఎంచుకున్న ఫీచర్‌లు (',
 'Selected-feature AOI captured successfully (':
   'ఎంచుకున్న-ఫీచర్ AOI విజయవంతంగా క్యాప్చర్ చేయబడింది (',
 'Selected-feature AOI captured successfully.':
   'ఎంచుకున్న-ఫీచర్ AOI విజయవంతంగా క్యాప్చర్ చేయబడింది.',
 'Selected-feature AOI is invalid.':
   'ఎంచుకున్న-ఫీచర్ AOI చెల్లదు.',
 'Selected-feature AOI requires a vector layer.':
   'ఎంచుకున్న-ఫీచర్ AOIకి వెక్టర్ లేయర్ అవసరం.',
 'Selected-feature AOI validation failed:':
   'ఎంచుకున్న-ఫీచర్ AOI ధృవీకరణ విఫలమైంది:',
 'Sending query to Overpass...': 'Overpassకి క్వెరీని పంపుతోంది…',
 'Server ': 'సర్వర్ ',
 'Shapefile': 'Shapefile',
 'Shapefile export completed in:':
   'Shapefile ఎగుమతి పూర్తయింది:',
 'Shapefile field names shortened for':
   'Shapefile ఫీల్డ్ పేర్లు చిన్నవి చేయబడ్డాయి',
 'Shapefile layer(s) to QGIS.': 'Shapefile లేయర్(లు) QGISలో.',
 'Short in-plugin help with links to the full online documentation.':
   'పూర్తి ఆన్‌లైన్ డాక్యుమెంటేషన్ లింక్‌లతో సంక్షిప్త ప్లగిన్-లోపలి సహాయం.',
 'Show AOI coordinates and source CRS in the dialog.':
   'డైలాగ్‌లో AOI కోఆర్డినేట్‌లు మరియు మూల CRSని చూపండి.',
 'Show a concise description of the active administrative filter.':
   'సక్రియ పరిపాలనా ఫిల్టర్ యొక్క సంక్షిప్త వివరణను చూపండి.',
 'Source CRS is invalid.': 'మూల CRS చెల్లదు.',
 'South latitude cannot be greater than north latitude.':
   'దక్షిణ అక్షాంశం ఉత్తర అక్షాంశం కంటే ఎక్కువగా ఉండకూడదు.',
 'South:': 'దక్షిణం:',
 'Starting Overpass download...':
   'Overpass డౌన్‌లోడ్ ప్రారంభిస్తోంది…',
 'Supporting copy: muted, wrapped and visually quiet.':
   'సహాయక వచనం: మ్యూట్ చేయబడింది, చుట్టబడింది మరియు దృశ్యపరంగా ప్రశాంతం.',
 "Tag '{tag}' contains an empty value list.":
   'ట్యాగ్ "{tag}" ఖాళీ విలువ జాబితాను కలిగి ఉంది.',
 'Temporary workspace cleanup complete:':
   'తాత్కాలిక వర్క్‌స్పేస్ క్లీనప్ పూర్తయింది:',
 'Temporary workspace cleanup complete: no matching files found.':
   'తాత్కాలిక వర్క్‌స్పేస్ క్లీనప్ పూర్తయింది: సరిపోలే ఫైల్‌లు ఏవీ కనుగొనబడలేదు.',
 'Temporary-file cleanup skipped: workspace directory is invalid.':
   'తాత్కాలిక-ఫైల్ క్లీనప్ దాటవేయబడింది: వర్క్‌స్పేస్ డైరెక్టరీ చెల్లదు.',
 'The OSM download succeeded, but the output could not be created.':
   'OSM డౌన్‌లోడ్ విజయవంతమైంది, కానీ అవుట్‌పుట్‌ను సృష్టించలేకపోయింది.',
 "The Overpass response must be a JSON object with an 'elements' list.":
   'Overpass ప్రతిస్పందన "elements" జాబితాతో JSON ఆబ్జెక్ట్ అయి ఉండాలి.',
 'The QGIS map canvas CRS is invalid.':
   'QGIS మ్యాప్ కాన్వాస్ CRS చెల్లదు.',
 'The active layer CRS is invalid.':
   'సక్రియ లేయర్ CRS చెల్లదు.',
 'The active layer extent is empty.':
   'సక్రియ లేయర్ పరిధి ఖాళీగా ఉంది.',
 'The active layer must be a vector layer.':
   'సక్రియ లేయర్ వెక్టర్ లేయర్ అయి ఉండాలి.',
 'The combined name is too long. Shorten one or more components.':
   'కలిపిన పేరు చాలా పొడవుగా ఉంది. ఒకటి లేదా అంతకంటే ఎక్కువ భాగాలను చిన్నవి చేయండి.',
 'The combined selected-feature geometry is empty.':
   'కలిపిన ఎంచుకున్న-ఫీచర్ జ్యామితి ఖాళీగా ఉంది.',
 'The current AOI is invalid:': 'ప్రస్తుత AOI చెల్లదు:',
 'The current QGIS map extent is empty.':
   'ప్రస్తుత QGIS మ్యాప్ పరిధి ఖాళీగా ఉంది.',
 'The dialog cannot close while a download thread is running. Cancellation has been requested; close the dialog after it stops.':
   'డౌన్‌లోడ్ థ్రెడ్ నడుస్తున్నప్పుడు డైలాగ్ మూసివేయలేము. రద్దు అభ్యర్థించబడింది; అది ఆగిన తర్వాత డైలాగ్‌ను మూసివేయండి.',
 'The download completed, but no confirmed output name was available.':
   'డౌన్‌లోడ్ పూర్తయింది, కానీ ధృవీకరించబడిన అవుట్‌పుట్ పేరు ఏదీ అందుబాటులో లేదు.',
 "The exported Shapefile '{path}' could not be opened in QGIS.":
   'ఎగుమతి చేసిన Shapefile "{path}"ని QGISలో తెరవలేకపోయింది.',
 "The exported layer '{layer_name}' could not be opened in QGIS.":
   'ఎగుమతి చేసిన లేయర్ "{layer_name}"ని QGISలో తెరవలేకపోయింది.',
 'The output name does not contain any valid filename characters.':
   'అవుట్‌పుట్ పేరులో చెల్లుబాటు అయ్యే ఫైల్‌నేమ్ అక్షరాలు ఏవీ లేవు.',
 'The output name is empty after filename validation.':
   'ఫైల్‌నేమ్ ధృవీకరణ తర్వాత అవుట్‌పుట్ పేరు ఖాళీగా ఉంది.',
 'The selected features contain no valid geometry.':
   'ఎంచుకున్న ఫీచర్‌లలో చెల్లుబాటు అయ్యే జ్యామితి ఏదీ లేదు.',
 'The selected output directory does not exist. Choose an existing folder.':
   'ఎంచుకున్న అవుట్‌పుట్ డైరెక్టరీ ఉనికిలో లేదు. ఇప్పటికే ఉన్న ఫోల్డర్‌ను ఎంచుకోండి.',
 'There is no active download to cancel.':
   'రద్దు చేయడానికి సక్రియ డౌన్‌లోడ్ ఏదీ లేదు.',
 'Timeout on server ': 'సర్వర్‌పై సమయం ముగిసింది ',
 'Translate widget labels while preserving each original English string.':
   'ప్రతి అసలు ఇంగ్లీష్ స్ట్రింగ్‌ను భద్రపరుస్తూ విడ్జెట్ లేబుల్‌లను అనువదించండి.',
 'Trying Overpass server ': 'Overpass సర్వర్‌ను ప్రయత్నిస్తోంది ',
 'Unable to start AOI drawing:': 'AOI గీయడం ప్రారంభించలేకపోయింది:',
 'Unclassified OSM elements not written to feature layers:':
   'ఫీచర్ లేయర్‌లకు రాయబడని వర్గీకరించని OSM మూలకాలు:',
 'Unsupported geometry family: {geometry_family}':
   'మద్దతు లేని జ్యామితి కుటుంబం: {geometry_family}',
 "Unsupported geometry type '{geometry_type}' for feature '{feature_key}'.":
   'ఫీచర్ "{feature_key}"కు మద్దతు లేని జ్యామితి రకం "{geometry_type}".',
 'Unsupported geometry type for Shapefile export: {geometry_type}':
   'Shapefile ఎగుమతికి మద్దతు లేని జ్యామితి రకం: {geometry_type}',
 "Unsupported match mode '{mode}' for feature '{feature_key}'.":
   'ఫీచర్ "{feature_key}"కు మద్దతు లేని మ్యాచ్ మోడ్ "{mode}".',
 'Unsupported output format:': 'మద్దతు లేని అవుట్‌పుట్ ఫార్మాట్:',
 "Unsupported tag value type for '{feature_key}': {value_type}":
   '"{feature_key}"కు మద్దతు లేని ట్యాగ్ విలువ రకం: {value_type}',
 'Update Current QGIS Map Extent':
   'ప్రస్తుత QGIS మ్యాప్ పరిధిని నవీకరించండి',
 'Update the "N selected" count next to the category heading.':
   'వర్గం శీర్షిక పక్కన "N ఎంచుకోబడింది" గణనను నవీకరించండి.',
 'Update the filename preview as the user edits the components.':
   'వినియోగదారు భాగాలను సవరిస్తున్నప్పుడు ఫైల్‌నేమ్ ప్రివ్యూను నవీకరించండి.',
 'Use Layer Extent': 'లేయర్ పరిధిని ఉపయోగించు',
 'Use Selected Features': 'ఎంచుకున్న ఫీచర్‌లను ఉపయోగించు',
 'Use local cache where available':
   'అందుబాటులో ఉన్న చోట స్థానిక కాష్‌ను ఉపయోగించండి',
 'Use selected features in the active vector layer as the AOI.':
   'సక్రియ వెక్టర్ లేయర్‌లో ఎంచుకున్న ఫీచర్‌లను AOIగా ఉపయోగించండి.',
 'Use the full extent of the active QGIS layer as the AOI.':
   'సక్రియ QGIS లేయర్ పూర్తి పరిధిని AOIగా ఉపయోగించండి.',
 'Use the full extent of the active QGIS layer.':
   'సక్రియ QGIS లేయర్ పూర్తి పరిధిని ఉపయోగించండి.',
 'Use the selected features of the active vector layer as the AOI.':
   'సక్రియ వెక్టర్ లేయర్ యొక్క ఎంచుకున్న ఫీచర్‌లను AOIగా ఉపయోగించండి.',
 'Using cached data; no Overpass network request was needed.':
   'కాష్ చేసిన డేటాను ఉపయోగిస్తోంది; Overpass నెట్‌వర్క్ అభ్యర్థన అవసరం లేదు.',
 'Validate filename and any explicitly selected admin levels.':
   'ఫైల్‌నేమ్ మరియు స్పష్టంగా ఎంచుకున్న admin స్థాయిలను ధృవీకరించండి.',
 'Validate inputs and start the background Overpass download.':
   'ఇన్‌పుట్‌లను ధృవీకరించి నేపథ్య Overpass డౌన్‌లోడ్‌ను ప్రారంభించండి.',
 'WGS84 AOI bbox: south=': 'WGS84 AOI బౌండింగ్ బాక్స్: దక్షిణం=',
 'WGS84 AOI geometry is not available.':
   'WGS84 AOI జ్యామితి అందుబాటులో లేదు.',
 'Warning: download succeeded, but the response could not be cached:':
   'హెచ్చరిక: డౌన్‌లోడ్ విజయవంతమైంది, కానీ ప్రతిస్పందనను కాష్ చేయలేకపోయింది:',
 'Waterways': 'నీటి మార్గాలు',
 'West longitude cannot be greater than east longitude.':
   'పడమర రేఖాంశం తూర్పు రేఖాంశం కంటే ఎక్కువగా ఉండకూడదు.',
 'West:': 'పడమర:',
 'Writing Shapefile {layer_index}/{total}: {layer_name}...':
   'Shapefile {layer_index}/{total} రాస్తోంది: {layer_name}…',
 'Writing layer {layer_index}/{total}: {layer_name} ({count:,} features)...':
   'లేయర్ {layer_index}/{total} రాస్తోంది: {layer_name} ({count:,} ఫీచర్‌లు)…',
 'attempt ': 'ప్రయత్నం ',
 'characters).': 'అక్షరాలు).',
 'connection error — ': 'కనెక్షన్ లోపం — ',
 'e.g. CBD': 'ఉదా. CBD',
 'e.g. Kenya': 'ఉదా. కెన్యా',
 'e.g. Nairobi': 'ఉదా. నైరోబీ',
 'e.g. NairobiCounty': 'ఉదా. NairobiCounty',
 'elements (': 'మూలకాలు (',
 'export failed:': 'ఎగుమతి విఫలమైంది:',
 'feature records).': 'ఫీచర్ రికార్డ్‌లు).',
 'feature(s)).': 'ఫీచర్(లు)).',
 'features written.': 'ఫీచర్‌లు రాయబడ్డాయి.',
 'file(s) deleted.': 'ఫైల్(లు) తొలగించబడ్డాయి.',
 'relation geometry assignment(s); relation-member geometry assembly is not implemented yet.':
   'రిలేషన్ జ్యామితి కేటాయింపు(లు); రిలేషన్-సభ్యుల జ్యామితి అసెంబ్లీ ఇంకా అమలు చేయబడలేదు.',
 'relations).': 'రిలేషన్‌లు).',
 'response_data must be a dictionary.':
   'response_data నిఘంటువు అయి ఉండాలి.',
 "response_data['elements'] must be a list.":
   "response_data['elements'] జాబితా అయి ఉండాలి.",
 'temporary file(s) could not be deleted. They may still be in use by QGIS or another process.':
   'తాత్కాలిక ఫైల్(లు) తొలగించలేకపోయింది. అవి ఇంకా QGIS లేదా మరొక ప్రాసెస్ ద్వారా ఉపయోగంలో ఉండవచ్చు.',
 'timeout — ': 'సమయం ముగిసింది — ',
 '{output_format} export failed: {error}':
   '{output_format} ఎగుమతి విఫలమైంది: {error}',
 '— Confirm Overwrite': '— ఓవర్‌రైట్‌ను నిర్ధారించండి',
 '— Export Error': '— ఎగుమతి లోపం',
 '— Help': '— సహాయం',
 '— Output Naming': '— అవుట్‌పుట్ నామకరణం',
}