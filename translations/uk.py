"""Ukrainian (Українська) translation pack for the OSM Data Toolkit plugin.
Keys remain the English source strings; preserve placeholders and HTML."""
TEXT = {
 '\n<h3>Quick start</h3>\n<ol>\n  <li><b>Choose an area.</b> Use the current map extent, draw a rectangle\n      on the map, or use the bounding box of selected features or a\n      layer\'s extent.</li>\n  <li><b>Tick the OSM categories</b> you need (POI, stops, roads,\n      buildings, boundaries, landuse, ...).</li>\n  <li><b>Choose an output format and folder</b>, then click\n      <b>Download OSM Data</b>.</li>\n</ol>\n\n<h3>Good to know</h3>\n<ul>\n  <li><b>GeoPackage is recommended.</b> A Shapefile cannot hold very many\n      attribute columns, so on large areas some rarely used tag columns\n      may be left out (the log tells you when this happens).</li>\n  <li><b>Keep the area focused.</b> Very large areas produce huge Overpass\n      responses and can be slow or rejected by the public servers.</li>\n  <li><b>The cache</b> lets repeat downloads of the same query reuse\n      earlier results.</li>\n  <li><b>"Unclassified OSM elements"</b> in the log is informational: they\n      are mostly untagged vertices of lines and polygons that do not belong\n      to any selected category.</li>\n</ul>\n\n<p>Data &copy; OpenStreetMap contributors, available under the\n<a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a>.</p>\n<p><i>This plugin is not endorsed by or affiliated with the\nOpenStreetMap Foundation.</i></p>\n':
 '\n<h3>Швидкий старт</h3>\n<ol>\n  <li><b>Виберіть область.</b> Використайте поточний екстент карти, намалюйте\n      прямокутник на карті або скористайтеся обмежувальною рамкою вибраних\n      об\'єктів чи екстентом шару.</li>\n  <li><b>Позначте потрібні категорії OSM</b> (POI, зупинки, дороги,\n      будівлі, межі, землекористування, ...).</li>\n  <li><b>Виберіть формат виводу та теку</b>, потім натисніть\n      <b>Завантажити дані OSM</b>.</li>\n</ol>\n\n<h3>Корисно знати</h3>\n<ul>\n  <li><b>Рекомендується GeoPackage.</b> Shapefile не може вмістити дуже багато\n      стовпців атрибутів, тому на великих територіях деякі рідко використовувані\n      стовпці тегів можуть бути пропущені (журнал повідомить вас, коли\n      це станеться).</li>\n  <li><b>Обмежуйте область.</b> Дуже великі території створюють величезні\n      відповіді Overpass і можуть працювати повільно або бути відхилені\n      публічними серверами.</li>\n  <li><b>Кеш</b> дозволяє повторним завантаженням того самого запиту\n      повторно використовувати попередні результати.</li>\n  <li><b>«Некатегоризовані елементи OSM»</b> у журналі — це інформація:\n      здебільшого це вершини ліній і полігонів без тегів, які не належать\n      до жодної вибраної категорії.</li>\n</ul>\n\n<p>Дані &copy; учасники OpenStreetMap, доступні за ліцензією\n<a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a>.</p>\n<p><i>Цей плагін не схвалений OpenStreetMap Foundation і не пов\'язаний з нею.</i></p>\n',
 ' responded successfully.': ' успішно відповів.',
 ' seconds...': ' секунд…',
 '" style="color:#0B5E8E; text-decoration:none;">OpenStreetMap contributors</a> (ODbL)':
   '" style="color:#0B5E8E; text-decoration:none;">Учасники OpenStreetMap</a> (ODbL)',
 ', east=': ', схід=',
 ', north=': ', північ=',
 ', west=': ', захід=',
 '0 selected': '0 вибрано',
 '<p>Plugin version': '<p>Версія плагіна',
 'A download is already running.': 'Завантаження вже виконується.',
 'A labelled column of feature checkboxes.':
   'Підписаний стовпець прапорців об\'єктів.',
 'AOI drawing cancelled.': 'Малювання AOI скасовано.',
 'AOI geometry is empty.': 'Геометрія AOI порожня.',
 'AOI geometry is missing.': 'Геометрія AOI відсутня.',
 'AOI name': 'Назва AOI',
 'AOI rectangle captured successfully.':
   'Прямокутник AOI успішно зафіксовано.',
 'AOI source CRS is invalid.': 'Вихідна CRS AOI недійсна.',
 'AOI validation failed:': 'Помилка перевірки AOI:',
 'AOI:': 'AOI:',
 'AOI: QGIS interface is not available.':
   'AOI: інтерфейс QGIS недоступний.',
 "AOI: click 'Draw AOI', then drag a rectangle on the QGIS map.":
   'AOI: натисніть «Намалювати AOI», потім протягніть прямокутник на карті QGIS.',
 "AOI: click 'Use Layer Extent' to use the full extent of the active QGIS layer.":
   'AOI: натисніть «Використати екстент шару», щоб використати повний екстент активного шару QGIS.',
 'AOI: click and drag on the QGIS map.':
   'AOI: клацніть і протягніть на карті QGIS.',
 'AOI: failed to resolve active layer extent':
   'AOI: не вдалося визначити екстент активного шару',
 'AOI: failed to resolve selected features':
   'AOI: не вдалося визначити вибрані об\'єкти',
 'AOI: invalid': 'AOI: недійсний',
 'AOI: no active QGIS layer.': 'AOI: немає активного шару QGIS.',
 'AOI: no feature(s) selected in the active layer.':
   'AOI: в активному шарі не вибрано жодного об\'єкта.',
 'AOI: not yet resolved': 'AOI: ще не визначено',
 "AOI: select feature(s) in the active QGIS layer, then click 'Use Selected Features'.":
   'AOI: виберіть об\'єкт(и) в активному шарі QGIS, потім натисніть «Використати вибрані об\'єкти».',
 'AOI: the active layer is not a vector layer.':
   'AOI: активний шар не є векторним шаром.',
 'AOI: unable to create': 'AOI: не вдалося створити',
 'AOI: unable to resolve': 'AOI: не вдалося визначити',
 'Activate the interactive rectangle AOI map tool.':
   'Активувати інтерактивний інструмент малювання прямокутника AOI на карті.',
 'Active layer extent': 'Екстент активного шару',
 'Active-layer extent AOI is invalid.':
   'AOI за екстентом активного шару недійсний.',
 'Active-layer extent captured successfully.':
   'Екстент активного шару успішно зафіксовано.',
 'Active-layer extent validation failed:':
   'Помилка перевірки екстенту активного шару:',
 'Administrative boundaries': 'Адміністративні межі',
 'Administrative boundary filter: all levels (no admin_level filter).':
   'Фільтр адміністративних меж: усі рівні (без фільтра admin_level).',
 'Administrative boundary levels': 'Рівні адміністративних меж',
 'Administrative boundary levels:': 'Рівні адміністративних меж:',
 'Administrative levels must be an integer, a numeric string, a sequence of levels, or None.':
   'Адміністративні рівні мають бути цілим числом, числовим рядком, послідовністю рівнів або None.',
 'All OSM feature categories cleared.': 'Усі категорії об\'єктів OSM очищено.',
 'All OSM feature categories selected.': 'Вибрано всі категорії об\'єктів OSM.',
 'All Overpass server URLs must be non-empty strings.':
   'Усі URL-адреси серверів Overpass мають бути непорожніми рядками.',
 'All Overpass servers and retry attempts failed.':
   'Усі сервери Overpass і повторні спроби не вдалися.',
 'All administrative levels will be included.':
   'Буде включено всі адміністративні рівні.',
 'All administrative levels will be included; no admin_level filter will be added to the query.':
   'Буде включено всі адміністративні рівні; фільтр admin_level до запиту не додаватиметься.',
 'All attempts failed for server ': 'Усі спроби не вдалися для сервера ',
 'All levels (0–15; no admin_level filter)':
   'Усі рівні (0–15; без фільтра admin_level)',
 'An existing output directory is required for Shapefile export.':
   'Для експорту Shapefile потрібна наявна тека виводу.',
 'An output GeoPackage path is required.':
   'Потрібен шлях виводу GeoPackage.',
 'An output name is required for Shapefile export.':
   'Для експорту Shapefile потрібна назва виводу.',
 'Append a timestamped message to the processing log.':
   'Додати повідомлення з часовою міткою до журналу обробки.',
 'Append an exported feature count to the processing log.':
   'Додати кількість експортованих об\'єктів до журналу обробки.',
 'Area of Interest': 'Область інтересу',
 'At least one OSM feature must be selected.':
   'Потрібно вибрати принаймні один об\'єкт OSM.',
 'At least one OSM feature must be supplied.':
   'Потрібно надати принаймні один об\'єкт OSM.',
 'At least one Overpass server must be provided.':
   'Потрібно вказати принаймні один сервер Overpass.',
 'Attempt details:': 'Деталі спроб:',
 'Automatically add downloaded layers to QGIS':
   'Автоматично додавати завантажені шари до QGIS',
 'Background Overpass download started.':
   'Фонове завантаження Overpass розпочато.',
 'Browse': 'Огляд',
 'Browse…': 'Огляд…',
 'Buildings': 'Будівлі',
 'Bus stops': 'Автобусні зупинки',
 'CRS:': 'CRS:',
 'Cache hit:': 'Влучення в кеш:',
 'Cache hit: using saved Overpass response ({age} day(s) old).':
   'Влучення в кеш: використовується збережена відповідь Overpass (вік {age} дн.).',
 'Cache miss:': 'Промах кешу:',
 'Cache miss: could not read saved response ({error}).':
   'Промах кешу: не вдалося прочитати збережену відповідь ({error}).',
 'Cache miss: query hash does not match the saved response.':
   'Промах кешу: хеш запиту не збігається зі збереженою відповіддю.',
 'Cache miss: saved response is incomplete or invalid.':
   'Промах кешу: збережена відповідь неповна або недійсна.',
 'Cache miss: saved response is older than {days} days.':
   'Промах кешу: збережена відповідь старша за {days} днів.',
 'Cache miss: saved response uses an unsupported cache format.':
   'Промах кешу: збережена відповідь використовує непідтримуваний формат кешу.',
 'Cached Overpass response:': 'Кешована відповідь Overpass:',
 'Cancel': 'Скасувати',
 'Cancellation has already been requested.': 'Скасування вже запитано.',
 'Cancellation requested': 'Запитано скасування',
 'Cancellation requested. If an HTTP request is already active, the downloader will stop when that request returns or times out.':
   'Запитано скасування. Якщо HTTP-запит уже активний, завантажувач зупиниться, коли цей запит повернеться або завершиться за тайм-аутом.',
 'Cancellation requested; waiting for the current request to finish...':
   'Запитано скасування; очікування завершення поточного запиту…',
 'Cannot draw AOI because the QGIS interface is unavailable.':
   'Неможливо намалювати AOI, оскільки інтерфейс QGIS недоступний.',
 'Cannot resolve active-layer extent because QGIS is unavailable.':
   'Неможливо визначити екстент активного шару, оскільки QGIS недоступний.',
 'Cannot resolve current map extent because QGIS is unavailable.':
   'Неможливо визначити поточний екстент карти, оскільки QGIS недоступний.',
 'Cannot resolve selected-feature AOI because QGIS is unavailable.':
   'Неможливо визначити AOI за вибраними об\'єктами, оскільки QGIS недоступний.',
 'Cannot transform an empty geometry.':
   'Неможливо перетворити порожню геометрію.',
 'Capture the current QGIS map canvas extent.':
   'Зафіксувати поточний екстент полотна карти QGIS.',
 'Choose all available levels, or select one or more levels to download (for example, 5–8 or level 5).':
   'Виберіть усі доступні рівні або один чи кілька рівнів для завантаження (наприклад, 5–8 або рівень 5).',
 'Choose an output directory before downloading.':
   'Виберіть теку виводу перед завантаженням.',
 'City name': 'Назва міста',
 'Classifying OSM elements and preparing GeoPackage layers.':
   'Класифікація елементів OSM і підготовка шарів GeoPackage.',
 'Classifying OSM elements and preparing Shapefile outputs.':
   'Класифікація елементів OSM і підготовка вихідних даних Shapefile.',
 'Clear all': 'Очистити все',
 'Clear log': 'Очистити журнал',
 'Clear only the visible log, without changing processing settings.':
   'Очистити лише видимий журнал, не змінюючи налаштування обробки.',
 'Clear selected levels so the user can make a narrower selection.':
   'Очистити вибрані рівні, щоб користувач міг зробити вужчий вибір.',
 'Clear the messages currently shown in the Processing Log.':
   'Очистити повідомлення, які зараз показуються в журналі обробки.',
 'Clear the previous AOI and display guidance for the chosen method.':
   'Очистити попередній AOI і показати підказку для вибраного методу.',
 'Close': 'Закрити',
 'Collect optional filename components before exporting OSM data.':
   'Зібрати необов\'язкові компоненти імені файлу перед експортом даних OSM.',
 'Compact product header above the scrollable workflow.':
   'Компактний заголовок продукту над прокручуваним робочим процесом.',
 'Connection error on server ': 'Помилка з\'єднання на сервері ',
 'Continue to Download': 'Продовжити до завантаження',
 'Convert a name component into a Windows-safe filename token.':
   'Перетворити компонент назви на безпечний для Windows токен імені файлу.',
 'Convert the drawn rectangle into the standard AOI object.':
   'Перетворити намальований прямокутник на стандартний об\'єкт AOI.',
 'Converting OSM response to GeoPackage...':
   'Перетворення відповіді OSM у GeoPackage…',
 'Converting OSM response to Shapefiles...':
   'Перетворення відповіді OSM у Shapefile…',
 'Could not combine the selected feature geometries.':
   'Не вдалося об\'єднати геометрії вибраних об\'єктів.',
 "Could not create Shapefile staging layer '{layer_name}'.":
   'Не вдалося створити проміжний шар Shapefile «{layer_name}».',
 'Could not create an empty bus_stops_points layer.':
   'Не вдалося створити порожній шар bus_stops_points.',
 "Could not create temporary QGIS layer '{layer_name}'.":
   'Не вдалося створити тимчасовий шар QGIS «{layer_name}».',
 'Could not create temporary layer for admin_level {admin_level}.':
   'Не вдалося створити тимчасовий шар для admin_level {admin_level}.',
 'Could not create the merged bus_stops_points layer.':
   'Не вдалося створити об\'єднаний шар bus_stops_points.',
 'Could not delete temporary file': 'Не вдалося видалити тимчасовий файл',
 "Could not load feature definition '{feature_key}': {error}":
   'Не вдалося завантажити визначення об\'єкта «{feature_key}»: {error}',
 'Could not merge bus-station centroids into bus-stop points.':
   'Не вдалося об\'єднати центроїди автостанцій із точками автобусних зупинок.',
 'Could not overwrite existing output file: {error}':
   'Не вдалося перезаписати наявний вихідний файл: {error}',
 'Could not populate Shapefile for admin_level {admin_level}.':
   'Не вдалося заповнити Shapefile для admin_level {admin_level}.',
 "Could not populate temporary layer '{layer_name}'.":
   'Не вдалося заповнити тимчасовий шар «{layer_name}».',
 'Could not prepare the Overpass query:':
   'Не вдалося підготувати запит Overpass:',
 "Could not reopen intermediate GeoPackage layer '{layer_name}'.":
   'Не вдалося повторно відкрити проміжний шар GeoPackage «{layer_name}».',
 'Could not restore previous QGIS map tool:':
   'Не вдалося відновити попередній інструмент карти QGIS:',
 'Could not search for temporary GeoPackages:':
   'Не вдалося виконати пошук тимчасових GeoPackage:',
 'Country name': 'Назва країни',
 'Create one section panel and return it with its body layout.':
   'Створити одну панель розділу й повернути її разом із макетом вмісту.',
 'Created bus_stops_points from bus-station polygon centroids.':
   'Створено bus_stops_points із центроїдів полігонів автостанцій.',
 'Current QGIS map extent': 'Поточний екстент карти QGIS',
 'Current QGIS map extent resolved.':
   'Поточний екстент карти QGIS визначено.',
 'Data © <a href="': 'Дані © <a href="',
 'Deleted temporary workspace file:':
   'Видалено тимчасовий файл робочої області:',
 'Details:': 'Деталі:',
 'Download': 'Завантажити',
 'Download OSM Data': 'Завантажити дані OSM',
 'Download OpenStreetMap data for any area and load it straight into QGIS.':
   'Завантажте дані OpenStreetMap для будь-якої області та завантажте їх безпосередньо в QGIS.',
 'Download cancelled because existing output files were not approved for overwrite.':
   'Завантаження скасовано, оскільки перезапис наявних вихідних файлів не було підтверджено.',
 'Download cancelled before it started.':
   'Завантаження скасовано до його початку.',
 'Download cancelled before results were returned.':
   'Завантаження скасовано до повернення результатів.',
 'Download cancelled before starting.':
   'Завантаження скасовано до початку.',
 'Download cancelled in the output-naming dialog.':
   'Завантаження скасовано в діалозі іменування вихідних файлів.',
 'Download cancelled.': 'Завантаження скасовано.',
 'Download cancelled; existing files preserved.':
   'Завантаження скасовано; наявні файли збережено.',
 'Download stopped.': 'Завантаження зупинено.',
 'Download succeeded, but export failed.':
   'Завантаження виконано успішно, але експорт не вдався.',
 'Downloading OSM data from Overpass...':
   'Завантаження даних OSM із Overpass…',
 'Draw AOI': 'Намалювати AOI',
 'Draw a rectangle on the QGIS map to define the AOI.':
   'Намалюйте прямокутник на карті QGIS, щоб визначити AOI.',
 'Draw rectangle on map': 'Намалювати прямокутник на карті',
 'Draw the AOI rectangle on the QGIS map.':
   'Намалюйте прямокутник AOI на карті QGIS.',
 'Drawn AOI validation failed:':
   'Помилка перевірки намальованого AOI:',
 'Drawn rectangle': 'Намальований прямокутник',
 'Drawn rectangle AOI captured successfully.':
   'Намальований прямокутник AOI успішно зафіксовано.',
 'ERROR:': 'ПОМИЛКА:',
 'East:': 'Схід:',
 'Enable level checkboxes only when a specific selection is active.':
   'Увімкнути прапорці рівнів лише коли активний конкретний вибір.',
 'Enable only the AOI action button for the selected method.':
   'Увімкнути лише кнопку дії AOI для вибраного методу.',
 'Enable or disable controls while a download is running.':
   'Увімкнути або вимкнути елементи керування під час завантаження.',
 'Enter at least one name (City, Country, Region, or AOI).':
   'Введіть принаймні одну назву (місто, країна, регіон або AOI).',
 'Enter one or more name components. Blank fields will be skipped, and the remaining names will be joined with underscores. The selected output format will be retained.':
   'Введіть один або кілька компонентів назви. Порожні поля буде пропущено, а решту назв з\'єднано символами підкреслення. Вибраний формат виводу буде збережено.',
 'Enter_a_name_to_preview': 'Введіть_назву_для_попереднього_перегляду',
 'Export cancelled: output name is missing.':
   'Експорт скасовано: відсутня назва виводу.',
 'Export complete:': 'Експорт завершено:',
 'Export the downloaded response and optionally load its layers.':
   'Експортувати завантажену відповідь і за бажанням завантажити її шари.',
 'Failed to activate rectangle AOI tool:':
   'Не вдалося активувати інструмент прямокутника AOI:',
 'Failed to create AOI.': 'Не вдалося створити AOI.',
 'Failed to process drawn rectangle AOI:':
   'Не вдалося обробити намальований прямокутник AOI:',
 'Failed to resolve active-layer extent.':
   'Не вдалося визначити екстент активного шару.',
 'Failed to resolve active-layer extent:':
   'Не вдалося визначити екстент активного шару:',
 'Failed to resolve current QGIS map extent:':
   'Не вдалося визначити поточний екстент карти QGIS:',
 'Failed to resolve selected-feature AOI.':
   'Не вдалося визначити AOI за вибраними об\'єктами.',
 'Failed to resolve selected-feature AOI:':
   'Не вдалося визначити AOI за вибраними об\'єктами:',
 "Failed to write layer '{layer_name}' to '{output_path}': {error}":
   'Не вдалося записати шар «{layer_name}» у «{output_path}»: {error}',
 "Feature '{feature_key}' has no tag definitions.":
   'Об\'єкт «{feature_key}» не має визначень тегів.',
 'Feature specification  does not expose a tag-filter mapping.':
   'Специфікація об\'єкта не надає зіставлення фільтрів тегів.',
 'Ferry stops': 'Поромні зупинки',
 'Filename preview': 'Попередній перегляд імені файлу',
 'Full documentation': 'Повна документація',
 'Generated Overpass query (': 'Згенерований запит Overpass (',
 'GeoPackage': 'GeoPackage',
 'GeoPackage layer(s) to QGIS.': 'шар(и) GeoPackage у QGIS.',
 'GeoPackage saved:': 'GeoPackage збережено:',
 'HTTP error on server ': 'Помилка HTTP на сервері ',
 'HTTP error — ': 'помилка HTTP — ',
 'HTTP {status} error on server {index}/{total}.':
   'Помилка HTTP {status} на сервері {index}/{total}.',
 'Handle a drawing tool deactivation initiated outside this dialog.':
   'Обробити деактивацію інструмента малювання, ініційовану поза цим діалогом.',
 'Help': 'Довідка',
 'Invalid east longitude: {value}':
   'Недійсна східна довгота: {value}',
 'Invalid north latitude: {value}':
   'Недійсна північна широта: {value}',
 'Invalid response from server ': 'Недійсна відповідь від сервера ',
 'Invalid south latitude: {value}':
   'Недійсна південна широта: {value}',
 'Invalid west longitude: {value}':
   'Недійсна західна довгота: {value}',
 'Keep the numeric readout in step with the progress bar.':
   'Синхронізувати числове значення з індикатором поступу.',
 'Land & built environment': 'Земля й забудоване середовище',
 'Landuse': 'Землекористування',
 'Language:': 'Мова:',
 'Linear features': 'Лінійні об\'єкти',
 'Load the saved interface language and translate visible UI strings.':
   'Завантажити збережену мову інтерфейсу й перекласти видимі рядки інтерфейсу.',
 'Local response cache is disabled.':
   'Локальний кеш відповідей вимкнено.',
 'Main OSM Data Toolkit window.': 'Головне вікно OSM Data Toolkit.',
 'Manually capture the map extent after the user pans or zooms.':
   'Вручну зафіксувати екстент карти після панорамування чи масштабування користувачем.',
 'Merged bus-station polygon centroids into bus_stops_points.':
   'Центроїди полігонів автостанцій об\'єднано в bus_stops_points.',
 'No Overpass selectors were generated.':
   'Не було згенеровано жодного селектора Overpass.',
 'No active QGIS layer is available.':
   'Немає доступного активного шару QGIS.',
 'No active layer is available.': 'Немає доступного активного шару.',
 'No exportable features matched the selected categories. Try another AOI or select additional OSM feature categories.':
   'Жоден об\'єкт, що підлягає експорту, не відповідає вибраним категоріям. Спробуйте інший AOI або виберіть додаткові категорії об\'єктів OSM.',
 'No features are selected in the active layer.':
   'В активному шарі не вибрано жодного об\'єкта.',
 'No levels selected. Select at least one level to continue.':
   'Рівні не вибрано. Виберіть принаймні один рівень, щоб продовжити.',
 'No selected features found.': 'Вибраних об\'єктів не знайдено.',
 'No valid Area of Interest is available. Select an AOI method and resolve the AOI before downloading.':
   'Немає дійсної області інтересу. Виберіть метод AOI і визначте AOI перед завантаженням.',
 'North:': 'Північ:',
 'Note: {layer_name} has too many tag columns for one Shapefile (DBF size limit); {count} rarely-used columns were left out.':
   'Примітка: {layer_name} має забагато стовпців тегів для одного Shapefile (обмеження розміру DBF); {count} рідко використовуваних стовпців пропущено.',
 'OSM Data Toolkit': 'OSM Data Toolkit',
 'OSM Data Toolkit initialised.':
   'OSM Data Toolkit ініціалізовано.',
 'OSM Feature Categories': 'Категорії об\'єктів OSM',
 'OSM export completed successfully.':
   'Експорт OSM успішно завершено.',
 'One or more output files with this name already exist. Do you want to overwrite the matching output files?':
   'Один або кілька вихідних файлів із цією назвою вже існують. Перезаписати відповідні вихідні файли?',
 'Only the selected levels': 'Лише вибрані рівні',
 'Only validated Overpass responses can be cached.':
   'Кешувати можна лише перевірені відповіді Overpass.',
 'Open public spaces': 'Відкриті громадські простори',
 'Open the in-plugin help with links to the online documentation.':
   'Відкрити довідку в плагіні з посиланнями на онлайн-документацію.',
 'Output Settings': 'Налаштування виводу',
 'Output directory': 'Тека виводу',
 'Output directory selected:': 'Вибрано теку виводу:',
 'Output format': 'Формат виводу',
 'Output settings': 'Налаштування виводу',
 'Overpass download cancelled.': 'Завантаження Overpass скасовано.',
 'Overpass download completed:': 'Завантаження Overpass завершено:',
 'Overpass download failed.': 'Завантаження Overpass не вдалося.',
 'Overpass download failed:': 'Завантаження Overpass не вдалося:',
 'Overpass download running...': 'Завантаження Overpass виконується…',
 'Overpass download was cancelled by the caller.':
   'Завантаження Overpass було скасовано стороною, що викликала.',
 'Overpass query must be a non-empty string.':
   'Запит Overpass має бути непорожнім рядком.',
 "Overpass response 'elements' field is not a list.":
   'Поле «elements» відповіді Overpass не є списком.',
 "Overpass response does not contain an 'elements' field.":
   'Відповідь Overpass не містить поля «elements».',
 'Overpass response is not a JSON object.':
   'Відповідь Overpass не є об\'єктом JSON.',
 'Overpass response received successfully:':
   'Відповідь Overpass успішно отримано:',
 'Overpass server ': 'Сервер Overpass ',
 'Overpass server returned invalid JSON. Response preview: ':
   'Сервер Overpass повернув недійсний JSON. Попередній перегляд відповіді: ',
 'Overpass servers available:': 'Доступні сервери Overpass:',
 'Overpass timeout must be greater than zero.':
   'Тайм-аут Overpass має бути більшим за нуль.',
 'Plugin version': 'Версія плагіна',
 'Points of interest (POI)': 'Точки інтересу (POI)',
 'Prepared {index:,} of {total:,} OSM elements for export...':
   'Підготовлено {index:,} з {total:,} елементів OSM до експорту…',
 'Preparing Overpass download...': 'Підготовка завантаження Overpass…',
 'Preparing Overpass query.': 'Підготовка запиту Overpass.',
 'Processing Options': 'Параметри обробки',
 'Processing log': 'Журнал обробки',
 'Processing messages will appear here...':
   'Повідомлення обробки з\'являтимуться тут…',
 'Processing options': 'Параметри обробки',
 'Public transport & places': 'Громадський транспорт і місця',
 'QGIS interface object was not detected. Canvas-dependent AOI tools are disabled.':
   'Об\'єкт інтерфейсу QGIS не виявлено. Інструменти AOI, що залежать від полотна, вимкнено.',
 'QGIS map canvas could not be accessed.':
   'Не вдалося отримати доступ до полотна карти QGIS.',
 'QGIS map canvas is unavailable.':
   'Полотно карти QGIS недоступне.',
 'Rail stops': 'Залізничні зупинки',
 'Railways': 'Залізниці',
 'Read the plugin version from metadata.txt (empty string if absent).':
   'Прочитати версію плагіна з metadata.txt (порожній рядок, якщо відсутній).',
 'Read, validate and store the current QGIS map canvas extent.':
   'Прочитати, перевірити й зберегти поточний екстент полотна карти QGIS.',
 'Ready.': 'Готово.',
 'Rectangle AOI drawing tool activated.':
   'Інструмент малювання прямокутника AOI активовано.',
 'Rectangle AOI drawing was cancelled.':
   'Малювання прямокутника AOI скасовано.',
 'Region name': 'Назва регіону',
 'Report an issue': 'Повідомити про проблему',
 'Request cooperative cancellation of the background worker.':
   'Запросити кооперативне скасування фонового працівника.',
 'Request error on server ': 'Помилка запиту на сервері ',
 'Restore default GUI settings when the dialog closes.':
   'Відновити типові налаштування GUI після закриття діалогу.',
 'Restore the GUI once the background thread has stopped.':
   'Відновити GUI після зупинки фонового потоку.',
 'Restore the QGIS map tool active before rectangle drawing.':
   'Відновити інструмент карти QGIS, активний до малювання прямокутника.',
 'Restore the map tool and reset state before hiding the dialog.':
   'Відновити інструмент карти та скинути стан перед приховуванням діалогу.',
 'Retrying in ': 'Повторна спроба через ',
 'Return selected levels, or None when all levels are requested.':
   'Повернути вибрані рівні або None, якщо запитано всі рівні.',
 'Return the combined, sanitized filename prefix.':
   'Повернути об\'єднаний, очищений префікс імені файлу.',
 'Return the mapping between feature keys and GUI checkboxes.':
   'Повернути зіставлення між ключами об\'єктів і прапорцями GUI.',
 'Return the selected GUI feature keys.':
   'Повернути вибрані ключі об\'єктів GUI.',
 'Roads': 'Дороги',
 'Run a modal dialog on both Qt5 and Qt6.':
   'Запустити модальний діалог як у Qt5, так і в Qt6.',
 'Select Output Directory': 'Вибрати теку виводу',
 'Select a vector layer with selected features.':
   'Виберіть векторний шар із вибраними об\'єктами.',
 'Select all': 'Вибрати все',
 'Select an active QGIS layer.': 'Виберіть активний шар QGIS.',
 'Select at least one OSM feature category before downloading.':
   'Виберіть принаймні одну категорію об\'єктів OSM перед завантаженням.',
 'Select at least one administrative level, or choose All levels.':
   'Виберіть принаймні один адміністративний рівень або виберіть «Усі рівні».',
 'Select at least one administrative level, or use None to retrieve all levels.':
   'Виберіть принаймні один адміністративний рівень або використайте None, щоб отримати всі рівні.',
 'Select levels 0–15 and switch to specific-level mode.':
   'Вибрати рівні 0–15 і перемкнутися в режим конкретних рівнів.',
 'Select one or more features in the active layer.':
   'Виберіть один або кілька об\'єктів в активному шарі.',
 'Select output directory...': 'Вибрати теку виводу…',
 'Selected administrative levels:': 'Вибрані адміністративні рівні:',
 'Selected feature IDs:': 'Ідентифікатори вибраних об\'єктів:',
 'Selected feature(s) in active layer':
   'Вибрані об\'єкти в активному шарі',
 'Selected features (': 'Вибрані об\'єкти (',
 'Selected-feature AOI captured successfully (':
   'AOI за вибраними об\'єктами успішно зафіксовано (',
 'Selected-feature AOI captured successfully.':
   'AOI за вибраними об\'єктами успішно зафіксовано.',
 'Selected-feature AOI is invalid.':
   'AOI за вибраними об\'єктами недійсний.',
 'Selected-feature AOI requires a vector layer.':
   'AOI за вибраними об\'єктами потребує векторного шару.',
 'Selected-feature AOI validation failed:':
   'Помилка перевірки AOI за вибраними об\'єктами:',
 'Sending query to Overpass...': 'Надсилання запиту до Overpass…',
 'Server ': 'Сервер ',
 'Shapefile': 'Shapefile',
 'Shapefile export completed in:':
   'Експорт Shapefile завершено за:',
 'Shapefile field names shortened for':
   'Назви полів Shapefile скорочено для',
 'Shapefile layer(s) to QGIS.': 'шар(и) Shapefile у QGIS.',
 'Short in-plugin help with links to the full online documentation.':
   'Коротка довідка в плагіні з посиланнями на повну онлайн-документацію.',
 'Show AOI coordinates and source CRS in the dialog.':
   'Показати координати AOI та вихідну CRS у діалозі.',
 'Show a concise description of the active administrative filter.':
   'Показати стислий опис активного адміністративного фільтра.',
 'Source CRS is invalid.': 'Вихідна CRS недійсна.',
 'South latitude cannot be greater than north latitude.':
   'Південна широта не може бути більшою за північну.',
 'South:': 'Південь:',
 'Starting Overpass download...':
   'Запуск завантаження Overpass…',
 'Supporting copy: muted, wrapped and visually quiet.':
   'Допоміжний текст: приглушений, з перенесеннями й візуально спокійний.',
 "Tag '{tag}' contains an empty value list.":
   'Тег «{tag}» містить порожній список значень.',
 'Temporary workspace cleanup complete:':
   'Очищення тимчасової робочої області завершено:',
 'Temporary workspace cleanup complete: no matching files found.':
   'Очищення тимчасової робочої області завершено: відповідних файлів не знайдено.',
 'Temporary-file cleanup skipped: workspace directory is invalid.':
   'Очищення тимчасових файлів пропущено: тека робочої області недійсна.',
 'The OSM download succeeded, but the output could not be created.':
   'Завантаження OSM виконано успішно, але вихідні дані створити не вдалося.',
 "The Overpass response must be a JSON object with an 'elements' list.":
   'Відповідь Overpass має бути об\'єктом JSON зі списком «elements».',
 'The QGIS map canvas CRS is invalid.':
   'CRS полотна карти QGIS недійсна.',
 'The active layer CRS is invalid.':
   'CRS активного шару недійсна.',
 'The active layer extent is empty.':
   'Екстент активного шару порожній.',
 'The active layer must be a vector layer.':
   'Активний шар має бути векторним шаром.',
 'The combined name is too long. Shorten one or more components.':
   'Об\'єднана назва задовга. Скоротіть один або кілька компонентів.',
 'The combined selected-feature geometry is empty.':
   'Об\'єднана геометрія вибраних об\'єктів порожня.',
 'The current AOI is invalid:': 'Поточний AOI недійсний:',
 'The current QGIS map extent is empty.':
   'Поточний екстент карти QGIS порожній.',
 'The dialog cannot close while a download thread is running. Cancellation has been requested; close the dialog after it stops.':
   'Діалог не може закритися, поки виконується потік завантаження. Скасування запитано; закрийте діалог після його зупинки.',
 'The download completed, but no confirmed output name was available.':
   'Завантаження завершено, але підтвердженої назви виводу не було.',
 "The exported Shapefile '{path}' could not be opened in QGIS.":
   'Експортований Shapefile «{path}» не вдалося відкрити в QGIS.',
 "The exported layer '{layer_name}' could not be opened in QGIS.":
   'Експортований шар «{layer_name}» не вдалося відкрити в QGIS.',
 'The output name does not contain any valid filename characters.':
   'Назва виводу не містить допустимих символів імені файлу.',
 'The output name is empty after filename validation.':
   'Назва виводу порожня після перевірки імені файлу.',
 'The selected features contain no valid geometry.':
   'Вибрані об\'єкти не містять дійсної геометрії.',
 'The selected output directory does not exist. Choose an existing folder.':
   'Вибрана тека виводу не існує. Виберіть наявну теку.',
 'There is no active download to cancel.':
   'Немає активного завантаження для скасування.',
 'Timeout on server ': 'Тайм-аут на сервері ',
 'Translate widget labels while preserving each original English string.':
   'Перекласти мітки віджетів, зберігаючи кожен оригінальний англійський рядок.',
 'Trying Overpass server ': 'Спроба використати сервер Overpass ',
 'Unable to start AOI drawing:': 'Не вдалося розпочати малювання AOI:',
 'Unclassified OSM elements not written to feature layers:':
   'Некатегоризовані елементи OSM, не записані до шарів об\'єктів:',
 'Unsupported geometry family: {geometry_family}':
   'Непідтримувана родина геометрій: {geometry_family}',
 "Unsupported geometry type '{geometry_type}' for feature '{feature_key}'.":
   'Непідтримуваний тип геометрії «{geometry_type}» для об\'єкта «{feature_key}».',
 'Unsupported geometry type for Shapefile export: {geometry_type}':
   'Непідтримуваний тип геометрії для експорту Shapefile: {geometry_type}',
 "Unsupported match mode '{mode}' for feature '{feature_key}'.":
   'Непідтримуваний режим зіставлення «{mode}» для об\'єкта «{feature_key}».',
 'Unsupported output format:': 'Непідтримуваний формат виводу:',
 "Unsupported tag value type for '{feature_key}': {value_type}":
   'Непідтримуваний тип значення тега для «{feature_key}»: {value_type}',
 'Update Current QGIS Map Extent':
   'Оновити поточний екстент карти QGIS',
 'Update the "N selected" count next to the category heading.':
   'Оновити лічильник «N вибрано» поруч із заголовком категорії.',
 'Update the filename preview as the user edits the components.':
   'Оновлювати попередній перегляд імені файлу під час редагування компонентів користувачем.',
 'Use Layer Extent': 'Використати екстент шару',
 'Use Selected Features': 'Використати вибрані об\'єкти',
 'Use local cache where available':
   'Використовувати локальний кеш, де доступно',
 'Use selected features in the active vector layer as the AOI.':
   'Використати вибрані об\'єкти в активному векторному шарі як AOI.',
 'Use the full extent of the active QGIS layer as the AOI.':
   'Використати повний екстент активного шару QGIS як AOI.',
 'Use the full extent of the active QGIS layer.':
   'Використати повний екстент активного шару QGIS.',
 'Use the selected features of the active vector layer as the AOI.':
   'Використати вибрані об\'єкти активного векторного шару як AOI.',
 'Using cached data; no Overpass network request was needed.':
   'Використовуються кешовані дані; мережевий запит Overpass не знадобився.',
 'Validate filename and any explicitly selected admin levels.':
   'Перевірити ім\'я файлу та будь-які явно вибрані адміністративні рівні.',
 'Validate inputs and start the background Overpass download.':
   'Перевірити вхідні дані й запустити фонове завантаження Overpass.',
 'WGS84 AOI bbox: south=': 'Обмежувальна рамка AOI у WGS84: південь=',
 'WGS84 AOI geometry is not available.':
   'Геометрія AOI у WGS84 недоступна.',
 'Warning: download succeeded, but the response could not be cached:':
   'Попередження: завантаження виконано успішно, але відповідь не вдалося закешувати:',
 'Waterways': 'Водні шляхи',
 'West longitude cannot be greater than east longitude.':
   'Західна довгота не може бути більшою за східну.',
 'West:': 'Захід:',
 'Writing Shapefile {layer_index}/{total}: {layer_name}...':
   'Запис Shapefile {layer_index}/{total}: {layer_name}…',
 'Writing layer {layer_index}/{total}: {layer_name} ({count:,} features)...':
   'Запис шару {layer_index}/{total}: {layer_name} ({count:,} об\'єктів)…',
 'attempt ': 'спроба ',
 'characters).': 'символів).',
 'connection error — ': 'помилка з\'єднання — ',
 'e.g. CBD': 'напр. CBD',
 'e.g. Kenya': 'напр. Кенія',
 'e.g. Nairobi': 'напр. Найробі',
 'e.g. NairobiCounty': 'напр. NairobiCounty',
 'elements (': 'елементів (',
 'export failed:': 'помилка експорту:',
 'feature records).': 'записів об\'єктів).',
 'feature(s)).': 'об\'єкт(ів)).',
 'features written.': 'об\'єктів записано.',
 'file(s) deleted.': 'файл(ів) видалено.',
 'relation geometry assignment(s); relation-member geometry assembly is not implemented yet.':
   'призначень геометрії відношення; складання геометрії членів відношення ще не реалізовано.',
 'relations).': 'відношень).',
 'response_data must be a dictionary.':
   'response_data має бути словником.',
 "response_data['elements'] must be a list.":
   "response_data['elements'] має бути списком.",
 'temporary file(s) could not be deleted. They may still be in use by QGIS or another process.':
   'тимчасові файли не вдалося видалити. Можливо, вони ще використовуються QGIS або іншим процесом.',
 'timeout — ': 'тайм-аут — ',
 '{output_format} export failed: {error}':
   'Помилка експорту {output_format}: {error}',
 '— Confirm Overwrite': '— Підтвердити перезапис',
 '— Export Error': '— Помилка експорту',
 '— Help': '— Довідка',
 '— Output Naming': '— Іменування вихідних файлів',
}