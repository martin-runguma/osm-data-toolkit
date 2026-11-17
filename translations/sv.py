"""Swedish (Svenska) translation pack for the OSM Data Toolkit plugin.
Keys remain the English source strings; preserve placeholders and HTML."""
TEXT = {
 '\n<h3>Quick start</h3>\n<ol>\n  <li><b>Choose an area.</b> Use the current map extent, draw a rectangle\n      on the map, or use the bounding box of selected features or a\n      layer\'s extent.</li>\n  <li><b>Tick the OSM categories</b> you need (POI, stops, roads,\n      buildings, boundaries, landuse, ...).</li>\n  <li><b>Choose an output format and folder</b>, then click\n      <b>Download OSM Data</b>.</li>\n</ol>\n\n<h3>Good to know</h3>\n<ul>\n  <li><b>GeoPackage is recommended.</b> A Shapefile cannot hold very many\n      attribute columns, so on large areas some rarely used tag columns\n      may be left out (the log tells you when this happens).</li>\n  <li><b>Keep the area focused.</b> Very large areas produce huge Overpass\n      responses and can be slow or rejected by the public servers.</li>\n  <li><b>The cache</b> lets repeat downloads of the same query reuse\n      earlier results.</li>\n  <li><b>"Unclassified OSM elements"</b> in the log is informational: they\n      are mostly untagged vertices of lines and polygons that do not belong\n      to any selected category.</li>\n</ul>\n\n<p>Data &copy; OpenStreetMap contributors, available under the\n<a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a>.</p>\n<p><i>This plugin is not endorsed by or affiliated with the\nOpenStreetMap Foundation.</i></p>\n':
 '\n<h3>Snabbstart</h3>\n<ol>\n  <li><b>Välj ett område.</b> Använd den aktuella kartutbredningen, rita en\n      rektangel på kartan eller använd begränsningsrutan för valda objekt\n      eller ett lagerobjekts utbredning.</li>\n  <li><b>Markera de OSM-kategorier</b> du behöver (POI, hållplatser, vägar,\n      byggnader, gränser, markanvändning, ...).</li>\n  <li><b>Välj utdataformat och mapp</b> och klicka sedan på\n      <b>Hämta OSM-data</b>.</li>\n</ol>\n\n<h3>Bra att veta</h3>\n<ul>\n  <li><b>GeoPackage rekommenderas.</b> En Shapefile kan inte rymma särskilt\n      många attributkolumner, så på stora områden kan vissa sällan använda\n      taggkolumner utelämnas (loggen berättar när detta händer).</li>\n  <li><b>Håll området fokuserat.</b> Mycket stora områden ger enorma\n      Overpass-svar och kan vara långsamma eller avvisas av de offentliga\n      servrarna.</li>\n  <li><b>Cachen</b> låter upprepade hämtningar av samma fråga återanvända\n      tidigare resultat.</li>\n  <li><b>"Oklassificerade OSM-element"</b> i loggen är information: de är\n      mestadels otaggade hörn i linjer och polygoner som inte tillhör\n      någon vald kategori.</li>\n</ul>\n\n<p>Data &copy; OpenStreetMap-bidragsgivare, tillgängliga under\n<a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a>.</p>\n<p><i>Detta plugin är inte godkänt av eller associerat med\nOpenStreetMap Foundation.</i></p>\n',
 ' responded successfully.': ' svarade framgångsrikt.',
 ' seconds...': ' sekunder…',
 '" style="color:#0B5E8E; text-decoration:none;">OpenStreetMap contributors</a> (ODbL)':
   '" style="color:#0B5E8E; text-decoration:none;">OpenStreetMap-bidragsgivare</a> (ODbL)',
 ', east=': ', öst=',
 ', north=': ', nord=',
 ', west=': ', väst=',
 '0 selected': '0 valda',
 '<p>Plugin version': '<p>Pluginversion',
 'A download is already running.': 'En hämtning pågår redan.',
 'A labelled column of feature checkboxes.':
   'En märkt kolumn med objektkryssrutor.',
 'AOI drawing cancelled.': 'AOI-ritning avbruten.',
 'AOI geometry is empty.': 'AOI-geometrin är tom.',
 'AOI geometry is missing.': 'AOI-geometrin saknas.',
 'AOI name': 'AOI-namn',
 'AOI rectangle captured successfully.':
   'AOI-rektangeln fångades framgångsrikt.',
 'AOI source CRS is invalid.': 'AOI-källans CRS är ogiltig.',
 'AOI validation failed:': 'AOI-validering misslyckades:',
 'AOI:': 'AOI:',
 'AOI: QGIS interface is not available.':
   'AOI: QGIS-gränssnittet är inte tillgängligt.',
 "AOI: click 'Draw AOI', then drag a rectangle on the QGIS map.":
   'AOI: klicka på "Rita AOI" och dra sedan en rektangel på QGIS-kartan.',
 "AOI: click 'Use Layer Extent' to use the full extent of the active QGIS layer.":
   'AOI: klicka på "Använd lagerutbredning" för att använda hela utbredningen för det aktiva QGIS-lagret.',
 'AOI: click and drag on the QGIS map.':
   'AOI: klicka och dra på QGIS-kartan.',
 'AOI: failed to resolve active layer extent':
   'AOI: kunde inte fastställa utbredningen för det aktiva lagret',
 'AOI: failed to resolve selected features':
   'AOI: kunde inte fastställa valda objekt',
 'AOI: invalid': 'AOI: ogiltig',
 'AOI: no active QGIS layer.': 'AOI: inget aktivt QGIS-lager.',
 'AOI: no feature(s) selected in the active layer.':
   'AOI: inga objekt valda i det aktiva lagret.',
 'AOI: not yet resolved': 'AOI: ännu inte fastställd',
 "AOI: select feature(s) in the active QGIS layer, then click 'Use Selected Features'.":
   'AOI: välj objekt i det aktiva QGIS-lagret och klicka sedan på "Använd valda objekt".',
 'AOI: the active layer is not a vector layer.':
   'AOI: det aktiva lagret är inte ett vektorlager.',
 'AOI: unable to create': 'AOI: kan inte skapa',
 'AOI: unable to resolve': 'AOI: kan inte fastställa',
 'Activate the interactive rectangle AOI map tool.':
   'Aktivera det interaktiva rektangel-AOI-kartverktyget.',
 'Active layer extent': 'Aktivt lagers utbredning',
 'Active-layer extent AOI is invalid.':
   'AOI från det aktiva lagrets utbredning är ogiltig.',
 'Active-layer extent captured successfully.':
   'Det aktiva lagrets utbredning fångades framgångsrikt.',
 'Active-layer extent validation failed:':
   'Validering av det aktiva lagrets utbredning misslyckades:',
 'Administrative boundaries': 'Administrativa gränser',
 'Administrative boundary filter: all levels (no admin_level filter).':
   'Filter för administrativa gränser: alla nivåer (inget admin_level-filter).',
 'Administrative boundary levels': 'Nivåer för administrativa gränser',
 'Administrative boundary levels:': 'Nivåer för administrativa gränser:',
 'Administrative levels must be an integer, a numeric string, a sequence of levels, or None.':
   'Administrativa nivåer måste vara ett heltal, en numerisk sträng, en sekvens av nivåer eller None.',
 'All OSM feature categories cleared.': 'Alla OSM-objektkategorier rensades.',
 'All OSM feature categories selected.': 'Alla OSM-objektkategorier valdes.',
 'All Overpass server URLs must be non-empty strings.':
   'Alla Overpass-server-URL:er måste vara icke-tomma strängar.',
 'All Overpass servers and retry attempts failed.':
   'Alla Overpass-servrar och återförsök misslyckades.',
 'All administrative levels will be included.':
   'Alla administrativa nivåer kommer att inkluderas.',
 'All administrative levels will be included; no admin_level filter will be added to the query.':
   'Alla administrativa nivåer kommer att inkluderas; inget admin_level-filter läggs till i frågan.',
 'All attempts failed for server ': 'Alla försök misslyckades för servern ',
 'All levels (0–15; no admin_level filter)':
   'Alla nivåer (0–15; inget admin_level-filter)',
 'An existing output directory is required for Shapefile export.':
   'En befintlig utdatamapp krävs för Shapefile-export.',
 'An output GeoPackage path is required.':
   'En utdata-GeoPackage-sökväg krävs.',
 'An output name is required for Shapefile export.':
   'Ett utdatanamn krävs för Shapefile-export.',
 'Append a timestamped message to the processing log.':
   'Lägg till ett tidsstämplat meddelande i bearbetningsloggen.',
 'Append an exported feature count to the processing log.':
   'Lägg till antalet exporterade objekt i bearbetningsloggen.',
 'Area of Interest': 'Intresseområde',
 'At least one OSM feature must be selected.':
   'Minst ett OSM-objekt måste väljas.',
 'At least one OSM feature must be supplied.':
   'Minst ett OSM-objekt måste anges.',
 'At least one Overpass server must be provided.':
   'Minst en Overpass-server måste anges.',
 'Attempt details:': 'Försöksdetaljer:',
 'Automatically add downloaded layers to QGIS':
   'Lägg automatiskt till hämtade lager i QGIS',
 'Background Overpass download started.':
   'Overpass-hämtning i bakgrunden startad.',
 'Browse': 'Bläddra',
 'Browse…': 'Bläddra…',
 'Buildings': 'Byggnader',
 'Bus stops': 'Busshållplatser',
 'CRS:': 'CRS:',
 'Cache hit:': 'Cacheträff:',
 'Cache hit: using saved Overpass response ({age} day(s) old).':
   'Cacheträff: använder sparat Overpass-svar ({age} dag(ar) gammalt).',
 'Cache miss:': 'Cachemiss:',
 'Cache miss: could not read saved response ({error}).':
   'Cachemiss: kunde inte läsa sparat svar ({error}).',
 'Cache miss: query hash does not match the saved response.':
   'Cachemiss: frågehashen matchar inte det sparade svaret.',
 'Cache miss: saved response is incomplete or invalid.':
   'Cachemiss: sparat svar är ofullständigt eller ogiltigt.',
 'Cache miss: saved response is older than {days} days.':
   'Cachemiss: sparat svar är äldre än {days} dagar.',
 'Cache miss: saved response uses an unsupported cache format.':
   'Cachemiss: sparat svar använder ett cacheformat som inte stöds.',
 'Cached Overpass response:': 'Cachat Overpass-svar:',
 'Cancel': 'Avbryt',
 'Cancellation has already been requested.': 'Avbrott har redan begärts.',
 'Cancellation requested': 'Avbrott begärt',
 'Cancellation requested. If an HTTP request is already active, the downloader will stop when that request returns or times out.':
   'Avbrott begärt. Om en HTTP-förfrågan redan är aktiv stoppar hämtaren när den förfrågan återvänder eller får timeout.',
 'Cancellation requested; waiting for the current request to finish...':
   'Avbrott begärt; väntar på att den aktuella förfrågan ska slutföras…',
 'Cannot draw AOI because the QGIS interface is unavailable.':
   'Kan inte rita AOI eftersom QGIS-gränssnittet inte är tillgängligt.',
 'Cannot resolve active-layer extent because QGIS is unavailable.':
   'Kan inte fastställa det aktiva lagrets utbredning eftersom QGIS inte är tillgängligt.',
 'Cannot resolve current map extent because QGIS is unavailable.':
   'Kan inte fastställa den aktuella kartutbredningen eftersom QGIS inte är tillgängligt.',
 'Cannot resolve selected-feature AOI because QGIS is unavailable.':
   'Kan inte fastställa AOI från valda objekt eftersom QGIS inte är tillgängligt.',
 'Cannot transform an empty geometry.':
   'Kan inte transformera en tom geometri.',
 'Capture the current QGIS map canvas extent.':
   'Fånga den aktuella utbredningen för QGIS-kartduken.',
 'Choose all available levels, or select one or more levels to download (for example, 5–8 or level 5).':
   'Välj alla tillgängliga nivåer eller välj en eller flera nivåer att hämta (till exempel 5–8 eller nivå 5).',
 'Choose an output directory before downloading.':
   'Välj en utdatamapp innan du hämtar.',
 'City name': 'Stadsnamn',
 'Classifying OSM elements and preparing GeoPackage layers.':
   'Klassificerar OSM-element och förbereder GeoPackage-lager.',
 'Classifying OSM elements and preparing Shapefile outputs.':
   'Klassificerar OSM-element och förbereder Shapefile-utdata.',
 'Clear all': 'Rensa alla',
 'Clear log': 'Rensa logg',
 'Clear only the visible log, without changing processing settings.':
   'Rensa endast den synliga loggen utan att ändra bearbetningsinställningarna.',
 'Clear selected levels so the user can make a narrower selection.':
   'Rensa valda nivåer så att användaren kan göra ett snävare val.',
 'Clear the messages currently shown in the Processing Log.':
   'Rensa meddelandena som för närvarande visas i bearbetningsloggen.',
 'Clear the previous AOI and display guidance for the chosen method.':
   'Rensa föregående AOI och visa vägledning för den valda metoden.',
 'Close': 'Stäng',
 'Collect optional filename components before exporting OSM data.':
   'Samla valfria filnamnskomponenter innan du exporterar OSM-data.',
 'Compact product header above the scrollable workflow.':
   'Kompakt produktrubrik ovanför det rullningsbara arbetsflödet.',
 'Connection error on server ': 'Anslutningsfel på servern ',
 'Continue to Download': 'Fortsätt till hämtning',
 'Convert a name component into a Windows-safe filename token.':
   'Konvertera en namnkomponent till en Windows-säker filnamnstoken.',
 'Convert the drawn rectangle into the standard AOI object.':
   'Konvertera den ritade rektangeln till standard-AOI-objektet.',
 'Converting OSM response to GeoPackage...':
   'Konverterar OSM-svar till GeoPackage…',
 'Converting OSM response to Shapefiles...':
   'Konverterar OSM-svar till Shapefiles…',
 'Could not combine the selected feature geometries.':
   'Kunde inte kombinera geometrierna för de valda objekten.',
 "Could not create Shapefile staging layer '{layer_name}'.":
   'Kunde inte skapa Shapefile-mellanlagret "{layer_name}".',
 'Could not create an empty bus_stops_points layer.':
   'Kunde inte skapa ett tomt bus_stops_points-lager.',
 "Could not create temporary QGIS layer '{layer_name}'.":
   'Kunde inte skapa det tillfälliga QGIS-lagret "{layer_name}".',
 'Could not create temporary layer for admin_level {admin_level}.':
   'Kunde inte skapa ett tillfälligt lager för admin_level {admin_level}.',
 'Could not create the merged bus_stops_points layer.':
   'Kunde inte skapa det sammanslagna bus_stops_points-lagret.',
 'Could not delete temporary file': 'Kunde inte radera tillfällig fil',
 "Could not load feature definition '{feature_key}': {error}":
   'Kunde inte läsa in objektdefinitionen "{feature_key}": {error}',
 'Could not merge bus-station centroids into bus-stop points.':
   'Kunde inte slå samman busstationers tyngdpunkter till busshållplatser.',
 'Could not overwrite existing output file: {error}':
   'Kunde inte skriva över befintlig utdatafil: {error}',
 'Could not populate Shapefile for admin_level {admin_level}.':
   'Kunde inte fylla Shapefile för admin_level {admin_level}.',
 "Could not populate temporary layer '{layer_name}'.":
   'Kunde inte fylla det tillfälliga lagret "{layer_name}".',
 'Could not prepare the Overpass query:':
   'Kunde inte förbereda Overpass-frågan:',
 "Could not reopen intermediate GeoPackage layer '{layer_name}'.":
   'Kunde inte återöppna det mellanliggande GeoPackage-lagret "{layer_name}".',
 'Could not restore previous QGIS map tool:':
   'Kunde inte återställa föregående QGIS-kartverktyg:',
 'Could not search for temporary GeoPackages:':
   'Kunde inte söka efter tillfälliga GeoPackages:',
 'Country name': 'Landsnamn',
 'Create one section panel and return it with its body layout.':
   'Skapa en sektionspanel och returnera den med dess innehållslayout.',
 'Created bus_stops_points from bus-station polygon centroids.':
   'Skapade bus_stops_points från tyngdpunkterna för busstationers polygoner.',
 'Current QGIS map extent': 'Aktuell QGIS-kartutbredning',
 'Current QGIS map extent resolved.':
   'Aktuell QGIS-kartutbredning fastställd.',
 'Data © <a href="': 'Data © <a href="',
 'Deleted temporary workspace file:':
   'Raderade tillfällig arbetsytefil:',
 'Details:': 'Detaljer:',
 'Download': 'Hämta',
 'Download OSM Data': 'Hämta OSM-data',
 'Download OpenStreetMap data for any area and load it straight into QGIS.':
   'Hämta OpenStreetMap-data för valfritt område och läs in dem direkt i QGIS.',
 'Download cancelled because existing output files were not approved for overwrite.':
   'Hämtning avbruten eftersom befintliga utdatafiler inte godkändes för överskrivning.',
 'Download cancelled before it started.':
   'Hämtning avbruten innan den startade.',
 'Download cancelled before results were returned.':
   'Hämtning avbruten innan resultat returnerades.',
 'Download cancelled before starting.':
   'Hämtning avbruten innan den startade.',
 'Download cancelled in the output-naming dialog.':
   'Hämtning avbruten i dialogrutan för utdatanamn.',
 'Download cancelled.': 'Hämtning avbruten.',
 'Download cancelled; existing files preserved.':
   'Hämtning avbruten; befintliga filer bevarades.',
 'Download stopped.': 'Hämtning stoppad.',
 'Download succeeded, but export failed.':
   'Hämtningen lyckades men exporten misslyckades.',
 'Downloading OSM data from Overpass...':
   'Hämtar OSM-data från Overpass…',
 'Draw AOI': 'Rita AOI',
 'Draw a rectangle on the QGIS map to define the AOI.':
   'Rita en rektangel på QGIS-kartan för att definiera AOI:n.',
 'Draw rectangle on map': 'Rita rektangel på kartan',
 'Draw the AOI rectangle on the QGIS map.':
   'Rita AOI-rektangeln på QGIS-kartan.',
 'Drawn AOI validation failed:':
   'Validering av ritad AOI misslyckades:',
 'Drawn rectangle': 'Ritad rektangel',
 'Drawn rectangle AOI captured successfully.':
   'Ritad rektangel-AOI fångades framgångsrikt.',
 'ERROR:': 'FEL:',
 'East:': 'Öst:',
 'Enable level checkboxes only when a specific selection is active.':
   'Aktivera nivåkryssrutorna endast när ett specifikt val är aktivt.',
 'Enable only the AOI action button for the selected method.':
   'Aktivera endast AOI-åtgärdsknappen för den valda metoden.',
 'Enable or disable controls while a download is running.':
   'Aktivera eller inaktivera kontroller medan en hämtning pågår.',
 'Enter at least one name (City, Country, Region, or AOI).':
   'Ange minst ett namn (stad, land, region eller AOI).',
 'Enter one or more name components. Blank fields will be skipped, and the remaining names will be joined with underscores. The selected output format will be retained.':
   'Ange en eller flera namnkomponenter. Tomma fält hoppas över och de återstående namnen sammanfogas med understreck. Det valda utdataformatet behålls.',
 'Enter_a_name_to_preview': 'Ange_ett_namn_för_förhandsgranskning',
 'Export cancelled: output name is missing.':
   'Export avbruten: utdatanamnet saknas.',
 'Export complete:': 'Export klar:',
 'Export the downloaded response and optionally load its layers.':
   'Exportera det hämtade svaret och läs eventuellt in dess lager.',
 'Failed to activate rectangle AOI tool:':
   'Kunde inte aktivera rektangel-AOI-verktyget:',
 'Failed to create AOI.': 'Kunde inte skapa AOI.',
 'Failed to process drawn rectangle AOI:':
   'Kunde inte bearbeta den ritade rektangel-AOI:n:',
 'Failed to resolve active-layer extent.':
   'Kunde inte fastställa det aktiva lagrets utbredning.',
 'Failed to resolve active-layer extent:':
   'Kunde inte fastställa det aktiva lagrets utbredning:',
 'Failed to resolve current QGIS map extent:':
   'Kunde inte fastställa aktuell QGIS-kartutbredning:',
 'Failed to resolve selected-feature AOI.':
   'Kunde inte fastställa AOI från valda objekt.',
 'Failed to resolve selected-feature AOI:':
   'Kunde inte fastställa AOI från valda objekt:',
 "Failed to write layer '{layer_name}' to '{output_path}': {error}":
   'Kunde inte skriva lagret "{layer_name}" till "{output_path}": {error}',
 "Feature '{feature_key}' has no tag definitions.":
   'Objektet "{feature_key}" har inga taggdefinitioner.',
 'Feature specification  does not expose a tag-filter mapping.':
   'Objektspecifikationen exponerar ingen taggfiltermappning.',
 'Ferry stops': 'Färjehållplatser',
 'Filename preview': 'Förhandsgranskning av filnamn',
 'Full documentation': 'Fullständig dokumentation',
 'Generated Overpass query (': 'Genererad Overpass-fråga (',
 'GeoPackage': 'GeoPackage',
 'GeoPackage layer(s) to QGIS.': 'GeoPackage-lager i QGIS.',
 'GeoPackage saved:': 'GeoPackage sparat:',
 'HTTP error on server ': 'HTTP-fel på servern ',
 'HTTP error — ': 'HTTP-fel — ',
 'HTTP {status} error on server {index}/{total}.':
   'HTTP {status}-fel på servern {index}/{total}.',
 'Handle a drawing tool deactivation initiated outside this dialog.':
   'Hantera inaktivering av ett ritverktyg som initierats utanför denna dialogruta.',
 'Help': 'Hjälp',
 'Invalid east longitude: {value}': 'Ogiltig östlig longitud: {value}',
 'Invalid north latitude: {value}': 'Ogiltig nordlig latitud: {value}',
 'Invalid response from server ': 'Ogiltigt svar från servern ',
 'Invalid south latitude: {value}': 'Ogiltig sydlig latitud: {value}',
 'Invalid west longitude: {value}': 'Ogiltig västlig longitud: {value}',
 'Keep the numeric readout in step with the progress bar.':
   'Håll den numeriska avläsningen i takt med förloppsindikatorn.',
 'Land & built environment': 'Mark och bebyggd miljö',
 'Landuse': 'Markanvändning',
 'Language:': 'Språk:',
 'Linear features': 'Linjära objekt',
 'Load the saved interface language and translate visible UI strings.':
   'Läs in det sparade gränssnittsspråket och översätt synliga UI-strängar.',
 'Local response cache is disabled.':
   'Lokal svarsache är inaktiverad.',
 'Main OSM Data Toolkit window.': 'Huvudfönstret för OSM Data Toolkit.',
 'Manually capture the map extent after the user pans or zooms.':
   'Fånga kartutbredningen manuellt efter att användaren panorerar eller zoomar.',
 'Merged bus-station polygon centroids into bus_stops_points.':
   'Slog samman busstationers polygontyngdpunkter till bus_stops_points.',
 'No Overpass selectors were generated.':
   'Inga Overpass-väljare genererades.',
 'No active QGIS layer is available.':
   'Inget aktivt QGIS-lager är tillgängligt.',
 'No active layer is available.': 'Inget aktivt lager är tillgängligt.',
 'No exportable features matched the selected categories. Try another AOI or select additional OSM feature categories.':
   'Inga exporterbara objekt matchade de valda kategorierna. Prova en annan AOI eller välj ytterligare OSM-objektkategorier.',
 'No features are selected in the active layer.':
   'Inga objekt är valda i det aktiva lagret.',
 'No levels selected. Select at least one level to continue.':
   'Inga nivåer valda. Välj minst en nivå för att fortsätta.',
 'No selected features found.': 'Inga valda objekt hittades.',
 'No valid Area of Interest is available. Select an AOI method and resolve the AOI before downloading.':
   'Inget giltigt intresseområde är tillgängligt. Välj en AOI-metod och fastställ AOI:n innan du hämtar.',
 'North:': 'Nord:',
 'Note: {layer_name} has too many tag columns for one Shapefile (DBF size limit); {count} rarely-used columns were left out.':
   'Obs: {layer_name} har för många taggkolumner för en Shapefile (DBF-storleksgräns); {count} sällan använda kolumner utelämnades.',
 'OSM Data Toolkit': 'OSM Data Toolkit',
 'OSM Data Toolkit initialised.': 'OSM Data Toolkit initierades.',
 'OSM Feature Categories': 'OSM-objektkategorier',
 'OSM export completed successfully.':
   'OSM-exporten slutfördes framgångsrikt.',
 'One or more output files with this name already exist. Do you want to overwrite the matching output files?':
   'En eller flera utdatafiler med detta namn finns redan. Vill du skriva över de matchande utdatafilerna?',
 'Only the selected levels': 'Endast de valda nivåerna',
 'Only validated Overpass responses can be cached.':
   'Endast validerade Overpass-svar kan cachas.',
 'Open public spaces': 'Öppna offentliga platser',
 'Open the in-plugin help with links to the online documentation.':
   'Öppna hjälpen i pluginen med länkar till onlinedokumentationen.',
 'Output Settings': 'Utdatainställningar',
 'Output directory': 'Utdatamapp',
 'Output directory selected:': 'Utdatamapp vald:',
 'Output format': 'Utdataformat',
 'Output settings': 'Utdatainställningar',
 'Overpass download cancelled.': 'Overpass-hämtning avbruten.',
 'Overpass download completed:': 'Overpass-hämtning klar:',
 'Overpass download failed.': 'Overpass-hämtning misslyckades.',
 'Overpass download failed:': 'Overpass-hämtning misslyckades:',
 'Overpass download running...': 'Overpass-hämtning pågår…',
 'Overpass download was cancelled by the caller.':
   'Overpass-hämtningen avbröts av anroparen.',
 'Overpass query must be a non-empty string.':
   'Overpass-frågan måste vara en icke-tom sträng.',
 "Overpass response 'elements' field is not a list.":
   'Overpass-svarets "elements"-fält är inte en lista.',
 "Overpass response does not contain an 'elements' field.":
   'Overpass-svaret innehåller inget "elements"-fält.',
 'Overpass response is not a JSON object.':
   'Overpass-svaret är inte ett JSON-objekt.',
 'Overpass response received successfully:':
   'Overpass-svar mottaget framgångsrikt:',
 'Overpass server ': 'Overpass-server ',
 'Overpass server returned invalid JSON. Response preview: ':
   'Overpass-servern returnerade ogiltig JSON. Förhandsgranskning av svar: ',
 'Overpass servers available:': 'Tillgängliga Overpass-servrar:',
 'Overpass timeout must be greater than zero.':
   'Overpass-timeout måste vara större än noll.',
 'Plugin version': 'Pluginversion',
 'Points of interest (POI)': 'Intressanta platser (POI)',
 'Prepared {index:,} of {total:,} OSM elements for export...':
   'Förberedde {index:,} av {total:,} OSM-element för export…',
 'Preparing Overpass download...': 'Förbereder Overpass-hämtning…',
 'Preparing Overpass query.': 'Förbereder Overpass-fråga.',
 'Processing Options': 'Bearbetningsalternativ',
 'Processing log': 'Bearbetningslogg',
 'Processing messages will appear here...':
   'Bearbetningsmeddelanden visas här…',
 'Processing options': 'Bearbetningsalternativ',
 'Public transport & places': 'Kollektivtrafik och platser',
 'QGIS interface object was not detected. Canvas-dependent AOI tools are disabled.':
   'QGIS-gränssnittsobjektet hittades inte. Dukberoende AOI-verktyg är inaktiverade.',
 'QGIS map canvas could not be accessed.':
   'Det gick inte att komma åt QGIS-kartduken.',
 'QGIS map canvas is unavailable.': 'QGIS-kartduken är inte tillgänglig.',
 'Rail stops': 'Järnvägshållplatser',
 'Railways': 'Järnvägar',
 'Read the plugin version from metadata.txt (empty string if absent).':
   'Läs pluginversionen från metadata.txt (tom sträng om den saknas).',
 'Read, validate and store the current QGIS map canvas extent.':
   'Läs, validera och lagra den aktuella utbredningen för QGIS-kartduken.',
 'Ready.': 'Klar.',
 'Rectangle AOI drawing tool activated.':
   'Ritverktyget för rektangel-AOI aktiverades.',
 'Rectangle AOI drawing was cancelled.':
   'Ritningen av rektangel-AOI avbröts.',
 'Region name': 'Regionnamn',
 'Report an issue': 'Rapportera ett problem',
 'Request cooperative cancellation of the background worker.':
   'Begär kooperativt avbrott av bakgrundsarbetaren.',
 'Request error on server ': 'Förfrågningsfel på servern ',
 'Restore default GUI settings when the dialog closes.':
   'Återställ standard-GUI-inställningar när dialogrutan stängs.',
 'Restore the GUI once the background thread has stopped.':
   'Återställ GUI:t när bakgrundstråden har stoppats.',
 'Restore the QGIS map tool active before rectangle drawing.':
   'Återställ det QGIS-kartverktyg som var aktivt före rektangelritningen.',
 'Restore the map tool and reset state before hiding the dialog.':
   'Återställ kartverktyget och återställ tillståndet innan dialogrutan döljs.',
 'Retrying in ': 'Försöker igen om ',
 'Return selected levels, or None when all levels are requested.':
   'Returnera valda nivåer eller None när alla nivåer begärs.',
 'Return the combined, sanitized filename prefix.':
   'Returnera det kombinerade, sanerade filnamnsprefixet.',
 'Return the mapping between feature keys and GUI checkboxes.':
   'Returnera mappningen mellan objektnycklar och GUI-kryssrutor.',
 'Return the selected GUI feature keys.':
   'Returnera de valda GUI-objektnycklarna.',
 'Roads': 'Vägar',
 'Run a modal dialog on both Qt5 and Qt6.':
   'Kör en modal dialogruta i både Qt5 och Qt6.',
 'Select Output Directory': 'Välj utdatamapp',
 'Select a vector layer with selected features.':
   'Välj ett vektorlager med valda objekt.',
 'Select all': 'Markera alla',
 'Select an active QGIS layer.': 'Välj ett aktivt QGIS-lager.',
 'Select at least one OSM feature category before downloading.':
   'Välj minst en OSM-objektkategori innan du hämtar.',
 'Select at least one administrative level, or choose All levels.':
   'Välj minst en administrativ nivå eller välj Alla nivåer.',
 'Select at least one administrative level, or use None to retrieve all levels.':
   'Välj minst en administrativ nivå eller använd None för att hämta alla nivåer.',
 'Select levels 0–15 and switch to specific-level mode.':
   'Välj nivåerna 0–15 och växla till läget för specifika nivåer.',
 'Select one or more features in the active layer.':
   'Välj ett eller flera objekt i det aktiva lagret.',
 'Select output directory...': 'Välj utdatamapp…',
 'Selected administrative levels:': 'Valda administrativa nivåer:',
 'Selected feature IDs:': 'ID:n för valda objekt:',
 'Selected feature(s) in active layer':
   'Valda objekt i aktivt lager',
 'Selected features (': 'Valda objekt (',
 'Selected-feature AOI captured successfully (':
   'AOI från valda objekt fångades framgångsrikt (',
 'Selected-feature AOI captured successfully.':
   'AOI från valda objekt fångades framgångsrikt.',
 'Selected-feature AOI is invalid.':
   'AOI från valda objekt är ogiltig.',
 'Selected-feature AOI requires a vector layer.':
   'AOI från valda objekt kräver ett vektorlager.',
 'Selected-feature AOI validation failed:':
   'Validering av AOI från valda objekt misslyckades:',
 'Sending query to Overpass...': 'Skickar fråga till Overpass…',
 'Server ': 'Server ',
 'Shapefile': 'Shapefile',
 'Shapefile export completed in:': 'Shapefile-export klar på:',
 'Shapefile field names shortened for':
   'Shapefile-fältnamn förkortades för',
 'Shapefile layer(s) to QGIS.': 'Shapefile-lager i QGIS.',
 'Short in-plugin help with links to the full online documentation.':
   'Kort hjälp i pluginen med länkar till den fullständiga onlinedokumentationen.',
 'Show AOI coordinates and source CRS in the dialog.':
   'Visa AOI-koordinater och käll-CRS i dialogrutan.',
 'Show a concise description of the active administrative filter.':
   'Visa en kortfattad beskrivning av det aktiva administrativa filtret.',
 'Source CRS is invalid.': 'Käll-CRS är ogiltig.',
 'South latitude cannot be greater than north latitude.':
   'Sydlig latitud kan inte vara större än nordlig latitud.',
 'South:': 'Syd:',
 'Starting Overpass download...': 'Startar Overpass-hämtning…',
 'Supporting copy: muted, wrapped and visually quiet.':
   'Stödjande text: dämpad, radbruten och visuellt lugn.',
 "Tag '{tag}' contains an empty value list.":
   'Taggen "{tag}" innehåller en tom värdelista.',
 'Temporary workspace cleanup complete:':
   'Rensning av tillfällig arbetsyta klar:',
 'Temporary workspace cleanup complete: no matching files found.':
   'Rensning av tillfällig arbetsyta klar: inga matchande filer hittades.',
 'Temporary-file cleanup skipped: workspace directory is invalid.':
   'Rensning av tillfälliga filer hoppades över: arbetsytemappen är ogiltig.',
 'The OSM download succeeded, but the output could not be created.':
   'OSM-hämtningen lyckades men utdata kunde inte skapas.',
 "The Overpass response must be a JSON object with an 'elements' list.":
   'Overpass-svaret måste vara ett JSON-objekt med en "elements"-lista.',
 'The QGIS map canvas CRS is invalid.':
   'CRS:en för QGIS-kartduken är ogiltig.',
 'The active layer CRS is invalid.':
   'CRS:en för det aktiva lagret är ogiltig.',
 'The active layer extent is empty.':
   'Det aktiva lagrets utbredning är tom.',
 'The active layer must be a vector layer.':
   'Det aktiva lagret måste vara ett vektorlager.',
 'The combined name is too long. Shorten one or more components.':
   'Det kombinerade namnet är för långt. Förkorta en eller flera komponenter.',
 'The combined selected-feature geometry is empty.':
   'Den kombinerade geometrin för valda objekt är tom.',
 'The current AOI is invalid:': 'Den aktuella AOI:n är ogiltig:',
 'The current QGIS map extent is empty.':
   'Den aktuella QGIS-kartutbredningen är tom.',
 'The dialog cannot close while a download thread is running. Cancellation has been requested; close the dialog after it stops.':
   'Dialogrutan kan inte stängas medan en hämtningstråd körs. Avbrott har begärts; stäng dialogrutan efter att den har stoppats.',
 'The download completed, but no confirmed output name was available.':
   'Hämtningen slutfördes men inget bekräftat utdatanamn var tillgängligt.',
 "The exported Shapefile '{path}' could not be opened in QGIS.":
   'Den exporterade Shapefilen "{path}" kunde inte öppnas i QGIS.',
 "The exported layer '{layer_name}' could not be opened in QGIS.":
   'Det exporterade lagret "{layer_name}" kunde inte öppnas i QGIS.',
 'The output name does not contain any valid filename characters.':
   'Utdatanamnet innehåller inga giltiga filnamnstecken.',
 'The output name is empty after filename validation.':
   'Utdatanamnet är tomt efter filnamnsvalidering.',
 'The selected features contain no valid geometry.':
   'De valda objekten innehåller ingen giltig geometri.',
 'The selected output directory does not exist. Choose an existing folder.':
   'Den valda utdatamappen finns inte. Välj en befintlig mapp.',
 'There is no active download to cancel.':
   'Det finns ingen aktiv hämtning att avbryta.',
 'Timeout on server ': 'Timeout på servern ',
 'Translate widget labels while preserving each original English string.':
   'Översätt widgetetiketter samtidigt som varje ursprunglig engelsk sträng bevaras.',
 'Trying Overpass server ': 'Provar Overpass-servern ',
 'Unable to start AOI drawing:': 'Kunde inte starta AOI-ritning:',
 'Unclassified OSM elements not written to feature layers:':
   'Oklassificerade OSM-element som inte skrevs till objektlager:',
 'Unsupported geometry family: {geometry_family}':
   'Geometrifylld som inte stöds: {geometry_family}',
 "Unsupported geometry type '{geometry_type}' for feature '{feature_key}'.":
   'Geometritypen "{geometry_type}" stöds inte för objektet "{feature_key}".',
 'Unsupported geometry type for Shapefile export: {geometry_type}':
   'Geometritypen stöds inte för Shapefile-export: {geometry_type}',
 "Unsupported match mode '{mode}' for feature '{feature_key}'.":
   'Matchningsläget "{mode}" stöds inte för objektet "{feature_key}".',
 'Unsupported output format:': 'Utdataformatet stöds inte:',
 "Unsupported tag value type for '{feature_key}': {value_type}":
   'Taggvärdetypen stöds inte för "{feature_key}": {value_type}',
 'Update Current QGIS Map Extent':
   'Uppdatera aktuell QGIS-kartutbredning',
 'Update the "N selected" count next to the category heading.':
   'Uppdatera antalet "N valda" bredvid kategorirubriken.',
 'Update the filename preview as the user edits the components.':
   'Uppdatera filnamnsförhandsgranskningen när användaren redigerar komponenterna.',
 'Use Layer Extent': 'Använd lagerutbredning',
 'Use Selected Features': 'Använd valda objekt',
 'Use local cache where available':
   'Använd lokal cache där det är möjligt',
 'Use selected features in the active vector layer as the AOI.':
   'Använd valda objekt i det aktiva vektorlagret som AOI.',
 'Use the full extent of the active QGIS layer as the AOI.':
   'Använd hela utbredningen för det aktiva QGIS-lagret som AOI.',
 'Use the full extent of the active QGIS layer.':
   'Använd hela utbredningen för det aktiva QGIS-lagret.',
 'Use the selected features of the active vector layer as the AOI.':
   'Använd de valda objekten i det aktiva vektorlagret som AOI.',
 'Using cached data; no Overpass network request was needed.':
   'Använder cachade data; ingen Overpass-nätverksförfrågan behövdes.',
 'Validate filename and any explicitly selected admin levels.':
   'Validera filnamn och eventuellt uttryckligen valda admin-nivåer.',
 'Validate inputs and start the background Overpass download.':
   'Validera indata och starta Overpass-hämtningen i bakgrunden.',
 'WGS84 AOI bbox: south=': 'WGS84 AOI-begränsningsruta: syd=',
 'WGS84 AOI geometry is not available.':
   'WGS84 AOI-geometri är inte tillgänglig.',
 'Warning: download succeeded, but the response could not be cached:':
   'Varning: hämtningen lyckades men svaret kunde inte cachas:',
 'Waterways': 'Vattendrag',
 'West longitude cannot be greater than east longitude.':
   'Västlig longitud kan inte vara större än östlig longitud.',
 'West:': 'Väst:',
 'Writing Shapefile {layer_index}/{total}: {layer_name}...':
   'Skriver Shapefile {layer_index}/{total}: {layer_name}…',
 'Writing layer {layer_index}/{total}: {layer_name} ({count:,} features)...':
   'Skriver lager {layer_index}/{total}: {layer_name} ({count:,} objekt)…',
 'attempt ': 'försök ',
 'characters).': 'tecken).',
 'connection error — ': 'anslutningsfel — ',
 'e.g. CBD': 't.ex. CBD',
 'e.g. Kenya': 't.ex. Kenya',
 'e.g. Nairobi': 't.ex. Nairobi',
 'e.g. NairobiCounty': 't.ex. NairobiCounty',
 'elements (': 'element (',
 'export failed:': 'exporten misslyckades:',
 'feature records).': 'objektposter).',
 'feature(s)).': 'objekt)).',
 'features written.': 'objekt skrivna.',
 'file(s) deleted.': 'fil(er) raderade.',
 'relation geometry assignment(s); relation-member geometry assembly is not implemented yet.':
   'relationstilldelning(ar) av geometri; sammansättning av relationsmedlemmars geometri är ännu inte implementerad.',
 'relations).': 'relationer).',
 'response_data must be a dictionary.':
   'response_data måste vara en ordbok.',
 "response_data['elements'] must be a list.":
   "response_data['elements'] måste vara en lista.",
 'temporary file(s) could not be deleted. They may still be in use by QGIS or another process.':
   'tillfälliga filer kunde inte raderas. De kan fortfarande användas av QGIS eller en annan process.',
 'timeout — ': 'timeout — ',
 '{output_format} export failed: {error}':
   '{output_format}-export misslyckades: {error}',
 '— Confirm Overwrite': '— Bekräfta överskrivning',
 '— Export Error': '— Exportfel',
 '— Help': '— Hjälp',
 '— Output Naming': '— Namngivning av utdata',
}