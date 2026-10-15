# 14 · Unsupervised ML — Análise de Cluster (Clustering I e II)
**Prof. Wilson Tarantin Jr. · 2 aulas · Prioridade: ALTA (início do bloco de Machine Learning; sempre cobra "qual método e por quê")**
*Livro-base: Fávero & Belfiore (2024), cap. 9. Código: Python (scipy, scikit-learn).*

## 1. Objetivo e características
- **Quando aplicar:** quando se quer **agrupar as observações (linhas)** em grupos **homogêneos internamente** e **heterogêneos entre si**, com base nas variáveis escolhidas. (Para agrupar **variáveis** usa-se a análise fatorial/PCA.)
- É **técnica exploratória, não supervisionada**: não há variável-alvo, não há relação esperada entre variáveis, **não tem caráter preditivo**, **não há inferência** para observações de fora da amostra. Se entrarem/saírem **observações** ou **variáveis**, **o agrupamento deve ser refeito**.
- Aplicações: segmentação de clientes, análise socioeconômica de regiões, detecção de fraude (transações atípicas), controle de qualidade, grupos de pacientes.
- Estrutura dos dados: tabela com observações em linhas e variáveis em colunas.

## 2. Tratamento inicial: padronização (Z-score)
- A análise é **muito sensível a unidades e escalas** → quando as variáveis têm escalas diferentes, **padronize (Z-score)**: Z = (X − média)/desvio, resultando em **média 0 e desvio 1**. Se já estiverem na mesma escala, pode não padronizar (como o professor fez em um dos exemplos).
- **Sensível a outliers** (ex.: um país pode ficar sozinho num cluster por destoar em uma variável). Com **variáveis categóricas**, aplica-se a **Análise de Correspondência** (resumo 16); no cluster usam-se só as quantitativas.

## 3. Método hierárquico aglomerativo (analítico, passo a passo)
- **Esquema:** começa com **n clusters** (cada observação sozinha, estágio 0) → une as **duas mais próximas** → repete **n−1 vezes** até restar **1 cluster**. **Dendrograma** é o gráfico da formação. **A quantidade de clusters é escolhida ao longo da análise** (olhando o dendrograma).
- **Escolha 1 — medida de dissimilaridade (distância entre observações):** **euclidiana** (padrão), **euclidiana quadrática**, **Manhattan/City Block** (soma de |diferenças|), **Chebychev** (máxima diferença), **Canberra**; ou **correlação de Pearson entre linhas** (é medida de *semelhança*: converter em dissimilaridade com **1 − r**).
- **Escolha 2 — método de encadeamento** (qual distância usar quando já há clusters):
  - **Nearest neighbor / single linkage:** distância **mínima** entre elementos; privilegia menores distâncias; bom quando observações são **distintas**.
  - **Furthest neighbor / complete linkage:** distância **máxima**; privilegia maiores distâncias; bom quando as observações são **parecidas**.
  - **Between groups / average linkage:** **média** das distâncias entre todos os pares.
  - Fórmulas: d(MN)W = mín{dMW; dNW} (single), máx (complete), média (average). **É importante comparar dendrogramas** de diferentes métodos (análise de sensibilidade).
- **Quantos clusters?** olhe os **saltos de distância** no dendrograma: **saltos grandes indicam união de observações muito diferentes** → corte antes do salto. Extremos (1 cluster ou n clusters) não fazem sentido prático; muitos clusters dificultam a interpretação.
- **Depois de formar:** cria-se a **variável indicadora do cluster** (label) e analisam-se as **estatísticas descritivas por grupo**.
- **Quais variáveis contribuíram? ANOVA/Teste F:** **F = variabilidade entre grupos / variabilidade dentro dos grupos**; gl numerador = **K − 1** (K = nº de clusters), gl denominador = **n − K**. **p < α → rejeita H0 → a variável tem média diferente em pelo menos um cluster → contribuiu para a formação**; maiores F (com significância) = variáveis mais importantes. **p > α** → média igual em todos os clusters (não ajudou).

## 4. Método não hierárquico: K-means
- **K definido a priori.** **Algoritmo:** escolhe K centroides iniciais (aleatórios) → aloca cada observação ao **centroide mais próximo** → **recalcula centroides** (média do grupo) → realoca → itera **até não haver realocações (convergência)**. Minimiza a **WCSS** (*within-cluster sum of squares*, soma dos quadrados das distâncias de cada observação ao centro do seu cluster).
- **Escolher K:**
  - **Método do cotovelo (Elbow):** plota WCSS × K e busca a "dobra" a partir da qual a queda deixa de ser expressiva (equilibrar queda do WCSS × interpretabilidade).
  - **Método da silhueta:** s = (b − a)/máx(a, b), onde **a** = distância média dentro do cluster onde está e **b** = distância média ao **cluster mais próximo** em que não está; **de −1 a 1: próximo de 1 = melhor; próximo de −1 = pior.** Calcula-se a média para vários K.
- **K-means × hierárquico:** hierárquico = analítico, mostra o passo a passo, mais difícil com muitas observações; **K-means é mais objetivo (minimização) e serve para amostras grandes**. O resultado do hierárquico pode ser **input do K-means** para sugerir K inicial.

## 5. Python (do script da aula)
`from scipy.stats import zscore` (padronizar) · `from scipy.spatial.distance import pdist` (matriz de distâncias) · `scipy.cluster.hierarchy as sch` → `sch.linkage(df, method='single|complete|average', metric='euclidean|cityblock')` e `sch.dendrogram` · `AgglomerativeClustering(n_clusters=3, metric='euclidean', linkage='complete')` · `KMeans(n_clusters=k, init='random', random_state=100)` (+ `.inertia_` para WCSS) · `silhouette_score` · `pingouin` (ANOVA) · plotly/matplotlib/seaborn para gráficos (ex.: scatter 3D).

## Pergunta típica
Diferença entre cluster hierárquico e K-means (quando se define K) · por que padronizar · single × complete × average · como escolher o nº de clusters (saltos no dendrograma; cotovelo; silhueta) · o que mede a silhueta · como saber quais variáveis formaram clusters (teste F/ANOVA) · por que cluster não é preditivo.
