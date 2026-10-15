# 14 · Unsupervised ML — Análise de Cluster (Clustering I e II)
**Prof. Wilson Tarantin Jr. · 2 aulas · Prioridade: ALTA (início do bloco de ML; sempre cobra "qual método e por quê")**
*Livro-base: Fávero & Belfiore (2024), cap. 9. Código: Python (scipy, scikit-learn).*

> **Em uma frase:** clustering **agrupa observações parecidas** (linhas) em grupos homogêneos por dentro e distintos entre si, **sem rótulo prévio**.

**Pré-requisitos:** Z-score e ANOVA/teste F (01); mapa de ML (02). **Vem depois:** 15 (agrupa variáveis) e 16 (variáveis categóricas).

## Por que isso importa (intuição)
Você tem milhares de clientes e quer perfis de comportamento, mas ninguém disse a "resposta certa". O cluster mede **distâncias** entre clientes e junta os próximos. Duas decisões moldam o resultado: **como medir a distância** e **como juntar os grupos**; a terceira, **quantos grupos manter**, depende de ler o dendrograma (ou do cotovelo/silhueta no K-means).

## 1. Objetivo e características
- Agrupa **observações (linhas)**; para agrupar **variáveis** use PCA/fatorial (15).
- **Exploratório e não supervisionado:** não há Y, **não é preditivo**, **não infere** para observações de fora da amostra. Se entram ou saem observações/variáveis, **refaz-se o agrupamento**.
- Aplicações: segmentação de clientes, regiões socioeconômicas, fraude (transações atípicas), grupos de pacientes.

## 2. Tratamento inicial
- A análise é **sensível à escala**: se as variáveis têm unidades diferentes, **padronize (Z-score)** — senão a de maior escala domina a distância.
- **Sensível a outliers** (um país pode ficar sozinho num cluster). Use só variáveis **quantitativas**; categóricas → ANACOR/ACM (16).

## 3. Método hierárquico aglomerativo
- **Esquema:** começa com **n clusters** (cada observação sozinha) → une os **dois mais próximos** → repete **n−1 vezes** até restar um. O **dendrograma** mostra o passo a passo; o nº de clusters se escolhe **depois**, olhando o gráfico.
- **Escolha 1 — distância entre observações:** **euclidiana** (padrão), euclidiana quadrática, **Manhattan** (soma de |diferenças|), **Chebychev** (maior diferença), Canberra; correlação entre linhas vira dissimilaridade com **1 − r**.
- **Escolha 2 — encadeamento (distância entre clusters):**
  - **Single (nearest neighbor):** distância **mínima** entre elementos dos dois grupos.
  - **Complete (furthest neighbor):** distância **máxima**.
  - **Average (between groups):** **média** das distâncias entre todos os pares.
- **Quantos clusters?** Procure **saltos grandes** de distância no dendrograma: um salto grande significa que você está unindo grupos **muito diferentes** → corte **antes** dele.
- **ANOVA/teste F** para saber **quais variáveis contribuíram:** F = variabilidade **entre** grupos ÷ variabilidade **dentro**; gl = (K − 1) e (n − K). **p < α → a variável tem média diferente em ao menos um cluster → ajudou a formá-los.**

**Exemplo resolvido (distâncias).** Pontos em uma reta: A = 1, B = 2, C = 6, D = 8.
- Estágio 1: junta **A e B** (distância 1). Estágio 2: junta **C e D** (distância 2).
- Distância entre {A,B} e {C,D}: **single** = mín = |B−C| = **4**; **complete** = máx = |A−D| = **7**; **average** = (5 + 7 + 4 + 6) ÷ 4 = **5,5**.
Os três métodos podem mudar a ordem das uniões em dados reais — por isso compare dendrogramas (análise de sensibilidade).
**ANOVA:** com n = 30 observações e K = 3 clusters, F tem gl = **2 e 27**.

