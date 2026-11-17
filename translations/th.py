"""Thai (ไทย) translation pack for the OSM Data Toolkit plugin.
Keys remain the English source strings; preserve placeholders and HTML."""
TEXT = {
 '\n<h3>Quick start</h3>\n<ol>\n  <li><b>Choose an area.</b> Use the current map extent, draw a rectangle\n      on the map, or use the bounding box of selected features or a\n      layer\'s extent.</li>\n  <li><b>Tick the OSM categories</b> you need (POI, stops, roads,\n      buildings, boundaries, landuse, ...).</li>\n  <li><b>Choose an output format and folder</b>, then click\n      <b>Download OSM Data</b>.</li>\n</ol>\n\n<h3>Good to know</h3>\n<ul>\n  <li><b>GeoPackage is recommended.</b> A Shapefile cannot hold very many\n      attribute columns, so on large areas some rarely used tag columns\n      may be left out (the log tells you when this happens).</li>\n  <li><b>Keep the area focused.</b> Very large areas produce huge Overpass\n      responses and can be slow or rejected by the public servers.</li>\n  <li><b>The cache</b> lets repeat downloads of the same query reuse\n      earlier results.</li>\n  <li><b>"Unclassified OSM elements"</b> in the log is informational: they\n      are mostly untagged vertices of lines and polygons that do not belong\n      to any selected category.</li>\n</ul>\n\n<p>Data &copy; OpenStreetMap contributors, available under the\n<a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a>.</p>\n<p><i>This plugin is not endorsed by or affiliated with the\nOpenStreetMap Foundation.</i></p>\n':
 '\n<h3>เริ่มต้นอย่างรวดเร็ว</h3>\n<ol>\n  <li><b>เลือกพื้นที่</b> ใช้ขอบเขตแผนที่ปัจจุบัน วาดสี่เหลี่ยมผืนผ้า\n      บนแผนที่ หรือใช้กรอบขอบเขตของฟีเจอร์ที่เลือกหรือขอบเขต\n      ของเลเยอร์</li>\n  <li><b>ทำเครื่องหมายในหมวดหมู่ OSM</b> ที่คุณต้องการ (POI, ป้ายหยุด,\n      ถนน, อาคาร, ขอบเขต, การใช้ที่ดิน, ...)</li>\n  <li><b>เลือกฟอร์แมตเอาต์พุตและโฟลเดอร์</b> แล้วคลิก\n      <b>ดาวน์โหลดข้อมูล OSM</b></li>\n</ol>\n\n<h3>สิ่งที่ควรทราบ</h3>\n<ul>\n  <li><b>แนะนำให้ใช้ GeoPackage</b> ไฟล์ Shapefile ไม่สามารถเก็บคอลัมน์\n      แอตทริบิวต์ได้มากนัก ดังนั้นในพื้นที่ขนาดใหญ่ คอลัมน์แท็กที่ใช้\n      ไม่บ่อยบางคอลัมน์อาจถูกตัดออก (บันทึกจะแจ้งให้ทราบเมื่อเกิดเหตุการณ์นี้)</li>\n  <li><b>จำกัดพื้นที่ให้เหมาะสม</b> พื้นที่ขนาดใหญ่มากจะสร้างการตอบกลับจาก\n      Overpass ขนาดมหึมาและอาจทำงานช้าหรือถูกปฏิเสธจากเซิร์ฟเวอร์สาธารณะ</li>\n  <li><b>แคช</b> ช่วยให้การดาวน์โหลดซ้ำของคำสั่งเดียวกันนำผลลัพธ์\n      ก่อนหน้ามาใช้ซ้ำได้</li>\n  <li><b>"องค์ประกอบ OSM ที่ไม่ถูกจัดประเภท"</b> ในบันทึกเป็นข้อมูลเท่านั้น:\n      ส่วนใหญ่เป็นจุดยอดของเส้นและรูปหลายเหลี่ยมที่ไม่มีแท็กและไม่ได้\n      อยู่ในหมวดหมู่ที่เลือกไว้</li>\n</ul>\n\n<p>ข้อมูล &copy; ผู้มีส่วนร่วมใน OpenStreetMap เผยแพร่ภายใต้\n<a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a></p>\n<p><i>ปลั๊กอินนี้ไม่ได้รับการรับรองหรือมีความเกี่ยวข้องกับ\nOpenStreetMap Foundation</i></p>\n',
 ' responded successfully.': ' ตอบกลับสำเร็จ',
 ' seconds...': ' วินาที…',
 '" style="color:#0B5E8E; text-decoration:none;">OpenStreetMap contributors</a> (ODbL)':
   '" style="color:#0B5E8E; text-decoration:none;">ผู้มีส่วนร่วมใน OpenStreetMap</a> (ODbL)',
 ', east=': ', ตะวันออก=',
 ', north=': ', เหนือ=',
 ', west=': ', ตะวันตก=',
 '0 selected': 'เลือก 0 รายการ',
 '<p>Plugin version': '<p>เวอร์ชันปลั๊กอิน',
 'A download is already running.': 'กำลังดาวน์โหลดอยู่แล้ว',
 'A labelled column of feature checkboxes.':
   'คอลัมน์ที่มีป้ายกำกับของช่องทำเครื่องหมายฟีเจอร์',
 'AOI drawing cancelled.': 'ยกเลิกการวาด AOI แล้ว',
 'AOI geometry is empty.': 'เรขาคณิต AOI ว่างเปล่า',
 'AOI geometry is missing.': 'ไม่มีเรขาคณิต AOI',
 'AOI name': 'ชื่อ AOI',
 'AOI rectangle captured successfully.': 'บันทึกสี่เหลี่ยมผืนผ้า AOI สำเร็จ',
 'AOI source CRS is invalid.': 'CRS ต้นทางของ AOI ไม่ถูกต้อง',
 'AOI validation failed:': 'การตรวจสอบ AOI ล้มเหลว:',
 'AOI:': 'AOI:',
 'AOI: QGIS interface is not available.': 'AOI: ไม่มีอินเทอร์เฟซ QGIS',
 "AOI: click 'Draw AOI', then drag a rectangle on the QGIS map.":
   'AOI: คลิก "วาด AOI" แล้วลากสี่เหลี่ยมผืนผ้าบนแผนที่ QGIS',
 "AOI: click 'Use Layer Extent' to use the full extent of the active QGIS layer.":
   'AOI: คลิก "ใช้ขอบเขตเลเยอร์" เพื่อใช้ขอบเขตเต็มของเลเยอร์ QGIS ที่ใช้งานอยู่',
 'AOI: click and drag on the QGIS map.':
   'AOI: คลิกและลากบนแผนที่ QGIS',
 'AOI: failed to resolve active layer extent':
   'AOI: ไม่สามารถระบุขอบเขตของเลเยอร์ที่ใช้งานอยู่ได้',
 'AOI: failed to resolve selected features':
   'AOI: ไม่สามารถระบุฟีเจอร์ที่เลือกได้',
 'AOI: invalid': 'AOI: ไม่ถูกต้อง',
 'AOI: no active QGIS layer.': 'AOI: ไม่มีเลเยอร์ QGIS ที่ใช้งานอยู่',
 'AOI: no feature(s) selected in the active layer.':
   'AOI: ไม่มีฟีเจอร์ที่เลือกในเลเยอร์ที่ใช้งานอยู่',
 'AOI: not yet resolved': 'AOI: ยังไม่ได้ระบุ',
 "AOI: select feature(s) in the active QGIS layer, then click 'Use Selected Features'.":
   'AOI: เลือกฟีเจอร์ในเลเยอร์ QGIS ที่ใช้งานอยู่ แล้วคลิก "ใช้ฟีเจอร์ที่เลือก"',
 'AOI: the active layer is not a vector layer.':
   'AOI: เลเยอร์ที่ใช้งานอยู่ไม่ใช่เลเยอร์เวกเตอร์',
 'AOI: unable to create': 'AOI: ไม่สามารถสร้างได้',
 'AOI: unable to resolve': 'AOI: ไม่สามารถระบุได้',
 'Activate the interactive rectangle AOI map tool.':
   'เปิดใช้งานเครื่องมือแผนที่ AOI แบบสี่เหลี่ยมผืนผ้าแบบโต้ตอบ',
 'Active layer extent': 'ขอบเขตของเลเยอร์ที่ใช้งานอยู่',
 'Active-layer extent AOI is invalid.':
   'AOI จากขอบเขตของเลเยอร์ที่ใช้งานอยู่ไม่ถูกต้อง',
 'Active-layer extent captured successfully.':
   'บันทึกขอบเขตของเลเยอร์ที่ใช้งานอยู่สำเร็จ',
 'Active-layer extent validation failed:':
   'การตรวจสอบขอบเขตของเลเยอร์ที่ใช้งานอยู่ล้มเหลว:',
 'Administrative boundaries': 'เขตการปกครอง',
 'Administrative boundary filter: all levels (no admin_level filter).':
   'ตัวกรองเขตการปกครอง: ทุกระดับ (ไม่มีตัวกรอง admin_level)',
 'Administrative boundary levels': 'ระดับเขตการปกครอง',
 'Administrative boundary levels:': 'ระดับเขตการปกครอง:',
 'Administrative levels must be an integer, a numeric string, a sequence of levels, or None.':
   'ระดับการปกครองต้องเป็นจำนวนเต็ม สตริงตัวเลข ลำดับของระดับ หรือ None',
 'All OSM feature categories cleared.': 'ล้างหมวดหมู่ฟีเจอร์ OSM ทั้งหมดแล้ว',
 'All OSM feature categories selected.': 'เลือกหมวดหมู่ฟีเจอร์ OSM ทั้งหมดแล้ว',
 'All Overpass server URLs must be non-empty strings.':
   'URL ของเซิร์ฟเวอร์ Overpass ทั้งหมดต้องเป็นสตริงที่ไม่ว่างเปล่า',
 'All Overpass servers and retry attempts failed.':
   'เซิร์ฟเวอร์ Overpass ทั้งหมดและการลองใหม่ล้มเหลว',
 'All administrative levels will be included.':
   'จะรวมระดับการปกครองทั้งหมด',
 'All administrative levels will be included; no admin_level filter will be added to the query.':
   'จะรวมระดับการปกครองทั้งหมด จะไม่เพิ่มตัวกรอง admin_level ลงในคิวรี',
 'All attempts failed for server ': 'การพยายามทั้งหมดล้มเหลวสำหรับเซิร์ฟเวอร์ ',
 'All levels (0–15; no admin_level filter)':
   'ทุกระดับ (0–15; ไม่มีตัวกรอง admin_level)',
 'An existing output directory is required for Shapefile export.':
   'ต้องมีโฟลเดอร์เอาต์พุตที่มีอยู่สำหรับการส่งออก Shapefile',
 'An output GeoPackage path is required.': 'ต้องระบุพาธ GeoPackage เอาต์พุต',
 'An output name is required for Shapefile export.':
   'ต้องระบุชื่อเอาต์พุตสำหรับการส่งออก Shapefile',
 'Append a timestamped message to the processing log.':
   'เพิ่มข้อความที่มีการประทับเวลาไปยังบันทึกการประมวลผล',
 'Append an exported feature count to the processing log.':
   'เพิ่มจำนวนฟีเจอร์ที่ส่งออกไปยังบันทึกการประมวลผล',
 'Area of Interest': 'พื้นที่สนใจ',
 'At least one OSM feature must be selected.':
   'ต้องเลือกฟีเจอร์ OSM อย่างน้อยหนึ่งรายการ',
 'At least one OSM feature must be supplied.':
   'ต้องระบุฟีเจอร์ OSM อย่างน้อยหนึ่งรายการ',
 'At least one Overpass server must be provided.':
   'ต้องระบุเซิร์ฟเวอร์ Overpass อย่างน้อยหนึ่งรายการ',
 'Attempt details:': 'รายละเอียดการพยายาม:',
 'Automatically add downloaded layers to QGIS':
   'เพิ่มเลเยอร์ที่ดาวน์โหลดไปยัง QGIS โดยอัตโนมัติ',
 'Background Overpass download started.':
   'เริ่มการดาวน์โหลด Overpass ในเบื้องหลังแล้ว',
 'Browse': 'เรียกดู',
 'Browse…': 'เรียกดู…',
 'Buildings': 'อาคาร',
 'Bus stops': 'ป้ายหยุดรถประจำทาง',
 'CRS:': 'CRS:',
 'Cache hit:': 'พบในแคช:',
 'Cache hit: using saved Overpass response ({age} day(s) old).':
   'พบในแคช: ใช้การตอบกลับ Overpass ที่บันทึกไว้ (เก่า {age} วัน)',
 'Cache miss:': 'ไม่พบในแคช:',
 'Cache miss: could not read saved response ({error}).':
   'ไม่พบในแคช: ไม่สามารถอ่านการตอบกลับที่บันทึกไว้ ({error})',
 'Cache miss: query hash does not match the saved response.':
   'ไม่พบในแคช: แฮชของคิวรีไม่ตรงกับการตอบกลับที่บันทึกไว้',
 'Cache miss: saved response is incomplete or invalid.':
   'ไม่พบในแคช: การตอบกลับที่บันทึกไว้ไม่สมบูรณ์หรือไม่ถูกต้อง',
 'Cache miss: saved response is older than {days} days.':
   'ไม่พบในแคช: การตอบกลับที่บันทึกไว้เก่ากว่า {days} วัน',
 'Cache miss: saved response uses an unsupported cache format.':
   'ไม่พบในแคช: การตอบกลับที่บันทึกไว้ใช้ฟอร์แมตแคชที่ไม่รองรับ',
 'Cached Overpass response:': 'การตอบกลับ Overpass ที่แคชไว้:',
 'Cancel': 'ยกเลิก',
 'Cancellation has already been requested.': 'มีการร้องขอยกเลิกแล้ว',
 'Cancellation requested': 'ร้องขอยกเลิกแล้ว',
 'Cancellation requested. If an HTTP request is already active, the downloader will stop when that request returns or times out.':
   'ร้องขอยกเลิกแล้ว หากคำขอ HTTP ทำงานอยู่แล้ว ตัวดาวน์โหลดจะหยุดเมื่อคำขอนั้นส่งคืนหรือหมดเวลา',
 'Cancellation requested; waiting for the current request to finish...':
   'ร้องขอยกเลิกแล้ว กำลังรอให้คำขอปัจจุบันเสร็จสิ้น…',
 'Cannot draw AOI because the QGIS interface is unavailable.':
   'ไม่สามารถวาด AOI ได้เนื่องจากไม่มีอินเทอร์เฟซ QGIS',
 'Cannot resolve active-layer extent because QGIS is unavailable.':
   'ไม่สามารถระบุขอบเขตของเลเยอร์ที่ใช้งานอยู่ได้เนื่องจากไม่มี QGIS',
 'Cannot resolve current map extent because QGIS is unavailable.':
   'ไม่สามารถระบุขอบเขตแผนที่ปัจจุบันได้เนื่องจากไม่มี QGIS',
 'Cannot resolve selected-feature AOI because QGIS is unavailable.':
   'ไม่สามารถระบุ AOI จากฟีเจอร์ที่เลือกได้เนื่องจากไม่มี QGIS',
 'Cannot transform an empty geometry.':
   'ไม่สามารถแปลงเรขาคณิตที่ว่างเปล่าได้',
 'Capture the current QGIS map canvas extent.':
   'บันทึกขอบเขตปัจจุบันของแคนวาสแผนที่ QGIS',
 'Choose all available levels, or select one or more levels to download (for example, 5–8 or level 5).':
   'เลือกระดับที่มีอยู่ทั้งหมด หรือเลือกระดับอย่างน้อยหนึ่งระดับเพื่อดาวน์โหลด (เช่น 5–8 หรือระดับ 5)',
 'Choose an output directory before downloading.':
   'เลือกโฟลเดอร์เอาต์พุตก่อนดาวน์โหลด',
 'City name': 'ชื่อเมือง',
 'Classifying OSM elements and preparing GeoPackage layers.':
   'กำลังจัดประเภทองค์ประกอบ OSM และเตรียมเลเยอร์ GeoPackage',
 'Classifying OSM elements and preparing Shapefile outputs.':
   'กำลังจัดประเภทองค์ประกอบ OSM และเตรียมเอาต์พุต Shapefile',
 'Clear all': 'ล้างทั้งหมด',
 'Clear log': 'ล้างบันทึก',
 'Clear only the visible log, without changing processing settings.':
   'ล้างเฉพาะบันทึกที่มองเห็น โดยไม่เปลี่ยนการตั้งค่าการประมวลผล',
 'Clear selected levels so the user can make a narrower selection.':
   'ล้างระดับที่เลือกเพื่อให้ผู้ใช้สามารถเลือกได้แคบลง',
 'Clear the messages currently shown in the Processing Log.':
   'ล้างข้อความที่แสดงอยู่ในบันทึกการประมวลผล',
 'Clear the previous AOI and display guidance for the chosen method.':
   'ล้าง AOI ก่อนหน้าและแสดงคำแนะนำสำหรับวิธีการที่เลือก',
 'Close': 'ปิด',
 'Collect optional filename components before exporting OSM data.':
   'รวบรวมส่วนประกอบชื่อไฟล์ที่เป็นทางเลือกก่อนส่งออกข้อมูล OSM',
 'Compact product header above the scrollable workflow.':
   'ส่วนหัวผลิตภัณฑ์แบบกะทัดรัดเหนือเวิร์กโฟลว์ที่เลื่อนได้',
 'Connection error on server ': 'ข้อผิดพลาดการเชื่อมต่อบนเซิร์ฟเวอร์ ',
 'Continue to Download': 'ดำเนินการต่อเพื่อดาวน์โหลด',
 'Convert a name component into a Windows-safe filename token.':
   'แปลงส่วนประกอบชื่อเป็นโทเค็นชื่อไฟล์ที่ปลอดภัยสำหรับ Windows',
 'Convert the drawn rectangle into the standard AOI object.':
   'แปลงสี่เหลี่ยมผืนผ้าที่วาดเป็นออบเจกต์ AOI มาตรฐาน',
 'Converting OSM response to GeoPackage...':
   'กำลังแปลงการตอบกลับ OSM เป็น GeoPackage…',
 'Converting OSM response to Shapefiles...':
   'กำลังแปลงการตอบกลับ OSM เป็น Shapefile…',
 'Could not combine the selected feature geometries.':
   'ไม่สามารถรวมเรขาคณิตของฟีเจอร์ที่เลือกได้',
 "Could not create Shapefile staging layer '{layer_name}'.":
   'ไม่สามารถสร้างเลเยอร์ชั่วคราว Shapefile "{layer_name}"',
 'Could not create an empty bus_stops_points layer.':
   'ไม่สามารถสร้างเลเยอร์ bus_stops_points ว่างเปล่าได้',
 "Could not create temporary QGIS layer '{layer_name}'.":
   'ไม่สามารถสร้างเลเยอร์ QGIS ชั่วคราว "{layer_name}"',
 'Could not create temporary layer for admin_level {admin_level}.':
   'ไม่สามารถสร้างเลเยอร์ชั่วคราวสำหรับ admin_level {admin_level}',
 'Could not create the merged bus_stops_points layer.':
   'ไม่สามารถสร้างเลเยอร์ bus_stops_points ที่รวมแล้วได้',
 'Could not delete temporary file': 'ไม่สามารถลบไฟล์ชั่วคราวได้',
 "Could not load feature definition '{feature_key}': {error}":
   'ไม่สามารถโหลดคำจำกัดความฟีเจอร์ "{feature_key}": {error}',
 'Could not merge bus-station centroids into bus-stop points.':
   'ไม่สามารถรวมจุดศูนย์กลางของสถานีขนส่งเข้ากับจุดป้ายหยุดรถประจำทางได้',
 'Could not overwrite existing output file: {error}':
   'ไม่สามารถเขียนทับไฟล์เอาต์พุตที่มีอยู่: {error}',
 'Could not populate Shapefile for admin_level {admin_level}.':
   'ไม่สามารถเติม Shapefile สำหรับ admin_level {admin_level}',
 "Could not populate temporary layer '{layer_name}'.":
   'ไม่สามารถเติมเลเยอร์ชั่วคราว "{layer_name}"',
 'Could not prepare the Overpass query:':
   'ไม่สามารถเตรียมคิวรี Overpass:',
 "Could not reopen intermediate GeoPackage layer '{layer_name}'.":
   'ไม่สามารถเปิดเลเยอร์ GeoPackage ระดับกลาง "{layer_name}" อีกครั้ง',
 'Could not restore previous QGIS map tool:':
   'ไม่สามารถคืนค่าเครื่องมือแผนที่ QGIS ก่อนหน้า:',
 'Could not search for temporary GeoPackages:':
   'ไม่สามารถค้นหา GeoPackage ชั่วคราว:',
 'Country name': 'ชื่อประเทศ',
 'Create one section panel and return it with its body layout.':
   'สร้างแผงส่วนหนึ่งและส่งคืนพร้อมเค้าโครงเนื้อหา',
 'Created bus_stops_points from bus-station polygon centroids.':
   'สร้าง bus_stops_points จากจุดศูนย์กลางของรูปหลายเหลี่ยมสถานีขนส่ง',
 'Current QGIS map extent': 'ขอบเขตแผนที่ QGIS ปัจจุบัน',
 'Current QGIS map extent resolved.':
   'ระบุขอบเขตแผนที่ QGIS ปัจจุบันแล้ว',
 'Data © <a href="': 'ข้อมูล © <a href="',
 'Deleted temporary workspace file:': 'ลบไฟล์เวิร์กสเปซชั่วคราวแล้ว:',
 'Details:': 'รายละเอียด:',
 'Download': 'ดาวน์โหลด',
 'Download OSM Data': 'ดาวน์โหลดข้อมูล OSM',
 'Download OpenStreetMap data for any area and load it straight into QGIS.':
   'ดาวน์โหลดข้อมูล OpenStreetMap สำหรับพื้นที่ใดก็ได้และโหลดเข้า QGIS โดยตรง',
 'Download cancelled because existing output files were not approved for overwrite.':
   'ยกเลิกการดาวน์โหลดเนื่องจากไฟล์เอาต์พุตที่มีอยู่ไม่ได้รับการอนุมัติให้เขียนทับ',
 'Download cancelled before it started.': 'ยกเลิกการดาวน์โหลดก่อนเริ่มต้น',
 'Download cancelled before results were returned.':
   'ยกเลิกการดาวน์โหลดก่อนที่ผลลัพธ์จะถูกส่งคืน',
 'Download cancelled before starting.': 'ยกเลิกการดาวน์โหลดก่อนเริ่มต้น',
 'Download cancelled in the output-naming dialog.':
   'ยกเลิกการดาวน์โหลดในไดอะล็อกการตั้งชื่อเอาต์พุต',
 'Download cancelled.': 'ยกเลิกการดาวน์โหลดแล้ว',
 'Download cancelled; existing files preserved.':
   'ยกเลิกการดาวน์โหลด; ไฟล์ที่มีอยู่ถูกเก็บรักษาไว้',
 'Download stopped.': 'หยุดการดาวน์โหลดแล้ว',
 'Download succeeded, but export failed.':
   'ดาวน์โหลดสำเร็จ แต่การส่งออกล้มเหลว',
 'Downloading OSM data from Overpass...':
   'กำลังดาวน์โหลดข้อมูล OSM จาก Overpass…',
 'Draw AOI': 'วาด AOI',
 'Draw a rectangle on the QGIS map to define the AOI.':
   'วาดสี่เหลี่ยมผืนผ้าบนแผนที่ QGIS เพื่อกำหนด AOI',
 'Draw rectangle on map': 'วาดสี่เหลี่ยมผืนผ้าบนแผนที่',
 'Draw the AOI rectangle on the QGIS map.':
   'วาดสี่เหลี่ยมผืนผ้า AOI บนแผนที่ QGIS',
 'Drawn AOI validation failed:': 'การตรวจสอบ AOI ที่วาดล้มเหลว:',
 'Drawn rectangle': 'สี่เหลี่ยมผืนผ้าที่วาด',
 'Drawn rectangle AOI captured successfully.':
   'บันทึก AOI จากสี่เหลี่ยมผืนผ้าที่วาดสำเร็จ',
 'ERROR:': 'ข้อผิดพลาด:',
 'East:': 'ตะวันออก:',
 'Enable level checkboxes only when a specific selection is active.':
   'เปิดใช้งานช่องทำเครื่องหมายระดับเฉพาะเมื่อมีการเลือกที่เฉพาะเจาะจงอยู่',
 'Enable only the AOI action button for the selected method.':
   'เปิดใช้งานเฉพาะปุ่มการกระทำ AOI สำหรับวิธีการที่เลือก',
 'Enable or disable controls while a download is running.':
   'เปิดหรือปิดใช้งานตัวควบคุมในขณะที่กำลังดาวน์โหลด',
 'Enter at least one name (City, Country, Region, or AOI).':
   'ป้อนชื่ออย่างน้อยหนึ่งชื่อ (เมือง ประเทศ ภูมิภาค หรือ AOI)',
 'Enter one or more name components. Blank fields will be skipped, and the remaining names will be joined with underscores. The selected output format will be retained.':
   'ป้อนส่วนประกอบชื่ออย่างน้อยหนึ่งรายการ ฟิลด์ว่างจะถูกข้าม และชื่อที่เหลือจะถูกเชื่อมด้วยขีดล่าง ฟอร์แมตเอาต์พุตที่เลือกจะยังคงอยู่',
 'Enter_a_name_to_preview': 'ป้อน_ชื่อเพื่อดูตัวอย่าง',
 'Export cancelled: output name is missing.':
   'ยกเลิกการส่งออก: ไม่มีชื่อเอาต์พุต',
 'Export complete:': 'ส่งออกเสร็จสมบูรณ์:',
 'Export the downloaded response and optionally load its layers.':
   'ส่งออกการตอบกลับที่ดาวน์โหลดและเลือกโหลดเลเยอร์ของมันได้',
 'Failed to activate rectangle AOI tool:':
   'ไม่สามารถเปิดใช้งานเครื่องมือ AOI แบบสี่เหลี่ยมผืนผ้า:',
 'Failed to create AOI.': 'ไม่สามารถสร้าง AOI',
 'Failed to process drawn rectangle AOI:':
   'ไม่สามารถประมวลผล AOI จากสี่เหลี่ยมผืนผ้าที่วาด:',
 'Failed to resolve active-layer extent.':
   'ไม่สามารถระบุขอบเขตของเลเยอร์ที่ใช้งานอยู่',
 'Failed to resolve active-layer extent:':
   'ไม่สามารถระบุขอบเขตของเลเยอร์ที่ใช้งานอยู่:',
 'Failed to resolve current QGIS map extent:':
   'ไม่สามารถระบุขอบเขตแผนที่ QGIS ปัจจุบัน:',
 'Failed to resolve selected-feature AOI.':
   'ไม่สามารถระบุ AOI จากฟีเจอร์ที่เลือก',
 'Failed to resolve selected-feature AOI:':
   'ไม่สามารถระบุ AOI จากฟีเจอร์ที่เลือก:',
 "Failed to write layer '{layer_name}' to '{output_path}': {error}":
   'ไม่สามารถเขียนเลเยอร์ "{layer_name}" ไปยัง "{output_path}": {error}',
 "Feature '{feature_key}' has no tag definitions.":
   'ฟีเจอร์ "{feature_key}" ไม่มีคำจำกัดความแท็ก',
 'Feature specification  does not expose a tag-filter mapping.':
   'ข้อกำหนดฟีเจอร์ไม่ได้แสดงการแมปตัวกรองแท็ก',
 'Ferry stops': 'ท่าเรือข้ามฟาก',
 'Filename preview': 'ตัวอย่างชื่อไฟล์',
 'Full documentation': 'เอกสารประกอบฉบับเต็ม',
 'Generated Overpass query (': 'คิวรี Overpass ที่สร้างขึ้น (',
 'GeoPackage': 'GeoPackage',
 'GeoPackage layer(s) to QGIS.': 'เลเยอร์ GeoPackage ไปยัง QGIS',
 'GeoPackage saved:': 'บันทึก GeoPackage แล้ว:',
 'HTTP error on server ': 'ข้อผิดพลาด HTTP บนเซิร์ฟเวอร์ ',
 'HTTP error — ': 'ข้อผิดพลาด HTTP — ',
 'HTTP {status} error on server {index}/{total}.':
   'ข้อผิดพลาด HTTP {status} บนเซิร์ฟเวอร์ {index}/{total}',
 'Handle a drawing tool deactivation initiated outside this dialog.':
   'จัดการการปิดใช้งานเครื่องมือวาดที่เริ่มต้นจากภายนอกไดอะล็อกนี้',
 'Help': 'ช่วยเหลือ',
 'Invalid east longitude: {value}': 'ลองจิจูดตะวันออกไม่ถูกต้อง: {value}',
 'Invalid north latitude: {value}': 'ละติจูดเหนือไม่ถูกต้อง: {value}',
 'Invalid response from server ': 'การตอบกลับไม่ถูกต้องจากเซิร์ฟเวอร์ ',
 'Invalid south latitude: {value}': 'ละติจูดใต้ไม่ถูกต้อง: {value}',
 'Invalid west longitude: {value}': 'ลองจิจูดตะวันตกไม่ถูกต้อง: {value}',
 'Keep the numeric readout in step with the progress bar.':
   'ทำให้การอ่านค่าตัวเลขตรงกับแถบความคืบหน้า',
 'Land & built environment': 'ที่ดินและสภาพแวดล้อมที่สร้างขึ้น',
 'Landuse': 'การใช้ที่ดิน',
 'Language:': 'ภาษา:',
 'Linear features': 'ฟีเจอร์เชิงเส้น',
 'Load the saved interface language and translate visible UI strings.':
   'โหลดภาษาของอินเทอร์เฟซที่บันทึกไว้และแปลสตริง UI ที่มองเห็น',
 'Local response cache is disabled.': 'แคชการตอบกลับในเครื่องถูกปิดใช้งาน',
 'Main OSM Data Toolkit window.': 'หน้าต่างหลักของ OSM Data Toolkit',
 'Manually capture the map extent after the user pans or zooms.':
   'บันทึกขอบเขตแผนที่ด้วยตนเองหลังจากผู้ใช้เลื่อนหรือซูม',
 'Merged bus-station polygon centroids into bus_stops_points.':
   'รวมจุดศูนย์กลางรูปหลายเหลี่ยมสถานีขนส่งเข้ากับ bus_stops_points แล้ว',
 'No Overpass selectors were generated.':
   'ไม่มีตัวเลือก Overpass ที่ถูกสร้างขึ้น',
 'No active QGIS layer is available.': 'ไม่มีเลเยอร์ QGIS ที่ใช้งานอยู่',
 'No active layer is available.': 'ไม่มีเลเยอร์ที่ใช้งานอยู่',
 'No exportable features matched the selected categories. Try another AOI or select additional OSM feature categories.':
   'ไม่มีฟีเจอร์ที่ส่งออกได้ตรงกับหมวดหมู่ที่เลือก ลองใช้ AOI อื่นหรือเลือกหมวดหมู่ฟีเจอร์ OSM เพิ่มเติม',
 'No features are selected in the active layer.':
   'ไม่มีฟีเจอร์ที่เลือกในเลเยอร์ที่ใช้งานอยู่',
 'No levels selected. Select at least one level to continue.':
   'ไม่ได้เลือกระดับ เลือกอย่างน้อยหนึ่งระดับเพื่อดำเนินการต่อ',
 'No selected features found.': 'ไม่พบฟีเจอร์ที่เลือก',
 'No valid Area of Interest is available. Select an AOI method and resolve the AOI before downloading.':
   'ไม่มีพื้นที่สนใจที่ถูกต้อง เลือกวิธีการ AOI และระบุ AOI ก่อนดาวน์โหลด',
 'North:': 'เหนือ:',
 'Note: {layer_name} has too many tag columns for one Shapefile (DBF size limit); {count} rarely-used columns were left out.':
   'หมายเหตุ: {layer_name} มีคอลัมน์แท็กมากเกินไปสำหรับ Shapefile หนึ่งไฟล์ (ขีดจำกัดขนาด DBF); คอลัมน์ที่ใช้น้อย {count} คอลัมน์ถูกตัดออก',
 'OSM Data Toolkit': 'OSM Data Toolkit',
 'OSM Data Toolkit initialised.': 'เริ่มต้น OSM Data Toolkit แล้ว',
 'OSM Feature Categories': 'หมวดหมู่ฟีเจอร์ OSM',
 'OSM export completed successfully.': 'การส่งออก OSM เสร็จสมบูรณ์',
 'One or more output files with this name already exist. Do you want to overwrite the matching output files?':
   'มีไฟล์เอาต์พุตอย่างน้อยหนึ่งไฟล์ที่มีชื่อนี้อยู่แล้ว คุณต้องการเขียนทับไฟล์เอาต์พุตที่ตรงกันหรือไม่',
 'Only the selected levels': 'เฉพาะระดับที่เลือก',
 'Only validated Overpass responses can be cached.':
   'แคชได้เฉพาะการตอบกลับ Overpass ที่ผ่านการตรวจสอบแล้วเท่านั้น',
 'Open public spaces': 'พื้นที่สาธารณะเปิด',
 'Open the in-plugin help with links to the online documentation.':
   'เปิดความช่วยเหลือในปลั๊กอินพร้อมลิงก์ไปยังเอกสารประกอบออนไลน์',
 'Output Settings': 'การตั้งค่าเอาต์พุต',
 'Output directory': 'โฟลเดอร์เอาต์พุต',
 'Output directory selected:': 'เลือกโฟลเดอร์เอาต์พุตแล้ว:',
 'Output format': 'ฟอร์แมตเอาต์พุต',
 'Output settings': 'การตั้งค่าเอาต์พุต',
 'Overpass download cancelled.': 'ยกเลิกการดาวน์โหลด Overpass แล้ว',
 'Overpass download completed:': 'การดาวน์โหลด Overpass เสร็จสมบูรณ์:',
 'Overpass download failed.': 'การดาวน์โหลด Overpass ล้มเหลว',
 'Overpass download failed:': 'การดาวน์โหลด Overpass ล้มเหลว:',
 'Overpass download running...': 'กำลังดาวน์โหลด Overpass…',
 'Overpass download was cancelled by the caller.':
   'การดาวน์โหลด Overpass ถูกยกเลิกโดยผู้เรียก',
 'Overpass query must be a non-empty string.':
   'คิวรี Overpass ต้องเป็นสตริงที่ไม่ว่างเปล่า',
 "Overpass response 'elements' field is not a list.":
   'ฟิลด์ "elements" ของการตอบกลับ Overpass ไม่ใช่รายการ',
 "Overpass response does not contain an 'elements' field.":
   'การตอบกลับ Overpass ไม่มีฟิลด์ "elements"',
 'Overpass response is not a JSON object.':
   'การตอบกลับ Overpass ไม่ใช่ออบเจกต์ JSON',
 'Overpass response received successfully:':
   'ได้รับการตอบกลับ Overpass สำเร็จ:',
 'Overpass server ': 'เซิร์ฟเวอร์ Overpass ',
 'Overpass server returned invalid JSON. Response preview: ':
   'เซิร์ฟเวอร์ Overpass ส่งคืน JSON ที่ไม่ถูกต้อง ตัวอย่างการตอบกลับ: ',
 'Overpass servers available:': 'เซิร์ฟเวอร์ Overpass ที่มีอยู่:',
 'Overpass timeout must be greater than zero.':
   'เวลาหมดของ Overpass ต้องมากกว่าศูนย์',
 'Plugin version': 'เวอร์ชันปลั๊กอิน',
 'Points of interest (POI)': 'จุดสนใจ (POI)',
 'Prepared {index:,} of {total:,} OSM elements for export...':
   'เตรียมองค์ประกอบ OSM {index:,} จาก {total:,} รายการสำหรับการส่งออก…',
 'Preparing Overpass download...': 'กำลังเตรียมการดาวน์โหลด Overpass…',
 'Preparing Overpass query.': 'กำลังเตรียมคิวรี Overpass',
 'Processing Options': 'ตัวเลือกการประมวลผล',
 'Processing log': 'บันทึกการประมวลผล',
 'Processing messages will appear here...':
   'ข้อความการประมวลผลจะปรากฏที่นี่…',
 'Processing options': 'ตัวเลือกการประมวลผล',
 'Public transport & places': 'ขนส่งสาธารณะและสถานที่',
 'QGIS interface object was not detected. Canvas-dependent AOI tools are disabled.':
   'ไม่พบออบเจกต์อินเทอร์เฟซ QGIS เครื่องมือ AOI ที่ขึ้นกับแคนวาสถูกปิดใช้งาน',
 'QGIS map canvas could not be accessed.':
   'ไม่สามารถเข้าถึงแคนวาสแผนที่ QGIS',
 'QGIS map canvas is unavailable.': 'แคนวาสแผนที่ QGIS ไม่พร้อมใช้งาน',
 'Rail stops': 'ป้ายหยุดรถไฟ',
 'Railways': 'ทางรถไฟ',
 'Read the plugin version from metadata.txt (empty string if absent).':
   'อ่านเวอร์ชันปลั๊กอินจาก metadata.txt (สตริงว่างหากไม่มี)',
 'Read, validate and store the current QGIS map canvas extent.':
   'อ่าน ตรวจสอบ และจัดเก็บขอบเขตปัจจุบันของแคนวาสแผนที่ QGIS',
 'Ready.': 'พร้อม',
 'Rectangle AOI drawing tool activated.':
   'เปิดใช้งานเครื่องมือวาด AOI แบบสี่เหลี่ยมผืนผ้าแล้ว',
 'Rectangle AOI drawing was cancelled.':
   'ยกเลิกการวาด AOI แบบสี่เหลี่ยมผืนผ้าแล้ว',
 'Region name': 'ชื่อภูมิภาค',
 'Report an issue': 'รายงานปัญหา',
 'Request cooperative cancellation of the background worker.':
   'ขอให้ยกเลิกการทำงานของผู้ปฏิบัติงานเบื้องหลังแบบร่วมมือ',
 'Request error on server ': 'ข้อผิดพลาดคำขอบนเซิร์ฟเวอร์ ',
 'Restore default GUI settings when the dialog closes.':
   'คืนค่าการตั้งค่า GUI เริ่มต้นเมื่อปิดไดอะล็อก',
 'Restore the GUI once the background thread has stopped.':
   'คืนค่า GUI เมื่อเธรดเบื้องหลังหยุดลง',
 'Restore the QGIS map tool active before rectangle drawing.':
   'คืนค่าเครื่องมือแผนที่ QGIS ที่ใช้งานอยู่ก่อนการวาดสี่เหลี่ยมผืนผ้า',
 'Restore the map tool and reset state before hiding the dialog.':
   'คืนค่าเครื่องมือแผนที่และรีเซ็ตสถานะก่อนซ่อนไดอะล็อก',
 'Retrying in ': 'กำลังลองใหม่ใน ',
 'Return selected levels, or None when all levels are requested.':
   'ส่งคืนระดับที่เลือก หรือ None เมื่อมีการร้องขอทุกระดับ',
 'Return the combined, sanitized filename prefix.':
   'ส่งคืนคำนำหน้าชื่อไฟล์ที่รวมและทำให้ปลอดภัยแล้ว',
 'Return the mapping between feature keys and GUI checkboxes.':
   'ส่งคืนการแมประหว่างคีย์ฟีเจอร์และช่องทำเครื่องหมาย GUI',
 'Return the selected GUI feature keys.':
   'ส่งคืนคีย์ฟีเจอร์ GUI ที่เลือก',
 'Roads': 'ถนน',
 'Run a modal dialog on both Qt5 and Qt6.':
   'เรียกใช้ไดอะล็อกแบบโมดัลบนทั้ง Qt5 และ Qt6',
 'Select Output Directory': 'เลือกโฟลเดอร์เอาต์พุต',
 'Select a vector layer with selected features.':
   'เลือกเลเยอร์เวกเตอร์ที่มีฟีเจอร์ที่เลือก',
 'Select all': 'เลือกทั้งหมด',
 'Select an active QGIS layer.': 'เลือกเลเยอร์ QGIS ที่ใช้งานอยู่',
 'Select at least one OSM feature category before downloading.':
   'เลือกหมวดหมู่ฟีเจอร์ OSM อย่างน้อยหนึ่งหมวดหมู่ก่อนดาวน์โหลด',
 'Select at least one administrative level, or choose All levels.':
   'เลือกเขตการปกครองอย่างน้อยหนึ่งระดับ หรือเลือก "ทุกระดับ"',
 'Select at least one administrative level, or use None to retrieve all levels.':
   'เลือกเขตการปกครองอย่างน้อยหนึ่งระดับ หรือใช้ None เพื่อเรียกดูทุกระดับ',
 'Select levels 0–15 and switch to specific-level mode.':
   'เลือกระดับ 0–15 และเปลี่ยนเป็นโหมดระดับเฉพาะ',
 'Select one or more features in the active layer.':
   'เลือกฟีเจอร์อย่างน้อยหนึ่งรายการในเลเยอร์ที่ใช้งานอยู่',
 'Select output directory...': 'เลือกโฟลเดอร์เอาต์พุต…',
 'Selected administrative levels:': 'ระดับการปกครองที่เลือก:',
 'Selected feature IDs:': 'ID ของฟีเจอร์ที่เลือก:',
 'Selected feature(s) in active layer':
   'ฟีเจอร์ที่เลือกในเลเยอร์ที่ใช้งานอยู่',
 'Selected features (': 'ฟีเจอร์ที่เลือก (',
 'Selected-feature AOI captured successfully (':
   'บันทึก AOI จากฟีเจอร์ที่เลือกสำเร็จ (',
 'Selected-feature AOI captured successfully.':
   'บันทึก AOI จากฟีเจอร์ที่เลือกสำเร็จ',
 'Selected-feature AOI is invalid.':
   'AOI จากฟีเจอร์ที่เลือกไม่ถูกต้อง',
 'Selected-feature AOI requires a vector layer.':
   'AOI จากฟีเจอร์ที่เลือกต้องใช้เลเยอร์เวกเตอร์',
 'Selected-feature AOI validation failed:':
   'การตรวจสอบ AOI จากฟีเจอร์ที่เลือกล้มเหลว:',
 'Sending query to Overpass...': 'กำลังส่งคิวรีไปยัง Overpass…',
 'Server ': 'เซิร์ฟเวอร์ ',
 'Shapefile': 'Shapefile',
 'Shapefile export completed in:': 'การส่งออก Shapefile เสร็จสมบูรณ์ใน:',
 'Shapefile field names shortened for':
   'ชื่อฟิลด์ Shapefile ถูกย่อสำหรับ',
 'Shapefile layer(s) to QGIS.': 'เลเยอร์ Shapefile ไปยัง QGIS',
 'Short in-plugin help with links to the full online documentation.':
   'ความช่วยเหลือแบบย่อในปลั๊กอินพร้อมลิงก์ไปยังเอกสารประกอบออนไลน์ฉบับเต็ม',
 'Show AOI coordinates and source CRS in the dialog.':
   'แสดงพิกัด AOI และ CRS ต้นทางในไดอะล็อก',
 'Show a concise description of the active administrative filter.':
   'แสดงคำอธิบายโดยย่อของตัวกรองการปกครองที่ใช้งานอยู่',
 'Source CRS is invalid.': 'CRS ต้นทางไม่ถูกต้อง',
 'South latitude cannot be greater than north latitude.':
   'ละติจูดใต้ไม่สามารถมากกว่าละติจูดเหนือได้',
 'South:': 'ใต้:',
 'Starting Overpass download...': 'กำลังเริ่มการดาวน์โหลด Overpass…',
 'Supporting copy: muted, wrapped and visually quiet.':
   'ข้อความสนับสนุน: เบา ตัดบรรทัด และดูสงบ',
 "Tag '{tag}' contains an empty value list.":
   'แท็ก "{tag}" มีรายการค่าที่ว่างเปล่า',
 'Temporary workspace cleanup complete:':
   'การล้างเวิร์กสเปซชั่วคราวเสร็จสมบูรณ์:',
 'Temporary workspace cleanup complete: no matching files found.':
   'การล้างเวิร์กสเปซชั่วคราวเสร็จสมบูรณ์: ไม่พบไฟล์ที่ตรงกัน',
 'Temporary-file cleanup skipped: workspace directory is invalid.':
   'ข้ามการล้างไฟล์ชั่วคราว: โฟลเดอร์เวิร์กสเปซไม่ถูกต้อง',
 'The OSM download succeeded, but the output could not be created.':
   'การดาวน์โหลด OSM สำเร็จ แต่ไม่สามารถสร้างเอาต์พุตได้',
 "The Overpass response must be a JSON object with an 'elements' list.":
   'การตอบกลับ Overpass ต้องเป็นออบเจกต์ JSON ที่มีรายการ "elements"',
 'The QGIS map canvas CRS is invalid.':
   'CRS ของแคนวาสแผนที่ QGIS ไม่ถูกต้อง',
 'The active layer CRS is invalid.':
   'CRS ของเลเยอร์ที่ใช้งานอยู่ไม่ถูกต้อง',
 'The active layer extent is empty.':
   'ขอบเขตของเลเยอร์ที่ใช้งานอยู่ว่างเปล่า',
 'The active layer must be a vector layer.':
   'เลเยอร์ที่ใช้งานอยู่ต้องเป็นเลเยอร์เวกเตอร์',
 'The combined name is too long. Shorten one or more components.':
   'ชื่อที่รวมแล้วยาวเกินไป ย่อส่วนประกอบอย่างน้อยหนึ่งรายการ',
 'The combined selected-feature geometry is empty.':
   'เรขาคณิตของฟีเจอร์ที่เลือกรวมกันว่างเปล่า',
 'The current AOI is invalid:': 'AOI ปัจจุบันไม่ถูกต้อง:',
 'The current QGIS map extent is empty.':
   'ขอบเขตแผนที่ QGIS ปัจจุบันว่างเปล่า',
 'The dialog cannot close while a download thread is running. Cancellation has been requested; close the dialog after it stops.':
   'ไม่สามารถปิดไดอะล็อกในขณะที่เธรดดาวน์โหลดกำลังทำงาน มีการร้องขอยกเลิกแล้ว ปิดไดอะล็อกหลังจากหยุดลง',
 'The download completed, but no confirmed output name was available.':
   'การดาวน์โหลดเสร็จสมบูรณ์ แต่ไม่มีชื่อเอาต์พุตที่ยืนยันแล้ว',
 "The exported Shapefile '{path}' could not be opened in QGIS.":
   'ไม่สามารถเปิด Shapefile ที่ส่งออก "{path}" ใน QGIS',
 "The exported layer '{layer_name}' could not be opened in QGIS.":
   'ไม่สามารถเปิดเลเยอร์ที่ส่งออก "{layer_name}" ใน QGIS',
 'The output name does not contain any valid filename characters.':
   'ชื่อเอาต์พุตไม่มีอักขระชื่อไฟล์ที่ถูกต้อง',
 'The output name is empty after filename validation.':
   'ชื่อเอาต์พุตว่างเปล่าหลังการตรวจสอบชื่อไฟล์',
 'The selected features contain no valid geometry.':
   'ฟีเจอร์ที่เลือกไม่มีเรขาคณิตที่ถูกต้อง',
 'The selected output directory does not exist. Choose an existing folder.':
   'โฟลเดอร์เอาต์พุตที่เลือกไม่มีอยู่ เลือกโฟลเดอร์ที่มีอยู่',
 'There is no active download to cancel.':
   'ไม่มีการดาวน์โหลดที่ใช้งานอยู่ให้ยกเลิก',
 'Timeout on server ': 'หมดเวลาบนเซิร์ฟเวอร์ ',
 'Translate widget labels while preserving each original English string.':
   'แปลป้ายกำกับวิดเจ็ตโดยรักษาแต่ละสตริงภาษาอังกฤษต้นฉบับ',
 'Trying Overpass server ': 'กำลังลองเซิร์ฟเวอร์ Overpass ',
 'Unable to start AOI drawing:': 'ไม่สามารถเริ่มวาด AOI:',
 'Unclassified OSM elements not written to feature layers:':
   'องค์ประกอบ OSM ที่ไม่ถูกจัดประเภทซึ่งไม่ได้เขียนลงในเลเยอร์ฟีเจอร์:',
 'Unsupported geometry family: {geometry_family}':
   'ตระกูลเรขาคณิตที่ไม่รองรับ: {geometry_family}',
 "Unsupported geometry type '{geometry_type}' for feature '{feature_key}'.":
   'ประเภทเรขาคณิต "{geometry_type}" ที่ไม่รองรับสำหรับฟีเจอร์ "{feature_key}"',
 'Unsupported geometry type for Shapefile export: {geometry_type}':
   'ประเภทเรขาคณิตที่ไม่รองรับสำหรับการส่งออก Shapefile: {geometry_type}',
 "Unsupported match mode '{mode}' for feature '{feature_key}'.":
   'โหมดการจับคู่ "{mode}" ที่ไม่รองรับสำหรับฟีเจอร์ "{feature_key}"',
 'Unsupported output format:': 'ฟอร์แมตเอาต์พุตที่ไม่รองรับ:',
 "Unsupported tag value type for '{feature_key}': {value_type}":
   'ประเภทค่าของแท็กที่ไม่รองรับสำหรับ "{feature_key}": {value_type}',
 'Update Current QGIS Map Extent':
   'อัปเดตขอบเขตแผนที่ QGIS ปัจจุบัน',
 'Update the "N selected" count next to the category heading.':
   'อัปเดตจำนวน "เลือก N รายการ" ถัดจากหัวข้อหมวดหมู่',
 'Update the filename preview as the user edits the components.':
   'อัปเดตตัวอย่างชื่อไฟล์เมื่อผู้ใช้แก้ไขส่วนประกอบ',
 'Use Layer Extent': 'ใช้ขอบเขตเลเยอร์',
 'Use Selected Features': 'ใช้ฟีเจอร์ที่เลือก',
 'Use local cache where available':
   'ใช้แคชในเครื่องเมื่อมี',
 'Use selected features in the active vector layer as the AOI.':
   'ใช้ฟีเจอร์ที่เลือกในเลเยอร์เวกเตอร์ที่ใช้งานอยู่เป็น AOI',
 'Use the full extent of the active QGIS layer as the AOI.':
   'ใช้ขอบเขตเต็มของเลเยอร์ QGIS ที่ใช้งานอยู่เป็น AOI',
 'Use the full extent of the active QGIS layer.':
   'ใช้ขอบเขตเต็มของเลเยอร์ QGIS ที่ใช้งานอยู่',
 'Use the selected features of the active vector layer as the AOI.':
   'ใช้ฟีเจอร์ที่เลือกของเลเยอร์เวกเตอร์ที่ใช้งานอยู่เป็น AOI',
 'Using cached data; no Overpass network request was needed.':
   'กำลังใช้ข้อมูลที่แคชไว้ ไม่จำเป็นต้องมีคำขอเครือข่าย Overpass',
 'Validate filename and any explicitly selected admin levels.':
   'ตรวจสอบชื่อไฟล์และระดับผู้ดูแลระบบที่เลือกไว้อย่างชัดเจน',
 'Validate inputs and start the background Overpass download.':
   'ตรวจสอบอินพุตและเริ่มการดาวน์โหลด Overpass ในเบื้องหลัง',
 'WGS84 AOI bbox: south=': 'กรอบขอบเขต AOI ใน WGS84: ใต้=',
 'WGS84 AOI geometry is not available.':
   'เรขาคณิต AOI ใน WGS84 ไม่พร้อมใช้งาน',
 'Warning: download succeeded, but the response could not be cached:':
   'คำเตือน: ดาวน์โหลดสำเร็จ แต่ไม่สามารถแคชการตอบกลับได้:',
 'Waterways': 'ทางน้ำ',
 'West longitude cannot be greater than east longitude.':
   'ลองจิจูดตะวันตกไม่สามารถมากกว่าลองจิจูดตะวันออกได้',
 'West:': 'ตะวันตก:',
 'Writing Shapefile {layer_index}/{total}: {layer_name}...':
   'กำลังเขียน Shapefile {layer_index}/{total}: {layer_name}…',
 'Writing layer {layer_index}/{total}: {layer_name} ({count:,} features)...':
   'กำลังเขียนเลเยอร์ {layer_index}/{total}: {layer_name} ({count:,} ฟีเจอร์)…',
 'attempt ': 'ความพยายาม ',
 'characters).': 'อักขระ)',
 'connection error — ': 'ข้อผิดพลาดการเชื่อมต่อ — ',
 'e.g. CBD': 'เช่น CBD',
 'e.g. Kenya': 'เช่น เคนยา',
 'e.g. Nairobi': 'เช่น ไนโรบี',
 'e.g. NairobiCounty': 'เช่น NairobiCounty',
 'elements (': 'องค์ประกอบ (',
 'export failed:': 'การส่งออกล้มเหลว:',
 'feature records).': 'ระเบียนฟีเจอร์)',
 'feature(s)).': 'ฟีเจอร์))',
 'features written.': 'ฟีเจอร์ที่เขียน',
 'file(s) deleted.': 'ไฟล์ที่ถูกลบ',
 'relation geometry assignment(s); relation-member geometry assembly is not implemented yet.':
   'การกำหนดเรขาคณิตของความสัมพันธ์; การประกอบเรขาคณิตของสมาชิกความสัมพันธ์ยังไม่ได้ใช้งาน',
 'relations).': 'ความสัมพันธ์)',
 'response_data must be a dictionary.':
   'response_data ต้องเป็นพจนานุกรม',
 "response_data['elements'] must be a list.":
   "response_data['elements'] ต้องเป็นรายการ",
 'temporary file(s) could not be deleted. They may still be in use by QGIS or another process.':
   'ไม่สามารถลบไฟล์ชั่วคราวได้ ไฟล์เหล่านี้อาจยังถูกใช้งานโดย QGIS หรือโปรเซสอื่น',
 'timeout — ': 'หมดเวลา — ',
 '{output_format} export failed: {error}':
   'การส่งออก {output_format} ล้มเหลว: {error}',
 '— Confirm Overwrite': '— ยืนยันการเขียนทับ',
 '— Export Error': '— ข้อผิดพลาดการส่งออก',
 '— Help': '— ช่วยเหลือ',
 '— Output Naming': '— การตั้งชื่อเอาต์พุต',
}