# Análise de sobre posição

## Sobre
Esta fase identifica áreas com conflito espacial (onde dois ou mais poligonos coexistem) e define qual camada deve prevalecer na malha final.
** **

## Procedimento
A metodologia aplicada para a consolidação das informações consistiu em uma análise de sobreposição espacial por meio da técnica de agregação de pixels. O processo foi executado através do cálculo do valor mínimo (mínimo pixel a pixel) entre todas as as imagens convertidas das camadas fundiárias, sem priorizado o menor valor, ou seja, o pixel da camada fundiária com maior prioridade(menor valor hierarquico) gerando um arquivo matricial da malha fundiária integrada.


** **
## Refinamento Vetorial
Após a finalização da malha fundiária, cada classe foi segregada e submetida a um cálculo de média de cada valor de pixel em relação ao seu dado na estrutura vetorial. Estabeleceu-se que, caso a estrutura vetorial apresentasse uma cobertura de sobreposição acima de 10% em relação à mesma classe na estrutura matricial, o vetor seria mantido. Essa operação foi realizada para as 14 classes fundiárias visando preservar a originalidade da informação, visto que a conversão da malha matricial para vetor resultou em uma geometria serrilhada ("pixelizada").  O limiar de 10% foi utilizado para excluir vetores com ruídos.
Para integrar todas as classes no formato vetorial, aplicou-se uma ordenação por peso: a classe de maior prioridade permaneceu intacta, enquanto as de menor peso foram recortadas em áreas sobrepostas.

** **
## Resultados do Processo
- Áreas sem sobreposição são incorporadas diretamente.
- Áreas com sobreposição passam pela hierarquização ponderada, gerando uma malha sem vazios ou duplicidades, com decisões rastreáveis.

![Figura 6 - Fluxograma de Análise de Sobreposição](/figuras/hierarquização.png)

Figura 6 - Fluxograma de Análise de Sobreposição

![Figura 9 - Nível Hierárquico de cada camada fundiária](/figuras/nivel_hierarquico.png)

Figura 9 - Nível Hierárquico de cada camada fundiária 


