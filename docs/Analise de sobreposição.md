# 05 - Análise de Sobreposição

Esta etapa é responsável por identificar áreas com conflito espacial — onde duas ou mais camadas fundiárias coexistem — e definir, de forma objetiva, qual classe deve prevalecer na malha final.
** **

## Como Funciona

01. **Agregação matricial:** A consolidação das camadas é realizada por meio de álgebra de mapas, aplicando-se uma operação de mínimo pixel a pixel entre todas as imagens raster. Como os valores dos pixels representam a hierarquia fundiária, o menor valor corresponde à classe de maior prioridade, sendo selecionado para compor a malha final.
02. **Geração da malha integrada:** O resultado da agregação é um único raster contínuo, no qual cada pixel representa a classe fundiária dominante, sem sobreposições ou lacunas.
   
** **
## Refinamento Vetorial


Após a finalização da malha fundiária, cada classe foi segregada e submetida a um cálculo de média de cada valor de pixel em relação ao seu dado na estrutura vetorial. Estabeleceu-se que, caso a estrutura vetorial apresentasse uma cobertura de sobreposição acima de 10% em relação à mesma classe na estrutura matricial, o vetor seria mantido. Essa operação foi realizada para as 14 classes fundiárias visando preservar a originalidade da informação, visto que a conversão da malha matricial para vetor resultou em uma geometria serrilhada ("pixelizada").  O limiar de 10% foi utilizado para excluir vetores com ruídos.
Para integrar todas as classes no formato vetorial, aplicou-se uma ordenação por peso: a classe de maior prioridade permaneceu intacta, enquanto as de menor peso foram recortadas em áreas sobrepostas.

** **
## Resultados do Processo
- Áreas sem sobreposição são incorporadas diretamente.
- Áreas com sobreposição passam pela hierarquização ponderada, gerando uma malha sem vazios ou duplicidades, com decisões rastreáveis.






