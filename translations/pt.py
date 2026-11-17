"""Portuguese (Português) translation pack for the OSM Data Toolkit plugin.
Keys remain the English source strings; preserve placeholders and HTML."""
TEXT = {
 '\n<h3>Quick start</h3>\n<ol>\n  <li><b>Choose an area.</b> Use the current map extent, draw a rectangle\n      on the map, or use the bounding box of selected features or a\n      layer\'s extent.</li>\n  <li><b>Tick the OSM categories</b> you need (POI, stops, roads,\n      buildings, boundaries, landuse, ...).</li>\n  <li><b>Choose an output format and folder</b>, then click\n      <b>Download OSM Data</b>.</li>\n</ol>\n\n<h3>Good to know</h3>\n<ul>\n  <li><b>GeoPackage is recommended.</b> A Shapefile cannot hold very many\n      attribute columns, so on large areas some rarely used tag columns\n      may be left out (the log tells you when this happens).</li>\n  <li><b>Keep the area focused.</b> Very large areas produce huge Overpass\n      responses and can be slow or rejected by the public servers.</li>\n  <li><b>The cache</b> lets repeat downloads of the same query reuse\n      earlier results.</li>\n  <li><b>"Unclassified OSM elements"</b> in the log is informational: they\n      are mostly untagged vertices of lines and polygons that do not belong\n      to any selected category.</li>\n</ul>\n\n<p>Data &copy; OpenStreetMap contributors, available under the\n<a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a>.</p>\n<p><i>This plugin is not endorsed by or affiliated with the\nOpenStreetMap Foundation.</i></p>\n':
 '\n<h3>Início rápido</h3>\n<ol>\n  <li><b>Escolha uma área.</b> Use a extensão atual do mapa, desenhe um retângulo\n      no mapa, ou use a caixa delimitadora dos elementos selecionados ou a\n      extensão de uma camada.</li>\n  <li><b>Marque as categorias OSM</b> que você precisa (POI, paradas, vias,\n      edifícios, limites, uso do solo, ...).</li>\n  <li><b>Escolha um formato de saída e uma pasta</b> e clique em\n      <b>Baixar dados OSM</b>.</li>\n</ol>\n\n<h3>Bom saber</h3>\n<ul>\n  <li><b>O GeoPackage é recomendado.</b> Um Shapefile não comporta muitas\n      colunas de atributos, por isso, em áreas grandes, algumas colunas de\n      etiquetas raramente usadas podem ser omitidas (o log informa quando\n      isso acontece).</li>\n  <li><b>Mantenha a área focada.</b> Áreas muito grandes geram respostas\n      enormes do Overpass e podem ser lentas ou rejeitadas pelos servidores\n      públicos.</li>\n  <li><b>O cache</b> permite que downloads repetidos da mesma consulta\n      reutilizem resultados anteriores.</li>\n  <li><b>"Elementos OSM não classificados"</b> no log é informativo: são\n      principalmente vértices sem etiquetas de linhas e polígonos que não\n      pertencem a nenhuma categoria selecionada.</li>\n</ul>\n\n<p>Dados &copy; colaboradores do OpenStreetMap, disponíveis sob a\n<a href="https://www.openstreetmap.org/copyright">Open Database\nLicence</a>.</p>\n<p><i>Este plugin não é endossado nem afiliado à\nOpenStreetMap Foundation.</i></p>\n',
 ' responded successfully.': ' respondeu com sucesso.',
 ' seconds...': ' segundos…',
 '" style="color:#0B5E8E; text-decoration:none;">OpenStreetMap contributors</a> (ODbL)':
   '" style="color:#0B5E8E; text-decoration:none;">Colaboradores do OpenStreetMap</a> (ODbL)',
 ', east=': ', leste=',
 ', north=': ', norte=',
 ', west=': ', oeste=',
 '0 selected': '0 selecionados',
 '<p>Plugin version': '<p>Versão do plugin',
 'A download is already running.': 'Já existe um download em andamento.',
 'A labelled column of feature checkboxes.':
   'Uma coluna rotulada de caixas de seleção de elementos.',
 'AOI drawing cancelled.': 'Desenho da AOI cancelado.',
 'AOI geometry is empty.': 'A geometria da AOI está vazia.',
 'AOI geometry is missing.': 'A geometria da AOI está ausente.',
 'AOI name': 'Nome da AOI',
 'AOI rectangle captured successfully.':
   'Retângulo da AOI capturado com sucesso.',
 'AOI source CRS is invalid.': 'O CRS de origem da AOI é inválido.',
 'AOI validation failed:': 'Falha na validação da AOI:',
 'AOI:': 'AOI:',
 'AOI: QGIS interface is not available.':
   'AOI: a interface do QGIS não está disponível.',
 "AOI: click 'Draw AOI', then drag a rectangle on the QGIS map.":
   'AOI: clique em "Desenhar AOI" e arraste um retângulo no mapa do QGIS.',
 "AOI: click 'Use Layer Extent' to use the full extent of the active QGIS layer.":
   'AOI: clique em "Usar extensão da camada" para usar a extensão completa da camada ativa do QGIS.',
 'AOI: click and drag on the QGIS map.':
   'AOI: clique e arraste no mapa do QGIS.',
 'AOI: failed to resolve active layer extent':
   'AOI: falha ao determinar a extensão da camada ativa',
 'AOI: failed to resolve selected features':
   'AOI: falha ao determinar os elementos selecionados',
 'AOI: invalid': 'AOI: inválida',
 'AOI: no active QGIS layer.': 'AOI: nenhuma camada ativa do QGIS.',
 'AOI: no feature(s) selected in the active layer.':
   'AOI: nenhum elemento selecionado na camada ativa.',
 'AOI: not yet resolved': 'AOI: ainda não determinada',
 "AOI: select feature(s) in the active QGIS layer, then click 'Use Selected Features'.":
   'AOI: selecione elemento(s) na camada ativa do QGIS e clique em "Usar elementos selecionados".',
 'AOI: the active layer is not a vector layer.':
   'AOI: a camada ativa não é uma camada vetorial.',
 'AOI: unable to create': 'AOI: não foi possível criar',
 'AOI: unable to resolve': 'AOI: não foi possível determinar',
 'Activate the interactive rectangle AOI map tool.':
   'Ativar a ferramenta interativa de retângulo de AOI no mapa.',
 'Active layer extent': 'Extensão da camada ativa',
 'Active-layer extent AOI is invalid.':
   'A AOI da extensão da camada ativa é inválida.',
 'Active-layer extent captured successfully.':
   'Extensão da camada ativa capturada com sucesso.',
 'Active-layer extent validation failed:':
   'Falha na validação da extensão da camada ativa:',
 'Administrative boundaries': 'Limites administrativos',
 'Administrative boundary filter: all levels (no admin_level filter).':
   'Filtro de limites administrativos: todos os níveis (sem filtro admin_level).',
 'Administrative boundary levels': 'Níveis de limites administrativos',
 'Administrative boundary levels:': 'Níveis de limites administrativos:',
 'Administrative levels must be an integer, a numeric string, a sequence of levels, or None.':
   'Os níveis administrativos devem ser um inteiro, uma string numérica, uma sequência de níveis ou None.',
 'All OSM feature categories cleared.': 'Todas as categorias de elementos OSM foram limpas.',
 'All OSM feature categories selected.': 'Todas as categorias de elementos OSM foram selecionadas.',
 'All Overpass server URLs must be non-empty strings.':
   'Todos os URLs dos servidores Overpass devem ser strings não vazias.',
 'All Overpass servers and retry attempts failed.':
   'Todos os servidores Overpass e as tentativas de nova execução falharam.',
 'All administrative levels will be included.':
   'Todos os níveis administrativos serão incluídos.',
 'All administrative levels will be included; no admin_level filter will be added to the query.':
   'Todos os níveis administrativos serão incluídos; nenhum filtro admin_level será adicionado à consulta.',
 'All attempts failed for server ': 'Todas as tentativas falharam para o servidor ',
 'All levels (0–15; no admin_level filter)':
   'Todos os níveis (0–15; sem filtro admin_level)',
 'An existing output directory is required for Shapefile export.':
   'É necessário um diretório de saída existente para exportação Shapefile.',
 'An output GeoPackage path is required.':
   'É necessário um caminho de saída GeoPackage.',
 'An output name is required for Shapefile export.':
   'É necessário um nome de saída para exportação Shapefile.',
 'Append a timestamped message to the processing log.':
   'Anexar uma mensagem com data/hora ao log de processamento.',
 'Append an exported feature count to the processing log.':
   'Anexar uma contagem de elementos exportados ao log de processamento.',
 'Area of Interest': 'Área de interesse',
 'At least one OSM feature must be selected.':
   'Pelo menos um elemento OSM deve ser selecionado.',
 'At least one OSM feature must be supplied.':
   'Pelo menos um elemento OSM deve ser fornecido.',
 'At least one Overpass server must be provided.':
   'Pelo menos um servidor Overpass deve ser fornecido.',
 'Attempt details:': 'Detalhes das tentativas:',
 'Automatically add downloaded layers to QGIS':
   'Adicionar automaticamente as camadas baixadas ao QGIS',
 'Background Overpass download started.':
   'Download Overpass em segundo plano iniciado.',
 'Browse': 'Procurar',
 'Browse…': 'Procurar…',
 'Buildings': 'Edifícios',
 'Bus stops': 'Paradas de ônibus',
 'CRS:': 'CRS:',
 'Cache hit:': 'Acerto no cache:',
 'Cache hit: using saved Overpass response ({age} day(s) old).':
   'Acerto no cache: usando resposta Overpass salva ({age} dia(s) de idade).',
 'Cache miss:': 'Falha no cache:',
 'Cache miss: could not read saved response ({error}).':
   'Falha no cache: não foi possível ler a resposta salva ({error}).',
 'Cache miss: query hash does not match the saved response.':
   'Falha no cache: o hash da consulta não corresponde à resposta salva.',
 'Cache miss: saved response is incomplete or invalid.':
   'Falha no cache: a resposta salva está incompleta ou é inválida.',
 'Cache miss: saved response is older than {days} days.':
   'Falha no cache: a resposta salva é mais antiga que {days} dias.',
 'Cache miss: saved response uses an unsupported cache format.':
   'Falha no cache: a resposta salva usa um formato de cache não suportado.',
 'Cached Overpass response:': 'Resposta Overpass em cache:',
 'Cancel': 'Cancelar',
 'Cancellation has already been requested.': 'O cancelamento já foi solicitado.',
 'Cancellation requested': 'Cancelamento solicitado',
 'Cancellation requested. If an HTTP request is already active, the downloader will stop when that request returns or times out.':
   'Cancelamento solicitado. Se já houver uma requisição HTTP ativa, o downloader parará quando essa requisição retornar ou expirar.',
 'Cancellation requested; waiting for the current request to finish...':
   'Cancelamento solicitado; aguardando a requisição atual terminar…',
 'Cannot draw AOI because the QGIS interface is unavailable.':
   'Não é possível desenhar a AOI porque a interface do QGIS não está disponível.',
 'Cannot resolve active-layer extent because QGIS is unavailable.':
   'Não é possível determinar a extensão da camada ativa porque o QGIS não está disponível.',
 'Cannot resolve current map extent because QGIS is unavailable.':
   'Não é possível determinar a extensão atual do mapa porque o QGIS não está disponível.',
 'Cannot resolve selected-feature AOI because QGIS is unavailable.':
   'Não é possível determinar a AOI dos elementos selecionados porque o QGIS não está disponível.',
 'Cannot transform an empty geometry.':
   'Não é possível transformar uma geometria vazia.',
 'Capture the current QGIS map canvas extent.':
   'Capturar a extensão atual da tela do mapa do QGIS.',
 'Choose all available levels, or select one or more levels to download (for example, 5–8 or level 5).':
   'Escolha todos os níveis disponíveis ou selecione um ou mais níveis para baixar (por exemplo, 5–8 ou nível 5).',
 'Choose an output directory before downloading.':
   'Escolha um diretório de saída antes de baixar.',
 'City name': 'Nome da cidade',
 'Classifying OSM elements and preparing GeoPackage layers.':
   'Classificando elementos OSM e preparando camadas GeoPackage.',
 'Classifying OSM elements and preparing Shapefile outputs.':
   'Classificando elementos OSM e preparando saídas Shapefile.',
 'Clear all': 'Limpar tudo',
 'Clear log': 'Limpar log',
 'Clear only the visible log, without changing processing settings.':
   'Limpar apenas o log visível, sem alterar as configurações de processamento.',
 'Clear selected levels so the user can make a narrower selection.':
   'Limpar os níveis selecionados para que o usuário possa fazer uma seleção mais restrita.',
 'Clear the messages currently shown in the Processing Log.':
   'Limpar as mensagens atualmente exibidas no log de processamento.',
 'Clear the previous AOI and display guidance for the chosen method.':
   'Limpar a AOI anterior e exibir orientações para o método escolhido.',
 'Close': 'Fechar',
 'Collect optional filename components before exporting OSM data.':
   'Coletar componentes opcionais do nome do arquivo antes de exportar dados OSM.',
 'Compact product header above the scrollable workflow.':
   'Cabeçalho compacto do produto acima do fluxo de trabalho rolável.',
 'Connection error on server ': 'Erro de conexão no servidor ',
 'Continue to Download': 'Continuar para o download',
 'Convert a name component into a Windows-safe filename token.':
   'Converter um componente de nome em um token de nome de arquivo seguro para Windows.',
 'Convert the drawn rectangle into the standard AOI object.':
   'Converter o retângulo desenhado no objeto AOI padrão.',
 'Converting OSM response to GeoPackage...':
   'Convertendo resposta OSM para GeoPackage…',
 'Converting OSM response to Shapefiles...':
   'Convertendo resposta OSM para Shapefiles…',
 'Could not combine the selected feature geometries.':
   'Não foi possível combinar as geometrias dos elementos selecionados.',
 "Could not create Shapefile staging layer '{layer_name}'.":
   'Não foi possível criar a camada de preparação Shapefile "{layer_name}".',
 'Could not create an empty bus_stops_points layer.':
   'Não foi possível criar uma camada bus_stops_points vazia.',
 "Could not create temporary QGIS layer '{layer_name}'.":
   'Não foi possível criar a camada temporária do QGIS "{layer_name}".',
 'Could not create temporary layer for admin_level {admin_level}.':
   'Não foi possível criar a camada temporária para admin_level {admin_level}.',
 'Could not create the merged bus_stops_points layer.':
   'Não foi possível criar a camada bus_stops_points mesclada.',
 'Could not delete temporary file':
   'Não foi possível excluir o arquivo temporário',
 "Could not load feature definition '{feature_key}': {error}":
   'Não foi possível carregar a definição de elemento "{feature_key}": {error}',
 'Could not merge bus-station centroids into bus-stop points.':
   'Não foi possível mesclar os centróides das estações de ônibus nos pontos de parada de ônibus.',
 'Could not overwrite existing output file: {error}':
   'Não foi possível sobrescrever o arquivo de saída existente: {error}',
 'Could not populate Shapefile for admin_level {admin_level}.':
   'Não foi possível preencher o Shapefile para admin_level {admin_level}.',
 "Could not populate temporary layer '{layer_name}'.":
   'Não foi possível preencher a camada temporária "{layer_name}".',
 'Could not prepare the Overpass query:':
   'Não foi possível preparar a consulta Overpass:',
 "Could not reopen intermediate GeoPackage layer '{layer_name}'.":
   'Não foi possível reabrir a camada GeoPackage intermediária "{layer_name}".',
 'Could not restore previous QGIS map tool:':
   'Não foi possível restaurar a ferramenta de mapa anterior do QGIS:',
 'Could not search for temporary GeoPackages:':
   'Não foi possível pesquisar GeoPackages temporários:',
 'Country name': 'Nome do país',
 'Create one section panel and return it with its body layout.':
   'Criar um painel de seção e retorná-lo com o layout do corpo.',
 'Created bus_stops_points from bus-station polygon centroids.':
   'bus_stops_points criado a partir dos centróides dos polígonos de estações de ônibus.',
 'Current QGIS map extent': 'Extensão atual do mapa do QGIS',
 'Current QGIS map extent resolved.':
   'Extensão atual do mapa do QGIS determinada.',
 'Data © <a href="': 'Dados © <a href="',
 'Deleted temporary workspace file:':
   'Arquivo temporário do espaço de trabalho excluído:',
 'Details:': 'Detalhes:',
 'Download': 'Baixar',
 'Download OSM Data': 'Baixar dados OSM',
 'Download OpenStreetMap data for any area and load it straight into QGIS.':
   'Baixe dados do OpenStreetMap para qualquer área e carregue-os diretamente no QGIS.',
 'Download cancelled because existing output files were not approved for overwrite.':
   'Download cancelado porque os arquivos de saída existentes não foram aprovados para sobrescrita.',
 'Download cancelled before it started.':
   'Download cancelado antes de começar.',
 'Download cancelled before results were returned.':
   'Download cancelado antes de os resultados serem retornados.',
 'Download cancelled before starting.':
   'Download cancelado antes de iniciar.',
 'Download cancelled in the output-naming dialog.':
   'Download cancelado na caixa de diálogo de nomenclatura de saída.',
 'Download cancelled.': 'Download cancelado.',
 'Download cancelled; existing files preserved.':
   'Download cancelado; arquivos existentes preservados.',
 'Download stopped.': 'Download interrompido.',
 'Download succeeded, but export failed.':
   'Download bem-sucedido, mas a exportação falhou.',
 'Downloading OSM data from Overpass...':
   'Baixando dados OSM do Overpass…',
 'Draw AOI': 'Desenhar AOI',
 'Draw a rectangle on the QGIS map to define the AOI.':
   'Desenhe um retângulo no mapa do QGIS para definir a AOI.',
 'Draw rectangle on map': 'Desenhar retângulo no mapa',
 'Draw the AOI rectangle on the QGIS map.':
   'Desenhe o retângulo da AOI no mapa do QGIS.',
 'Drawn AOI validation failed:':
   'Falha na validação da AOI desenhada:',
 'Drawn rectangle': 'Retângulo desenhado',
 'Drawn rectangle AOI captured successfully.':
   'Retângulo da AOI desenhado capturado com sucesso.',
 'ERROR:': 'ERRO:',
 'East:': 'Leste:',
 'Enable level checkboxes only when a specific selection is active.':
   'Habilitar as caixas de seleção de nível apenas quando uma seleção específica estiver ativa.',
 'Enable only the AOI action button for the selected method.':
   'Habilitar apenas o botão de ação de AOI para o método selecionado.',
 'Enable or disable controls while a download is running.':
   'Habilitar ou desabilitar controles enquanto um download está em andamento.',
 'Enter at least one name (City, Country, Region, or AOI).':
   'Digite pelo menos um nome (cidade, país, região ou AOI).',
 'Enter one or more name components. Blank fields will be skipped, and the remaining names will be joined with underscores. The selected output format will be retained.':
   'Digite um ou mais componentes de nome. Campos em branco serão ignorados e os nomes restantes serão unidos com sublinhados. O formato de saída selecionado será mantido.',
 'Enter_a_name_to_preview': 'Digite_um_nome_para_visualizar',
 'Export cancelled: output name is missing.':
   'Exportação cancelada: o nome de saída está ausente.',
 'Export complete:': 'Exportação concluída:',
 'Export the downloaded response and optionally load its layers.':
   'Exportar a resposta baixada e, opcionalmente, carregar suas camadas.',
 'Failed to activate rectangle AOI tool:':
   'Falha ao ativar a ferramenta de retângulo de AOI:',
 'Failed to create AOI.': 'Falha ao criar a AOI.',
 'Failed to process drawn rectangle AOI:':
   'Falha ao processar o retângulo de AOI desenhado:',
 'Failed to resolve active-layer extent.':
   'Falha ao determinar a extensão da camada ativa.',
 'Failed to resolve active-layer extent:':
   'Falha ao determinar a extensão da camada ativa:',
 'Failed to resolve current QGIS map extent:':
   'Falha ao determinar a extensão atual do mapa do QGIS:',
 'Failed to resolve selected-feature AOI.':
   'Falha ao determinar a AOI dos elementos selecionados.',
 'Failed to resolve selected-feature AOI:':
   'Falha ao determinar a AOI dos elementos selecionados:',
 "Failed to write layer '{layer_name}' to '{output_path}': {error}":
   'Falha ao gravar a camada "{layer_name}" em "{output_path}": {error}',
 "Feature '{feature_key}' has no tag definitions.":
   'O elemento "{feature_key}" não possui definições de etiquetas.',
 'Feature specification  does not expose a tag-filter mapping.':
   'A especificação de elemento não expõe um mapeamento de filtro de etiquetas.',
 'Ferry stops': 'Paradas de balsa',
 'Filename preview': 'Pré-visualização do nome do arquivo',
 'Full documentation': 'Documentação completa',
 'Generated Overpass query (': 'Consulta Overpass gerada (',
 'GeoPackage': 'GeoPackage',
 'GeoPackage layer(s) to QGIS.': 'camada(s) GeoPackage no QGIS.',
 'GeoPackage saved:': 'GeoPackage salvo:',
 'HTTP error on server ': 'Erro HTTP no servidor ',
 'HTTP error — ': 'erro HTTP — ',
 'HTTP {status} error on server {index}/{total}.':
   'Erro HTTP {status} no servidor {index}/{total}.',
 'Handle a drawing tool deactivation initiated outside this dialog.':
   'Tratar a desativação de uma ferramenta de desenho iniciada fora desta caixa de diálogo.',
 'Help': 'Ajuda',
 'Invalid east longitude: {value}':
   'Longitude leste inválida: {value}',
 'Invalid north latitude: {value}':
   'Latitude norte inválida: {value}',
 'Invalid response from server ': 'Resposta inválida do servidor ',
 'Invalid south latitude: {value}':
   'Latitude sul inválida: {value}',
 'Invalid west longitude: {value}':
   'Longitude oeste inválida: {value}',
 'Keep the numeric readout in step with the progress bar.':
   'Manter a leitura numérica sincronizada com a barra de progresso.',
 'Land & built environment': 'Terreno e ambiente construído',
 'Landuse': 'Uso do solo',
 'Language:': 'Idioma:',
 'Linear features': 'Elementos lineares',
 'Load the saved interface language and translate visible UI strings.':
   'Carregar o idioma da interface salvo e traduzir as strings visíveis da UI.',
 'Local response cache is disabled.':
   'O cache local de respostas está desativado.',
 'Main OSM Data Toolkit window.': 'Janela principal do OSM Data Toolkit.',
 'Manually capture the map extent after the user pans or zooms.':
   'Capturar manualmente a extensão do mapa após o usuário mover ou ampliar.',
 'Merged bus-station polygon centroids into bus_stops_points.':
   'Centróides de polígonos de estações de ônibus mesclados em bus_stops_points.',
 'No Overpass selectors were generated.':
   'Nenhum seletor Overpass foi gerado.',
 'No active QGIS layer is available.':
   'Nenhuma camada ativa do QGIS está disponível.',
 'No active layer is available.': 'Nenhuma camada ativa está disponível.',
 'No exportable features matched the selected categories. Try another AOI or select additional OSM feature categories.':
   'Nenhum elemento exportável correspondeu às categorias selecionadas. Tente outra AOI ou selecione categorias adicionais de elementos OSM.',
 'No features are selected in the active layer.':
   'Nenhum elemento está selecionado na camada ativa.',
 'No levels selected. Select at least one level to continue.':
   'Nenhum nível selecionado. Selecione pelo menos um nível para continuar.',
 'No selected features found.': 'Nenhum elemento selecionado encontrado.',
 'No valid Area of Interest is available. Select an AOI method and resolve the AOI before downloading.':
   'Nenhuma área de interesse válida está disponível. Selecione um método de AOI e determine a AOI antes de baixar.',
 'North:': 'Norte:',
 'Note: {layer_name} has too many tag columns for one Shapefile (DBF size limit); {count} rarely-used columns were left out.':
   'Nota: {layer_name} tem muitas colunas de etiquetas para um único Shapefile (limite de tamanho do DBF); {count} colunas raramente usadas foram omitidas.',
 'OSM Data Toolkit': 'OSM Data Toolkit',
 'OSM Data Toolkit initialised.': 'OSM Data Toolkit inicializado.',
 'OSM Feature Categories': 'Categorias de elementos OSM',
 'OSM export completed successfully.':
   'Exportação OSM concluída com sucesso.',
 'One or more output files with this name already exist. Do you want to overwrite the matching output files?':
   'Um ou mais arquivos de saída com este nome já existem. Deseja sobrescrever os arquivos de saída correspondentes?',
 'Only the selected levels': 'Apenas os níveis selecionados',
 'Only validated Overpass responses can be cached.':
   'Apenas respostas Overpass validadas podem ser armazenadas em cache.',
 'Open public spaces': 'Espaços públicos abertos',
 'Open the in-plugin help with links to the online documentation.':
   'Abrir a ajuda no plugin com links para a documentação online.',
 'Output Settings': 'Configurações de saída',
 'Output directory': 'Diretório de saída',
 'Output directory selected:': 'Diretório de saída selecionado:',
 'Output format': 'Formato de saída',
 'Output settings': 'Configurações de saída',
 'Overpass download cancelled.': 'Download Overpass cancelado.',
 'Overpass download completed:': 'Download Overpass concluído:',
 'Overpass download failed.': 'Falha no download Overpass.',
 'Overpass download failed:': 'Falha no download Overpass:',
 'Overpass download running...': 'Download Overpass em andamento…',
 'Overpass download was cancelled by the caller.':
   'O download Overpass foi cancelado pelo chamador.',
 'Overpass query must be a non-empty string.':
   'A consulta Overpass deve ser uma string não vazia.',
 "Overpass response 'elements' field is not a list.":
   'O campo "elements" da resposta Overpass não é uma lista.',
 "Overpass response does not contain an 'elements' field.":
   'A resposta Overpass não contém um campo "elements".',
 'Overpass response is not a JSON object.':
   'A resposta Overpass não é um objeto JSON.',
 'Overpass response received successfully:':
   'Resposta Overpass recebida com sucesso:',
 'Overpass server ': 'Servidor Overpass ',
 'Overpass server returned invalid JSON. Response preview: ':
   'O servidor Overpass retornou JSON inválido. Pré-visualização da resposta: ',
 'Overpass servers available:': 'Servidores Overpass disponíveis:',
 'Overpass timeout must be greater than zero.':
   'O tempo limite do Overpass deve ser maior que zero.',
 'Plugin version': 'Versão do plugin',
 'Points of interest (POI)': 'Pontos de interesse (POI)',
 'Prepared {index:,} of {total:,} OSM elements for export...':
   'Preparados {index:,} de {total:,} elementos OSM para exportação…',
 'Preparing Overpass download...': 'Preparando download Overpass…',
 'Preparing Overpass query.': 'Preparando consulta Overpass.',
 'Processing Options': 'Opções de processamento',
 'Processing log': 'Log de processamento',
 'Processing messages will appear here...':
   'As mensagens de processamento aparecerão aqui…',
 'Processing options': 'Opções de processamento',
 'Public transport & places': 'Transporte público e lugares',
 'QGIS interface object was not detected. Canvas-dependent AOI tools are disabled.':
   'O objeto de interface do QGIS não foi detectado. As ferramentas de AOI dependentes da tela estão desativadas.',
 'QGIS map canvas could not be accessed.':
   'Não foi possível acessar a tela do mapa do QGIS.',
 'QGIS map canvas is unavailable.':
   'A tela do mapa do QGIS não está disponível.',
 'Rail stops': 'Paradas ferroviárias',
 'Railways': 'Ferrovias',
 'Read the plugin version from metadata.txt (empty string if absent).':
   'Ler a versão do plugin do metadata.txt (string vazia se ausente).',
 'Read, validate and store the current QGIS map canvas extent.':
   'Ler, validar e armazenar a extensão atual da tela do mapa do QGIS.',
 'Ready.': 'Pronto.',
 'Rectangle AOI drawing tool activated.':
   'Ferramenta de desenho de retângulo de AOI ativada.',
 'Rectangle AOI drawing was cancelled.':
   'O desenho do retângulo de AOI foi cancelado.',
 'Region name': 'Nome da região',
 'Report an issue': 'Relatar um problema',
 'Request cooperative cancellation of the background worker.':
   'Solicitar cancelamento cooperativo do trabalhador em segundo plano.',
 'Request error on server ': 'Erro de requisição no servidor ',
 'Restore default GUI settings when the dialog closes.':
   'Restaurar as configurações padrão da GUI ao fechar a caixa de diálogo.',
 'Restore the GUI once the background thread has stopped.':
   'Restaurar a GUI quando a thread em segundo plano parar.',
 'Restore the QGIS map tool active before rectangle drawing.':
   'Restaurar a ferramenta de mapa do QGIS ativa antes do desenho do retângulo.',
 'Restore the map tool and reset state before hiding the dialog.':
   'Restaurar a ferramenta de mapa e redefinir o estado antes de ocultar a caixa de diálogo.',
 'Retrying in ': 'Tentando novamente em ',
 'Return selected levels, or None when all levels are requested.':
   'Retornar os níveis selecionados, ou None quando todos os níveis forem solicitados.',
 'Return the combined, sanitized filename prefix.':
   'Retornar o prefixo de nome de arquivo combinado e sanitizado.',
 'Return the mapping between feature keys and GUI checkboxes.':
   'Retornar o mapeamento entre chaves de elementos e caixas de seleção da GUI.',
 'Return the selected GUI feature keys.':
   'Retornar as chaves de elementos da GUI selecionadas.',
 'Roads': 'Vias',
 'Run a modal dialog on both Qt5 and Qt6.':
   'Executar uma caixa de diálogo modal tanto no Qt5 quanto no Qt6.',
 'Select Output Directory': 'Selecionar diretório de saída',
 'Select a vector layer with selected features.':
   'Selecione uma camada vetorial com elementos selecionados.',
 'Select all': 'Selecionar tudo',
 'Select an active QGIS layer.': 'Selecione uma camada ativa do QGIS.',
 'Select at least one OSM feature category before downloading.':
   'Selecione pelo menos uma categoria de elemento OSM antes de baixar.',
 'Select at least one administrative level, or choose All levels.':
   'Selecione pelo menos um nível administrativo ou escolha "Todos os níveis".',
 'Select at least one administrative level, or use None to retrieve all levels.':
   'Selecione pelo menos um nível administrativo ou use None para recuperar todos os níveis.',
 'Select levels 0–15 and switch to specific-level mode.':
   'Selecionar níveis 0–15 e alternar para o modo de nível específico.',
 'Select one or more features in the active layer.':
   'Selecione um ou mais elementos na camada ativa.',
 'Select output directory...': 'Selecionar diretório de saída…',
 'Selected administrative levels:': 'Níveis administrativos selecionados:',
 'Selected feature IDs:': 'IDs dos elementos selecionados:',
 'Selected feature(s) in active layer':
   'Elemento(s) selecionado(s) na camada ativa',
 'Selected features (': 'Elementos selecionados (',
 'Selected-feature AOI captured successfully (':
   'AOI dos elementos selecionados capturada com sucesso (',
 'Selected-feature AOI captured successfully.':
   'AOI dos elementos selecionados capturada com sucesso.',
 'Selected-feature AOI is invalid.':
   'A AOI dos elementos selecionados é inválida.',
 'Selected-feature AOI requires a vector layer.':
   'A AOI dos elementos selecionados requer uma camada vetorial.',
 'Selected-feature AOI validation failed:':
   'Falha na validação da AOI dos elementos selecionados:',
 'Sending query to Overpass...': 'Enviando consulta ao Overpass…',
 'Server ': 'Servidor ',
 'Shapefile': 'Shapefile',
 'Shapefile export completed in:':
   'Exportação Shapefile concluída em:',
 'Shapefile field names shortened for':
   'Nomes de campos Shapefile encurtados para',
 'Shapefile layer(s) to QGIS.': 'camada(s) Shapefile no QGIS.',
 'Short in-plugin help with links to the full online documentation.':
   'Ajuda curta no plugin com links para a documentação online completa.',
 'Show AOI coordinates and source CRS in the dialog.':
   'Mostrar as coordenadas da AOI e o CRS de origem na caixa de diálogo.',
 'Show a concise description of the active administrative filter.':
   'Mostrar uma descrição concisa do filtro administrativo ativo.',
 'Source CRS is invalid.': 'O CRS de origem é inválido.',
 'South latitude cannot be greater than north latitude.':
   'A latitude sul não pode ser maior que a latitude norte.',
 'South:': 'Sul:',
 'Starting Overpass download...': 'Iniciando download Overpass…',
 'Supporting copy: muted, wrapped and visually quiet.':
   'Texto de apoio: discreto, quebrado e visualmente silencioso.',
 "Tag '{tag}' contains an empty value list.":
   'A etiqueta "{tag}" contém uma lista de valores vazia.',
 'Temporary workspace cleanup complete:':
   'Limpeza do espaço de trabalho temporário concluída:',
 'Temporary workspace cleanup complete: no matching files found.':
   'Limpeza do espaço de trabalho temporário concluída: nenhum arquivo correspondente encontrado.',
 'Temporary-file cleanup skipped: workspace directory is invalid.':
   'Limpeza de arquivos temporários ignorada: o diretório do espaço de trabalho é inválido.',
 'The OSM download succeeded, but the output could not be created.':
   'O download OSM foi bem-sucedido, mas a saída não pôde ser criada.',
 "The Overpass response must be a JSON object with an 'elements' list.":
   'A resposta Overpass deve ser um objeto JSON com uma lista "elements".',
 'The QGIS map canvas CRS is invalid.':
   'O CRS da tela do mapa do QGIS é inválido.',
 'The active layer CRS is invalid.':
   'O CRS da camada ativa é inválido.',
 'The active layer extent is empty.':
   'A extensão da camada ativa está vazia.',
 'The active layer must be a vector layer.':
   'A camada ativa deve ser uma camada vetorial.',
 'The combined name is too long. Shorten one or more components.':
   'O nome combinado é muito longo. Encurte um ou mais componentes.',
 'The combined selected-feature geometry is empty.':
   'A geometria combinada dos elementos selecionados está vazia.',
 'The current AOI is invalid:': 'A AOI atual é inválida:',
 'The current QGIS map extent is empty.':
   'A extensão atual do mapa do QGIS está vazia.',
 'The dialog cannot close while a download thread is running. Cancellation has been requested; close the dialog after it stops.':
   'A caixa de diálogo não pode fechar enquanto uma thread de download estiver em execução. O cancelamento foi solicitado; feche a caixa de diálogo depois que ela parar.',
 'The download completed, but no confirmed output name was available.':
   'O download foi concluído, mas nenhum nome de saída confirmado estava disponível.',
 "The exported Shapefile '{path}' could not be opened in QGIS.":
   'O Shapefile exportado "{path}" não pôde ser aberto no QGIS.',
 "The exported layer '{layer_name}' could not be opened in QGIS.":
   'A camada exportada "{layer_name}" não pôde ser aberta no QGIS.',
 'The output name does not contain any valid filename characters.':
   'O nome de saída não contém nenhum caractere válido para nome de arquivo.',
 'The output name is empty after filename validation.':
   'O nome de saída está vazio após a validação do nome do arquivo.',
 'The selected features contain no valid geometry.':
   'Os elementos selecionados não contêm geometria válida.',
 'The selected output directory does not exist. Choose an existing folder.':
   'O diretório de saída selecionado não existe. Escolha uma pasta existente.',
 'There is no active download to cancel.':
   'Não há download ativo para cancelar.',
 'Timeout on server ': 'Tempo limite no servidor ',
 'Translate widget labels while preserving each original English string.':
   'Traduzir os rótulos dos widgets preservando cada string original em inglês.',
 'Trying Overpass server ': 'Tentando servidor Overpass ',
 'Unable to start AOI drawing:': 'Não foi possível iniciar o desenho da AOI:',
 'Unclassified OSM elements not written to feature layers:':
   'Elementos OSM não classificados que não foram gravados nas camadas de elementos:',
 'Unsupported geometry family: {geometry_family}':
   'Família de geometria não suportada: {geometry_family}',
 "Unsupported geometry type '{geometry_type}' for feature '{feature_key}'.":
   'Tipo de geometria não suportado "{geometry_type}" para o elemento "{feature_key}".',
 'Unsupported geometry type for Shapefile export: {geometry_type}':
   'Tipo de geometria não suportado para exportação Shapefile: {geometry_type}',
 "Unsupported match mode '{mode}' for feature '{feature_key}'.":
   'Modo de correspondência não suportado "{mode}" para o elemento "{feature_key}".',
 'Unsupported output format:': 'Formato de saída não suportado:',
 "Unsupported tag value type for '{feature_key}': {value_type}":
   'Tipo de valor de etiqueta não suportado para "{feature_key}": {value_type}',
 'Update Current QGIS Map Extent':
   'Atualizar extensão atual do mapa do QGIS',
 'Update the "N selected" count next to the category heading.':
   'Atualizar a contagem "N selecionados" ao lado do título da categoria.',
 'Update the filename preview as the user edits the components.':
   'Atualizar a pré-visualização do nome do arquivo enquanto o usuário edita os componentes.',
 'Use Layer Extent': 'Usar extensão da camada',
 'Use Selected Features': 'Usar elementos selecionados',
 'Use local cache where available':
   'Usar cache local quando disponível',
 'Use selected features in the active vector layer as the AOI.':
   'Usar os elementos selecionados na camada vetorial ativa como AOI.',
 'Use the full extent of the active QGIS layer as the AOI.':
   'Usar a extensão completa da camada ativa do QGIS como AOI.',
 'Use the full extent of the active QGIS layer.':
   'Usar a extensão completa da camada ativa do QGIS.',
 'Use the selected features of the active vector layer as the AOI.':
   'Usar os elementos selecionados da camada vetorial ativa como AOI.',
 'Using cached data; no Overpass network request was needed.':
   'Usando dados em cache; nenhuma requisição de rede Overpass foi necessária.',
 'Validate filename and any explicitly selected admin levels.':
   'Validar o nome do arquivo e quaisquer níveis administrativos explicitamente selecionados.',
 'Validate inputs and start the background Overpass download.':
   'Validar as entradas e iniciar o download Overpass em segundo plano.',
 'WGS84 AOI bbox: south=': 'Caixa delimitadora da AOI em WGS84: sul=',
 'WGS84 AOI geometry is not available.':
   'A geometria da AOI em WGS84 não está disponível.',
 'Warning: download succeeded, but the response could not be cached:':
   'Aviso: download bem-sucedido, mas a resposta não pôde ser armazenada em cache:',
 'Waterways': 'Vias navegáveis',
 'West longitude cannot be greater than east longitude.':
   'A longitude oeste não pode ser maior que a longitude leste.',
 'West:': 'Oeste:',
 'Writing Shapefile {layer_index}/{total}: {layer_name}...':
   'Gravando Shapefile {layer_index}/{total}: {layer_name}…',
 'Writing layer {layer_index}/{total}: {layer_name} ({count:,} features)...':
   'Gravando camada {layer_index}/{total}: {layer_name} ({count:,} elementos)…',
 'attempt ': 'tentativa ',
 'characters).': 'caracteres).',
 'connection error — ': 'erro de conexão — ',
 'e.g. CBD': 'ex.: CBD',
 'e.g. Kenya': 'ex.: Quênia',
 'e.g. Nairobi': 'ex.: Nairóbi',
 'e.g. NairobiCounty': 'ex.: NairobiCounty',
 'elements (': 'elementos (',
 'export failed:': 'falha na exportação:',
 'feature records).': 'registros de elementos).',
 'feature(s)).': 'elemento(s)).',
 'features written.': 'elementos gravados.',
 'file(s) deleted.': 'arquivo(s) excluído(s).',
 'relation geometry assignment(s); relation-member geometry assembly is not implemented yet.':
   'atribuição(ões) de geometria de relação; a montagem da geometria dos membros da relação ainda não está implementada.',
 'relations).': 'relações).',
 'response_data must be a dictionary.':
   'response_data deve ser um dicionário.',
 "response_data['elements'] must be a list.":
   "response_data['elements'] deve ser uma lista.",
 'temporary file(s) could not be deleted. They may still be in use by QGIS or another process.':
   'arquivo(s) temporário(s) não pôde(ram) ser excluído(s). Eles podem ainda estar em uso pelo QGIS ou por outro processo.',
 'timeout — ': 'tempo limite — ',
 '{output_format} export failed: {error}':
   'Falha na exportação {output_format}: {error}',
 '— Confirm Overwrite': '— Confirmar sobrescrita',
 '— Export Error': '— Erro de exportação',
 '— Help': '— Ajuda',
 '— Output Naming': '— Nomenclatura de saída',
}