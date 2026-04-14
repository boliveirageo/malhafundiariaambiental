# Integração da Malha Fundiária e Ambiental 

## Sobre
A etapa final integra os ativos ambientais à malha fundiária consolidada, gerando o produto final para análises territoriais de escala nacional.
** **

## Integração de Áreas de Preservação Permanente (APP)
A etapa final integra os ativos ambientais compostos pelas Áreas de Preservação Permanente (APPs), seu uso e cobertura da terra, e a Reserva Legal de cada imóvel — à malha consolidada. A fonte de dados varia conforme o bioma: para todos os biomas, exceto Pampa e Pantanal, as APPs são extraídas da FBDS (Fundação Brasileira de Desenvolvimento Sustentável); já para os biomas Pampa e Pantanal, utilizam-se dados do CAR, devido à ausência destas informações na FBDS. Os dados de Reserva Legal são extraídos exclusivamente do CAR, por ser a única fonte disponível por imóvel.
O produto final da metodologia consiste em dois (02) subprodutos principais: 
1. **Malha de Classe Fundiária Final (formatos vetorial e matricial)** 
2. **Malha da Quantidade de Sobreposições de Classes (formato matricial)**

Os procedimentos realizados nas APPs consistiram no agrupamento por classe de uso do solo, eliminando-se polígonos residuais (slivers). A Reserva Legal, por sua vez, foi agrupada pelo código do imóvel no CAR. Após a consolidação dos ativos ambientais, realizou-se uma análise de sobreposição entre as APPs e as Reservas Legais. Nos casos de intersecção, manteve-se a área da APP e removeu-se o excedente da Reserva Legal, visando evitar a duplicidade de áreas no cálculo do balanço de passivos ambientais. Posteriormente, executou-se nova análise de sobreposição entre os ativos ambientais e as camadas fundiárias; onde houvesse sobreposição, o ativo recebia o código da respectiva camada fundiária, identificando sua pertença. Por fim, todas as camadas foram unificadas em um único arquivo, denominado 'malha fundiária ambiental'.
** **

## Produtos Gerados
O algoritmo disponibiliza três subprodutos principais:
1. **Malha de Classe Fundiária Final:** Estrutura vetorial (Hard Class).
2. **Malha de Classe Fundiária Final:** Estrutura matricial (Hard Class).
3. **Malha de Sobreposições:** Estrutura matricial (Quantidade de sobreposições).
 

![Figura 4 - Fluxograma de Integração Ambiental](figuras/integracao_ambiental.png)

Figura 4 - Fluxograma de Integração Ambiental

