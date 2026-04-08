# Ingestão dos Dados 

A primeira etapa consiste na coleta e organização sistemática das bases fundiárias de referência. O objetivo é realizar o download dos dados e integrá-los em um banco de dados **PostgreSQL**, criando um ambiente unificado para o processamento.

## Bases de Dados Utilizadas


#### Grupo: Territórios Sociais e de Proteção
| Fonte | URL dos Dados |
| :--- | :--- |
| Terras Indígenas (homologadas e não homologadas)|https://geoserver.funai.gov.br/geoserver/Funai/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=Funai%3Atis_poligonais&maxFeatures=10000&outputFormat=SHAPE-ZIP|
| Territórios Quilombolas (declarados e não declarados) ||
| Unidades de Conservação (Uso Sustentável e Proteção Integral) ||
| Territórios de Proteção ||
| Áreas Militares ||
| Massa d'águas ||


#### Grupo: Reforma Agrária
| Fonte | URL dos Dados |
| :--- | :--- |
| Assentamentos ||
| Glebas Públicas ||
| Florestas Públicas Não Declaradas (FPND) ||

#### Grupo: Imóveis Rurais Privados
| Fonte | URL dos Dados |
| :--- | :--- |
| SIGEF / SNCI (INCRA) ||
| Cadastro Ambiental Rural (CAR) ||

Estes dados são integrados e armazenados em um banco de dados PostgreSQL para garantir a integridade e facilitar o processamento subsequente
** **
## Fluxo de Trabalho

![Figura 1 - Fluxograma de Ingestão de Dados](/figuras/ingestao_dados.png)

Figura 1 - Fluxograma de Ingestão de Dados

*Modelo de Referência: Cartas da Terra (Malha Fundiária v2, 2025)*


  
  
