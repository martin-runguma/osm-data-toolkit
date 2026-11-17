"""Norwegian Bokmål (nb) translation pack for the OSM Data Toolkit plugin.
Keys remain the English source strings; preserve placeholders and HTML."""
TEXT = {
 '\n<h3>Quick start</h3>\n<ol>\n  <li><b>Choose an area.</b> Use the current map extent, draw a rectangle\n      on the map, or use the bounding box of selected features or a\n      layer\'s extent.</li>\n  <li><b>Tick the OSM categories</b> you need (POI, stops, roads,\n      buildings, boundaries, landuse, ...).</li>\n  <li><b>Choose an output format and folder</b>, then click\n      <b>Download OSM Data</b>.</li>\n</ol>\n\n<h3>Good to know</h3>\n<ul>\n  <li><b>GeoPackage is recommended.</b> A Shapefile cannot hold very many\n      attribute columns, so on large areas some rarely used tag columns\n      may be left out (the log tells you when this happens).</li>\n  <li><b>Keep the area focused.</b> Very large areas produce huge Overpass\n      responses and can be slow or rejected by the public servers.</li>\n  <li><b>The cache</b> lets repeat downloads of the same query reuse\n      earlier results.</li>\n  <li><b>"Unclassified OSM elements"</b> in the log is informational: they\n      are mostly untagged vertices of lines and polygons that do not belong\n      to any selected category.</li>\n</ul>\n\n<p>Data &copy; OpenStreetMap contributors, available under the\n<a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a>.</p>\n<p><i>This plugin is not endorsed by or affiliated with the\nOpenStreetMap Foundation.</i></p>\n':
 '\n<h3>Hurtigstart</h3>\n<ol>\n  <li><b>Velg et område.</b> Bruk gjeldende kartutstrekning, tegn et\n      rektangel på kartet, eller bruk avgrensningsboksen til valgte\n      objekter eller et lags utstrekning.</li>\n  <li><b>Kryss av OSM-kategoriene</b> du trenger (POI, holdeplasser, veier,\n      bygninger, grenser, arealbruk, ...).</li>\n  <li><b>Velg utdataformat og mappe</b>, og klikk deretter\n      <b>Last ned OSM-data</b>.</li>\n</ol>\n\n<h3>Verdt å vite</h3>\n<ul>\n  <li><b>GeoPackage anbefales.</b> En Shapefile kan ikke inneholde særlig\n      mange attributtkolonner, så på store områder kan noen sjeldent brukte\n      tagg-kolonner utelates (loggen forteller deg når dette skjer).</li>\n  <li><b>Hold området fokusert.</b> Svært store områder gir enorme Overpass-\n      svar og kan være trege eller avvises av de offentlige serverne.</li>\n  <li><b>Hurtigbufferen</b> lar gjentatte nedlastinger av samme spørring\n      gjenbruke tidligere resultater.</li>\n  <li><b>"Uklassifiserte OSM-elementer"</b> i loggen er informativt: de\n      er stort sett umerkede knutepunkter i linjer og polygoner som ikke\n      tilhører noen valgt kategori.</li>\n</ul>\n\n<p>Data &copy; OpenStreetMap-bidragsytere, tilgjengelig under\n<a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a>.</p>\n<p><i>Denne utvidelsen er ikke godkjent av eller tilknyttet\nOpenStreetMap Foundation.</i></p>\n',
 ' responded successfully.': ' svarte vellykket.',
 ' seconds...': ' sekunder…',
 '" style="color:#0B5E8E; text-decoration:none;">OpenStreetMap contributors</a> (ODbL)':
   '" style="color:#0B5E8E; text-decoration:none;">OpenStreetMap-bidragsytere</a> (ODbL)',
 ', east=': ', øst=',
 ', north=': ', nord=',
 ', west=': ', vest=',
 '0 selected': '0 valgt',
 '<p>Plugin version': '<p>Utvidelsesversjon',
 'A download is already running.': 'En nedlasting kjører allerede.',
 'A labelled column of feature checkboxes.': 'En merket kolonne med avkrysningsbokser for objekter.',
 'AOI drawing cancelled.': 'Tegning av AOI avbrutt.',
 'AOI geometry is empty.': 'AOI-geometrien er tom.',
 'AOI geometry is missing.': 'AOI-geometrien mangler.',
 'AOI name': 'AOI-navn',
 'AOI rectangle captured successfully.': 'AOI-rektangelet ble registrert.',
 'AOI source CRS is invalid.': 'AOI-kilde-CRS er ugyldig.',
 'AOI validation failed:': 'AOI-validering mislyktes:',
 'AOI:': 'AOI:',
 'AOI: QGIS interface is not available.': 'AOI: QGIS-grensesnittet er ikke tilgjengelig.',
 "AOI: click 'Draw AOI', then drag a rectangle on the QGIS map.":
   'AOI: klikk «Tegn AOI», og dra deretter et rektangel på QGIS-kartet.',
 "AOI: click 'Use Layer Extent' to use the full extent of the active QGIS layer.":
   'AOI: klikk «Bruk lagutstrekning» for å bruke hele utstrekningen til det aktive QGIS-laget.',
 'AOI: click and drag on the QGIS map.': 'AOI: klikk og dra på QGIS-kartet.',
 'AOI: failed to resolve active layer extent': 'AOI: kunne ikke fastslå utstrekningen til det aktive laget',
 'AOI: failed to resolve selected features': 'AOI: kunne ikke fastslå valgte objekter',
 'AOI: invalid': 'AOI: ugyldig',
 'AOI: no active QGIS layer.': 'AOI: ingen aktivt QGIS-lag.',
 'AOI: no feature(s) selected in the active layer.': 'AOI: ingen objekter valgt i det aktive laget.',
 'AOI: not yet resolved': 'AOI: ennå ikke fastslått',
 "AOI: select feature(s) in the active QGIS layer, then click 'Use Selected Features'.":
   'AOI: velg objekter i det aktive QGIS-laget, og klikk deretter «Bruk valgte objekter».',
 'AOI: the active layer is not a vector layer.': 'AOI: det aktive laget er ikke et vektorlag.',
 'AOI: unable to create': 'AOI: kan ikke opprette',
 'AOI: unable to resolve': 'AOI: kan ikke fastslå',
 'Activate the interactive rectangle AOI map tool.': 'Aktiver det interaktive rektangel-AOI-kartverktøyet.',
 'Active layer extent': 'Utstrekning for aktivt lag',
 'Active-layer extent AOI is invalid.': 'AOI fra utstrekningen til det aktive laget er ugyldig.',
 'Active-layer extent captured successfully.': 'Utstrekningen til det aktive laget ble registrert.',
 'Active-layer extent validation failed:': 'Validering av utstrekningen til det aktive laget mislyktes:',
 'Administrative boundaries': 'Administrative grenser',
 'Administrative boundary filter: all levels (no admin_level filter).':
   'Filter for administrative grenser: alle nivåer (ingen admin_level-filter).',
 'Administrative boundary levels': 'Nivåer for administrative grenser',
 'Administrative boundary levels:': 'Nivåer for administrative grenser:',
 'Administrative levels must be an integer, a numeric string, a sequence of levels, or None.':
   'Administrative nivåer må være et heltall, en numerisk streng, en sekvens av nivåer eller None.',
 'All OSM feature categories cleared.': 'Alle OSM-objektkategorier er fjernet.',
 'All OSM feature categories selected.': 'Alle OSM-objektkategorier er valgt.',
 'All Overpass server URLs must be non-empty strings.':
   'Alle Overpass-server-URL-er må være ikke-tomme strenger.',
 'All Overpass servers and retry attempts failed.':
   'Alle Overpass-servere og nye forsøk mislyktes.',
 'All administrative levels will be included.': 'Alle administrative nivåer vil bli inkludert.',
 'All administrative levels will be included; no admin_level filter will be added to the query.':
   'Alle administrative nivåer vil bli inkludert; ingen admin_level-filter legges til i spørringen.',
 'All attempts failed for server ': 'Alle forsøk mislyktes for server ',
 'All levels (0–15; no admin_level filter)': 'Alle nivåer (0–15; ingen admin_level-filter)',
 'An existing output directory is required for Shapefile export.':
   'En eksisterende utdatamappe kreves for Shapefile-eksport.',
 'An output GeoPackage path is required.': 'En utdata-GeoPackage-sti kreves.',
 'An output name is required for Shapefile export.':
   'Et utdatanavn kreves for Shapefile-eksport.',
 'Append a timestamped message to the processing log.':
   'Legg til en tidsstemplet melding i behandlingsloggen.',
 'Append an exported feature count to the processing log.':
   'Legg til antall eksporterte objekter i behandlingsloggen.',
 'Area of Interest': 'Interesseområde',
 'At least one OSM feature must be selected.': 'Minst ett OSM-objekt må velges.',
 'At least one OSM feature must be supplied.': 'Minst ett OSM-objekt må angis.',
 'At least one Overpass server must be provided.': 'Minst én Overpass-server må angis.',
 'Attempt details:': 'Forsøksdetaljer:',
 'Automatically add downloaded layers to QGIS': 'Legg nedlastede lag automatisk til i QGIS',
 'Background Overpass download started.': 'Overpass-nedlasting i bakgrunnen startet.',
 'Browse': 'Bla gjennom',
 'Browse…': 'Bla gjennom…',
 'Buildings': 'Bygninger',
 'Bus stops': 'Bussholdeplasser',
 'CRS:': 'CRS:',
 'Cache hit:': 'Hurtigbuffer-treff:',
 'Cache hit: using saved Overpass response ({age} day(s) old).':
   'Hurtigbuffer-treff: bruker lagret Overpass-svar ({age} dag(er) gammelt).',
 'Cache miss:': 'Hurtigbuffer-bom:',
 'Cache miss: could not read saved response ({error}).':
   'Hurtigbuffer-bom: kunne ikke lese lagret svar ({error}).',
 'Cache miss: query hash does not match the saved response.':
   'Hurtigbuffer-bom: spørrings-hashen samsvarer ikke med det lagrede svaret.',
 'Cache miss: saved response is incomplete or invalid.':
   'Hurtigbuffer-bom: lagret svar er ufullstendig eller ugyldig.',
 'Cache miss: saved response is older than {days} days.':
   'Hurtigbuffer-bom: lagret svar er eldre enn {days} dager.',
 'Cache miss: saved response uses an unsupported cache format.':
   'Hurtigbuffer-bom: lagret svar bruker et ikke-støttet hurtigbufferformat.',
 'Cached Overpass response:': 'Bufret Overpass-svar:',
 'Cancel': 'Avbryt',
 'Cancellation has already been requested.': 'Avbrytelse er allerede forespurt.',
 'Cancellation requested': 'Avbrytelse forespurt',
 'Cancellation requested. If an HTTP request is already active, the downloader will stop when that request returns or times out.':
   'Avbrytelse forespurt. Hvis en HTTP-forespørsel allerede er aktiv, vil nedlasteren stoppe når den forespørselen returnerer eller tidsavbrytes.',
 'Cancellation requested; waiting for the current request to finish...':
   'Avbrytelse forespurt; venter på at gjeldende forespørsel skal fullføres…',
 'Cannot draw AOI because the QGIS interface is unavailable.':
   'Kan ikke tegne AOI fordi QGIS-grensesnittet ikke er tilgjengelig.',
 'Cannot resolve active-layer extent because QGIS is unavailable.':
   'Kan ikke fastslå utstrekningen til det aktive laget fordi QGIS ikke er tilgjengelig.',
 'Cannot resolve current map extent because QGIS is unavailable.':
   'Kan ikke fastslå gjeldende kartutstrekning fordi QGIS ikke er tilgjengelig.',
 'Cannot resolve selected-feature AOI because QGIS is unavailable.':
   'Kan ikke fastslå AOI for valgte objekter fordi QGIS ikke er tilgjengelig.',
 'Cannot transform an empty geometry.': 'Kan ikke transformere en tom geometri.',
 'Capture the current QGIS map canvas extent.': 'Registrer gjeldende utstrekning for QGIS-kartlerretet.',
 'Choose all available levels, or select one or more levels to download (for example, 5–8 or level 5).':
   'Velg alle tilgjengelige nivåer, eller velg ett eller flere nivåer å laste ned (for eksempel 5–8 eller nivå 5).',
 'Choose an output directory before downloading.':
   'Velg en utdatamappe før du laster ned.',
 'City name': 'Bynavn',
 'Classifying OSM elements and preparing GeoPackage layers.':
   'Klassifiserer OSM-elementer og forbereder GeoPackage-lag.',
 'Classifying OSM elements and preparing Shapefile outputs.':
   'Klassifiserer OSM-elementer og forbereder Shapefile-utdata.',
 'Clear all': 'Tøm alt',
 'Clear log': 'Tøm logg',
 'Clear only the visible log, without changing processing settings.':
   'Tøm bare den synlige loggen, uten å endre behandlingsinnstillingene.',
 'Clear selected levels so the user can make a narrower selection.':
   'Fjern valgte nivåer slik at brukeren kan gjøre et snevrere valg.',
 'Clear the messages currently shown in the Processing Log.':
   'Fjern meldingene som vises i behandlingsloggen.',
 'Clear the previous AOI and display guidance for the chosen method.':
   'Fjern forrige AOI og vis veiledning for den valgte metoden.',
 'Close': 'Lukk',
 'Collect optional filename components before exporting OSM data.':
   'Samle valgfrie filnavnkomponenter før du eksporterer OSM-data.',
 'Compact product header above the scrollable workflow.':
   'Kompakt produktoverskrift over den rullbare arbeidsflyten.',
 'Connection error on server ': 'Tilkoblingsfeil på server ',
 'Continue to Download': 'Fortsett til nedlasting',
 'Convert a name component into a Windows-safe filename token.':
   'Konverter en navnekomponent til et Windows-trygt filnavn-token.',
 'Convert the drawn rectangle into the standard AOI object.':
   'Konverter det tegnede rektangelet til standard AOI-objektet.',
 'Converting OSM response to GeoPackage...': 'Konverterer OSM-svar til GeoPackage…',
 'Converting OSM response to Shapefiles...': 'Konverterer OSM-svar til Shapefiles…',
 'Could not combine the selected feature geometries.':
   'Kunne ikke kombinere geometriene til de valgte objektene.',
 "Could not create Shapefile staging layer '{layer_name}'.":
   'Kunne ikke opprette Shapefile-mellomlag «{layer_name}».',
 'Could not create an empty bus_stops_points layer.':
   'Kunne ikke opprette et tomt bus_stops_points-lag.',
 "Could not create temporary QGIS layer '{layer_name}'.":
   'Kunne ikke opprette midlertidig QGIS-lag «{layer_name}».',
 'Could not create temporary layer for admin_level {admin_level}.':
   'Kunne ikke opprette midlertidig lag for admin_level {admin_level}.',
 'Could not create the merged bus_stops_points layer.':
   'Kunne ikke opprette det sammenslåtte bus_stops_points-laget.',
 'Could not delete temporary file': 'Kunne ikke slette midlertidig fil',
 "Could not load feature definition '{feature_key}': {error}":
   'Kunne ikke laste objektdefinisjonen «{feature_key}»: {error}',
 'Could not merge bus-station centroids into bus-stop points.':
   'Kunne ikke slå sammen busstasjons-sentroidene til bussholdeplasspunkter.',
 'Could not overwrite existing output file: {error}':
   'Kunne ikke overskrive eksisterende utdatafil: {error}',
 'Could not populate Shapefile for admin_level {admin_level}.':
   'Kunne ikke fylle Shapefile for admin_level {admin_level}.',
 "Could not populate temporary layer '{layer_name}'.":
   'Kunne ikke fylle det midlertidige laget «{layer_name}».',
 'Could not prepare the Overpass query:': 'Kunne ikke forberede Overpass-spørringen:',
 "Could not reopen intermediate GeoPackage layer '{layer_name}'.":
   'Kunne ikke gjenåpne mellomliggende GeoPackage-lag «{layer_name}».',
 'Could not restore previous QGIS map tool:':
   'Kunne ikke gjenopprette forrige QGIS-kartverktøy:',
 'Could not search for temporary GeoPackages:':
   'Kunne ikke søke etter midlertidige GeoPackages:',
 'Country name': 'Landnavn',
 'Create one section panel and return it with its body layout.':
   'Opprett ett seksjonspanel og returner det med innholdsoppsettet.',
 'Created bus_stops_points from bus-station polygon centroids.':
   'Opprettet bus_stops_points fra busstasjons-polygonsentroidene.',
 'Current QGIS map extent': 'Gjeldende QGIS-kartutstrekning',
 'Current QGIS map extent resolved.': 'Gjeldende QGIS-kartutstrekning er fastslått.',
 'Data © <a href="': 'Data © <a href="',
 'Deleted temporary workspace file:': 'Slettet midlertidig arbeidsområdefil:',
 'Details:': 'Detaljer:',
 'Download': 'Last ned',
 'Download OSM Data': 'Last ned OSM-data',
 'Download OpenStreetMap data for any area and load it straight into QGIS.':
   'Last ned OpenStreetMap-data for et hvilket som helst område og last dem rett inn i QGIS.',
 'Download cancelled because existing output files were not approved for overwrite.':
   'Nedlasting avbrutt fordi eksisterende utdatafiler ikke ble godkjent for overskriving.',
 'Download cancelled before it started.': 'Nedlasting avbrutt før den startet.',
 'Download cancelled before results were returned.':
   'Nedlasting avbrutt før resultatene ble returnert.',
 'Download cancelled before starting.': 'Nedlasting avbrutt før start.',
 'Download cancelled in the output-naming dialog.':
   'Nedlasting avbrutt i dialogen for utdatanavn.',
 'Download cancelled.': 'Nedlasting avbrutt.',
 'Download cancelled; existing files preserved.':
   'Nedlasting avbrutt; eksisterende filer er bevart.',
 'Download stopped.': 'Nedlasting stoppet.',
 'Download succeeded, but export failed.': 'Nedlastingen lyktes, men eksporten mislyktes.',
 'Downloading OSM data from Overpass...': 'Laster ned OSM-data fra Overpass…',
 'Draw AOI': 'Tegn AOI',
 'Draw a rectangle on the QGIS map to define the AOI.':
   'Tegn et rektangel på QGIS-kartet for å definere AOI.',
 'Draw rectangle on map': 'Tegn rektangel på kartet',
 'Draw the AOI rectangle on the QGIS map.':
   'Tegn AOI-rektangelet på QGIS-kartet.',
 'Drawn AOI validation failed:': 'Validering av tegnet AOI mislyktes:',
 'Drawn rectangle': 'Tegnet rektangel',
 'Drawn rectangle AOI captured successfully.':
   'Det tegnede rektangel-AOI-et ble registrert.',
 'ERROR:': 'FEIL:',
 'East:': 'Øst:',
 'Enable level checkboxes only when a specific selection is active.':
   'Aktiver avkrysningsboksene for nivå bare når et spesifikt valg er aktivt.',
 'Enable only the AOI action button for the selected method.':
   'Aktiver bare AOI-handlingsknappen for den valgte metoden.',
 'Enable or disable controls while a download is running.':
   'Aktiver eller deaktiver kontroller mens en nedlasting kjører.',
 'Enter at least one name (City, Country, Region, or AOI).':
   'Skriv inn minst ett navn (by, land, region eller AOI).',
 'Enter one or more name components. Blank fields will be skipped, and the remaining names will be joined with underscores. The selected output format will be retained.':
   'Skriv inn én eller flere navnekomponenter. Tomme felt hoppes over, og de gjenværende navnene settes sammen med understreker. Det valgte utdataformatet beholdes.',
 'Enter_a_name_to_preview': 'Skriv_inn_et_navn_for_forhåndsvisning',
 'Export cancelled: output name is missing.': 'Eksport avbrutt: utdatanavnet mangler.',
 'Export complete:': 'Eksport fullført:',
 'Export the downloaded response and optionally load its layers.':
   'Eksporter det nedlastede svaret og last eventuelt inn lagene.',
 'Failed to activate rectangle AOI tool:':
   'Kunne ikke aktivere rektangel-AOI-verktøyet:',
 'Failed to create AOI.': 'Kunne ikke opprette AOI.',
 'Failed to process drawn rectangle AOI:':
   'Kunne ikke behandle tegnet rektangel-AOI:',
 'Failed to resolve active-layer extent.':
   'Kunne ikke fastslå utstrekningen til det aktive laget.',
 'Failed to resolve active-layer extent:':
   'Kunne ikke fastslå utstrekningen til det aktive laget:',
 'Failed to resolve current QGIS map extent:':
   'Kunne ikke fastslå gjeldende QGIS-kartutstrekning:',
 'Failed to resolve selected-feature AOI.':
   'Kunne ikke fastslå AOI for valgte objekter.',
 'Failed to resolve selected-feature AOI:':
   'Kunne ikke fastslå AOI for valgte objekter:',
 "Failed to write layer '{layer_name}' to '{output_path}': {error}":
   'Kunne ikke skrive laget «{layer_name}» til «{output_path}»: {error}',
 "Feature '{feature_key}' has no tag definitions.":
   'Objektet «{feature_key}» har ingen taggdefinisjoner.',
 'Feature specification  does not expose a tag-filter mapping.':
   'Objektspesifikasjonen eksponerer ikke en tagg-filtertilordning.',
 'Ferry stops': 'Ferjeholdeplasser',
 'Filename preview': 'Forhåndsvisning av filnavn',
 'Full documentation': 'Fullstendig dokumentasjon',
 'Generated Overpass query (': 'Generert Overpass-spørring (',
 'GeoPackage': 'GeoPackage',
 'GeoPackage layer(s) to QGIS.': 'GeoPackage-lag i QGIS.',
 'GeoPackage saved:': 'GeoPackage lagret:',
 'HTTP error on server ': 'HTTP-feil på server ',
 'HTTP error — ': 'HTTP-feil — ',
 'HTTP {status} error on server {index}/{total}.':
   'HTTP {status}-feil på server {index}/{total}.',
 'Handle a drawing tool deactivation initiated outside this dialog.':
   'Håndter deaktivering av et tegneverktøy som startes utenfor denne dialogen.',
 'Help': 'Hjelp',
 'Invalid east longitude: {value}': 'Ugyldig østlig lengdegrad: {value}',
 'Invalid north latitude: {value}': 'Ugyldig nordlig breddegrad: {value}',
 'Invalid response from server ': 'Ugyldig svar fra server ',
 'Invalid south latitude: {value}': 'Ugyldig sørlig breddegrad: {value}',
 'Invalid west longitude: {value}': 'Ugyldig vestlig lengdegrad: {value}',
 'Keep the numeric readout in step with the progress bar.':
   'Hold den numeriske visningen i takt med fremdriftslinjen.',
 'Land & built environment': 'Land og bygd miljø',
 'Landuse': 'Arealbruk',
 'Language:': 'Språk:',
 'Linear features': 'Lineære objekter',
 'Load the saved interface language and translate visible UI strings.':
   'Last inn det lagrede grensesnittspråket og oversett synlige UI-strenger.',
 'Local response cache is disabled.': 'Lokal svarshurtigbuffer er deaktivert.',
 'Main OSM Data Toolkit window.': 'Hovedvinduet for OSM Data Toolkit.',
 'Manually capture the map extent after the user pans or zooms.':
   'Registrer kartutstrekningen manuelt etter at brukeren panorerer eller zoomer.',
 'Merged bus-station polygon centroids into bus_stops_points.':
   'Slått sammen busstasjons-polygonsentroidene til bus_stops_points.',
 'No Overpass selectors were generated.': 'Ingen Overpass-velgere ble generert.',
 'No active QGIS layer is available.': 'Ingen aktivt QGIS-lag er tilgjengelig.',
 'No active layer is available.': 'Ingen aktivt lag er tilgjengelig.',
 'No exportable features matched the selected categories. Try another AOI or select additional OSM feature categories.':
   'Ingen eksporterbare objekter samsvarte med de valgte kategoriene. Prøv et annet AOI eller velg flere OSM-objektkategorier.',
 'No features are selected in the active layer.': 'Ingen objekter er valgt i det aktive laget.',
 'No levels selected. Select at least one level to continue.':
   'Ingen nivåer valgt. Velg minst ett nivå for å fortsette.',
 'No selected features found.': 'Ingen valgte objekter funnet.',
 'No valid Area of Interest is available. Select an AOI method and resolve the AOI before downloading.':
   'Ingen gyldig interesseområde er tilgjengelig. Velg en AOI-metode og fastslå AOI før nedlasting.',
 'North:': 'Nord:',
 'Note: {layer_name} has too many tag columns for one Shapefile (DBF size limit); {count} rarely-used columns were left out.':
   'Merk: {layer_name} har for mange tagg-kolonner for én Shapefile (DBF-størrelsesgrense); {count} sjeldent brukte kolonner ble utelatt.',
 'OSM Data Toolkit': 'OSM Data Toolkit',
 'OSM Data Toolkit initialised.': 'OSM Data Toolkit er initialisert.',
 'OSM Feature Categories': 'OSM-objektkategorier',
 'OSM export completed successfully.': 'OSM-eksporten ble fullført.',
 'One or more output files with this name already exist. Do you want to overwrite the matching output files?':
   'Én eller flere utdatafiler med dette navnet finnes allerede. Vil du overskrive de samsvarende utdatafilene?',
 'Only the selected levels': 'Bare de valgte nivåene',
 'Only validated Overpass responses can be cached.':
   'Bare validerte Overpass-svar kan bufres.',
 'Open public spaces': 'Åpne offentlige rom',
 'Open the in-plugin help with links to the online documentation.':
   'Åpne hjelpen i utvidelsen med lenker til nettdokumentasjonen.',
 'Output Settings': 'Utdatainnstillinger',
 'Output directory': 'Utdatamappe',
 'Output directory selected:': 'Utdatamappe valgt:',
 'Output format': 'Utdataformat',
 'Output settings': 'Utdatainnstillinger',
 'Overpass download cancelled.': 'Overpass-nedlasting avbrutt.',
 'Overpass download completed:': 'Overpass-nedlasting fullført:',
 'Overpass download failed.': 'Overpass-nedlasting mislyktes.',
 'Overpass download failed:': 'Overpass-nedlasting mislyktes:',
 'Overpass download running...': 'Overpass-nedlasting kjører…',
 'Overpass download was cancelled by the caller.':
   'Overpass-nedlastingen ble avbrutt av kalleren.',
 'Overpass query must be a non-empty string.':
   'Overpass-spørringen må være en ikke-tom streng.',
 "Overpass response 'elements' field is not a list.":
   'Overpass-svarets «elements»-felt er ikke en liste.',
 "Overpass response does not contain an 'elements' field.":
   'Overpass-svaret inneholder ikke et «elements»-felt.',
 'Overpass response is not a JSON object.':
   'Overpass-svaret er ikke et JSON-objekt.',
 'Overpass response received successfully:': 'Overpass-svar mottatt:',
 'Overpass server ': 'Overpass-server ',
 'Overpass server returned invalid JSON. Response preview: ':
   'Overpass-serveren returnerte ugyldig JSON. Forhåndsvisning av svar: ',
 'Overpass servers available:': 'Overpass-servere tilgjengelig:',
 'Overpass timeout must be greater than zero.':
   'Overpass-tidsavbrudd må være større enn null.',
 'Plugin version': 'Utvidelsesversjon',
 'Points of interest (POI)': 'Interessepunkter (POI)',
 'Prepared {index:,} of {total:,} OSM elements for export...':
   'Forberedte {index:,} av {total:,} OSM-elementer for eksport…',
 'Preparing Overpass download...': 'Forbereder Overpass-nedlasting…',
 'Preparing Overpass query.': 'Forbereder Overpass-spørring.',
 'Processing Options': 'Behandlingsalternativer',
 'Processing log': 'Behandlingslogg',
 'Processing messages will appear here...': 'Behandlingsmeldinger vises her…',
 'Processing options': 'Behandlingsalternativer',
 'Public transport & places': 'Kollektivtransport og steder',
 'QGIS interface object was not detected. Canvas-dependent AOI tools are disabled.':
   'QGIS-grensesnittobjektet ble ikke funnet. Lerretavhengige AOI-verktøy er deaktivert.',
 'QGIS map canvas could not be accessed.':
   'Kunne ikke få tilgang til QGIS-kartlerretet.',
 'QGIS map canvas is unavailable.': 'QGIS-kartlerretet er utilgjengelig.',
 'Rail stops': 'Jernbaneholdeplasser',
 'Railways': 'Jernbaner',
 'Read the plugin version from metadata.txt (empty string if absent).':
   'Les utvidelsesversjonen fra metadata.txt (tom streng hvis den mangler).',
 'Read, validate and store the current QGIS map canvas extent.':
   'Les, valider og lagre gjeldende utstrekning for QGIS-kartlerretet.',
 'Ready.': 'Klar.',
 'Rectangle AOI drawing tool activated.':
   'Tegneverktøyet for rektangel-AOI er aktivert.',
 'Rectangle AOI drawing was cancelled.':
   'Tegning av rektangel-AOI ble avbrutt.',
 'Region name': 'Regionnavn',
 'Report an issue': 'Rapporter et problem',
 'Request cooperative cancellation of the background worker.':
   'Be om samarbeidsvillig avbrytelse av bakgrunnsarbeideren.',
 'Request error on server ': 'Forespørselsfeil på server ',
 'Restore default GUI settings when the dialog closes.':
   'Gjenopprett standard GUI-innstillinger når dialogen lukkes.',
 'Restore the GUI once the background thread has stopped.':
   'Gjenopprett GUI når bakgrunnstråden har stoppet.',
 'Restore the QGIS map tool active before rectangle drawing.':
   'Gjenopprett QGIS-kartverktøyet som var aktivt før rektangeltegningen.',
 'Restore the map tool and reset state before hiding the dialog.':
   'Gjenopprett kartverktøyet og tilbakestill tilstanden før dialogen skjules.',
 'Retrying in ': 'Prøver på nytt om ',
 'Return selected levels, or None when all levels are requested.':
   'Returner valgte nivåer, eller None når alle nivåer er forespurt.',
 'Return the combined, sanitized filename prefix.':
   'Returner det kombinerte, rensede filnavnprefikset.',
 'Return the mapping between feature keys and GUI checkboxes.':
   'Returner tilordningen mellom objektnøkler og GUI-avkrysningsbokser.',
 'Return the selected GUI feature keys.':
   'Returner de valgte GUI-objektnøklene.',
 'Roads': 'Veier',
 'Run a modal dialog on both Qt5 and Qt6.':
   'Kjør en modal dialog på både Qt5 og Qt6.',
 'Select Output Directory': 'Velg utdatamappe',
 'Select a vector layer with selected features.':
   'Velg et vektorlag med valgte objekter.',
 'Select all': 'Velg alle',
 'Select an active QGIS layer.': 'Velg et aktivt QGIS-lag.',
 'Select at least one OSM feature category before downloading.':
   'Velg minst én OSM-objektkategori før nedlasting.',
 'Select at least one administrative level, or choose All levels.':
   'Velg minst ett administrativt nivå, eller velg Alle nivåer.',
 'Select at least one administrative level, or use None to retrieve all levels.':
   'Velg minst ett administrativt nivå, eller bruk None for å hente alle nivåer.',
 'Select levels 0–15 and switch to specific-level mode.':
   'Velg nivåene 0–15 og bytt til modus for spesifikke nivåer.',
 'Select one or more features in the active layer.':
   'Velg ett eller flere objekter i det aktive laget.',
 'Select output directory...': 'Velg utdatamappe…',
 'Selected administrative levels:': 'Valgte administrative nivåer:',
 'Selected feature IDs:': 'ID-er for valgte objekter:',
 'Selected feature(s) in active layer': 'Valgt(e) objekt(er) i aktivt lag',
 'Selected features (': 'Valgte objekter (',
 'Selected-feature AOI captured successfully (':
   'AOI fra valgte objekter registrert (',
 'Selected-feature AOI captured successfully.':
   'AOI fra valgte objekter ble registrert.',
 'Selected-feature AOI is invalid.': 'AOI fra valgte objekter er ugyldig.',
 'Selected-feature AOI requires a vector layer.':
   'AOI fra valgte objekter krever et vektorlag.',
 'Selected-feature AOI validation failed:':
   'Validering av AOI fra valgte objekter mislyktes:',
 'Sending query to Overpass...': 'Sender spørring til Overpass…',
 'Server ': 'Server ',
 'Shapefile': 'Shapefile',
 'Shapefile export completed in:': 'Shapefile-eksport fullført i:',
 'Shapefile field names shortened for': 'Shapefile-feltnavn forkortet for',
 'Shapefile layer(s) to QGIS.': 'Shapefile-lag i QGIS.',
 'Short in-plugin help with links to the full online documentation.':
   'Kort hjelp i utvidelsen med lenker til den fullstendige nettdokumentasjonen.',
 'Show AOI coordinates and source CRS in the dialog.':
   'Vis AOI-koordinater og kilde-CRS i dialogen.',
 'Show a concise description of the active administrative filter.':
   'Vis en kort beskrivelse av det aktive administrative filteret.',
 'Source CRS is invalid.': 'Kilde-CRS er ugyldig.',
 'South latitude cannot be greater than north latitude.':
   'Sørlig breddegrad kan ikke være større enn nordlig breddegrad.',
 'South:': 'Sør:',
 'Starting Overpass download...': 'Starter Overpass-nedlasting…',
 'Supporting copy: muted, wrapped and visually quiet.':
   'Støttetekst: dempet, brutt og visuelt rolig.',
 "Tag '{tag}' contains an empty value list.":
   'Taggen «{tag}» inneholder en tom verdiliste.',
 'Temporary workspace cleanup complete:':
   'Opprydding av midlertidig arbeidsområde fullført:',
 'Temporary workspace cleanup complete: no matching files found.':
   'Opprydding av midlertidig arbeidsområde fullført: ingen samsvarende filer funnet.',
 'Temporary-file cleanup skipped: workspace directory is invalid.':
   'Opprydding av midlertidige filer hoppet over: arbeidsområdemappen er ugyldig.',
 'The OSM download succeeded, but the output could not be created.':
   'OSM-nedlastingen lyktes, men utdataene kunne ikke opprettes.',
 "The Overpass response must be a JSON object with an 'elements' list.":
   'Overpass-svaret må være et JSON-objekt med en «elements»-liste.',
 'The QGIS map canvas CRS is invalid.':
   'CRS-en til QGIS-kartlerretet er ugyldig.',
 'The active layer CRS is invalid.': 'CRS-en til det aktive laget er ugyldig.',
 'The active layer extent is empty.': 'Utstrekningen til det aktive laget er tom.',
 'The active layer must be a vector layer.':
   'Det aktive laget må være et vektorlag.',
 'The combined name is too long. Shorten one or more components.':
   'Det kombinerte navnet er for langt. Forkort én eller flere komponenter.',
 'The combined selected-feature geometry is empty.':
   'Den kombinerte geometrien til de valgte objektene er tom.',
 'The current AOI is invalid:': 'Gjeldende AOI er ugyldig:',
 'The current QGIS map extent is empty.':
   'Gjeldende QGIS-kartutstrekning er tom.',
 'The dialog cannot close while a download thread is running. Cancellation has been requested; close the dialog after it stops.':
   'Dialogen kan ikke lukkes mens en nedlastingstråd kjører. Avbrytelse er forespurt; lukk dialogen etter at den stopper.',
 'The download completed, but no confirmed output name was available.':
   'Nedlastingen ble fullført, men det var ikke noe bekreftet utdatanavn tilgjengelig.',
 "The exported Shapefile '{path}' could not be opened in QGIS.":
   'Den eksporterte Shapefilen «{path}» kunne ikke åpnes i QGIS.',
 "The exported layer '{layer_name}' could not be opened in QGIS.":
   'Det eksporterte laget «{layer_name}» kunne ikke åpnes i QGIS.',
 'The output name does not contain any valid filename characters.':
   'Utdatanavnet inneholder ingen gyldige filnavntegn.',
 'The output name is empty after filename validation.':
   'Utdatanavnet er tomt etter filnavnvalidering.',
 'The selected features contain no valid geometry.':
   'De valgte objektene inneholder ingen gyldig geometri.',
 'The selected output directory does not exist. Choose an existing folder.':
   'Den valgte utdatamappen finnes ikke. Velg en eksisterende mappe.',
 'There is no active download to cancel.':
   'Det er ingen aktiv nedlasting å avbryte.',
 'Timeout on server ': 'Tidsavbrudd på server ',
 'Translate widget labels while preserving each original English string.':
   'Oversett widgetetiketter mens hver opprinnelige engelske streng bevares.',
 'Trying Overpass server ': 'Prøver Overpass-server ',
 'Unable to start AOI drawing:': 'Kan ikke starte AOI-tegning:',
 'Unclassified OSM elements not written to feature layers:':
   'Uklassifiserte OSM-elementer som ikke er skrevet til objektlag:',
 'Unsupported geometry family: {geometry_family}':
   'Ikke-støttet geometrifamilie: {geometry_family}',
 "Unsupported geometry type '{geometry_type}' for feature '{feature_key}'.":
   'Ikke-støttet geometritype «{geometry_type}» for objektet «{feature_key}».',
 'Unsupported geometry type for Shapefile export: {geometry_type}':
   'Ikke-støttet geometritype for Shapefile-eksport: {geometry_type}',
 "Unsupported match mode '{mode}' for feature '{feature_key}'.":
   'Ikke-støttet samsvarsmodus «{mode}» for objektet «{feature_key}».',
 'Unsupported output format:': 'Ikke-støttet utdataformat:',
 "Unsupported tag value type for '{feature_key}': {value_type}":
   'Ikke-støttet tagg-verditype for «{feature_key}»: {value_type}',
 'Update Current QGIS Map Extent': 'Oppdater gjeldende QGIS-kartutstrekning',
 'Update the "N selected" count next to the category heading.':
   'Oppdater «N valgt»-antallet ved siden av kategoritittelen.',
 'Update the filename preview as the user edits the components.':
   'Oppdater filnavnforhåndsvisningen mens brukeren redigerer komponentene.',
 'Use Layer Extent': 'Bruk lagutstrekning',
 'Use Selected Features': 'Bruk valgte objekter',
 'Use local cache where available': 'Bruk lokal hurtigbuffer der den er tilgjengelig',
 'Use selected features in the active vector layer as the AOI.':
   'Bruk valgte objekter i det aktive vektorlaget som AOI.',
 'Use the full extent of the active QGIS layer as the AOI.':
   'Bruk hele utstrekningen til det aktive QGIS-laget som AOI.',
 'Use the full extent of the active QGIS layer.':
   'Bruk hele utstrekningen til det aktive QGIS-laget.',
 'Use the selected features of the active vector layer as the AOI.':
   'Bruk de valgte objektene i det aktive vektorlaget som AOI.',
 'Using cached data; no Overpass network request was needed.':
   'Bruker bufrede data; ingen Overpass-nettverksforespørsel var nødvendig.',
 'Validate filename and any explicitly selected admin levels.':
   'Valider filnavn og eventuelle eksplisitt valgte admin-nivåer.',
 'Validate inputs and start the background Overpass download.':
   'Valider inndata og start Overpass-nedlastingen i bakgrunnen.',
 'WGS84 AOI bbox: south=': 'WGS84 AOI-avgrensningsboks: sør=',
 'WGS84 AOI geometry is not available.': 'WGS84 AOI-geometri er ikke tilgjengelig.',
 'Warning: download succeeded, but the response could not be cached:':
   'Advarsel: nedlastingen lyktes, men svaret kunne ikke bufres:',
 'Waterways': 'Vannveier',
 'West longitude cannot be greater than east longitude.':
   'Vestlig lengdegrad kan ikke være større enn østlig lengdegrad.',
 'West:': 'Vest:',
 'Writing Shapefile {layer_index}/{total}: {layer_name}...':
   'Skriver Shapefile {layer_index}/{total}: {layer_name}…',
 'Writing layer {layer_index}/{total}: {layer_name} ({count:,} features)...':
   'Skriver lag {layer_index}/{total}: {layer_name} ({count:,} objekter)…',
 'attempt ': 'forsøk ',
 'characters).': 'tegn).',
 'connection error — ': 'tilkoblingsfeil — ',
 'e.g. CBD': 'f.eks. CBD',
 'e.g. Kenya': 'f.eks. Kenya',
 'e.g. Nairobi': 'f.eks. Nairobi',
 'e.g. NairobiCounty': 'f.eks. NairobiCounty',
 'elements (': 'elementer (',
 'export failed:': 'eksport mislyktes:',
 'feature records).': 'objektoppføringer).',
 'feature(s)).': 'objekt(er)).',
 'features written.': 'objekter skrevet.',
 'file(s) deleted.': 'fil(er) slettet.',
 'relation geometry assignment(s); relation-member geometry assembly is not implemented yet.':
   'relasjonsgeometritilordning(er); montering av relasjonsmedlemsgeometri er ennå ikke implementert.',
 'relations).': 'relasjoner).',
 'response_data must be a dictionary.': 'response_data må være en ordbok.',
 "response_data['elements'] must be a list.":
   "response_data['elements'] må være en liste.",
 'temporary file(s) could not be deleted. They may still be in use by QGIS or another process.':
   'midlertidige fil(er) kunne ikke slettes. De kan fortsatt være i bruk av QGIS eller en annen prosess.',
 'timeout — ': 'tidsavbrudd — ',
 '{output_format} export failed: {error}':
   '{output_format}-eksport mislyktes: {error}',
 '— Confirm Overwrite': '— Bekreft overskriving',
 '— Export Error': '— Eksportfeil',
 '— Help': '— Hjelp',
 '— Output Naming': '— Navngivning av utdata',
}