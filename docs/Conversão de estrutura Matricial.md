# Conversão de estrutura matricial

## Sobre
A conversão matricial (rasterização) é fundamental para permitir a análise de sobreposições em larga escala de forma eficiente.

## Parâmetros de Rasterização
- **Resolução Espacial:** Pixel de **10 metros**, compatível com escala 1:25.000.
- **Identificação:** Cada camada recebe um valor de pixel distinto para permitir a diferenciação na álgebra de mapas.

## Tabela de Identificação de Classes (Exemplo Ilustrativo)
| Classe | Valor do Pixel |
| :--- | :--- |
| Massa d'água | 1 |
| Massa d'água | 2 |
| Teraa Indígena Homologada | 3 |
| Unidade de Conservação Proteção Integral | 4 |
| Área Militar | 5 |
| Imóvel Privado (SIGEF) | 6 |
| Assentamento | 7 |
| Glebas Públicas - FNPD | 8 |
| Unidade de Conservação de Uso Sustentável | 9 |
| Glebas Públicas | 10 |
| Quilombola Declarado | 11 |
| Terra Indígena Não Homologada | 13 |
| Quilombola Não Declarado | 14 |
| CAR (Privado) | 15 e 16 |


## Construção da Imagem Multibanda
As camadas são empilhadas em uma imagem multibanda, onde cada banda corresponde a uma camada fundiária processada [6].

![Figura 5 - Processo de Conversão Matricial](/figuras/conversao_raster.png)

Figura 5 - Processo de Conversão Matricial
