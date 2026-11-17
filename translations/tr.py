"""Turkish (Türkçe) translation pack for the OSM Data Toolkit plugin.
Keys remain the English source strings; preserve placeholders and HTML."""
TEXT = {
 '\n<h3>Quick start</h3>\n<ol>\n  <li><b>Choose an area.</b> Use the current map extent, draw a rectangle\n      on the map, or use the bounding box of selected features or a\n      layer\'s extent.</li>\n  <li><b>Tick the OSM categories</b> you need (POI, stops, roads,\n      buildings, boundaries, landuse, ...).</li>\n  <li><b>Choose an output format and folder</b>, then click\n      <b>Download OSM Data</b>.</li>\n</ol>\n\n<h3>Good to know</h3>\n<ul>\n  <li><b>GeoPackage is recommended.</b> A Shapefile cannot hold very many\n      attribute columns, so on large areas some rarely used tag columns\n      may be left out (the log tells you when this happens).</li>\n  <li><b>Keep the area focused.</b> Very large areas produce huge Overpass\n      responses and can be slow or rejected by the public servers.</li>\n  <li><b>The cache</b> lets repeat downloads of the same query reuse\n      earlier results.</li>\n  <li><b>"Unclassified OSM elements"</b> in the log is informational: they\n      are mostly untagged vertices of lines and polygons that do not belong\n      to any selected category.</li>\n</ul>\n\n<p>Data &copy; OpenStreetMap contributors, available under the\n<a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a>.</p>\n<p><i>This plugin is not endorsed by or affiliated with the\nOpenStreetMap Foundation.</i></p>\n':
 '\n<h3>Hızlı başlangıç</h3>\n<ol>\n  <li><b>Bir alan seçin.</b> Geçerli harita kapsamını kullanın, harita üzerinde\n      bir dikdörtgen çizin veya seçili özelliklerin ya da bir katmanın\n      kapsamının sınırlayıcı kutusunu kullanın.</li>\n  <li><b>İhtiyacınız olan OSM kategorilerini işaretleyin</b> (POI, duraklar,\n      yollar, binalar, sınırlar, arazi kullanımı, ...).</li>\n  <li><b>Bir çıktı biçimi ve klasör seçin</b>, ardından\n      <b>OSM Verilerini İndir</b>\'e tıklayın.</li>\n</ol>\n\n<h3>Bilmeniz iyi olur</h3>\n<ul>\n  <li><b>GeoPackage önerilir.</b> Bir Shapefile çok fazla öznitelik sütunu\n      barındıramaz, bu nedenle büyük alanlarda nadiren kullanılan bazı\n      etiket sütunları atlanabilir (bu olduğunda günlük size bildirir).</li>\n  <li><b>Alanı odaklı tutun.</b> Çok büyük alanlar devasa Overpass\n      yanıtları üretir ve yavaş olabilir veya genel sunucular tarafından\n      reddedilebilir.</li>\n  <li><b>Önbellek</b>, aynı sorgunun tekrarlanan indirmelerinin önceki\n      sonuçları yeniden kullanmasını sağlar.</li>\n  <li>Günlükteki <b>"Sınıflandırılmamış OSM öğeleri"</b> bilgilendiricidir:\n      bunlar çoğunlukla seçilen herhangi bir kategoriye ait olmayan\n      etiketsiz çizgi ve çokgen köşeleridir.</li>\n</ul>\n\n<p>Veriler &copy; OpenStreetMap katkıda bulunanlar, <a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a> altında sunulmaktadır.</p>\n<p><i>Bu eklenti OpenStreetMap Foundation tarafından onaylanmamıştır veya onunla bağlantılı değildir.</i></p>\n',
 ' responded successfully.': ' başarıyla yanıt verdi.',
 ' seconds...': ' saniye…',
 '" style="color:#0B5E8E; text-decoration:none;">OpenStreetMap contributors</a> (ODbL)':
   '" style="color:#0B5E8E; text-decoration:none;">OpenStreetMap katkıda bulunanlar</a> (ODbL)',
 ', east=': ', doğu=',
 ', north=': ', kuzey=',
 ', west=': ', batı=',
 '0 selected': '0 seçili',
 '<p>Plugin version': '<p>Eklenti sürümü',
 'A download is already running.': 'Zaten bir indirme çalışıyor.',
 'A labelled column of feature checkboxes.':
   'Özellik onay kutularından oluşan etiketli bir sütun.',
 'AOI drawing cancelled.': 'AOI çizimi iptal edildi.',
 'AOI geometry is empty.': 'AOI geometrisi boş.',
 'AOI geometry is missing.': 'AOI geometrisi eksik.',
 'AOI name': 'AOI adı',
 'AOI rectangle captured successfully.': 'AOI dikdörtgeni başarıyla yakalandı.',
 'AOI source CRS is invalid.': 'AOI kaynak CRS geçersiz.',
 'AOI validation failed:': 'AOI doğrulaması başarısız:',
 'AOI:': 'AOI:',
 'AOI: QGIS interface is not available.': 'AOI: QGIS arayüzü kullanılamıyor.',
 "AOI: click 'Draw AOI', then drag a rectangle on the QGIS map.":
   'AOI: "AOI Çiz"e tıklayın, ardından QGIS haritasında bir dikdörtgen sürükleyin.',
 "AOI: click 'Use Layer Extent' to use the full extent of the active QGIS layer.":
   'AOI: etkin QGIS katmanının tam kapsamını kullanmak için "Katman Kapsamını Kullan"a tıklayın.',
 'AOI: click and drag on the QGIS map.':
   'AOI: QGIS haritasında tıklayın ve sürükleyin.',
 'AOI: failed to resolve active layer extent':
   'AOI: etkin katman kapsamı belirlenemedi',
 'AOI: failed to resolve selected features':
   'AOI: seçili özellikler belirlenemedi',
 'AOI: invalid': 'AOI: geçersiz',
 'AOI: no active QGIS layer.': 'AOI: etkin QGIS katmanı yok.',
 'AOI: no feature(s) selected in the active layer.':
   'AOI: etkin katmanda seçili özellik yok.',
 'AOI: not yet resolved': 'AOI: henüz belirlenmedi',
 "AOI: select feature(s) in the active QGIS layer, then click 'Use Selected Features'.":
   'AOI: etkin QGIS katmanında özellik(ler) seçin, ardından "Seçili Özellikleri Kullan"a tıklayın.',
 'AOI: the active layer is not a vector layer.':
   'AOI: etkin katman bir vektör katmanı değil.',
 'AOI: unable to create': 'AOI: oluşturulamıyor',
 'AOI: unable to resolve': 'AOI: belirlenemiyor',
 'Activate the interactive rectangle AOI map tool.':
   'Etkileşimli dikdörtgen AOI harita aracını etkinleştirin.',
 'Active layer extent': 'Etkin katman kapsamı',
 'Active-layer extent AOI is invalid.':
   'Etkin katman kapsamı AOI geçersiz.',
 'Active-layer extent captured successfully.':
   'Etkin katman kapsamı başarıyla yakalandı.',
 'Active-layer extent validation failed:':
   'Etkin katman kapsamı doğrulaması başarısız:',
 'Administrative boundaries': 'İdari sınırlar',
 'Administrative boundary filter: all levels (no admin_level filter).':
   'İdari sınır filtresi: tüm düzeyler (admin_level filtresi yok).',
 'Administrative boundary levels': 'İdari sınır düzeyleri',
 'Administrative boundary levels:': 'İdari sınır düzeyleri:',
 'Administrative levels must be an integer, a numeric string, a sequence of levels, or None.':
   'İdari düzeyler bir tamsayı, sayısal bir dize, düzey dizisi veya None olmalıdır.',
 'All OSM feature categories cleared.': 'Tüm OSM özellik kategorileri temizlendi.',
 'All OSM feature categories selected.': 'Tüm OSM özellik kategorileri seçildi.',
 'All Overpass server URLs must be non-empty strings.':
   'Tüm Overpass sunucu URL\'leri boş olmayan dizeler olmalıdır.',
 'All Overpass servers and retry attempts failed.':
   'Tüm Overpass sunucuları ve yeniden denemeler başarısız oldu.',
 'All administrative levels will be included.':
   'Tüm idari düzeyler dahil edilecek.',
 'All administrative levels will be included; no admin_level filter will be added to the query.':
   'Tüm idari düzeyler dahil edilecek; sorguya admin_level filtresi eklenmeyecek.',
 'All attempts failed for server ': 'Sunucu için tüm denemeler başarısız oldu ',
 'All levels (0–15; no admin_level filter)':
   'Tüm düzeyler (0–15; admin_level filtresi yok)',
 'An existing output directory is required for Shapefile export.':
   'Shapefile dışa aktarımı için mevcut bir çıktı dizini gerekir.',
 'An output GeoPackage path is required.':
   'Bir çıktı GeoPackage yolu gerekir.',
 'An output name is required for Shapefile export.':
   'Shapefile dışa aktarımı için bir çıktı adı gerekir.',
 'Append a timestamped message to the processing log.':
   'İşleme günlüğüne zaman damgalı bir ileti ekleyin.',
 'Append an exported feature count to the processing log.':
   'İşleme günlüğüne dışa aktarılan özellik sayısını ekleyin.',
 'Area of Interest': 'İlgi Alanı',
 'At least one OSM feature must be selected.':
   'En az bir OSM özelliği seçilmelidir.',
 'At least one OSM feature must be supplied.':
   'En az bir OSM özelliği sağlanmalıdır.',
 'At least one Overpass server must be provided.':
   'En az bir Overpass sunucusu sağlanmalıdır.',
 'Attempt details:': 'Deneme ayrıntıları:',
 'Automatically add downloaded layers to QGIS':
   'İndirilen katmanları QGIS\'e otomatik olarak ekle',
 'Background Overpass download started.':
   'Arka plan Overpass indirmesi başladı.',
 'Browse': 'Gözat',
 'Browse…': 'Gözat…',
 'Buildings': 'Binalar',
 'Bus stops': 'Otobüs durakları',
 'CRS:': 'CRS:',
 'Cache hit:': 'Önbellek isabeti:',
 'Cache hit: using saved Overpass response ({age} day(s) old).':
   'Önbellek isabeti: kayıtlı Overpass yanıtı kullanılıyor ({age} günlük).',
 'Cache miss:': 'Önbellek isabetsizliği:',
 'Cache miss: could not read saved response ({error}).':
   'Önbellek isabetsizliği: kayıtlı yanıt okunamadı ({error}).',
 'Cache miss: query hash does not match the saved response.':
   'Önbellek isabetsizliği: sorgu karması kayıtlı yanıtla eşleşmiyor.',
 'Cache miss: saved response is incomplete or invalid.':
   'Önbellek isabetsizliği: kayıtlı yanıt eksik veya geçersiz.',
 'Cache miss: saved response is older than {days} days.':
   'Önbellek isabetsizliği: kayıtlı yanıt {days} günden daha eski.',
 'Cache miss: saved response uses an unsupported cache format.':
   'Önbellek isabetsizliği: kayıtlı yanıt desteklenmeyen bir önbellek biçimi kullanıyor.',
 'Cached Overpass response:': 'Önbelleğe alınmış Overpass yanıtı:',
 'Cancel': 'İptal',
 'Cancellation has already been requested.': 'İptal zaten talep edildi.',
 'Cancellation requested': 'İptal talep edildi',
 'Cancellation requested. If an HTTP request is already active, the downloader will stop when that request returns or times out.':
   'İptal talep edildi. Bir HTTP isteği zaten etkinse, indirici o istek geri döndüğünde veya zaman aşımına uğradığında duracaktır.',
 'Cancellation requested; waiting for the current request to finish...':
   'İptal talep edildi; mevcut isteğin bitmesi bekleniyor…',
 'Cannot draw AOI because the QGIS interface is unavailable.':
   'QGIS arayüzü kullanılamadığından AOI çizilemiyor.',
 'Cannot resolve active-layer extent because QGIS is unavailable.':
   'QGIS kullanılamadığından etkin katman kapsamı belirlenemiyor.',
 'Cannot resolve current map extent because QGIS is unavailable.':
   'QGIS kullanılamadığından geçerli harita kapsamı belirlenemiyor.',
 'Cannot resolve selected-feature AOI because QGIS is unavailable.':
   'QGIS kullanılamadığından seçili özellik AOI\'si belirlenemiyor.',
 'Cannot transform an empty geometry.':
   'Boş bir geometri dönüştürülemiyor.',
 'Capture the current QGIS map canvas extent.':
   'Geçerli QGIS harita tuvali kapsamını yakalayın.',
 'Choose all available levels, or select one or more levels to download (for example, 5–8 or level 5).':
   'Kullanılabilir tüm düzeyleri seçin veya indirmek için bir ya da daha fazla düzey seçin (örneğin 5–8 veya düzey 5).',
 'Choose an output directory before downloading.':
   'İndirmeden önce bir çıktı dizini seçin.',
 'City name': 'Şehir adı',
 'Classifying OSM elements and preparing GeoPackage layers.':
   'OSM öğeleri sınıflandırılıyor ve GeoPackage katmanları hazırlanıyor.',
 'Classifying OSM elements and preparing Shapefile outputs.':
   'OSM öğeleri sınıflandırılıyor ve Shapefile çıktıları hazırlanıyor.',
 'Clear all': 'Tümünü temizle',
 'Clear log': 'Günlüğü temizle',
 'Clear only the visible log, without changing processing settings.':
   'İşleme ayarlarını değiştirmeden yalnızca görünür günlüğü temizleyin.',
 'Clear selected levels so the user can make a narrower selection.':
   'Kullanıcının daha dar bir seçim yapabilmesi için seçili düzeyleri temizleyin.',
 'Clear the messages currently shown in the Processing Log.':
   'İşleme Günlüğünde şu anda gösterilen iletileri temizleyin.',
 'Clear the previous AOI and display guidance for the chosen method.':
   'Önceki AOI\'yi temizleyin ve seçilen yöntem için yönergeleri gösterin.',
 'Close': 'Kapat',
 'Collect optional filename components before exporting OSM data.':
   'OSM verilerini dışa aktarmadan önce isteğe bağlı dosya adı bileşenlerini toplayın.',
 'Compact product header above the scrollable workflow.':
   'Kaydırılabilir iş akışının üzerinde kompakt ürün başlığı.',
 'Connection error on server ': 'Sunucuda bağlantı hatası ',
 'Continue to Download': 'İndirmeye Devam Et',
 'Convert a name component into a Windows-safe filename token.':
   'Bir ad bileşenini Windows için güvenli bir dosya adı belirtecine dönüştürün.',
 'Convert the drawn rectangle into the standard AOI object.':
   'Çizilen dikdörtgeni standart AOI nesnesine dönüştürün.',
 'Converting OSM response to GeoPackage...':
   'OSM yanıtı GeoPackage\'a dönüştürülüyor…',
 'Converting OSM response to Shapefiles...':
   'OSM yanıtı Shapefile\'lara dönüştürülüyor…',
 'Could not combine the selected feature geometries.':
   'Seçili özellik geometrileri birleştirilemedi.',
 "Could not create Shapefile staging layer '{layer_name}'.":
   'Shapefile hazırlık katmanı "{layer_name}" oluşturulamadı.',
 'Could not create an empty bus_stops_points layer.':
   'Boş bir bus_stops_points katmanı oluşturulamadı.',
 "Could not create temporary QGIS layer '{layer_name}'.":
   'Geçici QGIS katmanı "{layer_name}" oluşturulamadı.',
 'Could not create temporary layer for admin_level {admin_level}.':
   'admin_level {admin_level} için geçici katman oluşturulamadı.',
 'Could not create the merged bus_stops_points layer.':
   'Birleştirilmiş bus_stops_points katmanı oluşturulamadı.',
 'Could not delete temporary file': 'Geçici dosya silinemedi',
 "Could not load feature definition '{feature_key}': {error}":
   'Özellik tanımı "{feature_key}" yüklenemedi: {error}',
 'Could not merge bus-station centroids into bus-stop points.':
   'Otobüs terminali ağırlık merkezleri otobüs durağı noktalarıyla birleştirilemedi.',
 'Could not overwrite existing output file: {error}':
   'Mevcut çıktı dosyasının üzerine yazılamadı: {error}',
 'Could not populate Shapefile for admin_level {admin_level}.':
   'admin_level {admin_level} için Shapefile doldurulamadı.',
 "Could not populate temporary layer '{layer_name}'.":
   'Geçici katman "{layer_name}" doldurulamadı.',
 'Could not prepare the Overpass query:':
   'Overpass sorgusu hazırlanamadı:',
 "Could not reopen intermediate GeoPackage layer '{layer_name}'.":
   'Ara GeoPackage katmanı "{layer_name}" yeniden açılamadı.',
 'Could not restore previous QGIS map tool:':
   'Önceki QGIS harita aracı geri yüklenemedi:',
 'Could not search for temporary GeoPackages:':
   'Geçici GeoPackage\'lar aranamadı:',
 'Country name': 'Ülke adı',
 'Create one section panel and return it with its body layout.':
   'Bir bölüm paneli oluşturun ve gövde düzeniyle birlikte döndürün.',
 'Created bus_stops_points from bus-station polygon centroids.':
   'Otobüs terminali çokgen ağırlık merkezlerinden bus_stops_points oluşturuldu.',
 'Current QGIS map extent': 'Geçerli QGIS harita kapsamı',
 'Current QGIS map extent resolved.':
   'Geçerli QGIS harita kapsamı belirlendi.',
 'Data © <a href="': 'Veri © <a href="',
 'Deleted temporary workspace file:': 'Geçici çalışma alanı dosyası silindi:',
 'Details:': 'Ayrıntılar:',
 'Download': 'İndir',
 'Download OSM Data': 'OSM Verilerini İndir',
 'Download OpenStreetMap data for any area and load it straight into QGIS.':
   'Herhangi bir alan için OpenStreetMap verilerini indirin ve doğrudan QGIS\'e yükleyin.',
 'Download cancelled because existing output files were not approved for overwrite.':
   'Mevcut çıktı dosyalarının üzerine yazılması onaylanmadığından indirme iptal edildi.',
 'Download cancelled before it started.':
   'İndirme başlamadan önce iptal edildi.',
 'Download cancelled before results were returned.':
   'Sonuçlar döndürülmeden önce indirme iptal edildi.',
 'Download cancelled before starting.':
   'Başlamadan önce indirme iptal edildi.',
 'Download cancelled in the output-naming dialog.':
   'Çıktı adlandırma iletişim kutusunda indirme iptal edildi.',
 'Download cancelled.': 'İndirme iptal edildi.',
 'Download cancelled; existing files preserved.':
   'İndirme iptal edildi; mevcut dosyalar korundu.',
 'Download stopped.': 'İndirme durduruldu.',
 'Download succeeded, but export failed.':
   'İndirme başarılı oldu, ancak dışa aktarma başarısız oldu.',
 'Downloading OSM data from Overpass...':
   'Overpass\'tan OSM verileri indiriliyor…',
 'Draw AOI': 'AOI Çiz',
 'Draw a rectangle on the QGIS map to define the AOI.':
   'AOI\'yi tanımlamak için QGIS haritasında bir dikdörtgen çizin.',
 'Draw rectangle on map': 'Haritada dikdörtgen çiz',
 'Draw the AOI rectangle on the QGIS map.':
   'QGIS haritasında AOI dikdörtgenini çizin.',
 'Drawn AOI validation failed:':
   'Çizilen AOI doğrulaması başarısız:',
 'Drawn rectangle': 'Çizilen dikdörtgen',
 'Drawn rectangle AOI captured successfully.':
   'Çizilen dikdörtgen AOI başarıyla yakalandı.',
 'ERROR:': 'HATA:',
 'East:': 'Doğu:',
 'Enable level checkboxes only when a specific selection is active.':
   'Düzey onay kutularını yalnızca belirli bir seçim etkinken etkinleştirin.',
 'Enable only the AOI action button for the selected method.':
   'Seçilen yöntem için yalnızca AOI eylem düğmesini etkinleştirin.',
 'Enable or disable controls while a download is running.':
   'İndirme çalışırken denetimleri etkinleştirin veya devre dışı bırakın.',
 'Enter at least one name (City, Country, Region, or AOI).':
   'En az bir ad girin (Şehir, Ülke, Bölge veya AOI).',
 'Enter one or more name components. Blank fields will be skipped, and the remaining names will be joined with underscores. The selected output format will be retained.':
   'Bir veya daha fazla ad bileşeni girin. Boş alanlar atlanır ve kalan adlar alt çizgiyle birleştirilir. Seçili çıktı biçimi korunur.',
 'Enter_a_name_to_preview': 'Önizleme_için_bir_ad_girin',
 'Export cancelled: output name is missing.':
   'Dışa aktarma iptal edildi: çıktı adı eksik.',
 'Export complete:': 'Dışa aktarma tamamlandı:',
 'Export the downloaded response and optionally load its layers.':
   'İndirilen yanıtı dışa aktarın ve isteğe bağlı olarak katmanlarını yükleyin.',
 'Failed to activate rectangle AOI tool:':
   'Dikdörtgen AOI aracı etkinleştirilemedi:',
 'Failed to create AOI.': 'AOI oluşturulamadı.',
 'Failed to process drawn rectangle AOI:':
   'Çizilen dikdörtgen AOI işlenemedi:',
 'Failed to resolve active-layer extent.':
   'Etkin katman kapsamı belirlenemedi.',
 'Failed to resolve active-layer extent:':
   'Etkin katman kapsamı belirlenemedi:',
 'Failed to resolve current QGIS map extent:':
   'Geçerli QGIS harita kapsamı belirlenemedi:',
 'Failed to resolve selected-feature AOI.':
   'Seçili özellik AOI\'si belirlenemedi.',
 'Failed to resolve selected-feature AOI:':
   'Seçili özellik AOI\'si belirlenemedi:',
 "Failed to write layer '{layer_name}' to '{output_path}': {error}":
   '"{layer_name}" katmanı "{output_path}" konumuna yazılamadı: {error}',
 "Feature '{feature_key}' has no tag definitions.":
   '"{feature_key}" özelliğinin etiket tanımı yok.',
 'Feature specification  does not expose a tag-filter mapping.':
   'Özellik belirtimi bir etiket filtresi eşlemesi sunmuyor.',
 'Ferry stops': 'Feribot durakları',
 'Filename preview': 'Dosya adı önizlemesi',
 'Full documentation': 'Tam belgeler',
 'Generated Overpass query (': 'Oluşturulan Overpass sorgusu (',
 'GeoPackage': 'GeoPackage',
 'GeoPackage layer(s) to QGIS.': 'GeoPackage katman(lar)ı QGIS\'e.',
 'GeoPackage saved:': 'GeoPackage kaydedildi:',
 'HTTP error on server ': 'Sunucuda HTTP hatası ',
 'HTTP error — ': 'HTTP hatası — ',
 'HTTP {status} error on server {index}/{total}.':
   '{index}/{total} numaralı sunucuda HTTP {status} hatası.',
 'Handle a drawing tool deactivation initiated outside this dialog.':
   'Bu iletişim kutusunun dışında başlatılan bir çizim aracı devre dışı bırakmasını işleyin.',
 'Help': 'Yardım',
 'Invalid east longitude: {value}': 'Geçersiz doğu boylamı: {value}',
 'Invalid north latitude: {value}': 'Geçersiz kuzey enlemi: {value}',
 'Invalid response from server ': 'Sunucudan geçersiz yanıt ',
 'Invalid south latitude: {value}': 'Geçersiz güney enlemi: {value}',
 'Invalid west longitude: {value}': 'Geçersiz batı boylamı: {value}',
 'Keep the numeric readout in step with the progress bar.':
   'Sayısal göstergeleri ilerleme çubuğuyla eşzamanlı tutun.',
 'Land & built environment': 'Arazi ve yapılı çevre',
 'Landuse': 'Arazi kullanımı',
 'Language:': 'Dil:',
 'Linear features': 'Doğrusal özellikler',
 'Load the saved interface language and translate visible UI strings.':
   'Kayıtlı arayüz dilini yükleyin ve görünür UI dizelerini çevirin.',
 'Local response cache is disabled.':
   'Yerel yanıt önbelleği devre dışı.',
 'Main OSM Data Toolkit window.': 'Ana OSM Data Toolkit penceresi.',
 'Manually capture the map extent after the user pans or zooms.':
   'Kullanıcı kaydırdıktan veya yakınlaştırdıktan sonra harita kapsamını el ile yakalayın.',
 'Merged bus-station polygon centroids into bus_stops_points.':
   'Otobüs terminali çokgen ağırlık merkezleri bus_stops_points içinde birleştirildi.',
 'No Overpass selectors were generated.':
   'Hiçbir Overpass seçici oluşturulmadı.',
 'No active QGIS layer is available.': 'Etkin bir QGIS katmanı yok.',
 'No active layer is available.': 'Etkin bir katman yok.',
 'No exportable features matched the selected categories. Try another AOI or select additional OSM feature categories.':
   'Hiçbir dışa aktarılabilir özellik seçili kategorilerle eşleşmedi. Başka bir AOI deneyin veya ek OSM özellik kategorileri seçin.',
 'No features are selected in the active layer.':
   'Etkin katmanda hiçbir özellik seçili değil.',
 'No levels selected. Select at least one level to continue.':
   'Hiçbir düzey seçilmedi. Devam etmek için en az bir düzey seçin.',
 'No selected features found.': 'Seçili özellik bulunamadı.',
 'No valid Area of Interest is available. Select an AOI method and resolve the AOI before downloading.':
   'Geçerli bir İlgi Alanı yok. İndirmeden önce bir AOI yöntemi seçin ve AOI\'yi belirleyin.',
 'North:': 'Kuzey:',
 'Note: {layer_name} has too many tag columns for one Shapefile (DBF size limit); {count} rarely-used columns were left out.':
   'Not: {layer_name} tek bir Shapefile için çok fazla etiket sütununa sahip (DBF boyut sınırı); {count} nadiren kullanılan sütun atlandı.',
 'OSM Data Toolkit': 'OSM Data Toolkit',
 'OSM Data Toolkit initialised.': 'OSM Data Toolkit başlatıldı.',
 'OSM Feature Categories': 'OSM Özellik Kategorileri',
 'OSM export completed successfully.':
   'OSM dışa aktarımı başarıyla tamamlandı.',
 'One or more output files with this name already exist. Do you want to overwrite the matching output files?':
   'Bu ada sahip bir veya daha fazla çıktı dosyası zaten var. Eşleşen çıktı dosyalarının üzerine yazmak istiyor musunuz?',
 'Only the selected levels': 'Yalnızca seçili düzeyler',
 'Only validated Overpass responses can be cached.':
   'Yalnızca doğrulanmış Overpass yanıtları önbelleğe alınabilir.',
 'Open public spaces': 'Açık kamusal alanlar',
 'Open the in-plugin help with links to the online documentation.':
   'Çevrimiçi belgelere bağlantılar içeren eklenti içi yardımı açın.',
 'Output Settings': 'Çıktı Ayarları',
 'Output directory': 'Çıktı dizini',
 'Output directory selected:': 'Çıktı dizini seçildi:',
 'Output format': 'Çıktı biçimi',
 'Output settings': 'Çıktı ayarları',
 'Overpass download cancelled.': 'Overpass indirmesi iptal edildi.',
 'Overpass download completed:': 'Overpass indirmesi tamamlandı:',
 'Overpass download failed.': 'Overpass indirmesi başarısız oldu.',
 'Overpass download failed:': 'Overpass indirmesi başarısız oldu:',
 'Overpass download running...': 'Overpass indirmesi çalışıyor…',
 'Overpass download was cancelled by the caller.':
   'Overpass indirmesi çağıran tarafından iptal edildi.',
 'Overpass query must be a non-empty string.':
   'Overpass sorgusu boş olmayan bir dize olmalıdır.',
 "Overpass response 'elements' field is not a list.":
   'Overpass yanıtının "elements" alanı bir liste değil.',
 "Overpass response does not contain an 'elements' field.":
   'Overpass yanıtı "elements" alanı içermiyor.',
 'Overpass response is not a JSON object.':
   'Overpass yanıtı bir JSON nesnesi değil.',
 'Overpass response received successfully:':
   'Overpass yanıtı başarıyla alındı:',
 'Overpass server ': 'Overpass sunucusu ',
 'Overpass server returned invalid JSON. Response preview: ':
   'Overpass sunucusu geçersiz JSON döndürdü. Yanıt önizlemesi: ',
 'Overpass servers available:': 'Kullanılabilir Overpass sunucuları:',
 'Overpass timeout must be greater than zero.':
   'Overpass zaman aşımı sıfırdan büyük olmalıdır.',
 'Plugin version': 'Eklenti sürümü',
 'Points of interest (POI)': 'İlgi çekici noktalar (POI)',
 'Prepared {index:,} of {total:,} OSM elements for export...':
   'Dışa aktarma için {total:,} OSM öğesinden {index:,} tanesi hazırlandı…',
 'Preparing Overpass download...':
   'Overpass indirmesi hazırlanıyor…',
 'Preparing Overpass query.': 'Overpass sorgusu hazırlanıyor.',
 'Processing Options': 'İşleme Seçenekleri',
 'Processing log': 'İşleme günlüğü',
 'Processing messages will appear here...':
   'İşleme iletileri burada görünecek…',
 'Processing options': 'İşleme seçenekleri',
 'Public transport & places': 'Toplu taşıma ve yerler',
 'QGIS interface object was not detected. Canvas-dependent AOI tools are disabled.':
   'QGIS arayüz nesnesi algılanmadı. Tuvale bağlı AOI araçları devre dışı.',
 'QGIS map canvas could not be accessed.':
   'QGIS harita tuvaline erişilemedi.',
 'QGIS map canvas is unavailable.':
   'QGIS harita tuvali kullanılamıyor.',
 'Rail stops': 'Demiryolu durakları',
 'Railways': 'Demiryolları',
 'Read the plugin version from metadata.txt (empty string if absent).':
   'Eklenti sürümünü metadata.txt dosyasından okuyun (yoksa boş dize).',
 'Read, validate and store the current QGIS map canvas extent.':
   'Geçerli QGIS harita tuvali kapsamını okuyun, doğrulayın ve saklayın.',
 'Ready.': 'Hazır.',
 'Rectangle AOI drawing tool activated.':
   'Dikdörtgen AOI çizim aracı etkinleştirildi.',
 'Rectangle AOI drawing was cancelled.':
   'Dikdörtgen AOI çizimi iptal edildi.',
 'Region name': 'Bölge adı',
 'Report an issue': 'Sorun bildir',
 'Request cooperative cancellation of the background worker.':
   'Arka plan çalışanının işbirliğine dayalı iptalini talep edin.',
 'Request error on server ': 'Sunucuda istek hatası ',
 'Restore default GUI settings when the dialog closes.':
   'İletişim kutusu kapandığında varsayılan GUI ayarlarını geri yükleyin.',
 'Restore the GUI once the background thread has stopped.':
   'Arka plan iş parçacığı durduğunda GUI\'yi geri yükleyin.',
 'Restore the QGIS map tool active before rectangle drawing.':
   'Dikdörtgen çiziminden önce etkin olan QGIS harita aracını geri yükleyin.',
 'Restore the map tool and reset state before hiding the dialog.':
   'İletişim kutusunu gizlemeden önce harita aracını geri yükleyin ve durumu sıfırlayın.',
 'Retrying in ': 'Yeniden deneniyor ',
 'Return selected levels, or None when all levels are requested.':
   'Seçili düzeyleri veya tüm düzeyler istendiğinde None döndürün.',
 'Return the combined, sanitized filename prefix.':
   'Birleştirilmiş, temizlenmiş dosya adı önekini döndürün.',
 'Return the mapping between feature keys and GUI checkboxes.':
   'Özellik anahtarları ile GUI onay kutuları arasındaki eşlemeyi döndürün.',
 'Return the selected GUI feature keys.':
   'Seçili GUI özellik anahtarlarını döndürün.',
 'Roads': 'Yollar',
 'Run a modal dialog on both Qt5 and Qt6.':
   'Hem Qt5 hem de Qt6 üzerinde modal bir iletişim kutusu çalıştırın.',
 'Select Output Directory': 'Çıktı Dizini Seç',
 'Select a vector layer with selected features.':
   'Seçili özellikleri olan bir vektör katmanı seçin.',
 'Select all': 'Tümünü seç',
 'Select an active QGIS layer.': 'Etkin bir QGIS katmanı seçin.',
 'Select at least one OSM feature category before downloading.':
   'İndirmeden önce en az bir OSM özellik kategorisi seçin.',
 'Select at least one administrative level, or choose All levels.':
   'En az bir idari düzey seçin veya "Tüm düzeyler"i seçin.',
 'Select at least one administrative level, or use None to retrieve all levels.':
   'En az bir idari düzey seçin veya tüm düzeyleri almak için None kullanın.',
 'Select levels 0–15 and switch to specific-level mode.':
   '0–15 düzeylerini seçin ve belirli düzey moduna geçin.',
 'Select one or more features in the active layer.':
   'Etkin katmanda bir veya daha fazla özellik seçin.',
 'Select output directory...': 'Çıktı dizini seç…',
 'Selected administrative levels:': 'Seçili idari düzeyler:',
 'Selected feature IDs:': 'Seçili özellik kimlikleri:',
 'Selected feature(s) in active layer':
   'Etkin katmanda seçili özellik(ler)',
 'Selected features (': 'Seçili özellikler (',
 'Selected-feature AOI captured successfully (':
   'Seçili özellik AOI başarıyla yakalandı (',
 'Selected-feature AOI captured successfully.':
   'Seçili özellik AOI başarıyla yakalandı.',
 'Selected-feature AOI is invalid.':
   'Seçili özellik AOI geçersiz.',
 'Selected-feature AOI requires a vector layer.':
   'Seçili özellik AOI bir vektör katmanı gerektirir.',
 'Selected-feature AOI validation failed:':
   'Seçili özellik AOI doğrulaması başarısız:',
 'Sending query to Overpass...': 'Overpass\'a sorgu gönderiliyor…',
 'Server ': 'Sunucu ',
 'Shapefile': 'Shapefile',
 'Shapefile export completed in:':
   'Shapefile dışa aktarımı tamamlandı:',
 'Shapefile field names shortened for':
   'Shapefile alan adları şunun için kısaltıldı',
 'Shapefile layer(s) to QGIS.': 'Shapefile katman(lar)ı QGIS\'e.',
 'Short in-plugin help with links to the full online documentation.':
   'Tam çevrimiçi belgelere bağlantılar içeren kısa eklenti içi yardım.',
 'Show AOI coordinates and source CRS in the dialog.':
   'İletişim kutusunda AOI koordinatlarını ve kaynak CRS\'yi gösterin.',
 'Show a concise description of the active administrative filter.':
   'Etkin idari filtrenin kısa bir açıklamasını gösterin.',
 'Source CRS is invalid.': 'Kaynak CRS geçersiz.',
 'South latitude cannot be greater than north latitude.':
   'Güney enlemi kuzey enleminden büyük olamaz.',
 'South:': 'Güney:',
 'Starting Overpass download...':
   'Overpass indirmesi başlatılıyor…',
 'Supporting copy: muted, wrapped and visually quiet.':
   'Destekleyici metin: sessiz, sarmalanmış ve görsel olarak sakin.',
 "Tag '{tag}' contains an empty value list.":
   '"{tag}" etiketi boş bir değer listesi içeriyor.',
 'Temporary workspace cleanup complete:':
   'Geçici çalışma alanı temizliği tamamlandı:',
 'Temporary workspace cleanup complete: no matching files found.':
   'Geçici çalışma alanı temizliği tamamlandı: eşleşen dosya bulunamadı.',
 'Temporary-file cleanup skipped: workspace directory is invalid.':
   'Geçici dosya temizliği atlandı: çalışma alanı dizini geçersiz.',
 'The OSM download succeeded, but the output could not be created.':
   'OSM indirmesi başarılı oldu, ancak çıktı oluşturulamadı.',
 "The Overpass response must be a JSON object with an 'elements' list.":
   'Overpass yanıtı, "elements" listesi içeren bir JSON nesnesi olmalıdır.',
 'The QGIS map canvas CRS is invalid.':
   'QGIS harita tuvali CRS\'si geçersiz.',
 'The active layer CRS is invalid.': 'Etkin katman CRS\'si geçersiz.',
 'The active layer extent is empty.': 'Etkin katman kapsamı boş.',
 'The active layer must be a vector layer.':
   'Etkin katman bir vektör katmanı olmalıdır.',
 'The combined name is too long. Shorten one or more components.':
   'Birleştirilmiş ad çok uzun. Bir veya daha fazla bileşeni kısaltın.',
 'The combined selected-feature geometry is empty.':
   'Birleştirilmiş seçili özellik geometrisi boş.',
 'The current AOI is invalid:': 'Geçerli AOI geçersiz:',
 'The current QGIS map extent is empty.':
   'Geçerli QGIS harita kapsamı boş.',
 'The dialog cannot close while a download thread is running. Cancellation has been requested; close the dialog after it stops.':
   'Bir indirme iş parçacığı çalışırken iletişim kutusu kapatılamaz. İptal talep edildi; durduktan sonra iletişim kutusunu kapatın.',
 'The download completed, but no confirmed output name was available.':
   'İndirme tamamlandı, ancak onaylanmış bir çıktı adı mevcut değildi.',
 "The exported Shapefile '{path}' could not be opened in QGIS.":
   'Dışa aktarılan Shapefile "{path}" QGIS\'te açılamadı.',
 "The exported layer '{layer_name}' could not be opened in QGIS.":
   'Dışa aktarılan "{layer_name}" katmanı QGIS\'te açılamadı.',
 'The output name does not contain any valid filename characters.':
   'Çıktı adı herhangi bir geçerli dosya adı karakteri içermiyor.',
 'The output name is empty after filename validation.':
   'Dosya adı doğrulamasından sonra çıktı adı boş.',
 'The selected features contain no valid geometry.':
   'Seçili özellikler geçerli bir geometri içermiyor.',
 'The selected output directory does not exist. Choose an existing folder.':
   'Seçili çıktı dizini mevcut değil. Mevcut bir klasör seçin.',
 'There is no active download to cancel.':
   'İptal edilecek etkin bir indirme yok.',
 'Timeout on server ': 'Sunucuda zaman aşımı ',
 'Translate widget labels while preserving each original English string.':
   'Her orijinal İngilizce dizeyi koruyarak pencere öğesi etiketlerini çevirin.',
 'Trying Overpass server ': 'Overpass sunucusu deneniyor ',
 'Unable to start AOI drawing:': 'AOI çizimi başlatılamıyor:',
 'Unclassified OSM elements not written to feature layers:':
   'Özellik katmanlarına yazılmayan sınıflandırılmamış OSM öğeleri:',
 'Unsupported geometry family: {geometry_family}':
   'Desteklenmeyen geometri ailesi: {geometry_family}',
 "Unsupported geometry type '{geometry_type}' for feature '{feature_key}'.":
   '"{feature_key}" özelliği için desteklenmeyen geometri türü "{geometry_type}".',
 'Unsupported geometry type for Shapefile export: {geometry_type}':
   'Shapefile dışa aktarımı için desteklenmeyen geometri türü: {geometry_type}',
 "Unsupported match mode '{mode}' for feature '{feature_key}'.":
   '"{feature_key}" özelliği için desteklenmeyen eşleşme modu "{mode}".',
 'Unsupported output format:': 'Desteklenmeyen çıktı biçimi:',
 "Unsupported tag value type for '{feature_key}': {value_type}":
   '"{feature_key}" için desteklenmeyen etiket değeri türü: {value_type}',
 'Update Current QGIS Map Extent':
   'Geçerli QGIS Harita Kapsamını Güncelle',
 'Update the "N selected" count next to the category heading.':
   'Kategori başlığının yanındaki "N seçili" sayısını güncelleyin.',
 'Update the filename preview as the user edits the components.':
   'Kullanıcı bileşenleri düzenlerken dosya adı önizlemesini güncelleyin.',
 'Use Layer Extent': 'Katman Kapsamını Kullan',
 'Use Selected Features': 'Seçili Özellikleri Kullan',
 'Use local cache where available':
   'Mevcut olduğunda yerel önbelleği kullan',
 'Use selected features in the active vector layer as the AOI.':
   'Etkin vektör katmanındaki seçili özellikleri AOI olarak kullanın.',
 'Use the full extent of the active QGIS layer as the AOI.':
   'Etkin QGIS katmanının tam kapsamını AOI olarak kullanın.',
 'Use the full extent of the active QGIS layer.':
   'Etkin QGIS katmanının tam kapsamını kullanın.',
 'Use the selected features of the active vector layer as the AOI.':
   'Etkin vektör katmanının seçili özelliklerini AOI olarak kullanın.',
 'Using cached data; no Overpass network request was needed.':
   'Önbelleğe alınmış veriler kullanılıyor; Overpass ağ isteği gerekmedi.',
 'Validate filename and any explicitly selected admin levels.':
   'Dosya adını ve açıkça seçilen yönetici düzeylerini doğrulayın.',
 'Validate inputs and start the background Overpass download.':
   'Girdileri doğrulayın ve arka plan Overpass indirmesini başlatın.',
 'WGS84 AOI bbox: south=': 'WGS84 AOI sınırlayıcı kutusu: güney=',
 'WGS84 AOI geometry is not available.':
   'WGS84 AOI geometrisi mevcut değil.',
 'Warning: download succeeded, but the response could not be cached:':
   'Uyarı: indirme başarılı oldu, ancak yanıt önbelleğe alınamadı:',
 'Waterways': 'Su yolları',
 'West longitude cannot be greater than east longitude.':
   'Batı boylamı doğu boylamından büyük olamaz.',
 'West:': 'Batı:',
 'Writing Shapefile {layer_index}/{total}: {layer_name}...':
   'Shapefile {layer_index}/{total} yazılıyor: {layer_name}…',
 'Writing layer {layer_index}/{total}: {layer_name} ({count:,} features)...':
   'Katman {layer_index}/{total} yazılıyor: {layer_name} ({count:,} özellik)…',
 'attempt ': 'deneme ',
 'characters).': 'karakter).',
 'connection error — ': 'bağlantı hatası — ',
 'e.g. CBD': 'örn. CBD',
 'e.g. Kenya': 'örn. Kenya',
 'e.g. Nairobi': 'örn. Nairobi',
 'e.g. NairobiCounty': 'örn. NairobiCounty',
 'elements (': 'öğe (',
 'export failed:': 'dışa aktarma başarısız:',
 'feature records).': 'özellik kaydı).',
 'feature(s)).': 'özellik)).',
 'features written.': 'özellik yazıldı.',
 'file(s) deleted.': 'dosya silindi.',
 'relation geometry assignment(s); relation-member geometry assembly is not implemented yet.':
   'ilişki geometrisi ataması; ilişki üyesi geometrisi birleştirmesi henüz uygulanmadı.',
 'relations).': 'ilişki).',
 'response_data must be a dictionary.':
   'response_data bir sözlük olmalıdır.',
 "response_data['elements'] must be a list.":
   "response_data['elements'] bir liste olmalıdır.",
 'temporary file(s) could not be deleted. They may still be in use by QGIS or another process.':
   'geçici dosya(lar) silinemedi. QGIS veya başka bir işlem tarafından hâlâ kullanılıyor olabilirler.',
 'timeout — ': 'zaman aşımı — ',
 '{output_format} export failed: {error}':
   '{output_format} dışa aktarımı başarısız oldu: {error}',
 '— Confirm Overwrite': '— Üzerine Yazmayı Onayla',
 '— Export Error': '— Dışa Aktarma Hatası',
 '— Help': '— Yardım',
 '— Output Naming': '— Çıktı Adlandırma',
}