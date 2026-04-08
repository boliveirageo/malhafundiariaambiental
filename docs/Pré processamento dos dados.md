# Pré-processamento dos dados 

## Sobre
Nesta etapa, os dados brutos integrados no PostgreSQL passam por correções geométricas e filtragens rigorosas para garantir a precisão dos cálculos e a integridade da malha

## Procedimentos Principais
1. **Correção Topológica e Reprojeção**: As camadas são convertidas para um sistema métrico para assegurar a precisão nos cálculos de área.
2. **Filtragem do CAR**: Remoção de imóveis com status 'cancelado' ou 'suspenso', além de registros de assentamentos e povos tradicionais já contemplados em bases específicas.
3. **Mitigação de 'Grilagem Digital'**: Exclusão de registros onde a área do imóvel iguala ou supera a área total do município.
4. **Resolução de Duplicidades**: Priorização do registro mais recente e eliminação de sobreposição com áreas do INCRA (SIGEF/SNCI) por meio do recorte das feições.
5. **Priorização Social**: Recorte delimitado a pequenas propriedades de até quatro módulos fiscais.

## Fluxograma
![Figura 2 - Fluxograma de Pré-processamento](/figuras/pre_processamento.png)

Figura 2 - Fluxograma de Pré-processamento

## Exemplos Visuais

![Figura 3 - Exemplo de Grilagem Digital](/figuras/grilagem_digital.png)

Figura 3 - Exemplo de Grilagem Digital
