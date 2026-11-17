"""Marathi (मराठी) translation pack for the OSM Data Toolkit plugin.
Keys remain the English source strings; preserve placeholders and HTML."""
TEXT = {
 '\n<h3>Quick start</h3>\n<ol>\n  <li><b>Choose an area.</b> Use the current map extent, draw a rectangle\n      on the map, or use the bounding box of selected features or a\n      layer\'s extent.</li>\n  <li><b>Tick the OSM categories</b> you need (POI, stops, roads,\n      buildings, boundaries, landuse, ...).</li>\n  <li><b>Choose an output format and folder</b>, then click\n      <b>Download OSM Data</b>.</li>\n</ol>\n\n<h3>Good to know</h3>\n<ul>\n  <li><b>GeoPackage is recommended.</b> A Shapefile cannot hold very many\n      attribute columns, so on large areas some rarely used tag columns\n      may be left out (the log tells you when this happens).</li>\n  <li><b>Keep the area focused.</b> Very large areas produce huge Overpass\n      responses and can be slow or rejected by the public servers.</li>\n  <li><b>The cache</b> lets repeat downloads of the same query reuse\n      earlier results.</li>\n  <li><b>"Unclassified OSM elements"</b> in the log is informational: they\n      are mostly untagged vertices of lines and polygons that do not belong\n      to any selected category.</li>\n</ul>\n\n<p>Data &copy; OpenStreetMap contributors, available under the\n<a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a>.</p>\n<p><i>This plugin is not endorsed by or affiliated with the\nOpenStreetMap Foundation.</i></p>\n':
 '\n<h3>झटपट सुरुवात</h3>\n<ol>\n  <li><b>एक भाग निवडा.</b> सध्याची नकाशा व्याप्ती वापरा, नकाशावर\n      आयत काढा, किंवा निवडलेल्या वैशिष्ट्यांची किंवा स्तराची\n      व्याप्ती वापरा.</li>\n  <li><b>आवश्यक OSM श्रेणी निवडा</b> (POI, थांबे, रस्ते,\n      इमारती, सीमा, भूवापर, ...).</li>\n  <li><b>आउटपुट स्वरूप आणि फोल्डर निवडा</b>, नंतर\n      <b>OSM डेटा डाउनलोड करा</b> वर क्लिक करा.</li>\n</ol>\n\n<h3>हे जाणून घ्या</h3>\n<ul>\n  <li><b>GeoPackage शिफारस केले जाते.</b> Shapefile मध्ये खूप जास्त\n      गुणधर्म स्तंभ ठेवता येत नाहीत, म्हणून मोठ्या भागांमध्ये काही\n      क्वचित वापरले जाणारे टॅग स्तंभ वगळले जाऊ शकतात (असे झाल्यास लॉग सांगतो).</li>\n  <li><b>भाग मर्यादित ठेवा.</b> खूप मोठे भाग प्रचंड Overpass\n      प्रतिसाद तयार करतात आणि ते हळू होऊ शकतात किंवा सार्वजनिक सर्व्हरद्वारे नाकारले जाऊ शकतात.</li>\n  <li><b>कॅशे</b> मुळे त्याच क्वेरीचे पुन्हा डाउनलोड\n      आधीचे निकाल पुन्हा वापरू शकतात.</li>\n  <li>लॉगमधील <b>"अवर्गीकृत OSM घटक"</b> ही माहितीपर आहे: ते\n      बहुतेक रेषा आणि बहुभुजांचे टॅग नसलेले शिरोबिंदू असतात जे कोणत्याही\n      निवडलेल्या श्रेणीत नसतात.</li>\n</ul>\n\n<p>डेटा &copy; OpenStreetMap योगदानकर्ते, <a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a> अंतर्गत उपलब्ध.</p>\n<p><i>हा प्लगइन OpenStreetMap Foundation कडून समर्थित किंवा संलग्न नाही.</i></p>\n',
 ' responded successfully.': ' ने यशस्वीरित्या प्रतिसाद दिला.',
 ' seconds...': ' सेकंद…',
 '" style="color:#0B5E8E; text-decoration:none;">OpenStreetMap contributors</a> (ODbL)':
   '" style="color:#0B5E8E; text-decoration:none;">OpenStreetMap योगदानकर्ते</a> (ODbL)',
 ', east=': ', पूर्व=',
 ', north=': ', उत्तर=',
 ', west=': ', पश्चिम=',
 '0 selected': '0 निवडले',
 '<p>Plugin version': '<p>प्लगइन आवृत्ती',
 'A download is already running.': 'डाउनलोड आधीच सुरू आहे.',
 'A labelled column of feature checkboxes.': 'वैशिष्ट्य चेकबॉक्सचा लेबल असलेला स्तंभ.',
 'AOI drawing cancelled.': 'AOI रेखाटन रद्द केले.',
 'AOI geometry is empty.': 'AOI भूमिती रिकामी आहे.',
 'AOI geometry is missing.': 'AOI भूमिती गहाळ आहे.',
 'AOI name': 'AOI नाव',
 'AOI rectangle captured successfully.': 'AOI आयत यशस्वीरित्या कॅप्चर केला.',
 'AOI source CRS is invalid.': 'AOI स्रोत CRS अवैध आहे.',
 'AOI validation failed:': 'AOI प्रमाणीकरण अयशस्वी:',
 'AOI:': 'AOI:',
 'AOI: QGIS interface is not available.': 'AOI: QGIS इंटरफेस उपलब्ध नाही.',
 "AOI: click 'Draw AOI', then drag a rectangle on the QGIS map.":
   'AOI: "AOI काढा" वर क्लिक करा, नंतर QGIS नकाशावर आयत ओढा.',
 "AOI: click 'Use Layer Extent' to use the full extent of the active QGIS layer.":
   'AOI: सक्रिय QGIS स्तराची संपूर्ण व्याप्ती वापरण्यासाठी "स्तर व्याप्ती वापरा" वर क्लिक करा.',
 'AOI: click and drag on the QGIS map.': 'AOI: QGIS नकाशावर क्लिक करा आणि ओढा.',
 'AOI: failed to resolve active layer extent': 'AOI: सक्रिय स्तर व्याप्ती निश्चित करता आली नाही',
 'AOI: failed to resolve selected features': 'AOI: निवडलेली वैशिष्ट्ये निश्चित करता आली नाहीत',
 'AOI: invalid': 'AOI: अवैध',
 'AOI: no active QGIS layer.': 'AOI: कोणताही सक्रिय QGIS स्तर नाही.',
 'AOI: no feature(s) selected in the active layer.': 'AOI: सक्रिय स्तरात कोणतेही वैशिष्ट्य निवडलेले नाही.',
 'AOI: not yet resolved': 'AOI: अद्याप निश्चित केलेले नाही',
 "AOI: select feature(s) in the active QGIS layer, then click 'Use Selected Features'.":
   'AOI: सक्रिय QGIS स्तरात वैशिष्ट्ये निवडा, नंतर "निवडलेली वैशिष्ट्ये वापरा" वर क्लिक करा.',
 'AOI: the active layer is not a vector layer.': 'AOI: सक्रिय स्तर वेक्टर स्तर नाही.',
 'AOI: unable to create': 'AOI: तयार करता आले नाही',
 'AOI: unable to resolve': 'AOI: निश्चित करता आले नाही',
 'Activate the interactive rectangle AOI map tool.': 'परस्परसंवादी आयत AOI नकाशा साधन सक्रिय करा.',
 'Active layer extent': 'सक्रिय स्तर व्याप्ती',
 'Active-layer extent AOI is invalid.': 'सक्रिय-स्तर व्याप्ती AOI अवैध आहे.',
 'Active-layer extent captured successfully.': 'सक्रिय-स्तर व्याप्ती यशस्वीरित्या कॅप्चर केली.',
 'Active-layer extent validation failed:': 'सक्रिय-स्तर व्याप्ती प्रमाणीकरण अयशस्वी:',
 'Administrative boundaries': 'प्रशासकीय सीमा',
 'Administrative boundary filter: all levels (no admin_level filter).':
   'प्रशासकीय सीमा फिल्टर: सर्व स्तर (admin_level फिल्टर नाही).',
 'Administrative boundary levels': 'प्रशासकीय सीमा स्तर',
 'Administrative boundary levels:': 'प्रशासकीय सीमा स्तर:',
 'Administrative levels must be an integer, a numeric string, a sequence of levels, or None.':
   'प्रशासकीय स्तर पूर्णांक, संख्यात्मक स्ट्रिंग, स्तरांचा क्रम किंवा None असणे आवश्यक आहे.',
 'All OSM feature categories cleared.': 'सर्व OSM वैशिष्ट्य श्रेणी साफ केल्या.',
 'All OSM feature categories selected.': 'सर्व OSM वैशिष्ट्य श्रेणी निवडल्या.',
 'All Overpass server URLs must be non-empty strings.':
   'सर्व Overpass सर्व्हर URL रिकाम्या नसलेल्या स्ट्रिंग असणे आवश्यक आहे.',
 'All Overpass servers and retry attempts failed.':
   'सर्व Overpass सर्व्हर आणि पुन्हा प्रयत्न अयशस्वी झाले.',
 'All administrative levels will be included.': 'सर्व प्रशासकीय स्तर समाविष्ट केले जातील.',
 'All administrative levels will be included; no admin_level filter will be added to the query.':
   'सर्व प्रशासकीय स्तर समाविष्ट केले जातील; क्वेरीमध्ये admin_level फिल्टर जोडला जाणार नाही.',
 'All attempts failed for server ': 'सर्व्हरसाठी सर्व प्रयत्न अयशस्वी: ',
 'All levels (0–15; no admin_level filter)': 'सर्व स्तर (0–15; admin_level फिल्टर नाही)',
 'An existing output directory is required for Shapefile export.':
   'Shapefile निर्यातीसाठी विद्यमान आउटपुट फोल्डर आवश्यक आहे.',
 'An output GeoPackage path is required.': 'आउटपुट GeoPackage पथ आवश्यक आहे.',
 'An output name is required for Shapefile export.':
   'Shapefile निर्यातीसाठी आउटपुट नाव आवश्यक आहे.',
 'Append a timestamped message to the processing log.':
   'प्रक्रिया लॉगमध्ये वेळेसह संदेश जोडा.',
 'Append an exported feature count to the processing log.':
   'प्रक्रिया लॉगमध्ये निर्यात केलेल्या वैशिष्ट्यांची संख्या जोडा.',
 'Area of Interest': 'स्वारस्याचा भाग',
 'At least one OSM feature must be selected.': 'किमान एक OSM वैशिष्ट्य निवडणे आवश्यक आहे.',
 'At least one OSM feature must be supplied.': 'किमान एक OSM वैशिष्ट्य पुरवणे आवश्यक आहे.',
 'At least one Overpass server must be provided.': 'किमान एक Overpass सर्व्हर प्रदान करणे आवश्यक आहे.',
 'Attempt details:': 'प्रयत्न तपशील:',
 'Automatically add downloaded layers to QGIS': 'डाउनलोड केलेले स्तर आपोआप QGIS मध्ये जोडा',
 'Background Overpass download started.': 'पार्श्वभूमी Overpass डाउनलोड सुरू झाले.',
 'Browse': 'ब्राउझ करा',
 'Browse…': 'ब्राउझ करा…',
 'Buildings': 'इमारती',
 'Bus stops': 'बस थांबे',
 'CRS:': 'CRS:',
 'Cache hit:': 'कॅशे हिट:',
 'Cache hit: using saved Overpass response ({age} day(s) old).':
   'कॅशे हिट: जतन केलेला Overpass प्रतिसाद वापरत आहे ({age} दिवस जुना).',
 'Cache miss:': 'कॅशे मिस:',
 'Cache miss: could not read saved response ({error}).':
   'कॅशे मिस: जतन केलेला प्रतिसाद वाचता आला नाही ({error}).',
 'Cache miss: query hash does not match the saved response.':
   'कॅशे मिस: क्वेरी हॅश जतन केलेल्या प्रतिसादाशी जुळत नाही.',
 'Cache miss: saved response is incomplete or invalid.':
   'कॅशे मिस: जतन केलेला प्रतिसाद अपूर्ण किंवा अवैध आहे.',
 'Cache miss: saved response is older than {days} days.':
   'कॅशे मिस: जतन केलेला प्रतिसाद {days} दिवसांपेक्षा जुना आहे.',
 'Cache miss: saved response uses an unsupported cache format.':
   'कॅशे मिस: जतन केलेला प्रतिसाद असमर्थित कॅशे स्वरूप वापरतो.',
 'Cached Overpass response:': 'कॅशे केलेला Overpass प्रतिसाद:',
 'Cancel': 'रद्द करा',
 'Cancellation has already been requested.': 'रद्द करण्याची विनंती आधीच केली आहे.',
 'Cancellation requested': 'रद्द करण्याची विनंती केली',
 'Cancellation requested. If an HTTP request is already active, the downloader will stop when that request returns or times out.':
   'रद्द करण्याची विनंती केली. HTTP विनंती आधीच सक्रिय असल्यास, ती विनंती परत आल्यावर किंवा कालबाह्य झाल्यावर डाउनलोडर थांबेल.',
 'Cancellation requested; waiting for the current request to finish...':
   'रद्द करण्याची विनंती केली; सध्याची विनंती पूर्ण होण्याची प्रतीक्षा…',
 'Cannot draw AOI because the QGIS interface is unavailable.':
   'QGIS इंटरफेस उपलब्ध नसल्यामुळे AOI काढता येत नाही.',
 'Cannot resolve active-layer extent because QGIS is unavailable.':
   'QGIS उपलब्ध नसल्यामुळे सक्रिय-स्तर व्याप्ती निश्चित करता येत नाही.',
 'Cannot resolve current map extent because QGIS is unavailable.':
   'QGIS उपलब्ध नसल्यामुळे सध्याची नकाशा व्याप्ती निश्चित करता येत नाही.',
 'Cannot resolve selected-feature AOI because QGIS is unavailable.':
   'QGIS उपलब्ध नसल्यामुळे निवडलेल्या-वैशिष्ट्य AOI निश्चित करता येत नाही.',
 'Cannot transform an empty geometry.': 'रिकामी भूमिती रूपांतरित करता येत नाही.',
 'Capture the current QGIS map canvas extent.': 'सध्याची QGIS नकाशा कॅनव्हास व्याप्ती कॅप्चर करा.',
 'Choose all available levels, or select one or more levels to download (for example, 5–8 or level 5).':
   'सर्व उपलब्ध स्तर निवडा, किंवा डाउनलोड करण्यासाठी एक किंवा अधिक स्तर निवडा (उदा. 5–8 किंवा स्तर 5).',
 'Choose an output directory before downloading.':
   'डाउनलोड करण्यापूर्वी आउटपुट फोल्डर निवडा.',
 'City name': 'शहराचे नाव',
 'Classifying OSM elements and preparing GeoPackage layers.':
   'OSM घटकांचे वर्गीकरण आणि GeoPackage स्तर तयार करत आहे.',
 'Classifying OSM elements and preparing Shapefile outputs.':
   'OSM घटकांचे वर्गीकरण आणि Shapefile आउटपुट तयार करत आहे.',
 'Clear all': 'सर्व साफ करा',
 'Clear log': 'लॉग साफ करा',
 'Clear only the visible log, without changing processing settings.':
   'प्रक्रिया सेटिंग्ज न बदलता फक्त दृश्यमान लॉग साफ करा.',
 'Clear selected levels so the user can make a narrower selection.':
   'वापरकर्त्याला अधिक अरुंद निवड करता यावी म्हणून निवडलेले स्तर साफ करा.',
 'Clear the messages currently shown in the Processing Log.':
   'प्रक्रिया लॉगमध्ये सध्या दर्शविलेले संदेश साफ करा.',
 'Clear the previous AOI and display guidance for the chosen method.':
   'मागील AOI साफ करा आणि निवडलेल्या पद्धतीसाठी मार्गदर्शन दाखवा.',
 'Close': 'बंद करा',
 'Collect optional filename components before exporting OSM data.':
   'OSM डेटा निर्यात करण्यापूर्वी पर्यायी फाइलनाव घटक गोळा करा.',
 'Compact product header above the scrollable workflow.':
   'स्क्रोल करण्यायोग्य कार्यप्रवाहाच्या वर संक्षिप्त उत्पादन हेडर.',
 'Connection error on server ': 'सर्व्हरवर कनेक्शन त्रुटी: ',
 'Continue to Download': 'डाउनलोडकडे सुरू ठेवा',
 'Convert a name component into a Windows-safe filename token.':
   'नाव घटक Windows-सुरक्षित फाइलनाव टोकनमध्ये रूपांतरित करा.',
 'Convert the drawn rectangle into the standard AOI object.':
   'काढलेला आयत मानक AOI ऑब्जेक्टमध्ये रूपांतरित करा.',
 'Converting OSM response to GeoPackage...': 'OSM प्रतिसाद GeoPackage मध्ये रूपांतरित करत आहे…',
 'Converting OSM response to Shapefiles...': 'OSM प्रतिसाद Shapefile मध्ये रूपांतरित करत आहे…',
 'Could not combine the selected feature geometries.':
   'निवडलेल्या वैशिष्ट्य भूमिती एकत्र करता आल्या नाहीत.',
 "Could not create Shapefile staging layer '{layer_name}'.":
   'Shapefile स्टेजिंग स्तर «{layer_name}» तयार करता आला नाही.',
 'Could not create an empty bus_stops_points layer.':
   'रिकामा bus_stops_points स्तर तयार करता आला नाही.',
 "Could not create temporary QGIS layer '{layer_name}'.":
   'तात्पुरता QGIS स्तर «{layer_name}» तयार करता आला नाही.',
 'Could not create temporary layer for admin_level {admin_level}.':
   'admin_level {admin_level} साठी तात्पुरता स्तर तयार करता आला नाही.',
 'Could not create the merged bus_stops_points layer.':
   'विलीन केलेला bus_stops_points स्तर तयार करता आला नाही.',
 'Could not delete temporary file': 'तात्पुरती फाइल हटवता आली नाही',
 "Could not load feature definition '{feature_key}': {error}":
   'वैशिष्ट्य व्याख्या «{feature_key}» लोड करता आली नाही: {error}',
 'Could not merge bus-station centroids into bus-stop points.':
   'बस-स्थानक केंद्रबिंदू बस-थांबा बिंदूंमध्ये विलीन करता आले नाहीत.',
 'Could not overwrite existing output file: {error}':
   'विद्यमान आउटपुट फाइल अधिलिखित करता आली नाही: {error}',
 'Could not populate Shapefile for admin_level {admin_level}.':
   'admin_level {admin_level} साठी Shapefile भरता आला नाही.',
 "Could not populate temporary layer '{layer_name}'.":
   'तात्पुरता स्तर «{layer_name}» भरता आला नाही.',
 'Could not prepare the Overpass query:': 'Overpass क्वेरी तयार करता आली नाही:',
 "Could not reopen intermediate GeoPackage layer '{layer_name}'.":
   'मध्यस्थ GeoPackage स्तर «{layer_name}» पुन्हा उघडता आला नाही.',
 'Could not restore previous QGIS map tool:': 'मागील QGIS नकाशा साधन पुनर्संचयित करता आले नाही:',
 'Could not search for temporary GeoPackages:': 'तात्पुरते GeoPackage शोधता आले नाहीत:',
 'Country name': 'देशाचे नाव',
 'Create one section panel and return it with its body layout.':
   'एक विभाग पॅनेल तयार करा आणि त्याच्या मुख्य भाग लेआउटसह परत करा.',
 'Created bus_stops_points from bus-station polygon centroids.':
   'बस-स्थानक बहुभुज केंद्रबिंदूंपासून bus_stops_points तयार केला.',
 'Current QGIS map extent': 'सध्याची QGIS नकाशा व्याप्ती',
 'Current QGIS map extent resolved.': 'सध्याची QGIS नकाशा व्याप्ती निश्चित केली.',
 'Data © <a href="': 'डेटा © <a href="',
 'Deleted temporary workspace file:': 'तात्पुरती कार्यक्षेत्र फाइल हटवली:',
 'Details:': 'तपशील:',
 'Download': 'डाउनलोड',
 'Download OSM Data': 'OSM डेटा डाउनलोड करा',
 'Download OpenStreetMap data for any area and load it straight into QGIS.':
   'कोणत्याही भागासाठी OpenStreetMap डेटा डाउनलोड करा आणि थेट QGIS मध्ये लोड करा.',
 'Download cancelled because existing output files were not approved for overwrite.':
   'विद्यमान आउटपुट फाइलींना अधिलिखित करण्यास मान्यता न दिल्यामुळे डाउनलोड रद्द केले.',
 'Download cancelled before it started.': 'सुरू होण्यापूर्वी डाउनलोड रद्द केले.',
 'Download cancelled before results were returned.': 'निकाल परत येण्यापूर्वी डाउनलोड रद्द केले.',
 'Download cancelled before starting.': 'सुरू करण्यापूर्वी डाउनलोड रद्द केले.',
 'Download cancelled in the output-naming dialog.':
   'आउटपुट-नामकरण संवादात डाउनलोड रद्द केले.',
 'Download cancelled.': 'डाउनलोड रद्द केले.',
 'Download cancelled; existing files preserved.': 'डाउनलोड रद्द केले; विद्यमान फाइली जपल्या.',
 'Download stopped.': 'डाउनलोड थांबवले.',
 'Download succeeded, but export failed.': 'डाउनलोड यशस्वी, पण निर्यात अयशस्वी.',
 'Downloading OSM data from Overpass...': 'Overpass वरून OSM डेटा डाउनलोड करत आहे…',
 'Draw AOI': 'AOI काढा',
 'Draw a rectangle on the QGIS map to define the AOI.':
   'AOI परिभाषित करण्यासाठी QGIS नकाशावर आयत काढा.',
 'Draw rectangle on map': 'नकाशावर आयत काढा',
 'Draw the AOI rectangle on the QGIS map.': 'QGIS नकाशावर AOI आयत काढा.',
 'Drawn AOI validation failed:': 'काढलेल्या AOI प्रमाणीकरण अयशस्वी:',
 'Drawn rectangle': 'काढलेला आयत',
 'Drawn rectangle AOI captured successfully.': 'काढलेला आयत AOI यशस्वीरित्या कॅप्चर केला.',
 'ERROR:': 'त्रुटी:',
 'East:': 'पूर्व:',
 'Enable level checkboxes only when a specific selection is active.':
   'विशिष्ट निवड सक्रिय असतानाच स्तर चेकबॉक्स सक्षम करा.',
 'Enable only the AOI action button for the selected method.':
   'निवडलेल्या पद्धतीसाठी फक्त AOI क्रिया बटण सक्षम करा.',
 'Enable or disable controls while a download is running.':
   'डाउनलोड सुरू असताना नियंत्रणे सक्षम किंवा अक्षम करा.',
 'Enter at least one name (City, Country, Region, or AOI).':
   'किमान एक नाव प्रविष्ट करा (शहर, देश, प्रदेश किंवा AOI).',
 'Enter one or more name components. Blank fields will be skipped, and the remaining names will be joined with underscores. The selected output format will be retained.':
   'एक किंवा अधिक नाव घटक प्रविष्ट करा. रिकामी फील्ड वगळली जातील आणि उर्वरित नावे अंडरस्कोअरने जोडली जातील. निवडलेले आउटपुट स्वरूप टिकवले जाईल.',
 'Enter_a_name_to_preview': 'पूर्वावलोकनासाठी_नाव_प्रविष्ट_करा',
 'Export cancelled: output name is missing.': 'निर्यात रद्द: आउटपुट नाव गहाळ आहे.',
 'Export complete:': 'निर्यात पूर्ण:',
 'Export the downloaded response and optionally load its layers.':
   'डाउनलोड केलेला प्रतिसाद निर्यात करा आणि इच्छित असल्यास त्याचे स्तर लोड करा.',
 'Failed to activate rectangle AOI tool:': 'आयत AOI साधन सक्रिय करण्यात अयशस्वी:',
 'Failed to create AOI.': 'AOI तयार करण्यात अयशस्वी.',
 'Failed to process drawn rectangle AOI:': 'काढलेला आयत AOI प्रक्रिया करण्यात अयशस्वी:',
 'Failed to resolve active-layer extent.': 'सक्रिय-स्तर व्याप्ती निश्चित करण्यात अयशस्वी.',
 'Failed to resolve active-layer extent:': 'सक्रिय-स्तर व्याप्ती निश्चित करण्यात अयशस्वी:',
 'Failed to resolve current QGIS map extent:':
   'सध्याची QGIS नकाशा व्याप्ती निश्चित करण्यात अयशस्वी:',
 'Failed to resolve selected-feature AOI.':
   'निवडलेल्या-वैशिष्ट्य AOI निश्चित करण्यात अयशस्वी.',
 'Failed to resolve selected-feature AOI:':
   'निवडलेल्या-वैशिष्ट्य AOI निश्चित करण्यात अयशस्वी:',
 "Failed to write layer '{layer_name}' to '{output_path}': {error}":
   'स्तर «{layer_name}» «{output_path}» मध्ये लिहिण्यात अयशस्वी: {error}',
 "Feature '{feature_key}' has no tag definitions.":
   'वैशिष्ट्य «{feature_key}» मध्ये टॅग व्याख्या नाहीत.',
 'Feature specification  does not expose a tag-filter mapping.':
   'वैशिष्ट्य स्पेसिफिकेशन टॅग-फिल्टर मॅपिंग देत नाही.',
 'Ferry stops': 'फेरी थांबे',
 'Filename preview': 'फाइलनाव पूर्वावलोकन',
 'Full documentation': 'संपूर्ण दस्तऐवजीकरण',
 'Generated Overpass query (': 'व्युत्पन्न Overpass क्वेरी (',
 'GeoPackage': 'GeoPackage',
 'GeoPackage layer(s) to QGIS.': 'GeoPackage स्तर QGIS मध्ये.',
 'GeoPackage saved:': 'GeoPackage जतन केले:',
 'HTTP error on server ': 'सर्व्हरवर HTTP त्रुटी: ',
 'HTTP error — ': 'HTTP त्रुटी — ',
 'HTTP {status} error on server {index}/{total}.':
   'सर्व्हर {index}/{total} वर HTTP {status} त्रुटी.',
 'Handle a drawing tool deactivation initiated outside this dialog.':
   'या संवादाबाहेर सुरू झालेले रेखाटन साधन निष्क्रिय करणे हाताळा.',
 'Help': 'मदत',
 'Invalid east longitude: {value}': 'अवैध पूर्व रेखांश: {value}',
 'Invalid north latitude: {value}': 'अवैध उत्तर अक्षांश: {value}',
 'Invalid response from server ': 'सर्व्हरकडून अवैध प्रतिसाद: ',
 'Invalid south latitude: {value}': 'अवैध दक्षिण अक्षांश: {value}',
 'Invalid west longitude: {value}': 'अवैध पश्चिम रेखांश: {value}',
 'Keep the numeric readout in step with the progress bar.':
   'संख्यात्मक रीडआउट प्रगती पट्टीशी सुसंगत ठेवा.',
 'Land & built environment': 'जमीन आणि बांधलेले वातावरण',
 'Landuse': 'भूवापर',
 'Language:': 'भाषा:',
 'Linear features': 'रेषीय वैशिष्ट्ये',
 'Load the saved interface language and translate visible UI strings.':
   'जतन केलेली इंटरफेस भाषा लोड करा आणि दृश्यमान UI स्ट्रिंग भाषांतरित करा.',
 'Local response cache is disabled.': 'स्थानिक प्रतिसाद कॅशे अक्षम आहे.',
 'Main OSM Data Toolkit window.': 'मुख्य OSM Data Toolkit विंडो.',
 'Manually capture the map extent after the user pans or zooms.':
   'वापरकर्त्याने पॅन किंवा झूम केल्यानंतर नकाशा व्याप्ती स्वहस्ते कॅप्चर करा.',
 'Merged bus-station polygon centroids into bus_stops_points.':
   'बस-स्थानक बहुभुज केंद्रबिंदू bus_stops_points मध्ये विलीन केले.',
 'No Overpass selectors were generated.': 'कोणतेही Overpass निवडक तयार केले नाहीत.',
 'No active QGIS layer is available.': 'कोणताही सक्रिय QGIS स्तर उपलब्ध नाही.',
 'No active layer is available.': 'कोणताही सक्रिय स्तर उपलब्ध नाही.',
 'No exportable features matched the selected categories. Try another AOI or select additional OSM feature categories.':
   'निवडलेल्या श्रेणींशी जुळणारी कोणतीही निर्यातयोग्य वैशिष्ट्ये नाहीत. दुसरा AOI वापरून पहा किंवा अधिक OSM वैशिष्ट्य श्रेणी निवडा.',
 'No features are selected in the active layer.': 'सक्रिय स्तरात कोणतीही वैशिष्ट्ये निवडलेली नाहीत.',
 'No levels selected. Select at least one level to continue.':
   'कोणतेही स्तर निवडलेले नाहीत. सुरू ठेवण्यासाठी किमान एक स्तर निवडा.',
 'No selected features found.': 'कोणतीही निवडलेली वैशिष्ट्ये आढळली नाहीत.',
 'No valid Area of Interest is available. Select an AOI method and resolve the AOI before downloading.':
   'कोणताही वैध स्वारस्याचा भाग उपलब्ध नाही. डाउनलोड करण्यापूर्वी AOI पद्धत निवडा आणि AOI निश्चित करा.',
 'North:': 'उत्तर:',
 'Note: {layer_name} has too many tag columns for one Shapefile (DBF size limit); {count} rarely-used columns were left out.':
   'टीप: {layer_name} मध्ये एका Shapefile साठी खूप जास्त टॅग स्तंभ आहेत (DBF आकार मर्यादा); {count} क्वचित वापरले जाणारे स्तंभ वगळले.',
 'OSM Data Toolkit': 'OSM Data Toolkit',
 'OSM Data Toolkit initialised.': 'OSM Data Toolkit सुरू केले.',
 'OSM Feature Categories': 'OSM वैशिष्ट्य श्रेणी',
 'OSM export completed successfully.': 'OSM निर्यात यशस्वीरित्या पूर्ण झाली.',
 'One or more output files with this name already exist. Do you want to overwrite the matching output files?':
   'या नावाच्या एक किंवा अधिक आउटपुट फाइली आधीच अस्तित्वात आहेत. जुळणाऱ्या आउटपुट फाइलींना अधिलिखित करायचे?',
 'Only the selected levels': 'फक्त निवडलेले स्तर',
 'Only validated Overpass responses can be cached.':
   'फक्त प्रमाणित Overpass प्रतिसाद कॅशे करता येतात.',
 'Open public spaces': 'खुली सार्वजनिक जागा',
 'Open the in-plugin help with links to the online documentation.':
   'ऑनलाइन दस्तऐवजीकरणाच्या दुव्यांसह प्लगइन-अंतर्गत मदत उघडा.',
 'Output Settings': 'आउटपुट सेटिंग्ज',
 'Output directory': 'आउटपुट फोल्डर',
 'Output directory selected:': 'आउटपुट फोल्डर निवडले:',
 'Output format': 'आउटपुट स्वरूप',
 'Output settings': 'आउटपुट सेटिंग्ज',
 'Overpass download cancelled.': 'Overpass डाउनलोड रद्द केले.',
 'Overpass download completed:': 'Overpass डाउनलोड पूर्ण:',
 'Overpass download failed.': 'Overpass डाउनलोड अयशस्वी.',
 'Overpass download failed:': 'Overpass डाउनलोड अयशस्वी:',
 'Overpass download running...': 'Overpass डाउनलोड सुरू आहे…',
 'Overpass download was cancelled by the caller.': 'कॉलरने Overpass डाउनलोड रद्द केले.',
 'Overpass query must be a non-empty string.': 'Overpass क्वेरी रिकामी नसलेली स्ट्रिंग असणे आवश्यक आहे.',
 "Overpass response 'elements' field is not a list.":
   'Overpass प्रतिसादातील «elements» फील्ड सूची नाही.',
 "Overpass response does not contain an 'elements' field.":
   'Overpass प्रतिसादात «elements» फील्ड नाही.',
 'Overpass response is not a JSON object.': 'Overpass प्रतिसाद JSON ऑब्जेक्ट नाही.',
 'Overpass response received successfully:': 'Overpass प्रतिसाद यशस्वीरित्या प्राप्त:',
 'Overpass server ': 'Overpass सर्व्हर ',
 'Overpass server returned invalid JSON. Response preview: ':
   'Overpass सर्व्हरने अवैध JSON दिले. प्रतिसाद पूर्वावलोकन: ',
 'Overpass servers available:': 'उपलब्ध Overpass सर्व्हर:',
 'Overpass timeout must be greater than zero.': 'Overpass कालबाह्यता शून्यापेक्षा जास्त असणे आवश्यक आहे.',
 'Plugin version': 'प्लगइन आवृत्ती',
 'Points of interest (POI)': 'आस्थेची ठिकाणे (POI)',
 'Prepared {index:,} of {total:,} OSM elements for export...':
   'निर्यातीसाठी {total:,} पैकी {index:,} OSM घटक तयार…',
 'Preparing Overpass download...': 'Overpass डाउनलोड तयार करत आहे…',
 'Preparing Overpass query.': 'Overpass क्वेरी तयार करत आहे.',
 'Processing Options': 'प्रक्रिया पर्याय',
 'Processing log': 'प्रक्रिया लॉग',
 'Processing messages will appear here...': 'प्रक्रिया संदेश येथे दिसतील…',
 'Processing options': 'प्रक्रिया पर्याय',
 'Public transport & places': 'सार्वजनिक वाहतूक आणि ठिकाणे',
 'QGIS interface object was not detected. Canvas-dependent AOI tools are disabled.':
   'QGIS इंटरफेस ऑब्जेक्ट आढळला नाही. कॅनव्हास-अवलंबून AOI साधने अक्षम आहेत.',
 'QGIS map canvas could not be accessed.': 'QGIS नकाशा कॅनव्हासमध्ये प्रवेश करता आला नाही.',
 'QGIS map canvas is unavailable.': 'QGIS नकाशा कॅनव्हास उपलब्ध नाही.',
 'Rail stops': 'रेल्वे थांबे',
 'Railways': 'रेल्वे',
 'Read the plugin version from metadata.txt (empty string if absent).':
   'metadata.txt मधून प्लगइन आवृत्ती वाचा (नसल्यास रिकामी स्ट्रिंग).',
 'Read, validate and store the current QGIS map canvas extent.':
   'सध्याची QGIS नकाशा कॅनव्हास व्याप्ती वाचा, प्रमाणित करा आणि संग्रहित करा.',
 'Ready.': 'तयार.',
 'Rectangle AOI drawing tool activated.': 'आयत AOI रेखाटन साधन सक्रिय केले.',
 'Rectangle AOI drawing was cancelled.': 'आयत AOI रेखाटन रद्द केले.',
 'Region name': 'प्रदेशाचे नाव',
 'Report an issue': 'समस्या नोंदवा',
 'Request cooperative cancellation of the background worker.':
   'पार्श्वभूमी कार्यकर्त्याच्या सहकारी रद्दीकरणाची विनंती करा.',
 'Request error on server ': 'सर्व्हरवर विनंती त्रुटी: ',
 'Restore default GUI settings when the dialog closes.':
   'संवाद बंद झाल्यावर डीफॉल्ट GUI सेटिंग्ज पुनर्संचयित करा.',
 'Restore the GUI once the background thread has stopped.':
   'पार्श्वभूमी थ्रेड थांबल्यावर GUI पुनर्संचयित करा.',
 'Restore the QGIS map tool active before rectangle drawing.':
   'आयत रेखाटनापूर्वी सक्रिय असलेले QGIS नकाशा साधन पुनर्संचयित करा.',
 'Restore the map tool and reset state before hiding the dialog.':
   'संवाद लपवण्यापूर्वी नकाशा साधन पुनर्संचयित करा आणि स्थिती रीसेट करा.',
 'Retrying in ': 'पुन्हा प्रयत्न ',
 'Return selected levels, or None when all levels are requested.':
   'निवडलेले स्तर परत करा, किंवा सर्व स्तरांची विनंती केल्यास None.',
 'Return the combined, sanitized filename prefix.':
   'एकत्रित, स्वच्छ केलेला फाइलनाव उपसर्ग परत करा.',
 'Return the mapping between feature keys and GUI checkboxes.':
   'वैशिष्ट्य की आणि GUI चेकबॉक्समधील मॅपिंग परत करा.',
 'Return the selected GUI feature keys.': 'निवडलेल्या GUI वैशिष्ट्य की परत करा.',
 'Roads': 'रस्ते',
 'Run a modal dialog on both Qt5 and Qt6.':
   'Qt5 आणि Qt6 दोन्हीवर मोडल संवाद चालवा.',
 'Select Output Directory': 'आउटपुट फोल्डर निवडा',
 'Select a vector layer with selected features.':
   'निवडलेल्या वैशिष्ट्यांसह वेक्टर स्तर निवडा.',
 'Select all': 'सर्व निवडा',
 'Select an active QGIS layer.': 'सक्रिय QGIS स्तर निवडा.',
 'Select at least one OSM feature category before downloading.':
   'डाउनलोड करण्यापूर्वी किमान एक OSM वैशिष्ट्य श्रेणी निवडा.',
 'Select at least one administrative level, or choose All levels.':
   'किमान एक प्रशासकीय स्तर निवडा किंवा "सर्व स्तर" निवडा.',
 'Select at least one administrative level, or use None to retrieve all levels.':
   'किमान एक प्रशासकीय स्तर निवडा किंवा सर्व स्तर मिळवण्यासाठी None वापरा.',
 'Select levels 0–15 and switch to specific-level mode.':
   'स्तर 0–15 निवडा आणि विशिष्ट-स्तर मोडवर जा.',
 'Select one or more features in the active layer.':
   'सक्रिय स्तरात एक किंवा अधिक वैशिष्ट्ये निवडा.',
 'Select output directory...': 'आउटपुट फोल्डर निवडा…',
 'Selected administrative levels:': 'निवडलेले प्रशासकीय स्तर:',
 'Selected feature IDs:': 'निवडलेल्या वैशिष्ट्यांचे ID:',
 'Selected feature(s) in active layer': 'सक्रिय स्तरातील निवडलेले वैशिष्ट्य(े)',
 'Selected features (': 'निवडलेली वैशिष्ट्ये (',
 'Selected-feature AOI captured successfully (':
   'निवडलेल्या-वैशिष्ट्य AOI यशस्वीरित्या कॅप्चर केला (',
 'Selected-feature AOI captured successfully.':
   'निवडलेल्या-वैशिष्ट्य AOI यशस्वीरित्या कॅप्चर केला.',
 'Selected-feature AOI is invalid.': 'निवडलेल्या-वैशिष्ट्य AOI अवैध आहे.',
 'Selected-feature AOI requires a vector layer.':
   'निवडलेल्या-वैशिष्ट्य AOI साठी वेक्टर स्तर आवश्यक आहे.',
 'Selected-feature AOI validation failed:':
   'निवडलेल्या-वैशिष्ट्य AOI प्रमाणीकरण अयशस्वी:',
 'Sending query to Overpass...': 'Overpass ला क्वेरी पाठवत आहे…',
 'Server ': 'सर्व्हर ',
 'Shapefile': 'Shapefile',
 'Shapefile export completed in:': 'Shapefile निर्यात पूर्ण झाली:',
 'Shapefile field names shortened for': 'साठी Shapefile फील्ड नावे लहान केली',
 'Shapefile layer(s) to QGIS.': 'Shapefile स्तर QGIS मध्ये.',
 'Short in-plugin help with links to the full online documentation.':
   'संपूर्ण ऑनलाइन दस्तऐवजीकरणाच्या दुव्यांसह संक्षिप्त प्लगइन-अंतर्गत मदत.',
 'Show AOI coordinates and source CRS in the dialog.':
   'संवादात AOI निर्देशांक आणि स्रोत CRS दाखवा.',
 'Show a concise description of the active administrative filter.':
   'सक्रिय प्रशासकीय फिल्टरचे संक्षिप्त वर्णन दाखवा.',
 'Source CRS is invalid.': 'स्रोत CRS अवैध आहे.',
 'South latitude cannot be greater than north latitude.':
   'दक्षिण अक्षांश उत्तर अक्षांशापेक्षा जास्त असू शकत नाही.',
 'South:': 'दक्षिण:',
 'Starting Overpass download...': 'Overpass डाउनलोड सुरू करत आहे…',
 'Supporting copy: muted, wrapped and visually quiet.':
   'सहाय्यक मजकूर: सौम्य, गुंडाळलेला आणि दृष्यदृष्ट्या शांत.',
 "Tag '{tag}' contains an empty value list.":
   'टॅग «{tag}» मध्ये रिकामी मूल्य सूची आहे.',
 'Temporary workspace cleanup complete:': 'तात्पुरते कार्यक्षेत्र साफसफाई पूर्ण:',
 'Temporary workspace cleanup complete: no matching files found.':
   'तात्पुरते कार्यक्षेत्र साफसफाई पूर्ण: जुळणाऱ्या फाइली आढळल्या नाहीत.',
 'Temporary-file cleanup skipped: workspace directory is invalid.':
   'तात्पुरते-फाइल साफसफाई वगळली: कार्यक्षेत्र फोल्डर अवैध आहे.',
 'The OSM download succeeded, but the output could not be created.':
   'OSM डाउनलोड यशस्वी झाले, पण आउटपुट तयार करता आले नाही.',
 "The Overpass response must be a JSON object with an 'elements' list.":
   'Overpass प्रतिसाद «elements» सूचीसह JSON ऑब्जेक्ट असणे आवश्यक आहे.',
 'The QGIS map canvas CRS is invalid.': 'QGIS नकाशा कॅनव्हास CRS अवैध आहे.',
 'The active layer CRS is invalid.': 'सक्रिय स्तर CRS अवैध आहे.',
 'The active layer extent is empty.': 'सक्रिय स्तर व्याप्ती रिकामी आहे.',
 'The active layer must be a vector layer.': 'सक्रिय स्तर वेक्टर स्तर असणे आवश्यक आहे.',
 'The combined name is too long. Shorten one or more components.':
   'एकत्रित नाव खूप लांब आहे. एक किंवा अधिक घटक लहान करा.',
 'The combined selected-feature geometry is empty.':
   'एकत्रित निवडलेल्या-वैशिष्ट्य भूमिती रिकामी आहे.',
 'The current AOI is invalid:': 'सध्याचा AOI अवैध आहे:',
 'The current QGIS map extent is empty.': 'सध्याची QGIS नकाशा व्याप्ती रिकामी आहे.',
 'The dialog cannot close while a download thread is running. Cancellation has been requested; close the dialog after it stops.':
   'डाउनलोड थ्रेड सुरू असताना संवाद बंद करता येत नाही. रद्द करण्याची विनंती केली आहे; तो थांबल्यावर संवाद बंद करा.',
 'The download completed, but no confirmed output name was available.':
   'डाउनलोड पूर्ण झाले, पण पुष्टी केलेले आउटपुट नाव उपलब्ध नव्हते.',
 "The exported Shapefile '{path}' could not be opened in QGIS.":
   'निर्यात केलेला Shapefile «{path}» QGIS मध्ये उघडता आला नाही.',
 "The exported layer '{layer_name}' could not be opened in QGIS.":
   'निर्यात केलेला स्तर «{layer_name}» QGIS मध्ये उघडता आला नाही.',
 'The output name does not contain any valid filename characters.':
   'आउटपुट नावात फाइलनावासाठी कोणतेही वैध वर्ण नाहीत.',
 'The output name is empty after filename validation.':
   'फाइलनाव प्रमाणीकरणानंतर आउटपुट नाव रिकामे आहे.',
 'The selected features contain no valid geometry.':
   'निवडलेल्या वैशिष्ट्यांमध्ये वैध भूमिती नाही.',
 'The selected output directory does not exist. Choose an existing folder.':
   'निवडलेले आउटपुट फोल्डर अस्तित्वात नाही. विद्यमान फोल्डर निवडा.',
 'There is no active download to cancel.': 'रद्द करण्यासाठी कोणतेही सक्रिय डाउनलोड नाही.',
 'Timeout on server ': 'सर्व्हरवर कालबाह्यता: ',
 'Translate widget labels while preserving each original English string.':
   'प्रत्येक मूळ इंग्रजी स्ट्रिंग जपून विजेट लेबल भाषांतरित करा.',
 'Trying Overpass server ': 'Overpass सर्व्हर वापरून पहात आहे: ',
 'Unable to start AOI drawing:': 'AOI रेखाटन सुरू करता आले नाही:',
 'Unclassified OSM elements not written to feature layers:':
   'वैशिष्ट्य स्तरांमध्ये न लिहिलेले अवर्गीकृत OSM घटक:',
 'Unsupported geometry family: {geometry_family}':
   'असमर्थित भूमिती कुटुंब: {geometry_family}',
 "Unsupported geometry type '{geometry_type}' for feature '{feature_key}'.":
   'वैशिष्ट्य «{feature_key}» साठी असमर्थित भूमिती प्रकार «{geometry_type}».',
 'Unsupported geometry type for Shapefile export: {geometry_type}':
   'Shapefile निर्यातीसाठी असमर्थित भूमिती प्रकार: {geometry_type}',
 "Unsupported match mode '{mode}' for feature '{feature_key}'.":
   'वैशिष्ट्य «{feature_key}» साठी असमर्थित जुळणी मोड «{mode}».',
 'Unsupported output format:': 'असमर्थित आउटपुट स्वरूप:',
 "Unsupported tag value type for '{feature_key}': {value_type}":
   '«{feature_key}» साठी असमर्थित टॅग मूल्य प्रकार: {value_type}',
 'Update Current QGIS Map Extent': 'सध्याची QGIS नकाशा व्याप्ती अद्यतनित करा',
 'Update the "N selected" count next to the category heading.':
   'श्रेणी शीर्षकाशेजारील «N निवडले» संख्या अद्यतनित करा.',
 'Update the filename preview as the user edits the components.':
   'वापरकर्त्याने घटक संपादित करताना फाइलनाव पूर्वावलोकन अद्यतनित करा.',
 'Use Layer Extent': 'स्तर व्याप्ती वापरा',
 'Use Selected Features': 'निवडलेली वैशिष्ट्ये वापरा',
 'Use local cache where available': 'उपलब्ध असल्यास स्थानिक कॅशे वापरा',
 'Use selected features in the active vector layer as the AOI.':
   'सक्रिय वेक्टर स्तरातील निवडलेली वैशिष्ट्ये AOI म्हणून वापरा.',
 'Use the full extent of the active QGIS layer as the AOI.':
   'सक्रिय QGIS स्तराची संपूर्ण व्याप्ती AOI म्हणून वापरा.',
 'Use the full extent of the active QGIS layer.':
   'सक्रिय QGIS स्तराची संपूर्ण व्याप्ती वापरा.',
 'Use the selected features of the active vector layer as the AOI.':
   'सक्रिय वेक्टर स्तराची निवडलेली वैशिष्ट्ये AOI म्हणून वापरा.',
 'Using cached data; no Overpass network request was needed.':
   'कॅशे केलेला डेटा वापरत आहे; कोणतीही Overpass नेटवर्क विनंती आवश्यक नव्हती.',
 'Validate filename and any explicitly selected admin levels.':
   'फाइलनाव आणि स्पष्टपणे निवडलेले admin स्तर प्रमाणित करा.',
 'Validate inputs and start the background Overpass download.':
   'इनपुट प्रमाणित करा आणि पार्श्वभूमी Overpass डाउनलोड सुरू करा.',
 'WGS84 AOI bbox: south=': 'WGS84 AOI बाउंडिंग बॉक्स: दक्षिण=',
 'WGS84 AOI geometry is not available.': 'WGS84 AOI भूमिती उपलब्ध नाही.',
 'Warning: download succeeded, but the response could not be cached:':
   'इशारा: डाउनलोड यशस्वी, पण प्रतिसाद कॅशे करता आला नाही:',
 'Waterways': 'जलमार्ग',
 'West longitude cannot be greater than east longitude.':
   'पश्चिम रेखांश पूर्व रेखांशापेक्षा जास्त असू शकत नाही.',
 'West:': 'पश्चिम:',
 'Writing Shapefile {layer_index}/{total}: {layer_name}...':
   'Shapefile लिहित आहे {layer_index}/{total}: {layer_name}…',
 'Writing layer {layer_index}/{total}: {layer_name} ({count:,} features)...':
   'स्तर लिहित आहे {layer_index}/{total}: {layer_name} ({count:,} वैशिष्ट्ये)…',
 'attempt ': 'प्रयत्न ',
 'characters).': 'वर्ण).',
 'connection error — ': 'कनेक्शन त्रुटी — ',
 'e.g. CBD': 'उदा. CBD',
 'e.g. Kenya': 'उदा. केनिया',
 'e.g. Nairobi': 'उदा. नैरोबी',
 'e.g. NairobiCounty': 'उदा. NairobiCounty',
 'elements (': 'घटक (',
 'export failed:': 'निर्यात अयशस्वी:',
 'feature records).': 'वैशिष्ट्य नोंदी).',
 'feature(s)).': 'वैशिष्ट्य(े)).',
 'features written.': 'वैशिष्ट्ये लिहिली.',
 'file(s) deleted.': 'फाइल(ी) हटवली.',
 'relation geometry assignment(s); relation-member geometry assembly is not implemented yet.':
   'रिलेशन भूमिती नियुक्ती; रिलेशन-सदस्य भूमिती संयोजन अद्याप लागू केलेले नाही.',
 'relations).': 'रिलेशन).',
 'response_data must be a dictionary.': 'response_data डिक्शनरी असणे आवश्यक आहे.',
 "response_data['elements'] must be a list.":
   "response_data['elements'] सूची असणे आवश्यक आहे.",
 'temporary file(s) could not be deleted. They may still be in use by QGIS or another process.':
   'तात्पुरती फाइल(ी) हटवता आली नाहीत. त्या QGIS किंवा दुसऱ्या प्रक्रियेद्वारे अद्याप वापरात असू शकतात.',
 'timeout — ': 'कालबाह्यता — ',
 '{output_format} export failed: {error}':
   '{output_format} निर्यात अयशस्वी: {error}',
 '— Confirm Overwrite': '— अधिलिखित करण्याची पुष्टी करा',
 '— Export Error': '— निर्यात त्रुटी',
 '— Help': '— मदत',
 '— Output Naming': '— आउटपुट नामकरण',
}