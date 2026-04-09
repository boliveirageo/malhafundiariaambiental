# Algoritmo de Malha Fundiária Ambiental: Metodologia e Processamento Territorial 

## Sobre
O material apresenta o desenvolvimento de um algoritmo avançado voltado para a criação de uma malha fundiária ambiental integrada e precisa para o território brasileiro. O processo é estruturado em cinco etapas principais, que abrangem desde a coleta e tratamento de dados brutos até a resolução de conflitos de sobreposição territorial por meio do método multicritério AHP. Essa metodologia transforma registros diversos em um produto geoespacial padronizado, garantindo segurança jurídica e precisão técnica ao classificar áreas como propriedades privadas, terras indígenas e unidades de conservação. Além de fornecer uma visão detalhada dos ativos ambientais, é possível atualizações mensais para apoiar análises territoriais de escala nacional. O objetivo final é oferecer uma ferramenta robusta para a gestão territorial, capaz de identificar com clareza a ocupação do solo e a conformidade ambiental no Brasil. A atual versão (v1.0) foi testado para o estado de Goiás

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
  
  
