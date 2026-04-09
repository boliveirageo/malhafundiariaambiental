# Conversão de estrutura matricial

## Sobre
A conversão matricial (rasterização) é fundamental para permitir a análise de sobreposições em larga escala de forma eficiente.

## Parâmetros de Rasterização
- **Resolução Espacial**: O arquivo vetorial é convertido para o  Pixel de **10 metros**, compatível com escala 1:25.000.
- **Cálculo do peso da camada fundiária**: Para cada camada fundiária, atribuiu-se um peso específico fundamentado nos critérios estabelecidos neste estudo. As notas foram conferidas seguindo a escala de Saaty e, posteriormente, multiplicadas pelos pesos de importância derivados da matriz de ponderação. O resultado final consiste na média ponderada desses valores, na qual as camadas de maior relevância apresentam os maiores índices de prioridade em relação às demais. A tabela 1 mostra o cálculo e ordem de relevância das cada camada fundiária.
- **Valor do Pixel da Imagem:** Cada camada recebe um valor de pixel distinto do peso calculado no processo de hierarquização para permitir a diferenciação na álgebra de mapas.


### Tabela 1 - Cálculo da Hierarquização das camadas fundiárias
| Classe Fundiária | Seg. Jurídica (0,56) | Precisão Geo (0,26) | Sobreposição (0,12) | Estabilidade (0,06) | Peso Global (AHP) | Nível Hierarquizado |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Massa d'água / Urbana | 9 | 9 | 9 | 9 | 9,00 | 1 |
| TI Homologada | 9 | 8 | 7 | 9 | 8,52 | 3 |
| UC Proteção Integral | 9 | 8 | 7 | 9 | 8,52 | 4 |
| Área Militar | 8 | 8 | 9 | 9 | 8,18 | 5 |
| Imóvel Privado (SIGEF/SNCI) | 8 | 9 | 6 | 7 | 7,86 | 6 |
| Assentamento | 7 | 7 | 6 | 6 | 6,76 | 7 |
| Glebas Públicas - Floresta Pública Não Destinada | 6 | 7 | 5 | 7 | 6,20 | 8 |
| UC Uso Sustentável | 6 | 6 | 6 | 7 | 6,06 | 9 |
| Glebas Públicas | 6 | 6 | 4 | 5 | 5,70 | 10 |
| Quilombola Declarado | 5 | 6 | 4 | 6 | 5,20 | 11 |
| TI Não Homologada | 4 | 4 | 3 | 4 | 3,88 | 12 |
| Quilombola Não Declarado | 3 | 4 | 3 | 4 | 3,32 | 13 |
| Imóvel Privado (CAR) | 2 | 4 | 1 | 3 | 2,46 | 14/15 |

**Observação:** Imóvel Privado do CAR recebeu dois níveis de hierarquia (14 e 15), para distinguir o CAR sem sobreposição do CAR com sobreposição respectivamente

No final da conversão, foram gerados 14 imagens de cada camada fundiária, onde o valor do pixel é igual ao seu nivel hierarquico atribuído.

