# Pré-processamento dos dados 

## Sobre
Nesta etapa, os dados brutos integrados no PostgreSQL passam por correções geométricas e filtragens rigorosas para garantir a precisão dos cálculos e a integridade da malha

## Procedimentos Principais
1. **Correção e Reprojeção:** Eliminação de inconsistências geométricas e reprojeção de todas as camadas para uma projeção métrica (Albers).
2. **Filtragem do CAR:** Remoção de imóveis com status "Cancelado" ou "Suspenso", e exclusão de tipos de assentamentos e povos tradicionais que já existem em bases oficiais mais estáveis.
3. **Exclusão de Grilagem Digital:** Imóveis com área igual ou superior à área total do município são removidos para prevenir distorções.
4. **Resolução de Duplicidades:** No CAR, mantém-se o registro mais recente. Entre SIGEF e CAR, o CAR é recortado para eliminar o conflito.
5. **Priorização Social:** O recorte das propriedades é feito da menor para a maior área. Esse critério é aplicado nos dados do CAR. Já na relação entre SIGEF e SNCI, aplica-se a priorização social, sendo que os dados do SIGEF têm maior prioridade sobre os do SNCI.

## Fluxograma
![Figura 2 - Fluxograma de Pré-processamento](/figuras/pre_processamento.png)

Figura 2 - Fluxograma de Pré-processamento

## Exemplos Visuais

![Figura 3 - Exemplo de Grilagem Digital](/figuras/grilagem_digital.png)

Figura 3 - Exemplo de Grilagem Digital
