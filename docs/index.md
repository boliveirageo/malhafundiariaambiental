# Malha Fundiária Ambiental do Brasil: Base Integrada para Análise e Gestão Territorial 

## Sobre
A Malha Fundiária Ambiental é um produto geoespacial integrado que organiza, de forma padronizada, as diferentes categorias territoriais do Brasil — como propriedades privadas, terras indígenas e unidades de conservação — em uma única base contínua. Ao consolidar dados dispersos e inconsistentes, a malha permite identificar limites, sobreposições e lacunas no território, oferecendo uma visão clara da ocupação do solo e possibilitando análises de ativos ambientais. Esse dado é estratégico para o Brasil, pois fortalece a segurança jurídica, apoia políticas públicas (como o Código Florestal), qualifica análises ambientais e contribui para a governança territorial e cadeias produtivas livres de desmatamento.

Este dado foi desenvolvido pelo Laboratório de Processamento de Imagens e Geoprocessamento (LAPIG) da Universidade Federal de Goiás (UFG). Esta documentação descreve o desenvolvimento de um algoritmo avançado voltado à geração da Malha Fundiária Ambiental, estruturado para integrar, padronizar e resolver conflitos entre diferentes bases territoriais. Adicionalmente, junto à documentação, são disponibilizadas estatísticas de ativos ambientais, ampliando as possibilidades de análise e aplicação do produto.


## Etapas Metodológicas

O algoritmo de malha fundiária ambiental é composto por seis (06) etapas principais, conforme detalhado nos documentos:

* **1 - Ingestão dos Dados:** Consiste na coleta, organização e download das bases fundiárias, abrangendo territórios sociais e de proteção, reforma agrária e imóveis rurais privados.

* **2 - Pré-processamento de dados:** Inclui a correção topológica para eliminar inconsistências geométricas, reprojeção das camadas, filtragem (como a exclusão de imóveis com status cancelado ou suspenso no CAR) e resolução de duplicidades e sobreposições.

* **3 - Hierarquização das Camadas :** Nesta etapa é realizada uma hierarquização de prioridades entre as camadas fundiárias. Ou seja, define-se qual camada será priorizada em casos de sobreposição. Para isso, aplicou-se o método multicritério Analytic Hierarchy Process (AHP), que é uma técnica estruturada para tomadas de decisão complexas.

* **4 - Conversão Matricial:** Realiza-se a rasterização das camadas fundiárias processadas, organizando-as em imagens cujos valores de pixel seguem o processo de hierarquização aplicado por meio do método AHP.

* **5 - Análise de sobreposição fundiária:** No processo de análise de sobreposição, aplica-se uma estatística de agregação na qual se mantém o pixel com o valor da camada fundiária de maior prioridade. Subsequentemente, selecionam-se os arquivos vetoriais originais de cada camada fundiária que apresentou sobreposição com o arquivo raster hierarquizado final.

* **6- Integração Ambiental:** Integram-se os ativos ambientais (como Áreas de Preservação Permanente - APPs) à malha fundiária, gerando o produto final consolidado, o qual contém informações das malhas fundiárias em conjunto com os seus respectivos ativos ambientais.

** **
## Requisito

* Python versão 3.9 acima

* QGIS Desktop versão 3.44 acima

* GDAL 

* Duckdb 


## Histórico de versões

* v 1.0
    * Construção da Malha Fundiária Ambiental para o estado de Goiás. 
  
  
