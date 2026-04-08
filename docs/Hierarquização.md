# Hierarquização das camadas fundiárias

## Sobre
Esta fase identifica áreas com conflito espacial (onde dois ou mais polígonos coexistem) e define qual camada deve prevalecer na malha final.
** **

## Método AHP (Processo Hierárquico Analítico)
Para resolver sobreposições, utiliza-se o método multicritério **AHP**, que pondera as camadas com base em quatro critérios principais:

1. **Segurança Jurídica:** Grau de respaldo legal e reconhecimento formal.
2. **Precisão Geométrica:** Qualidade e acurácia espacial dos dados.
3. **Sobreposição:** Capacidade de manter a integridade diante de conflitos.
4. **Estabilidade do domínio:** Permanência e consolidação histórica da posse ou uso.

Matrizes de Pesos e Critérios
Abaixo, os pesos definidos por meio da escala de Saaty (1 a 9):
Tabela 1: Matriz de Peso dos Critérios Normalizados | Critérios | Seg. Jurídica | Precisão Geo. | Sobreposição | Estabilidade | Média (Peso) | | :--- | :---: | :---: | :---: | :---: | :---: | | Segurança Jurídica | 0,599 | 0,662 | 0,536 | 0,438 | 0,56 | | Precisão Geométrica | 0,198 | 0,221 | 0,322 | 0,313 | 0,26 | | Sobreposição | 0,120 | 0,073 | 0,107 | 0,188 | 0,12 | | Estabilidade | 0,084 | 0,044 | 0,035 | 0,063 | 0,06 |
## Resultados do Processo
- Áreas sem sobreposição são incorporadas diretamente.
- Áreas com sobreposição passam pela hierarquização ponderada, gerando uma malha sem vazios ou duplicidades, com decisões rastreáveis.

![Figura 6 - Fluxograma de Análise de Sobreposição](/figuras/hierarquização.png)

Figura 6 - Fluxograma de Análise de Sobreposição

![Figura 7 - Matriz de Critérios AHP](/figuras/critérios.png)

Figura 7 - Matriz de Paridade entre os Critérios 

![Figura 8 - Matriz de peso dos critérios normalizados](/figuras/criterios_normal.png)

Figura 8 - Matriz de peso dos critérios normalizados 

![Figura 9 - Nível Hierárquico de cada camada fundiária](/figuras/nivel_hierarquico.png)

Figura 9 - Nível Hierárquico de cada camada fundiária 


