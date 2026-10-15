# 15 · Unsupervised ML — Análise Fatorial por Componentes Principais (PCA)
**Prof. Wilson Tarantin Jr. · 2 aulas · Prioridade: ALTA (conceitos centrais e vocabulário que se repete em outras disciplinas)**

> **Em uma frase:** a PCA **resume muitas variáveis correlacionadas em poucos fatores** (combinações lineares, não correlacionados entre si), perdendo o mínimo de informação.

**Pré-requisitos:** correlação de Pearson e Z-score (01); cluster (14). **Vem depois:** 16 (ANACOR/ACM) e uso dos fatores em regressões (17).

## Por que isso importa (intuição)
Se três variáveis medem quase a mesma coisa (renda, patrimônio, gasto), guardar as três é redundante. A PCA descobre **eixos novos** que juntam essa informação repetida — você passa de 10 colunas para 3 fatores que explicam quase tudo. Isso (1) simplifica, (2) cria índices/rankings e (3) **elimina a multicolinearidade** nos modelos supervisionados, porque os fatores são **ortogonais** (correlação zero).

## 1. Objetivo e diferenças
- **Agrupa VARIÁVEIS (colunas)** em fatores; cluster agrupa **observações (linhas)**.
- **Não supervisionada**; só para variáveis **métricas**; baseia-se na **matriz de correlações de Pearson** (por isso não precisa padronizar antes — o cluster precisa).
- **Objetivos:** (1) **redução estrutural** (5 variáveis → 2 fatores); (2) **análise de construtos** (interpretar o que cada fator significa); (3) **criar rankings/índices**; (4) **criar fatores ortogonais** para modelos supervisionados.
- Fatores são **ortogonais** por construção. Sem caráter preditivo/inferência fora da amostra.

## 2. Passo a passo
1. **Matriz de correlações.** Correlações altas (±1) → poucos fatores bastam; próximas de 0 → a PCA não ajuda.
2. **Adequação — teste de esfericidade de Bartlett:** H0: a matriz de correlações é a **identidade** (variáveis não correlacionadas). **Queremos rejeitar H0 (p < 0,05)** para a análise ser viável.
3. **Autovalores (λ):** quanto da variância das variáveis originais cada fator captura. Soma dos autovalores = K (nº de variáveis); **% de variância = λ ÷ K**. O 1º fator tem o maior autovalor.
4. **Quantos fatores? Critério de Kaiser: manter os de autovalor > 1** (um fator com λ < 1 carrega menos informação que uma variável original).
5. **Cargas fatoriais (loadings):** correlação de cada variável original com cada fator; servem para **interpretar** o fator. A **rotação** (ex.: varimax) deixa a interpretação mais limpa sem mudar a variância total acumulada.
6. **Comunalidade:** parte da variância de **cada variável original** retida pelos fatores mantidos (0–100%).
7. **Ranking/índice:** Rᵢ = F₁ᵢ·(% var. F₁) + F₂ᵢ·(% var. F₂) + … — cada fator ponderado pelo seu % de variância; depois ordena.
- **Scores:** os fatores são calculados a partir das variáveis **padronizadas (Z)** e têm média 0.

**Exemplo resolvido.** 4 variáveis, autovalores 2,6; 1,1; 0,2; 0,1 (soma = 4). % de variância: 65%; 27,5%; 5%; 2,5%. Kaiser mantém os **dois primeiros** (λ > 1) → **92,5%** acumulados.
**Comunalidade:** uma variável com cargas 0,8 (F1) e 0,3 (F2) tem comunalidade = 0,8² + 0,3² = 0,64 + 0,09 = **0,73** → 73% da sua variância é explicada pelos dois fatores.
**Índice:** observação com F1 = 1,2 e F2 = −0,4: R = 1,2·0,65 + (−0,4)·0,275 = 0,78 − 0,11 = **0,67**.

## 3. Python
`FactorAnalyzer(n_factors=k, method='principal', rotation=None)` · `calculate_bartlett_sphericity` · `fa.get_eigenvalues()` · `fa.loadings_` · `fa.get_communalities()` · `fa.transform(df)`. Exemplos: desempenho de áreas de uma empresa e banco de casas (3 fatores retêm 68,5%).

## Armadilhas e confusões comuns
| Confusão | O correto |
|---|---|
| PCA agrupa observações | agrupa **variáveis**; observações → cluster |
| Bartlett: queremos não rejeitar H0 | queremos **rejeitar** H0 (há correlação) |
| Manter fatores com autovalor < 1 | Kaiser: manter **λ > 1** |
| Cargas = pesos que multiplicam a variável | cargas = **correlações** variável–fator |
| Rotação muda a variância total | **não** muda a variância acumulada nem as comunalidades |
| PCA serve para variáveis categóricas | só **métricas**; categóricas → ANACOR/ACM |
| Fatores têm correlação entre si | são **ortogonais** (correlação zero) |

## Resumo-relâmpago
- Agrupa variáveis; ortogonais; baseada em correlações. Bartlett: rejeitar H0.
- Autovalor = variância capturada; Kaiser: λ > 1; % variância = λ ÷ K.
- Cargas = correlações; comunalidade = variância retida por variável; ranking = soma ponderada.

## Teste-se
1. Por que a PCA ajuda a resolver multicolinearidade?
<details markdown="1"><summary>Ver resposta</summary>Porque os fatores são ortogonais (correlação zero), então usá-los como regressores elimina a correlação entre preditores.</details>

2. Qual a H0 do teste de Bartlett e qual decisão desejamos?
<details markdown="1"><summary>Ver resposta</summary>H0: a matriz de correlações é a identidade. Queremos rejeitá-la (p < 0,05).</details>

3. Autovalores 2,6; 1,1; 0,2; 0,1. Quantos fatores pelo critério de Kaiser?
<details markdown="1"><summary>Ver resposta</summary>Dois (os de autovalor maior que 1).</details>

4. O que é comunalidade?
<details markdown="1"><summary>Ver resposta</summary>A proporção da variância de uma variável original retida pelos fatores mantidos.</details>

## Pergunta típica
O que difere PCA de cluster (variáveis × observações) · quando a análise é adequada (Bartlett: rejeitar H0) · critério de Kaiser (autovalor > 1) · o que é autovalor/% de variância · o que são cargas fatoriais e comunalidades · por que fatores são ortogonais e como isso ajuda em modelos supervisionados · como montar um ranking com soma ponderada · PCA exige variáveis métricas
