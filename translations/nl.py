"""Dutch (nl) translation pack for the OSM Data Toolkit plugin.
Keys remain the English source strings; preserve placeholders and HTML."""
TEXT = {
 '\n<h3>Quick start</h3>\n<ol>\n  <li><b>Choose an area.</b> Use the current map extent, draw a rectangle\n      on the map, or use the bounding box of selected features or a\n      layer\'s extent.</li>\n  <li><b>Tick the OSM categories</b> you need (POI, stops, roads,\n      buildings, boundaries, landuse, ...).</li>\n  <li><b>Choose an output format and folder</b>, then click\n      <b>Download OSM Data</b>.</li>\n</ol>\n\n<h3>Good to know</h3>\n<ul>\n  <li><b>GeoPackage is recommended.</b> A Shapefile cannot hold very many\n      attribute columns, so on large areas some rarely used tag columns\n      may be left out (the log tells you when this happens).</li>\n  <li><b>Keep the area focused.</b> Very large areas produce huge Overpass\n      responses and can be slow or rejected by the public servers.</li>\n  <li><b>The cache</b> lets repeat downloads of the same query reuse\n      earlier results.</li>\n  <li><b>"Unclassified OSM elements"</b> in the log is informational: they\n      are mostly untagged vertices of lines and polygons that do not belong\n      to any selected category.</li>\n</ul>\n\n<p>Data &copy; OpenStreetMap contributors, available under the\n<a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a>.</p>\n<p><i>This plugin is not endorsed by or affiliated with the\nOpenStreetMap Foundation.</i></p>\n':
 '\n<h3>Snel starten</h3>\n<ol>\n  <li><b>Kies een gebied.</b> Gebruik de huidige kaartuitsnede, teken een\n      rechthoek op de kaart, of gebruik de begrenzingsbox van geselecteerde\n      objecten of de uitsnede van een laag.</li>\n  <li><b>Vink de OSM-categorieën aan</b> die je nodig hebt (POI, haltes,\n      wegen, gebouwen, grenzen, landgebruik, ...).</li>\n  <li><b>Kies een uitvoerformaat en map</b> en klik vervolgens op\n      <b>OSM-gegevens downloaden</b>.</li>\n</ol>\n\n<h3>Goed om te weten</h3>\n<ul>\n  <li><b>GeoPackage wordt aanbevolen.</b> Een Shapefile kan niet erg veel\n      attribuutkolommen bevatten, dus bij grote gebieden kunnen sommige\n      zelden gebruikte tag-kolommen worden weggelaten (het logboek vertelt\n      je wanneer dit gebeurt).</li>\n  <li><b>Houd het gebied gericht.</b> Zeer grote gebieden leveren enorme\n      Overpass-antwoorden op en kunnen traag zijn of worden geweigerd door\n      de publieke servers.</li>\n  <li><b>De cache</b> laat herhaalde downloads van dezelfde query eerdere\n      resultaten hergebruiken.</li>\n  <li><b>"Niet-geclassificeerde OSM-elementen"</b> in het logboek is\n      informatief: het zijn meestal niet-gelabelde knooppunten van lijnen en\n      polygonen die niet tot een geselecteerde categorie behoren.</li>\n</ul>\n\n<p>Gegevens &copy; OpenStreetMap-bijdragers, beschikbaar onder de\n<a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a>.</p>\n<p><i>Deze plug-in wordt niet onderschreven door of is niet verbonden aan de\nOpenStreetMap Foundation.</i></p>\n',
 ' responded successfully.': ' heeft succesvol geantwoord.',
 ' seconds...': ' seconden…',
 '" style="color:#0B5E8E; text-decoration:none;">OpenStreetMap contributors</a> (ODbL)':
   '" style="color:#0B5E8E; text-decoration:none;">OpenStreetMap-bijdragers</a> (ODbL)',
 ', east=': ', oost=',
 ', north=': ', noord=',
 ', west=': ', west=',
 '0 selected': '0 geselecteerd',
 '<p>Plugin version': '<p>Plug-inversie',
 'A download is already running.': 'Er wordt al een download uitgevoerd.',
 'A labelled column of feature checkboxes.':
   'Een gelabelde kolom met selectievakjes voor objecten.',
 'AOI drawing cancelled.': 'AOI-tekenen geannuleerd.',
 'AOI geometry is empty.': 'AOI-geometrie is leeg.',
 'AOI geometry is missing.': 'AOI-geometrie ontbreekt.',
 'AOI name': 'AOI-naam',
 'AOI rectangle captured successfully.': 'AOI-rechthoek succesvol vastgelegd.',
 'AOI source CRS is invalid.': 'AOI-bron-CRS is ongeldig.',
 'AOI validation failed:': 'AOI-validatie mislukt:',
 'AOI:': 'AOI:',
 'AOI: QGIS interface is not available.': 'AOI: QGIS-interface is niet beschikbaar.',
 "AOI: click 'Draw AOI', then drag a rectangle on the QGIS map.":
   'AOI: klik op "AOI tekenen" en sleep vervolgens een rechthoek op de QGIS-kaart.',
 "AOI: click 'Use Layer Extent' to use the full extent of the active QGIS layer.":
   'AOI: klik op "Laaguitsnede gebruiken" om de volledige uitsnede van de actieve QGIS-laag te gebruiken.',
 'AOI: click and drag on the QGIS map.': 'AOI: klik en sleep op de QGIS-kaart.',
 'AOI: failed to resolve active layer extent':
   'AOI: kon de uitsnede van de actieve laag niet bepalen',
 'AOI: failed to resolve selected features':
   'AOI: kon geselecteerde objecten niet bepalen',
 'AOI: invalid': 'AOI: ongeldig',
 'AOI: no active QGIS layer.': 'AOI: geen actieve QGIS-laag.',
 'AOI: no feature(s) selected in the active layer.':
   'AOI: geen object(en) geselecteerd in de actieve laag.',
 'AOI: not yet resolved': 'AOI: nog niet bepaald',
 "AOI: select feature(s) in the active QGIS layer, then click 'Use Selected Features'.":
   'AOI: selecteer object(en) in de actieve QGIS-laag en klik vervolgens op "Geselecteerde objecten gebruiken".',
 'AOI: the active layer is not a vector layer.':
   'AOI: de actieve laag is geen vectorlaag.',
 'AOI: unable to create': 'AOI: kan niet aanmaken',
 'AOI: unable to resolve': 'AOI: kan niet bepalen',
 'Activate the interactive rectangle AOI map tool.':
   'Activeer het interactieve rechthoek-AOI-kaartgereedschap.',
 'Active layer extent': 'Uitsnede van actieve laag',
 'Active-layer extent AOI is invalid.':
   'AOI uit uitsnede van actieve laag is ongeldig.',
 'Active-layer extent captured successfully.':
   'Uitsnede van actieve laag succesvol vastgelegd.',
 'Active-layer extent validation failed:':
   'Validatie van uitsnede van actieve laag mislukt:',
 'Administrative boundaries': 'Administratieve grenzen',
 'Administrative boundary filter: all levels (no admin_level filter).':
   'Filter voor administratieve grenzen: alle niveaus (geen admin_level-filter).',
 'Administrative boundary levels': 'Niveaus van administratieve grenzen',
 'Administrative boundary levels:': 'Niveaus van administratieve grenzen:',
 'Administrative levels must be an integer, a numeric string, a sequence of levels, or None.':
   'Administratieve niveaus moeten een geheel getal, een numerieke tekenreeks, een reeks niveaus of None zijn.',
 'All OSM feature categories cleared.': 'Alle OSM-objectcategorieën gewist.',
 'All OSM feature categories selected.': 'Alle OSM-objectcategorieën geselecteerd.',
 'All Overpass server URLs must be non-empty strings.':
   'Alle Overpass-server-URL\'s moeten niet-lege tekenreeksen zijn.',
 'All Overpass servers and retry attempts failed.':
   'Alle Overpass-servers en nieuwe pogingen zijn mislukt.',
 'All administrative levels will be included.':
   'Alle administratieve niveaus worden opgenomen.',
 'All administrative levels will be included; no admin_level filter will be added to the query.':
   'Alle administratieve niveaus worden opgenomen; er wordt geen admin_level-filter aan de query toegevoegd.',
 'All attempts failed for server ': 'Alle pogingen mislukt voor server ',
 'All levels (0–15; no admin_level filter)': 'Alle niveaus (0–15; geen admin_level-filter)',
 'An existing output directory is required for Shapefile export.':
   'Een bestaande uitvoermap is vereist voor Shapefile-export.',
 'An output GeoPackage path is required.': 'Een uitvoer-GeoPackage-pad is vereist.',
 'An output name is required for Shapefile export.':
   'Een uitvoernaam is vereist voor Shapefile-export.',
 'Append a timestamped message to the processing log.':
   'Voeg een bericht met tijdstempel toe aan het verwerkingslogboek.',
 'Append an exported feature count to the processing log.':
   'Voeg het aantal geëxporteerde objecten toe aan het verwerkingslogboek.',
 'Area of Interest': 'Interessegebied',
 'At least one OSM feature must be selected.':
   'Er moet ten minste één OSM-object worden geselecteerd.',
 'At least one OSM feature must be supplied.':
   'Er moet ten minste één OSM-object worden opgegeven.',
 'At least one Overpass server must be provided.':
   'Er moet ten minste één Overpass-server worden opgegeven.',
 'Attempt details:': 'Pogingsdetails:',
 'Automatically add downloaded layers to QGIS':
   'Gedownloade lagen automatisch aan QGIS toevoegen',
 'Background Overpass download started.':
   'Overpass-download op de achtergrond gestart.',
 'Browse': 'Bladeren',
 'Browse…': 'Bladeren…',
 'Buildings': 'Gebouwen',
 'Bus stops': 'Bushaltes',
 'CRS:': 'CRS:',
 'Cache hit:': 'Cache-treffer:',
 'Cache hit: using saved Overpass response ({age} day(s) old).':
   'Cache-treffer: opgeslagen Overpass-antwoord wordt gebruikt ({age} dag(en) oud).',
 'Cache miss:': 'Cache-misser:',
 'Cache miss: could not read saved response ({error}).':
   'Cache-misser: kon opgeslagen antwoord niet lezen ({error}).',
 'Cache miss: query hash does not match the saved response.':
   'Cache-misser: query-hash komt niet overeen met het opgeslagen antwoord.',
 'Cache miss: saved response is incomplete or invalid.':
   'Cache-misser: opgeslagen antwoord is onvolledig of ongeldig.',
 'Cache miss: saved response is older than {days} days.':
   'Cache-misser: opgeslagen antwoord is ouder dan {days} dagen.',
 'Cache miss: saved response uses an unsupported cache format.':
   'Cache-misser: opgeslagen antwoord gebruikt een niet-ondersteund cacheformaat.',
 'Cached Overpass response:': 'Gecachet Overpass-antwoord:',
 'Cancel': 'Annuleren',
 'Cancellation has already been requested.': 'Annulering is al aangevraagd.',
 'Cancellation requested': 'Annulering aangevraagd',
 'Cancellation requested. If an HTTP request is already active, the downloader will stop when that request returns or times out.':
   'Annulering aangevraagd. Als er al een HTTP-verzoek actief is, stopt de downloader wanneer dat verzoek terugkeert of een time-out optreedt.',
 'Cancellation requested; waiting for the current request to finish...':
   'Annulering aangevraagd; wachten tot het huidige verzoek is voltooid…',
 'Cannot draw AOI because the QGIS interface is unavailable.':
   'Kan AOI niet tekenen omdat de QGIS-interface niet beschikbaar is.',
 'Cannot resolve active-layer extent because QGIS is unavailable.':
   'Kan de uitsnede van de actieve laag niet bepalen omdat QGIS niet beschikbaar is.',
 'Cannot resolve current map extent because QGIS is unavailable.':
   'Kan de huidige kaartuitsnede niet bepalen omdat QGIS niet beschikbaar is.',
 'Cannot resolve selected-feature AOI because QGIS is unavailable.':
   'Kan de AOI uit geselecteerde objecten niet bepalen omdat QGIS niet beschikbaar is.',
 'Cannot transform an empty geometry.': 'Kan een lege geometrie niet transformeren.',
 'Capture the current QGIS map canvas extent.':
   'Leg de huidige uitsnede van het QGIS-kaartcanvas vast.',
 'Choose all available levels, or select one or more levels to download (for example, 5–8 or level 5).':
   'Kies alle beschikbare niveaus, of selecteer een of meer niveaus om te downloaden (bijvoorbeeld 5–8 of niveau 5).',
 'Choose an output directory before downloading.':
   'Kies een uitvoermap voordat je gaat downloaden.',
 'City name': 'Stadsnaam',
 'Classifying OSM elements and preparing GeoPackage layers.':
   'OSM-elementen classificeren en GeoPackage-lagen voorbereiden.',
 'Classifying OSM elements and preparing Shapefile outputs.':
   'OSM-elementen classificeren en Shapefile-uitvoer voorbereiden.',
 'Clear all': 'Alles wissen',
 'Clear log': 'Logboek wissen',
 'Clear only the visible log, without changing processing settings.':
   'Wis alleen het zichtbare logboek, zonder de verwerkingsinstellingen te wijzigen.',
 'Clear selected levels so the user can make a narrower selection.':
   'Wis geselecteerde niveaus zodat de gebruiker een nauwere selectie kan maken.',
 'Clear the messages currently shown in the Processing Log.':
   'Wis de berichten die momenteel in het verwerkingslogboek worden weergegeven.',
 'Clear the previous AOI and display guidance for the chosen method.':
   'Wis de vorige AOI en toon begeleiding voor de gekozen methode.',
 'Close': 'Sluiten',
 'Collect optional filename components before exporting OSM data.':
   'Verzamel optionele bestandsnaamonderdelen voordat je OSM-gegevens exporteert.',
 'Compact product header above the scrollable workflow.':
   'Compacte productkop boven de scrollbare werkstroom.',
 'Connection error on server ': 'Verbindingsfout op server ',
 'Continue to Download': 'Doorgaan naar downloaden',
 'Convert a name component into a Windows-safe filename token.':
   'Converteer een naamonderdeel naar een Windows-veilig bestandsnaamtoken.',
 'Convert the drawn rectangle into the standard AOI object.':
   'Converteer de getekende rechthoek naar het standaard AOI-object.',
 'Converting OSM response to GeoPackage...':
   'OSM-antwoord converteren naar GeoPackage…',
 'Converting OSM response to Shapefiles...':
   'OSM-antwoord converteren naar Shapefiles…',
 'Could not combine the selected feature geometries.':
   'Kon de geometrieën van de geselecteerde objecten niet combineren.',
 "Could not create Shapefile staging layer '{layer_name}'.":
   'Kon Shapefile-tussenlaag "{layer_name}" niet aanmaken.',
 'Could not create an empty bus_stops_points layer.':
   'Kon geen lege bus_stops_points-laag aanmaken.',
 "Could not create temporary QGIS layer '{layer_name}'.":
   'Kon tijdelijke QGIS-laag "{layer_name}" niet aanmaken.',
 'Could not create temporary layer for admin_level {admin_level}.':
   'Kon geen tijdelijke laag aanmaken voor admin_level {admin_level}.',
 'Could not create the merged bus_stops_points layer.':
   'Kon de samengevoegde bus_stops_points-laag niet aanmaken.',
 'Could not delete temporary file': 'Kon tijdelijk bestand niet verwijderen',
 "Could not load feature definition '{feature_key}': {error}":
   'Kon objectdefinitie "{feature_key}" niet laden: {error}',
 'Could not merge bus-station centroids into bus-stop points.':
   'Kon de centroïden van busstations niet samenvoegen met bushoudepunten.',
 'Could not overwrite existing output file: {error}':
   'Kon bestaand uitvoerbestand niet overschrijven: {error}',
 'Could not populate Shapefile for admin_level {admin_level}.':
   'Kon Shapefile voor admin_level {admin_level} niet vullen.',
 "Could not populate temporary layer '{layer_name}'.":
   'Kon tijdelijke laag "{layer_name}" niet vullen.',
 'Could not prepare the Overpass query:': 'Kon de Overpass-query niet voorbereiden:',
 "Could not reopen intermediate GeoPackage layer '{layer_name}'.":
   'Kon tussentijdse GeoPackage-laag "{layer_name}" niet opnieuw openen.',
 'Could not restore previous QGIS map tool:':
   'Kon het vorige QGIS-kaartgereedschap niet herstellen:',
 'Could not search for temporary GeoPackages:':
   'Kon niet zoeken naar tijdelijke GeoPackages:',
 'Country name': 'Landnaam',
 'Create one section panel and return it with its body layout.':
   'Maak één sectiepaneel en retourneer het met de bijbehorende inhoudslayout.',
 'Created bus_stops_points from bus-station polygon centroids.':
   'bus_stops_points aangemaakt op basis van centroïden van busstation-polygonen.',
 'Current QGIS map extent': 'Huidige QGIS-kaartuitsnede',
 'Current QGIS map extent resolved.':
   'Huidige QGIS-kaartuitsnede bepaald.',
 'Data © <a href="': 'Gegevens © <a href="',
 'Deleted temporary workspace file:': 'Tijdelijk werkruimtebestand verwijderd:',
 'Details:': 'Details:',
 'Download': 'Downloaden',
 'Download OSM Data': 'OSM-gegevens downloaden',
 'Download OpenStreetMap data for any area and load it straight into QGIS.':
   'Download OpenStreetMap-gegevens voor elk gebied en laad ze rechtstreeks in QGIS.',
 'Download cancelled because existing output files were not approved for overwrite.':
   'Download geannuleerd omdat bestaande uitvoerbestanden niet zijn goedgekeurd voor overschrijving.',
 'Download cancelled before it started.':
   'Download geannuleerd voordat deze begon.',
 'Download cancelled before results were returned.':
   'Download geannuleerd voordat resultaten werden geretourneerd.',
 'Download cancelled before starting.': 'Download geannuleerd voordat deze begon.',
 'Download cancelled in the output-naming dialog.':
   'Download geannuleerd in het dialoogvenster voor uitvoernaamgeving.',
 'Download cancelled.': 'Download geannuleerd.',
 'Download cancelled; existing files preserved.':
   'Download geannuleerd; bestaande bestanden behouden.',
 'Download stopped.': 'Download gestopt.',
 'Download succeeded, but export failed.':
   'Download geslaagd, maar export mislukt.',
 'Downloading OSM data from Overpass...':
   'OSM-gegevens downloaden van Overpass…',
 'Draw AOI': 'AOI tekenen',
 'Draw a rectangle on the QGIS map to define the AOI.':
   'Teken een rechthoek op de QGIS-kaart om de AOI te definiëren.',
 'Draw rectangle on map': 'Rechthoek op kaart tekenen',
 'Draw the AOI rectangle on the QGIS map.':
   'Teken de AOI-rechthoek op de QGIS-kaart.',
 'Drawn AOI validation failed:': 'Validatie van getekende AOI mislukt:',
 'Drawn rectangle': 'Getekende rechthoek',
 'Drawn rectangle AOI captured successfully.':
   'Getekende rechthoek-AOI succesvol vastgelegd.',
 'ERROR:': 'FOUT:',
 'East:': 'Oost:',
 'Enable level checkboxes only when a specific selection is active.':
   'Schakel niveau-selectievakjes alleen in wanneer een specifieke selectie actief is.',
 'Enable only the AOI action button for the selected method.':
   'Schakel alleen de AOI-actieknop in voor de geselecteerde methode.',
 'Enable or disable controls while a download is running.':
   'Schakel besturingselementen in of uit terwijl een download wordt uitgevoerd.',
 'Enter at least one name (City, Country, Region, or AOI).':
   'Voer ten minste één naam in (stad, land, regio of AOI).',
 'Enter one or more name components. Blank fields will be skipped, and the remaining names will be joined with underscores. The selected output format will be retained.':
   'Voer een of meer naamonderdelen in. Lege velden worden overgeslagen en de overige namen worden samengevoegd met underscores. Het geselecteerde uitvoerformaat blijft behouden.',
 'Enter_a_name_to_preview': 'Voer_een_naam_in_voor_voorbeeld',
 'Export cancelled: output name is missing.':
   'Export geannuleerd: uitvoernaam ontbreekt.',
 'Export complete:': 'Export voltooid:',
 'Export the downloaded response and optionally load its layers.':
   'Exporteer het gedownloade antwoord en laad indien gewenst de bijbehorende lagen.',
 'Failed to activate rectangle AOI tool:':
   'Kon rechthoek-AOI-gereedschap niet activeren:',
 'Failed to create AOI.': 'Kon AOI niet aanmaken.',
 'Failed to process drawn rectangle AOI:':
   'Kon getekende rechthoek-AOI niet verwerken:',
 'Failed to resolve active-layer extent.':
   'Kon uitsnede van actieve laag niet bepalen.',
 'Failed to resolve active-layer extent:':
   'Kon uitsnede van actieve laag niet bepalen:',
 'Failed to resolve current QGIS map extent:':
   'Kon huidige QGIS-kaartuitsnede niet bepalen:',
 'Failed to resolve selected-feature AOI.':
   'Kon AOI uit geselecteerde objecten niet bepalen.',
 'Failed to resolve selected-feature AOI:':
   'Kon AOI uit geselecteerde objecten niet bepalen:',
 "Failed to write layer '{layer_name}' to '{output_path}': {error}":
   'Kon laag "{layer_name}" niet naar "{output_path}" schrijven: {error}',
 "Feature '{feature_key}' has no tag definitions.":
   'Object "{feature_key}" heeft geen tagdefinities.',
 'Feature specification  does not expose a tag-filter mapping.':
   'Objectspecificatie biedt geen tag-filtertoewijzing.',
 'Ferry stops': 'Veerboothaltes',
 'Filename preview': 'Voorbeeld van bestandsnaam',
 'Full documentation': 'Volledige documentatie',
 'Generated Overpass query (': 'Gegenereerde Overpass-query (',
 'GeoPackage': 'GeoPackage',
 'GeoPackage layer(s) to QGIS.': 'GeoPackage-la(a)g(en) in QGIS.',
 'GeoPackage saved:': 'GeoPackage opgeslagen:',
 'HTTP error on server ': 'HTTP-fout op server ',
 'HTTP error — ': 'HTTP-fout — ',
 'HTTP {status} error on server {index}/{total}.':
   'HTTP {status}-fout op server {index}/{total}.',
 'Handle a drawing tool deactivation initiated outside this dialog.':
   'Verwerk het deactiveren van een tekenhulpmiddel dat buiten dit dialoogvenster is gestart.',
 'Help': 'Help',
 'Invalid east longitude: {value}': 'Ongeldige oosterlengte: {value}',
 'Invalid north latitude: {value}': 'Ongeldige noorderbreedte: {value}',
 'Invalid response from server ': 'Ongeldig antwoord van server ',
 'Invalid south latitude: {value}': 'Ongeldige zuiderbreedte: {value}',
 'Invalid west longitude: {value}': 'Ongeldige westerlengte: {value}',
 'Keep the numeric readout in step with the progress bar.':
   'Houd de numerieke uitlezing in lijn met de voortgangsbalk.',
 'Land & built environment': 'Land en bebouwde omgeving',
 'Landuse': 'Landgebruik',
 'Language:': 'Taal:',
 'Linear features': 'Lijnobjecten',
 'Load the saved interface language and translate visible UI strings.':
   'Laad de opgeslagen interfacetaal en vertaal zichtbare UI-tekenreeksen.',
 'Local response cache is disabled.': 'Lokale antwoordcache is uitgeschakeld.',
 'Main OSM Data Toolkit window.': 'Hoofdvenster van OSM Data Toolkit.',
 'Manually capture the map extent after the user pans or zooms.':
   'Leg de kaartuitsnede handmatig vast nadat de gebruiker heeft gepand of gezoomd.',
 'Merged bus-station polygon centroids into bus_stops_points.':
   'Centroïden van busstation-polygonen samengevoegd in bus_stops_points.',
 'No Overpass selectors were generated.':
   'Er zijn geen Overpass-selectors gegenereerd.',
 'No active QGIS layer is available.': 'Er is geen actieve QGIS-laag beschikbaar.',
 'No active layer is available.': 'Er is geen actieve laag beschikbaar.',
 'No exportable features matched the selected categories. Try another AOI or select additional OSM feature categories.':
   'Geen exporteerbare objecten gevonden die overeenkomen met de geselecteerde categorieën. Probeer een andere AOI of selecteer extra OSM-objectcategorieën.',
 'No features are selected in the active layer.':
   'Er zijn geen objecten geselecteerd in de actieve laag.',
 'No levels selected. Select at least one level to continue.':
   'Geen niveaus geselecteerd. Selecteer ten minste één niveau om door te gaan.',
 'No selected features found.': 'Geen geselecteerde objecten gevonden.',
 'No valid Area of Interest is available. Select an AOI method and resolve the AOI before downloading.':
   'Er is geen geldig interessegebied beschikbaar. Selecteer een AOI-methode en bepaal de AOI voordat je gaat downloaden.',
 'North:': 'Noord:',
 'Note: {layer_name} has too many tag columns for one Shapefile (DBF size limit); {count} rarely-used columns were left out.':
   'Opmerking: {layer_name} heeft te veel tag-kolommen voor één Shapefile (DBF-groottebeperking); {count} zelden gebruikte kolommen zijn weggelaten.',
 'OSM Data Toolkit': 'OSM Data Toolkit',
 'OSM Data Toolkit initialised.': 'OSM Data Toolkit geïnitialiseerd.',
 'OSM Feature Categories': 'OSM-objectcategorieën',
 'OSM export completed successfully.': 'OSM-export succesvol voltooid.',
 'One or more output files with this name already exist. Do you want to overwrite the matching output files?':
   'Een of meer uitvoerbestanden met deze naam bestaan al. Wil je de overeenkomende uitvoerbestanden overschrijven?',
 'Only the selected levels': 'Alleen de geselecteerde niveaus',
 'Only validated Overpass responses can be cached.':
   'Alleen gevalideerde Overpass-antwoorden kunnen worden gecachet.',
 'Open public spaces': 'Openbare ruimtes',
 'Open the in-plugin help with links to the online documentation.':
   'Open de hulp in de plug-in met links naar de online documentatie.',
 'Output Settings': 'Uitvoerinstellingen',
 'Output directory': 'Uitvoermap',
 'Output directory selected:': 'Uitvoermap geselecteerd:',
 'Output format': 'Uitvoerformaat',
 'Output settings': 'Uitvoerinstellingen',
 'Overpass download cancelled.': 'Overpass-download geannuleerd.',
 'Overpass download completed:': 'Overpass-download voltooid:',
 'Overpass download failed.': 'Overpass-download mislukt.',
 'Overpass download failed:': 'Overpass-download mislukt:',
 'Overpass download running...': 'Overpass-download wordt uitgevoerd…',
 'Overpass download was cancelled by the caller.':
   'Overpass-download is geannuleerd door de aanroeper.',
 'Overpass query must be a non-empty string.':
   'Overpass-query moet een niet-lege tekenreeks zijn.',
 "Overpass response 'elements' field is not a list.":
   'Het veld "elements" in het Overpass-antwoord is geen lijst.',
 "Overpass response does not contain an 'elements' field.":
   'Het Overpass-antwoord bevat geen veld "elements".',
 'Overpass response is not a JSON object.':
   'Overpass-antwoord is geen JSON-object.',
 'Overpass response received successfully:':
   'Overpass-antwoord succesvol ontvangen:',
 'Overpass server ': 'Overpass-server ',
 'Overpass server returned invalid JSON. Response preview: ':
   'Overpass-server retourneerde ongeldige JSON. Voorbeeld van antwoord: ',
 'Overpass servers available:': 'Beschikbare Overpass-servers:',
 'Overpass timeout must be greater than zero.':
   'Overpass-time-out moet groter zijn dan nul.',
 'Plugin version': 'Plug-inversie',
 'Points of interest (POI)': 'Interessepunten (POI)',
 'Prepared {index:,} of {total:,} OSM elements for export...':
   '{index:,} van {total:,} OSM-elementen voorbereid voor export…',
 'Preparing Overpass download...': 'Overpass-download voorbereiden…',
 'Preparing Overpass query.': 'Overpass-query voorbereiden.',
 'Processing Options': 'Verwerkingsopties',
 'Processing log': 'Verwerkingslogboek',
 'Processing messages will appear here...':
   'Verwerkingsberichten verschijnen hier…',
 'Processing options': 'Verwerkingsopties',
 'Public transport & places': 'Openbaar vervoer en plaatsen',
 'QGIS interface object was not detected. Canvas-dependent AOI tools are disabled.':
   'QGIS-interfaceobject is niet gedetecteerd. Canvasafhankelijke AOI-gereedschappen zijn uitgeschakeld.',
 'QGIS map canvas could not be accessed.':
   'Kon geen toegang krijgen tot het QGIS-kaartcanvas.',
 'QGIS map canvas is unavailable.': 'QGIS-kaartcanvas is niet beschikbaar.',
 'Rail stops': 'Spoorweghaltes',
 'Railways': 'Spoorwegen',
 'Read the plugin version from metadata.txt (empty string if absent).':
   'Lees de plug-inversie uit metadata.txt (lege tekenreeks indien afwezig).',
 'Read, validate and store the current QGIS map canvas extent.':
   'Lees, valideer en sla de huidige uitsnede van het QGIS-kaartcanvas op.',
 'Ready.': 'Gereed.',
 'Rectangle AOI drawing tool activated.':
   'Rechthoek-AOI-tekengereedschap geactiveerd.',
 'Rectangle AOI drawing was cancelled.':
   'Het tekenen van de rechthoek-AOI is geannuleerd.',
 'Region name': 'Regionaam',
 'Report an issue': 'Een probleem melden',
 'Request cooperative cancellation of the background worker.':
   'Vraag om coöperatieve annulering van de achtergrondwerker.',
 'Request error on server ': 'Verzoekfout op server ',
 'Restore default GUI settings when the dialog closes.':
   'Herstel de standaard-GUI-instellingen wanneer het dialoogvenster sluit.',
 'Restore the GUI once the background thread has stopped.':
   'Herstel de GUI zodra de achtergrondthread is gestopt.',
 'Restore the QGIS map tool active before rectangle drawing.':
   'Herstel het QGIS-kaartgereedschap dat actief was vóór het tekenen van de rechthoek.',
 'Restore the map tool and reset state before hiding the dialog.':
   'Herstel het kaartgereedschap en reset de status voordat het dialoogvenster wordt verborgen.',
 'Retrying in ': 'Opnieuw proberen over ',
 'Return selected levels, or None when all levels are requested.':
   'Retourneer geselecteerde niveaus, of None wanneer alle niveaus worden aangevraagd.',
 'Return the combined, sanitized filename prefix.':
   'Retourneer het gecombineerde, opgeschoonde bestandsnaamvoorvoegsel.',
 'Return the mapping between feature keys and GUI checkboxes.':
   'Retourneer de toewijzing tussen objectsleutels en GUI-selectievakjes.',
 'Return the selected GUI feature keys.':
   'Retourneer de geselecteerde GUI-objectsleutels.',
 'Roads': 'Wegen',
 'Run a modal dialog on both Qt5 and Qt6.':
   'Voer een modaal dialoogvenster uit op zowel Qt5 als Qt6.',
 'Select Output Directory': 'Uitvoermap selecteren',
 'Select a vector layer with selected features.':
   'Selecteer een vectorlaag met geselecteerde objecten.',
 'Select all': 'Alles selecteren',
 'Select an active QGIS layer.': 'Selecteer een actieve QGIS-laag.',
 'Select at least one OSM feature category before downloading.':
   'Selecteer ten minste één OSM-objectcategorie voordat je gaat downloaden.',
 'Select at least one administrative level, or choose All levels.':
   'Selecteer ten minste één administratief niveau, of kies Alle niveaus.',
 'Select at least one administrative level, or use None to retrieve all levels.':
   'Selecteer ten minste één administratief niveau, of gebruik None om alle niveaus op te halen.',
 'Select levels 0–15 and switch to specific-level mode.':
   'Selecteer niveaus 0–15 en schakel over naar de modus voor specifieke niveaus.',
 'Select one or more features in the active layer.':
   'Selecteer een of meer objecten in de actieve laag.',
 'Select output directory...': 'Uitvoermap selecteren…',
 'Selected administrative levels:': 'Geselecteerde administratieve niveaus:',
 'Selected feature IDs:': 'ID\'s van geselecteerde objecten:',
 'Selected feature(s) in active layer':
   'Geselecteerde object(en) in actieve laag',
 'Selected features (': 'Geselecteerde objecten (',
 'Selected-feature AOI captured successfully (':
   'AOI uit geselecteerde objecten succesvol vastgelegd (',
 'Selected-feature AOI captured successfully.':
   'AOI uit geselecteerde objecten succesvol vastgelegd.',
 'Selected-feature AOI is invalid.':
   'AOI uit geselecteerde objecten is ongeldig.',
 'Selected-feature AOI requires a vector layer.':
   'AOI uit geselecteerde objecten vereist een vectorlaag.',
 'Selected-feature AOI validation failed:':
   'Validatie van AOI uit geselecteerde objecten mislukt:',
 'Sending query to Overpass...': 'Query naar Overpass verzenden…',
 'Server ': 'Server ',
 'Shapefile': 'Shapefile',
 'Shapefile export completed in:': 'Shapefile-export voltooid in:',
 'Shapefile field names shortened for':
   'Shapefile-veldnamen ingekort voor',
 'Shapefile layer(s) to QGIS.': 'Shapefile-la(a)g(en) in QGIS.',
 'Short in-plugin help with links to the full online documentation.':
   'Korte hulp in de plug-in met links naar de volledige online documentatie.',
 'Show AOI coordinates and source CRS in the dialog.':
   'Toon AOI-coördinaten en bron-CRS in het dialoogvenster.',
 'Show a concise description of the active administrative filter.':
   'Toon een beknopte beschrijving van het actieve administratieve filter.',
 'Source CRS is invalid.': 'Bron-CRS is ongeldig.',
 'South latitude cannot be greater than north latitude.':
   'Zuiderbreedte kan niet groter zijn dan noorderbreedte.',
 'South:': 'Zuid:',
 'Starting Overpass download...': 'Overpass-download starten…',
 'Supporting copy: muted, wrapped and visually quiet.':
   'Ondersteunende tekst: gedempt, afgebroken en visueel rustig.',
 "Tag '{tag}' contains an empty value list.":
   'Tag "{tag}" bevat een lege waardelijst.',
 'Temporary workspace cleanup complete:':
   'Opruimen van tijdelijke werkruimte voltooid:',
 'Temporary workspace cleanup complete: no matching files found.':
   'Opruimen van tijdelijke werkruimte voltooid: geen overeenkomende bestanden gevonden.',
 'Temporary-file cleanup skipped: workspace directory is invalid.':
   'Opruimen van tijdelijke bestanden overgeslagen: werkruimtemap is ongeldig.',
 'The OSM download succeeded, but the output could not be created.':
   'De OSM-download is geslaagd, maar de uitvoer kon niet worden aangemaakt.',
 "The Overpass response must be a JSON object with an 'elements' list.":
   'Het Overpass-antwoord moet een JSON-object zijn met een lijst "elements".',
 'The QGIS map canvas CRS is invalid.':
   'De CRS van het QGIS-kaartcanvas is ongeldig.',
 'The active layer CRS is invalid.': 'De CRS van de actieve laag is ongeldig.',
 'The active layer extent is empty.': 'De uitsnede van de actieve laag is leeg.',
 'The active layer must be a vector layer.':
   'De actieve laag moet een vectorlaag zijn.',
 'The combined name is too long. Shorten one or more components.':
   'De gecombineerde naam is te lang. Verkort een of meer onderdelen.',
 'The combined selected-feature geometry is empty.':
   'De gecombineerde geometrie van de geselecteerde objecten is leeg.',
 'The current AOI is invalid:': 'De huidige AOI is ongeldig:',
 'The current QGIS map extent is empty.':
   'De huidige QGIS-kaartuitsnede is leeg.',
 'The dialog cannot close while a download thread is running. Cancellation has been requested; close the dialog after it stops.':
   'Het dialoogvenster kan niet sluiten terwijl een downloadthread wordt uitgevoerd. Annulering is aangevraagd; sluit het dialoogvenster nadat deze is gestopt.',
 'The download completed, but no confirmed output name was available.':
   'De download is voltooid, maar er was geen bevestigde uitvoernaam beschikbaar.',
 "The exported Shapefile '{path}' could not be opened in QGIS.":
   'De geëxporteerde Shapefile "{path}" kon niet in QGIS worden geopend.',
 "The exported layer '{layer_name}' could not be opened in QGIS.":
   'De geëxporteerde laag "{layer_name}" kon niet in QGIS worden geopend.',
 'The output name does not contain any valid filename characters.':
   'De uitvoernaam bevat geen geldige bestandsnaamtekens.',
 'The output name is empty after filename validation.':
   'De uitvoernaam is leeg na validatie van de bestandsnaam.',
 'The selected features contain no valid geometry.':
   'De geselecteerde objecten bevatten geen geldige geometrie.',
 'The selected output directory does not exist. Choose an existing folder.':
   'De geselecteerde uitvoermap bestaat niet. Kies een bestaande map.',
 'There is no active download to cancel.':
   'Er is geen actieve download om te annuleren.',
 'Timeout on server ': 'Time-out op server ',
 'Translate widget labels while preserving each original English string.':
   'Vertaal widgetlabels met behoud van elke oorspronkelijke Engelse tekenreeks.',
 'Trying Overpass server ': 'Overpass-server proberen: ',
 'Unable to start AOI drawing:': 'Kan AOI-tekenen niet starten:',
 'Unclassified OSM elements not written to feature layers:':
   'Niet-geclassificeerde OSM-elementen die niet naar objectlagen zijn geschreven:',
 'Unsupported geometry family: {geometry_family}':
   'Niet-ondersteunde geometriefamilie: {geometry_family}',
 "Unsupported geometry type '{geometry_type}' for feature '{feature_key}'.":
   'Niet-ondersteund geometrietype "{geometry_type}" voor object "{feature_key}".',
 'Unsupported geometry type for Shapefile export: {geometry_type}':
   'Niet-ondersteund geometrietype voor Shapefile-export: {geometry_type}',
 "Unsupported match mode '{mode}' for feature '{feature_key}'.":
   'Niet-ondersteunde overeenkomstenmodus "{mode}" voor object "{feature_key}".',
 'Unsupported output format:': 'Niet-ondersteund uitvoerformaat:',
 "Unsupported tag value type for '{feature_key}': {value_type}":
   'Niet-ondersteund tag-waardetype voor "{feature_key}": {value_type}',
 'Update Current QGIS Map Extent':
   'Huidige QGIS-kaartuitsnede bijwerken',
 'Update the "N selected" count next to the category heading.':
   'Werk de teller "N geselecteerd" naast de categorietitel bij.',
 'Update the filename preview as the user edits the components.':
   'Werk het voorbeeld van de bestandsnaam bij terwijl de gebruiker de onderdelen bewerkt.',
 'Use Layer Extent': 'Laaguitsnede gebruiken',
 'Use Selected Features': 'Geselecteerde objecten gebruiken',
 'Use local cache where available':
   'Gebruik lokale cache waar beschikbaar',
 'Use selected features in the active vector layer as the AOI.':
   'Gebruik geselecteerde objecten in de actieve vectorlaag als de AOI.',
 'Use the full extent of the active QGIS layer as the AOI.':
   'Gebruik de volledige uitsnede van de actieve QGIS-laag als de AOI.',
 'Use the full extent of the active QGIS layer.':
   'Gebruik de volledige uitsnede van de actieve QGIS-laag.',
 'Use the selected features of the active vector layer as the AOI.':
   'Gebruik de geselecteerde objecten van de actieve vectorlaag als de AOI.',
 'Using cached data; no Overpass network request was needed.':
   'Gecachte gegevens worden gebruikt; er was geen Overpass-netwerkverzoek nodig.',
 'Validate filename and any explicitly selected admin levels.':
   'Valideer de bestandsnaam en eventuele expliciet geselecteerde admin-niveaus.',
 'Validate inputs and start the background Overpass download.':
   'Valideer invoer en start de Overpass-download op de achtergrond.',
 'WGS84 AOI bbox: south=': 'WGS84 AOI-begrenzingsbox: zuid=',
 'WGS84 AOI geometry is not available.':
   'WGS84 AOI-geometrie is niet beschikbaar.',
 'Warning: download succeeded, but the response could not be cached:':
   'Waarschuwing: download geslaagd, maar het antwoord kon niet worden gecachet:',
 'Waterways': 'Waterwegen',
 'West longitude cannot be greater than east longitude.':
   'Westerlengte kan niet groter zijn dan oosterlengte.',
 'West:': 'West:',
 'Writing Shapefile {layer_index}/{total}: {layer_name}...':
   'Shapefile {layer_index}/{total} schrijven: {layer_name}…',
 'Writing layer {layer_index}/{total}: {layer_name} ({count:,} features)...':
   'Laag {layer_index}/{total} schrijven: {layer_name} ({count:,} objecten)…',
 'attempt ': 'poging ',
 'characters).': 'tekens).',
 'connection error — ': 'verbindingsfout — ',
 'e.g. CBD': 'bijv. CBD',
 'e.g. Kenya': 'bijv. Kenia',
 'e.g. Nairobi': 'bijv. Nairobi',
 'e.g. NairobiCounty': 'bijv. NairobiCounty',
 'elements (': 'elementen (',
 'export failed:': 'export mislukt:',
 'feature records).': 'objectrecords).',
 'feature(s)).': 'object(en)).',
 'features written.': 'objecten geschreven.',
 'file(s) deleted.': 'bestand(en) verwijderd.',
 'relation geometry assignment(s); relation-member geometry assembly is not implemented yet.':
   'relatiegeometrietoewijzing(en); samenstelling van relatie-lidgeometrie is nog niet geïmplementeerd.',
 'relations).': 'relaties).',
 'response_data must be a dictionary.':
   'response_data moet een woordenboek zijn.',
 "response_data['elements'] must be a list.":
   "response_data['elements'] moet een lijst zijn.",
 'temporary file(s) could not be deleted. They may still be in use by QGIS or another process.':
   'tijdelijke bestand(en) konden niet worden verwijderd. Ze zijn mogelijk nog in gebruik door QGIS of een ander proces.',
 'timeout — ': 'time-out — ',
 '{output_format} export failed: {error}':
   '{output_format}-export mislukt: {error}',
 '— Confirm Overwrite': '— Overschrijven bevestigen',
 '— Export Error': '— Exportfout',
 '— Help': '— Help',
 '— Output Naming': '— Naamgeving van uitvoer',
}