## 4. Método não hierárquico: K-means
- **K definido a priori.** Algoritmo: escolhe K centroides → aloca cada observação ao **centroide mais próximo** → **recalcula** os centroides (médias) → repete até **não haver realocações**. Minimiza a **WCSS** (soma dos quadrados das distâncias aos centroides).
- **Escolher K:**
  - **Cotovelo (Elbow):** gráfico WCSS × K; escolha a "dobra" onde a queda deixa de ser grande.
  - **Silhueta:** s = (b − a) ÷ máx(a, b), com **a** = distância média dentro do próprio cluster e **b** = distância média ao **cluster vizinho mais próximo**; vai de **−1 a 1** (**próximo de 1 = melhor**).
- **K-means × hierárquico:** hierárquico é analítico e mostra o passo a passo (difícil com muitas observações); **K-means é objetivo e escala melhor**. O hierárquico pode sugerir o K inicial.

**Exemplo resolvido (K-means).** Pontos 1, 2, 6, 8 com K = 2 e centroides iniciais 1 e 8. Alocação: {1, 2} e {6, 8}. Novos centroides: **1,5** e **7**. Ninguém muda de grupo → convergiu. WCSS = (0,25 + 0,25) + (1 + 1) = **2,5**.
**Silhueta:** se a = 2 e b = 6, s = (6 − 2) ÷ 6 ≈ **0,67** (bom).

## 5. Python
`zscore` (padronizar) · `scipy.cluster.hierarchy` (`linkage`, `dendrogram`) · `AgglomerativeClustering` · `KMeans(n_clusters=k)` (`.inertia_` = WCSS) · `silhouette_score` · `pingouin` (ANOVA).

## Armadilhas e confusões comuns
| Confusão | O correto |
|---|---|
| Cluster agrupa variáveis | agrupa **observações**; variáveis → PCA/fatorial |
| Cluster é preditivo | **não**; sem Y e sem inferência fora da amostra |
| Não precisa padronizar | **precisa**, se as escalas diferem |
| Hierárquico exige K no início | K se escolhe **depois**, no dendrograma; o K-means exige K **antes** |
| Silhueta perto de −1 é boa | **perto de 1** é boa |
| Variável com p > α ajudou a formar clusters | **não**: a média é igual em todos os clusters |
| Single e complete dão o mesmo resultado | single = mínimo; complete = máximo; mudam o dendrograma |

## Resumo-relâmpago
- Agrupa linhas, sem Y. Padronize. Distância (euclidiana) + encadeamento (single/complete/average).
- Dendrograma: cortar antes dos grandes saltos. K-means: K a priori; cotovelo e silhueta.
- ANOVA (F, gl K−1 e n−K): p < α → variável relevante.

## Teste-se
1. Por que padronizar antes do cluster?
<details markdown="1"><summary>Ver resposta</summary>Porque a distância é sensível à escala: variáveis em unidades maiores dominariam o agrupamento.</details>

2. Quando se define o número de clusters no hierárquico e no K-means?
<details markdown="1"><summary>Ver resposta</summary>No hierárquico, depois, olhando o dendrograma; no K-means, antes (K a priori), apoiado em cotovelo e silhueta.</details>

3. Qual a diferença entre single e complete linkage?
<details markdown="1"><summary>Ver resposta</summary>Single usa a menor distância entre elementos dos dois clusters; complete usa a maior.</details>

4. O que indica silhueta próxima de 1?
<details markdown="1"><summary>Ver resposta</summary>Observações bem alocadas: perto do próprio cluster e longe do vizinho.</details>

5. Como saber quais variáveis formaram os clusters?
<details markdown="1"><summary>Ver resposta</summary>Pelo teste F (ANOVA): p < α indica que a média da variável difere entre clusters.</details>

## Pergunta típica
Diferença entre cluster hierárquico e K-means (quando se define K) · por que padronizar · single × complete × average · como escolher o nº de clusters (saltos no dendrograma, cotovelo, silhueta) · o que mede a silhueta · como saber quais variáveis formaram clusters (F/ANOVA) · por que cluster não é preditivo
