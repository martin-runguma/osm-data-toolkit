"""Russian (Русский) translation pack for the OSM Data Toolkit plugin.
Keys remain the English source strings; preserve placeholders and HTML."""
TEXT = {
 '\n<h3>Quick start</h3>\n<ol>\n  <li><b>Choose an area.</b> Use the current map extent, draw a rectangle\n      on the map, or use the bounding box of selected features or a\n      layer\'s extent.</li>\n  <li><b>Tick the OSM categories</b> you need (POI, stops, roads,\n      buildings, boundaries, landuse, ...).</li>\n  <li><b>Choose an output format and folder</b>, then click\n      <b>Download OSM Data</b>.</li>\n</ol>\n\n<h3>Good to know</h3>\n<ul>\n  <li><b>GeoPackage is recommended.</b> A Shapefile cannot hold very many\n      attribute columns, so on large areas some rarely used tag columns\n      may be left out (the log tells you when this happens).</li>\n  <li><b>Keep the area focused.</b> Very large areas produce huge Overpass\n      responses and can be slow or rejected by the public servers.</li>\n  <li><b>The cache</b> lets repeat downloads of the same query reuse\n      earlier results.</li>\n  <li><b>"Unclassified OSM elements"</b> in the log is informational: they\n      are mostly untagged vertices of lines and polygons that do not belong\n      to any selected category.</li>\n</ul>\n\n<p>Data &copy; OpenStreetMap contributors, available under the\n<a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a>.</p>\n<p><i>This plugin is not endorsed by or affiliated with the\nOpenStreetMap Foundation.</i></p>\n':
 '\n<h3>Быстрый старт</h3>\n<ol>\n  <li><b>Выберите область.</b> Используйте текущий экстент карты, нарисуйте\n      прямоугольник на карте или используйте ограничивающий прямоугольник\n      выбранных объектов либо экстент слоя.</li>\n  <li><b>Отметьте нужные категории OSM</b> (POI, остановки, дороги,\n      здания, границы, землепользование, ...).</li>\n  <li><b>Выберите формат вывода и папку</b>, затем нажмите\n      <b>Скачать данные OSM</b>.</li>\n</ol>\n\n<h3>Полезно знать</h3>\n<ul>\n  <li><b>Рекомендуется GeoPackage.</b> Shapefile не может содержать очень много\n      столбцов атрибутов, поэтому на больших территориях некоторые редко\n      используемые столбцы тегов могут быть опущены (журнал сообщит вам, когда\n      это произойдёт).</li>\n  <li><b>Ограничивайте область.</b> Очень большие территории создают огромные\n      ответы Overpass и могут работать медленно или быть отклонены публичными\n      серверами.</li>\n  <li><b>Кэш</b> позволяет повторным загрузкам того же запроса использовать\n      ранее полученные результаты.</li>\n  <li><b>«Неклассифицированные элементы OSM»</b> в журнале — это информация:\n      в основном это вершины линий и полигонов без тегов, не относящиеся\n      ни к одной выбранной категории.</li>\n</ul>\n\n<p>Данные &copy; участники OpenStreetMap, доступны по лицензии\n<a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a>.</p>\n<p><i>Этот плагин не одобрен OpenStreetMap Foundation и не связан с ней.</i></p>\n',
 ' responded successfully.': ' ответил успешно.',
 ' seconds...': ' секунд…',
 '" style="color:#0B5E8E; text-decoration:none;">OpenStreetMap contributors</a> (ODbL)':
   '" style="color:#0B5E8E; text-decoration:none;">Участники OpenStreetMap</a> (ODbL)',
 ', east=': ', восток=',
 ', north=': ', север=',
 ', west=': ', запад=',
 '0 selected': '0 выбрано',
 '<p>Plugin version': '<p>Версия плагина',
 'A download is already running.': 'Загрузка уже выполняется.',
 'A labelled column of feature checkboxes.':
   'Подписанный столбец флажков объектов.',
 'AOI drawing cancelled.': 'Рисование AOI отменено.',
 'AOI geometry is empty.': 'Геометрия AOI пуста.',
 'AOI geometry is missing.': 'Геометрия AOI отсутствует.',
 'AOI name': 'Имя AOI',
 'AOI rectangle captured successfully.':
   'Прямоугольник AOI успешно зафиксирован.',
 'AOI source CRS is invalid.': 'Исходная CRS AOI недействительна.',
 'AOI validation failed:': 'Ошибка проверки AOI:',
 'AOI:': 'AOI:',
 'AOI: QGIS interface is not available.':
   'AOI: интерфейс QGIS недоступен.',
 "AOI: click 'Draw AOI', then drag a rectangle on the QGIS map.":
   'AOI: нажмите «Нарисовать AOI», затем перетащите прямоугольник на карте QGIS.',
 "AOI: click 'Use Layer Extent' to use the full extent of the active QGIS layer.":
   'AOI: нажмите «Использовать экстент слоя», чтобы использовать полный экстент активного слоя QGIS.',
 'AOI: click and drag on the QGIS map.':
   'AOI: щёлкните и перетащите на карте QGIS.',
 'AOI: failed to resolve active layer extent':
   'AOI: не удалось определить экстент активного слоя',
 'AOI: failed to resolve selected features':
   'AOI: не удалось определить выбранные объекты',
 'AOI: invalid': 'AOI: недействителен',
 'AOI: no active QGIS layer.': 'AOI: нет активного слоя QGIS.',
 'AOI: no feature(s) selected in the active layer.':
   'AOI: в активном слое не выбрано ни одного объекта.',
 'AOI: not yet resolved': 'AOI: ещё не определён',
 "AOI: select feature(s) in the active QGIS layer, then click 'Use Selected Features'.":
   'AOI: выберите объект(ы) в активном слое QGIS, затем нажмите «Использовать выбранные объекты».',
 'AOI: the active layer is not a vector layer.':
   'AOI: активный слой не является векторным слоем.',
 'AOI: unable to create': 'AOI: не удалось создать',
 'AOI: unable to resolve': 'AOI: не удалось определить',
 'Activate the interactive rectangle AOI map tool.':
   'Активировать интерактивный инструмент рисования прямоугольника AOI на карте.',
 'Active layer extent': 'Экстент активного слоя',
 'Active-layer extent AOI is invalid.':
   'AOI по экстенту активного слоя недействителен.',
 'Active-layer extent captured successfully.':
   'Экстент активного слоя успешно зафиксирован.',
 'Active-layer extent validation failed:':
   'Ошибка проверки экстента активного слоя:',
 'Administrative boundaries': 'Административные границы',
 'Administrative boundary filter: all levels (no admin_level filter).':
   'Фильтр административных границ: все уровни (без фильтра admin_level).',
 'Administrative boundary levels': 'Уровни административных границ',
 'Administrative boundary levels:': 'Уровни административных границ:',
 'Administrative levels must be an integer, a numeric string, a sequence of levels, or None.':
   'Административные уровни должны быть целым числом, числовой строкой, последовательностью уровней или None.',
 'All OSM feature categories cleared.': 'Все категории объектов OSM сброшены.',
 'All OSM feature categories selected.': 'Выбраны все категории объектов OSM.',
 'All Overpass server URLs must be non-empty strings.':
   'Все URL серверов Overpass должны быть непустыми строками.',
 'All Overpass servers and retry attempts failed.':
   'Все серверы Overpass и повторные попытки завершились неудачно.',
 'All administrative levels will be included.':
   'Будут включены все административные уровни.',
 'All administrative levels will be included; no admin_level filter will be added to the query.':
   'Будут включены все административные уровни; фильтр admin_level в запрос не добавляется.',
 'All attempts failed for server ': 'Все попытки не удались для сервера ',
 'All levels (0–15; no admin_level filter)':
   'Все уровни (0–15; без фильтра admin_level)',
 'An existing output directory is required for Shapefile export.':
   'Для экспорта Shapefile требуется существующая папка вывода.',
 'An output GeoPackage path is required.':
   'Требуется путь к выходному GeoPackage.',
 'An output name is required for Shapefile export.':
   'Для экспорта Shapefile требуется имя вывода.',
 'Append a timestamped message to the processing log.':
   'Добавить сообщение с отметкой времени в журнал обработки.',
 'Append an exported feature count to the processing log.':
   'Добавить количество экспортированных объектов в журнал обработки.',
 'Area of Interest': 'Область интереса',
 'At least one OSM feature must be selected.':
   'Необходимо выбрать хотя бы один объект OSM.',
 'At least one OSM feature must be supplied.':
   'Необходимо указать хотя бы один объект OSM.',
 'At least one Overpass server must be provided.':
   'Необходимо указать хотя бы один сервер Overpass.',
 'Attempt details:': 'Подробности попыток:',
 'Automatically add downloaded layers to QGIS':
   'Автоматически добавлять загруженные слои в QGIS',
 'Background Overpass download started.':
   'Фоновая загрузка Overpass запущена.',
 'Browse': 'Обзор',
 'Browse…': 'Обзор…',
 'Buildings': 'Здания',
 'Bus stops': 'Автобусные остановки',
 'CRS:': 'CRS:',
 'Cache hit:': 'Попадание в кэш:',
 'Cache hit: using saved Overpass response ({age} day(s) old).':
   'Попадание в кэш: используется сохранённый ответ Overpass (возраст {age} дн.).',
 'Cache miss:': 'Промах кэша:',
 'Cache miss: could not read saved response ({error}).':
   'Промах кэша: не удалось прочитать сохранённый ответ ({error}).',
 'Cache miss: query hash does not match the saved response.':
   'Промах кэша: хэш запроса не соответствует сохранённому ответу.',
 'Cache miss: saved response is incomplete or invalid.':
   'Промах кэша: сохранённый ответ неполон или недействителен.',
 'Cache miss: saved response is older than {days} days.':
   'Промах кэша: сохранённый ответ старше {days} дней.',
 'Cache miss: saved response uses an unsupported cache format.':
   'Промах кэша: сохранённый ответ использует неподдерживаемый формат кэша.',
 'Cached Overpass response:': 'Кэшированный ответ Overpass:',
 'Cancel': 'Отмена',
 'Cancellation has already been requested.': 'Отмена уже запрошена.',
 'Cancellation requested': 'Запрошена отмена',
 'Cancellation requested. If an HTTP request is already active, the downloader will stop when that request returns or times out.':
   'Запрошена отмена. Если HTTP-запрос уже активен, загрузчик остановится, когда этот запрос вернётся или истечёт время ожидания.',
 'Cancellation requested; waiting for the current request to finish...':
   'Запрошена отмена; ожидание завершения текущего запроса…',
 'Cannot draw AOI because the QGIS interface is unavailable.':
   'Невозможно нарисовать AOI, поскольку интерфейс QGIS недоступен.',
 'Cannot resolve active-layer extent because QGIS is unavailable.':
   'Невозможно определить экстент активного слоя, поскольку QGIS недоступен.',
 'Cannot resolve current map extent because QGIS is unavailable.':
   'Невозможно определить текущий экстент карты, поскольку QGIS недоступен.',
 'Cannot resolve selected-feature AOI because QGIS is unavailable.':
   'Невозможно определить AOI по выбранным объектам, поскольку QGIS недоступен.',
 'Cannot transform an empty geometry.':
   'Невозможно преобразовать пустую геометрию.',
 'Capture the current QGIS map canvas extent.':
   'Зафиксировать текущий экстент холста карты QGIS.',
 'Choose all available levels, or select one or more levels to download (for example, 5–8 or level 5).':
   'Выберите все доступные уровни или один/несколько уровней для загрузки (например, 5–8 или уровень 5).',
 'Choose an output directory before downloading.':
   'Выберите папку вывода перед загрузкой.',
 'City name': 'Название города',
 'Classifying OSM elements and preparing GeoPackage layers.':
   'Классификация элементов OSM и подготовка слоёв GeoPackage.',
 'Classifying OSM elements and preparing Shapefile outputs.':
   'Классификация элементов OSM и подготовка выходных данных Shapefile.',
 'Clear all': 'Очистить всё',
 'Clear log': 'Очистить журнал',
 'Clear only the visible log, without changing processing settings.':
   'Очистить только видимый журнал, не изменяя настройки обработки.',
 'Clear selected levels so the user can make a narrower selection.':
   'Сбросить выбранные уровни, чтобы пользователь мог сделать более узкий выбор.',
 'Clear the messages currently shown in the Processing Log.':
   'Очистить сообщения, отображаемые в журнале обработки.',
 'Clear the previous AOI and display guidance for the chosen method.':
   'Очистить предыдущий AOI и показать подсказку для выбранного метода.',
 'Close': 'Закрыть',
 'Collect optional filename components before exporting OSM data.':
   'Собрать дополнительные компоненты имени файла перед экспортом данных OSM.',
 'Compact product header above the scrollable workflow.':
   'Компактный заголовок продукта над прокручиваемым рабочим процессом.',
 'Connection error on server ': 'Ошибка подключения к серверу ',
 'Continue to Download': 'Продолжить к загрузке',
 'Convert a name component into a Windows-safe filename token.':
   'Преобразовать компонент имени в безопасный для Windows токен имени файла.',
 'Convert the drawn rectangle into the standard AOI object.':
   'Преобразовать нарисованный прямоугольник в стандартный объект AOI.',
 'Converting OSM response to GeoPackage...':
   'Преобразование ответа OSM в GeoPackage…',
 'Converting OSM response to Shapefiles...':
   'Преобразование ответа OSM в Shapefile…',
 'Could not combine the selected feature geometries.':
   'Не удалось объединить геометрии выбранных объектов.',
 "Could not create Shapefile staging layer '{layer_name}'.":
   'Не удалось создать промежуточный слой Shapefile «{layer_name}».',
 'Could not create an empty bus_stops_points layer.':
   'Не удалось создать пустой слой bus_stops_points.',
 "Could not create temporary QGIS layer '{layer_name}'.":
   'Не удалось создать временный слой QGIS «{layer_name}».',
 'Could not create temporary layer for admin_level {admin_level}.':
   'Не удалось создать временный слой для admin_level {admin_level}.',
 'Could not create the merged bus_stops_points layer.':
   'Не удалось создать объединённый слой bus_stops_points.',
 'Could not delete temporary file': 'Не удалось удалить временный файл',
 "Could not load feature definition '{feature_key}': {error}":
   'Не удалось загрузить определение объекта «{feature_key}»: {error}',
 'Could not merge bus-station centroids into bus-stop points.':
   'Не удалось объединить центроиды автовокзалов с точками автобусных остановок.',
 'Could not overwrite existing output file: {error}':
   'Не удалось перезаписать существующий выходной файл: {error}',
 'Could not populate Shapefile for admin_level {admin_level}.':
   'Не удалось заполнить Shapefile для admin_level {admin_level}.',
 "Could not populate temporary layer '{layer_name}'.":
   'Не удалось заполнить временный слой «{layer_name}».',
 'Could not prepare the Overpass query:':
   'Не удалось подготовить запрос Overpass:',
 "Could not reopen intermediate GeoPackage layer '{layer_name}'.":
   'Не удалось повторно открыть промежуточный слой GeoPackage «{layer_name}».',
 'Could not restore previous QGIS map tool:':
   'Не удалось восстановить предыдущий инструмент карты QGIS:',
 'Could not search for temporary GeoPackages:':
   'Не удалось выполнить поиск временных GeoPackage:',
 'Country name': 'Название страны',
 'Create one section panel and return it with its body layout.':
   'Создать одну панель раздела и вернуть её с макетом содержимого.',
 'Created bus_stops_points from bus-station polygon centroids.':
   'Создан bus_stops_points из центроидов полигонов автовокзалов.',
 'Current QGIS map extent': 'Текущий экстент карты QGIS',
 'Current QGIS map extent resolved.':
   'Текущий экстент карты QGIS определён.',
 'Data © <a href="': 'Данные © <a href="',
 'Deleted temporary workspace file:':
   'Удалён временный файл рабочей области:',
 'Details:': 'Подробности:',
 'Download': 'Скачать',
 'Download OSM Data': 'Скачать данные OSM',
 'Download OpenStreetMap data for any area and load it straight into QGIS.':
   'Загрузите данные OpenStreetMap для любой области и загрузите их прямо в QGIS.',
 'Download cancelled because existing output files were not approved for overwrite.':
   'Загрузка отменена, поскольку перезапись существующих выходных файлов не была подтверждена.',
 'Download cancelled before it started.':
   'Загрузка отменена до её начала.',
 'Download cancelled before results were returned.':
   'Загрузка отменена до возврата результатов.',
 'Download cancelled before starting.':
   'Загрузка отменена до начала.',
 'Download cancelled in the output-naming dialog.':
   'Загрузка отменена в диалоге именования выходных файлов.',
 'Download cancelled.': 'Загрузка отменена.',
 'Download cancelled; existing files preserved.':
   'Загрузка отменена; существующие файлы сохранены.',
 'Download stopped.': 'Загрузка остановлена.',
 'Download succeeded, but export failed.':
   'Загрузка выполнена успешно, но экспорт завершился неудачно.',
 'Downloading OSM data from Overpass...':
   'Загрузка данных OSM из Overpass…',
 'Draw AOI': 'Нарисовать AOI',
 'Draw a rectangle on the QGIS map to define the AOI.':
   'Нарисуйте прямоугольник на карте QGIS, чтобы задать AOI.',
 'Draw rectangle on map': 'Нарисовать прямоугольник на карте',
 'Draw the AOI rectangle on the QGIS map.':
   'Нарисуйте прямоугольник AOI на карте QGIS.',
 'Drawn AOI validation failed:':
   'Ошибка проверки нарисованного AOI:',
 'Drawn rectangle': 'Нарисованный прямоугольник',
 'Drawn rectangle AOI captured successfully.':
   'Нарисованный прямоугольник AOI успешно зафиксирован.',
 'ERROR:': 'ОШИБКА:',
 'East:': 'Восток:',
 'Enable level checkboxes only when a specific selection is active.':
   'Включать флажки уровней только при активном конкретном выборе.',
 'Enable only the AOI action button for the selected method.':
   'Включить только кнопку действия AOI для выбранного метода.',
 'Enable or disable controls while a download is running.':
   'Включать или отключать элементы управления во время загрузки.',
 'Enter at least one name (City, Country, Region, or AOI).':
   'Введите хотя бы одно имя (город, страна, регион или AOI).',
 'Enter one or more name components. Blank fields will be skipped, and the remaining names will be joined with underscores. The selected output format will be retained.':
   'Введите один или несколько компонентов имени. Пустые поля будут пропущены, а оставшиеся имена будут соединены подчёркиваниями. Выбранный формат вывода будет сохранён.',
 'Enter_a_name_to_preview': 'Введите_имя_для_предпросмотра',
 'Export cancelled: output name is missing.':
   'Экспорт отменён: отсутствует имя вывода.',
 'Export complete:': 'Экспорт завершён:',
 'Export the downloaded response and optionally load its layers.':
   'Экспортировать загруженный ответ и при необходимости загрузить его слои.',
 'Failed to activate rectangle AOI tool:':
   'Не удалось активировать инструмент прямоугольника AOI:',
 'Failed to create AOI.': 'Не удалось создать AOI.',
 'Failed to process drawn rectangle AOI:':
   'Не удалось обработать нарисованный прямоугольник AOI:',
 'Failed to resolve active-layer extent.':
   'Не удалось определить экстент активного слоя.',
 'Failed to resolve active-layer extent:':
   'Не удалось определить экстент активного слоя:',
 'Failed to resolve current QGIS map extent:':
   'Не удалось определить текущий экстент карты QGIS:',
 'Failed to resolve selected-feature AOI.':
   'Не удалось определить AOI по выбранным объектам.',
 'Failed to resolve selected-feature AOI:':
   'Не удалось определить AOI по выбранным объектам:',
 "Failed to write layer '{layer_name}' to '{output_path}': {error}":
   'Не удалось записать слой «{layer_name}» в «{output_path}»: {error}',
 "Feature '{feature_key}' has no tag definitions.":
   'Объект «{feature_key}» не имеет определений тегов.',
 'Feature specification  does not expose a tag-filter mapping.':
   'Спецификация объекта не предоставляет сопоставление фильтров тегов.',
 'Ferry stops': 'Паромные остановки',
 'Filename preview': 'Предпросмотр имени файла',
 'Full documentation': 'Полная документация',
 'Generated Overpass query (': 'Сгенерированный запрос Overpass (',
 'GeoPackage': 'GeoPackage',
 'GeoPackage layer(s) to QGIS.': 'слой(и) GeoPackage в QGIS.',
 'GeoPackage saved:': 'GeoPackage сохранён:',
 'HTTP error on server ': 'Ошибка HTTP на сервере ',
 'HTTP error — ': 'ошибка HTTP — ',
 'HTTP {status} error on server {index}/{total}.':
   'Ошибка HTTP {status} на сервере {index}/{total}.',
 'Handle a drawing tool deactivation initiated outside this dialog.':
   'Обработать деактивацию инструмента рисования, инициированную вне этого диалога.',
 'Help': 'Справка',
 'Invalid east longitude: {value}':
   'Недействительная восточная долгота: {value}',
 'Invalid north latitude: {value}':
   'Недействительная северная широта: {value}',
 'Invalid response from server ': 'Недействительный ответ от сервера ',
 'Invalid south latitude: {value}':
   'Недействительная южная широта: {value}',
 'Invalid west longitude: {value}':
   'Недействительная западная долгота: {value}',
 'Keep the numeric readout in step with the progress bar.':
   'Синхронизировать числовое значение с индикатором выполнения.',
 'Land & built environment': 'Земля и застроенная среда',
 'Landuse': 'Землепользование',
 'Language:': 'Язык:',
 'Linear features': 'Линейные объекты',
 'Load the saved interface language and translate visible UI strings.':
   'Загрузить сохранённый язык интерфейса и перевести видимые строки интерфейса.',
 'Local response cache is disabled.':
   'Локальный кэш ответов отключён.',
 'Main OSM Data Toolkit window.': 'Главное окно OSM Data Toolkit.',
 'Manually capture the map extent after the user pans or zooms.':
   'Вручную зафиксировать экстент карты после панорамирования или масштабирования пользователем.',
 'Merged bus-station polygon centroids into bus_stops_points.':
   'Центроиды полигонов автовокзалов объединены в bus_stops_points.',
 'No Overpass selectors were generated.':
   'Не было сгенерировано ни одного селектора Overpass.',
 'No active QGIS layer is available.':
   'Нет доступного активного слоя QGIS.',
 'No active layer is available.': 'Нет доступного активного слоя.',
 'No exportable features matched the selected categories. Try another AOI or select additional OSM feature categories.':
   'Ни один экспортируемый объект не соответствует выбранным категориям. Попробуйте другой AOI или выберите дополнительные категории объектов OSM.',
 'No features are selected in the active layer.':
   'В активном слое не выбрано ни одного объекта.',
 'No levels selected. Select at least one level to continue.':
   'Уровни не выбраны. Выберите хотя бы один уровень, чтобы продолжить.',
 'No selected features found.': 'Выбранные объекты не найдены.',
 'No valid Area of Interest is available. Select an AOI method and resolve the AOI before downloading.':
   'Нет действительной области интереса. Выберите метод AOI и определите AOI перед загрузкой.',
 'North:': 'Север:',
 'Note: {layer_name} has too many tag columns for one Shapefile (DBF size limit); {count} rarely-used columns were left out.':
   'Примечание: {layer_name} содержит слишком много столбцов тегов для одного Shapefile (ограничение размера DBF); {count} редко используемых столбцов были опущены.',
 'OSM Data Toolkit': 'OSM Data Toolkit',
 'OSM Data Toolkit initialised.': 'OSM Data Toolkit инициализирован.',
 'OSM Feature Categories': 'Категории объектов OSM',
 'OSM export completed successfully.':
   'Экспорт OSM успешно завершён.',
 'One or more output files with this name already exist. Do you want to overwrite the matching output files?':
   'Один или несколько выходных файлов с этим именем уже существуют. Перезаписать соответствующие выходные файлы?',
 'Only the selected levels': 'Только выбранные уровни',
 'Only validated Overpass responses can be cached.':
   'Кэшировать можно только проверенные ответы Overpass.',
 'Open public spaces': 'Открытые общественные пространства',
 'Open the in-plugin help with links to the online documentation.':
   'Открыть справку внутри плагина со ссылками на онлайн-документацию.',
 'Output Settings': 'Настройки вывода',
 'Output directory': 'Папка вывода',
 'Output directory selected:': 'Выбрана папка вывода:',
 'Output format': 'Формат вывода',
 'Output settings': 'Настройки вывода',
 'Overpass download cancelled.': 'Загрузка Overpass отменена.',
 'Overpass download completed:': 'Загрузка Overpass завершена:',
 'Overpass download failed.': 'Загрузка Overpass не удалась.',
 'Overpass download failed:': 'Загрузка Overpass не удалась:',
 'Overpass download running...': 'Загрузка Overpass выполняется…',
 'Overpass download was cancelled by the caller.':
   'Загрузка Overpass была отменена вызывающей стороной.',
 'Overpass query must be a non-empty string.':
   'Запрос Overpass должен быть непустой строкой.',
 "Overpass response 'elements' field is not a list.":
   'Поле «elements» ответа Overpass не является списком.',
 "Overpass response does not contain an 'elements' field.":
   'Ответ Overpass не содержит поля «elements».',
 'Overpass response is not a JSON object.':
   'Ответ Overpass не является объектом JSON.',
 'Overpass response received successfully:':
   'Ответ Overpass успешно получен:',
 'Overpass server ': 'Сервер Overpass ',
 'Overpass server returned invalid JSON. Response preview: ':
   'Сервер Overpass вернул недействительный JSON. Предпросмотр ответа: ',
 'Overpass servers available:': 'Доступные серверы Overpass:',
 'Overpass timeout must be greater than zero.':
   'Тайм-аут Overpass должен быть больше нуля.',
 'Plugin version': 'Версия плагина',
 'Points of interest (POI)': 'Точки интереса (POI)',
 'Prepared {index:,} of {total:,} OSM elements for export...':
   'Подготовлено {index:,} из {total:,} элементов OSM к экспорту…',
 'Preparing Overpass download...': 'Подготовка загрузки Overpass…',
 'Preparing Overpass query.': 'Подготовка запроса Overpass.',
 'Processing Options': 'Параметры обработки',
 'Processing log': 'Журнал обработки',
 'Processing messages will appear here...':
   'Сообщения обработки появятся здесь…',
 'Processing options': 'Параметры обработки',
 'Public transport & places': 'Общественный транспорт и места',
 'QGIS interface object was not detected. Canvas-dependent AOI tools are disabled.':
   'Объект интерфейса QGIS не обнаружен. Зависимые от холста инструменты AOI отключены.',
 'QGIS map canvas could not be accessed.':
   'Не удалось получить доступ к холсту карты QGIS.',
 'QGIS map canvas is unavailable.':
   'Холст карты QGIS недоступен.',
 'Rail stops': 'Железнодорожные остановки',
 'Railways': 'Железные дороги',
 'Read the plugin version from metadata.txt (empty string if absent).':
   'Прочитать версию плагина из metadata.txt (пустая строка, если отсутствует).',
 'Read, validate and store the current QGIS map canvas extent.':
   'Прочитать, проверить и сохранить текущий экстент холста карты QGIS.',
 'Ready.': 'Готово.',
 'Rectangle AOI drawing tool activated.':
   'Инструмент рисования прямоугольника AOI активирован.',
 'Rectangle AOI drawing was cancelled.':
   'Рисование прямоугольника AOI было отменено.',
 'Region name': 'Название региона',
 'Report an issue': 'Сообщить о проблеме',
 'Request cooperative cancellation of the background worker.':
   'Запросить кооперативную отмену фонового исполнителя.',
 'Request error on server ': 'Ошибка запроса на сервере ',
 'Restore default GUI settings when the dialog closes.':
   'Восстановить настройки GUI по умолчанию при закрытии диалога.',
 'Restore the GUI once the background thread has stopped.':
   'Восстановить GUI после остановки фонового потока.',
 'Restore the QGIS map tool active before rectangle drawing.':
   'Восстановить инструмент карты QGIS, активный до рисования прямоугольника.',
 'Restore the map tool and reset state before hiding the dialog.':
   'Восстановить инструмент карты и сбросить состояние перед скрытием диалога.',
 'Retrying in ': 'Повторная попытка через ',
 'Return selected levels, or None when all levels are requested.':
   'Вернуть выбранные уровни или None, если запрошены все уровни.',
 'Return the combined, sanitized filename prefix.':
   'Вернуть объединённый очищенный префикс имени файла.',
 'Return the mapping between feature keys and GUI checkboxes.':
   'Вернуть сопоставление между ключами объектов и флажками GUI.',
 'Return the selected GUI feature keys.':
   'Вернуть выбранные ключи объектов GUI.',
 'Roads': 'Дороги',
 'Run a modal dialog on both Qt5 and Qt6.':
   'Запустить модальный диалог как в Qt5, так и в Qt6.',
 'Select Output Directory': 'Выбрать папку вывода',
 'Select a vector layer with selected features.':
   'Выберите векторный слой с выбранными объектами.',
 'Select all': 'Выбрать все',
 'Select an active QGIS layer.': 'Выберите активный слой QGIS.',
 'Select at least one OSM feature category before downloading.':
   'Выберите хотя бы одну категорию объектов OSM перед загрузкой.',
 'Select at least one administrative level, or choose All levels.':
   'Выберите хотя бы один административный уровень или выберите «Все уровни».',
 'Select at least one administrative level, or use None to retrieve all levels.':
   'Выберите хотя бы один административный уровень или используйте None, чтобы получить все уровни.',
 'Select levels 0–15 and switch to specific-level mode.':
   'Выбрать уровни 0–15 и переключиться в режим конкретных уровней.',
 'Select one or more features in the active layer.':
   'Выберите один или несколько объектов в активном слое.',
 'Select output directory...': 'Выбрать папку вывода…',
 'Selected administrative levels:': 'Выбранные административные уровни:',
 'Selected feature IDs:': 'Идентификаторы выбранных объектов:',
 'Selected feature(s) in active layer':
   'Выбранные объекты в активном слое',
 'Selected features (': 'Выбранные объекты (',
 'Selected-feature AOI captured successfully (':
   'AOI по выбранным объектам успешно зафиксирован (',
 'Selected-feature AOI captured successfully.':
   'AOI по выбранным объектам успешно зафиксирован.',
 'Selected-feature AOI is invalid.':
   'AOI по выбранным объектам недействителен.',
 'Selected-feature AOI requires a vector layer.':
   'AOI по выбранным объектам требует векторного слоя.',
 'Selected-feature AOI validation failed:':
   'Ошибка проверки AOI по выбранным объектам:',
 'Sending query to Overpass...': 'Отправка запроса в Overpass…',
 'Server ': 'Сервер ',
 'Shapefile': 'Shapefile',
 'Shapefile export completed in:':
   'Экспорт Shapefile завершён за:',
 'Shapefile field names shortened for':
   'Имена полей Shapefile сокращены для',
 'Shapefile layer(s) to QGIS.': 'слой(и) Shapefile в QGIS.',
 'Short in-plugin help with links to the full online documentation.':
   'Краткая справка внутри плагина со ссылками на полную онлайн-документацию.',
 'Show AOI coordinates and source CRS in the dialog.':
   'Показать координаты AOI и исходную CRS в диалоге.',
 'Show a concise description of the active administrative filter.':
   'Показать краткое описание активного административного фильтра.',
 'Source CRS is invalid.': 'Исходная CRS недействительна.',
 'South latitude cannot be greater than north latitude.':
   'Южная широта не может быть больше северной широты.',
 'South:': 'Юг:',
 'Starting Overpass download...': 'Запуск загрузки Overpass…',
 'Supporting copy: muted, wrapped and visually quiet.':
   'Вспомогательный текст: приглушённый, с переносами и визуально спокойный.',
 "Tag '{tag}' contains an empty value list.":
   'Тег «{tag}» содержит пустой список значений.',
 'Temporary workspace cleanup complete:':
   'Очистка временной рабочей области завершена:',
 'Temporary workspace cleanup complete: no matching files found.':
   'Очистка временной рабочей области завершена: подходящих файлов не найдено.',
 'Temporary-file cleanup skipped: workspace directory is invalid.':
   'Очистка временных файлов пропущена: папка рабочей области недействительна.',
 'The OSM download succeeded, but the output could not be created.':
   'Загрузка OSM выполнена успешно, но выходные данные создать не удалось.',
 "The Overpass response must be a JSON object with an 'elements' list.":
   'Ответ Overpass должен быть объектом JSON со списком «elements».',
 'The QGIS map canvas CRS is invalid.':
   'CRS холста карты QGIS недействительна.',
 'The active layer CRS is invalid.':
   'CRS активного слоя недействительна.',
 'The active layer extent is empty.':
   'Экстент активного слоя пуст.',
 'The active layer must be a vector layer.':
   'Активный слой должен быть векторным слоем.',
 'The combined name is too long. Shorten one or more components.':
   'Объединённое имя слишком длинное. Сократите один или несколько компонентов.',
 'The combined selected-feature geometry is empty.':
   'Объединённая геометрия выбранных объектов пуста.',
 'The current AOI is invalid:': 'Текущий AOI недействителен:',
 'The current QGIS map extent is empty.':
   'Текущий экстент карты QGIS пуст.',
 'The dialog cannot close while a download thread is running. Cancellation has been requested; close the dialog after it stops.':
   'Диалог не может закрыться, пока выполняется поток загрузки. Отмена запрошена; закройте диалог после его остановки.',
 'The download completed, but no confirmed output name was available.':
   'Загрузка завершена, но подтверждённое имя вывода отсутствовало.',
 "The exported Shapefile '{path}' could not be opened in QGIS.":
   'Экспортированный Shapefile «{path}» не удалось открыть в QGIS.',
 "The exported layer '{layer_name}' could not be opened in QGIS.":
   'Экспортированный слой «{layer_name}» не удалось открыть в QGIS.',
 'The output name does not contain any valid filename characters.':
   'Имя вывода не содержит допустимых символов имени файла.',
 'The output name is empty after filename validation.':
   'Имя вывода пусто после проверки имени файла.',
 'The selected features contain no valid geometry.':
   'Выбранные объекты не содержат допустимой геометрии.',
 'The selected output directory does not exist. Choose an existing folder.':
   'Выбранная папка вывода не существует. Выберите существующую папку.',
 'There is no active download to cancel.':
   'Нет активной загрузки для отмены.',
 'Timeout on server ': 'Тайм-аут на сервере ',
 'Translate widget labels while preserving each original English string.':
   'Перевести подписи виджетов, сохраняя каждую исходную английскую строку.',
 'Trying Overpass server ': 'Попытка использовать сервер Overpass ',
 'Unable to start AOI drawing:': 'Не удалось начать рисование AOI:',
 'Unclassified OSM elements not written to feature layers:':
   'Неклассифицированные элементы OSM, не записанные в слои объектов:',
 'Unsupported geometry family: {geometry_family}':
   'Неподдерживаемое семейство геометрий: {geometry_family}',
 "Unsupported geometry type '{geometry_type}' for feature '{feature_key}'.":
   'Неподдерживаемый тип геометрии «{geometry_type}» для объекта «{feature_key}».',
 'Unsupported geometry type for Shapefile export: {geometry_type}':
   'Неподдерживаемый тип геометрии для экспорта Shapefile: {geometry_type}',
 "Unsupported match mode '{mode}' for feature '{feature_key}'.":
   'Неподдерживаемый режим сопоставления «{mode}» для объекта «{feature_key}».',
 'Unsupported output format:': 'Неподдерживаемый формат вывода:',
 "Unsupported tag value type for '{feature_key}': {value_type}":
   'Неподдерживаемый тип значения тега для «{feature_key}»: {value_type}',
 'Update Current QGIS Map Extent':
   'Обновить текущий экстент карты QGIS',
 'Update the "N selected" count next to the category heading.':
   'Обновить счётчик «N выбрано» рядом с заголовком категории.',
 'Update the filename preview as the user edits the components.':
   'Обновлять предпросмотр имени файла по мере редактирования компонентов пользователем.',
 'Use Layer Extent': 'Использовать экстент слоя',
 'Use Selected Features': 'Использовать выбранные объекты',
 'Use local cache where available':
   'Использовать локальный кэш, где это возможно',
 'Use selected features in the active vector layer as the AOI.':
   'Использовать выбранные объекты в активном векторном слое как AOI.',
 'Use the full extent of the active QGIS layer as the AOI.':
   'Использовать полный экстент активного слоя QGIS как AOI.',
 'Use the full extent of the active QGIS layer.':
   'Использовать полный экстент активного слоя QGIS.',
 'Use the selected features of the active vector layer as the AOI.':
   'Использовать выбранные объекты активного векторного слоя как AOI.',
 'Using cached data; no Overpass network request was needed.':
   'Используются кэшированные данные; сетевой запрос Overpass не потребовался.',
 'Validate filename and any explicitly selected admin levels.':
   'Проверить имя файла и любые явно выбранные административные уровни.',
 'Validate inputs and start the background Overpass download.':
   'Проверить входные данные и запустить фоновую загрузку Overpass.',
 'WGS84 AOI bbox: south=': 'Ограничивающий прямоугольник AOI в WGS84: юг=',
 'WGS84 AOI geometry is not available.':
   'Геометрия AOI в WGS84 недоступна.',
 'Warning: download succeeded, but the response could not be cached:':
   'Предупреждение: загрузка выполнена успешно, но ответ не удалось кэшировать:',
 'Waterways': 'Водные пути',
 'West longitude cannot be greater than east longitude.':
   'Западная долгота не может быть больше восточной долготы.',
 'West:': 'Запад:',
 'Writing Shapefile {layer_index}/{total}: {layer_name}...':
   'Запись Shapefile {layer_index}/{total}: {layer_name}…',
 'Writing layer {layer_index}/{total}: {layer_name} ({count:,} features)...':
   'Запись слоя {layer_index}/{total}: {layer_name} ({count:,} объектов)…',
 'attempt ': 'попытка ',
 'characters).': 'символов).',
 'connection error — ': 'ошибка подключения — ',
 'e.g. CBD': 'напр. CBD',
 'e.g. Kenya': 'напр. Кения',
 'e.g. Nairobi': 'напр. Найроби',
 'e.g. NairobiCounty': 'напр. NairobiCounty',
 'elements (': 'элементов (',
 'export failed:': 'ошибка экспорта:',
 'feature records).': 'записей объектов).',
 'feature(s)).': 'объект(ов)).',
 'features written.': 'объектов записано.',
 'file(s) deleted.': 'файл(ов) удалено.',
 'relation geometry assignment(s); relation-member geometry assembly is not implemented yet.':
   'назначений геометрии отношения; сборка геометрии членов отношения ещё не реализована.',
 'relations).': 'отношений).',
 'response_data must be a dictionary.':
   'response_data должен быть словарём.',
 "response_data['elements'] must be a list.":
   "response_data['elements'] должен быть списком.",
 'temporary file(s) could not be deleted. They may still be in use by QGIS or another process.':
   'временные файлы не удалось удалить. Возможно, они всё ещё используются QGIS или другим процессом.',
 'timeout — ': 'тайм-аут — ',
 '{output_format} export failed: {error}':
   'Ошибка экспорта {output_format}: {error}',
 '— Confirm Overwrite': '— Подтвердить перезапись',
 '— Export Error': '— Ошибка экспорта',
 '— Help': '— Справка',
 '— Output Naming': '— Именование выходных файлов',
}