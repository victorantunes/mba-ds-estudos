# 08 · Social Network Analysis (SNA)
**Profa. Adriana Silva · 2 aulas (02 e 09/09/2025) · Prioridade: ALTA (métricas de centralidade e cálculo "na mão" são cobráveis)**

> SNA **não é análise de redes sociais/mídias sociais** (Instagram/Facebook). É a análise de **relacionamentos entre entidades** (ligações telefônicas, e-mails, transações financeiras). **Também não é análise de cluster** (embora alguns materiais chamem comunidade de cluster).

## 1. Conceitos
- **Grafo:** **nós** (vértices; indivíduos ou entidades) ligados por **links/arestas** (evidência de interdependência: e-mail, ligação, transação, endereço). Objetivo: medir **quão importante é cada nó** dentro da rede a que pertence.
- Origens: **Seis Graus de Separação (Stanley Milgram)** — experimento das cartas: em média estamos a ~6 passos de qualquer pessoa (em rede completa, ~4 conexões).
- **Rede direcionada (directed)** × **não direcionada (undirected):** direcionada quando a direção da relação importa (A liga 100 vezes para B ≠ B para A); **peso** quando a intensidade importa (precisa de coluna `weight`). A estrutura dos dados deve comportar o objetivo (a direção é definida já na extração).
- **Comunidades:** grupos de nós **mais fortemente ligados entre si do que com o resto da rede** (sub-redes). Comunidade **interna** (predomínio da sua marca) × **externa** (predomínio da concorrência).
- **Papéis dos nós:** **Líder** (conectividade recíproca, nó central da comunidade), **Seguidor** (comportamento parecido, menor magnitude, ligação direta ao líder), **Marginal** (perfil de seguidor sem proximidade ao líder), **Outlier** (poucas/escassas conexões), **Bridge/ponte** (conecta comunidades). Visão **estática × dinâmica** (comunidades e papéis mudam no tempo).
- **Aplicações (marketing/telecom):** segmentação além de rentabilidade/ciclo de vida; **retenção de líderes** e de seguidores (**redução de churn**); **cross-sell/up-sell em líderes (efeito viral)**; seleção melhor na **aquisição**; incluir a métrica da rede no **modelo de churn**.

## 2. Processo de SNA (passo a passo)
1) obter acesso à informação/contexto → 2) extrair dados e **determinar links (A→B) e forças**, definir se a rede é direcionada → 3) montar a base → 4) **detectar comunidades** → 5) estipular **papéis** → resultados/aplicações. Passos 1–3 são contexto e manipulação de dados; **SNA propriamente dito = 4 e 5**.

## 3. Métricas de centralidade (CAI NA PROVA)
| Métrica | O que mede | Como calcula / interpreta |
|---|---|---|
| **Degree (grau)** | nº de links do nó (importância local) | undirected: nº de links. Directed: **out-degree** (saem), **in-degree** (chegam), **degree = in + out** |
| **Degree ponderado** | generalização do degree considerando o **peso** dos links | soma dos pesos |
| **Clustering Coefficient (CC)** | quão conectados estão os **vizinhos** do nó entre si | **CC = (ligações existentes entre os vizinhos) / (ligações possíveis entre eles)**. Medida "**egoísta**": do nó para a rede dele. CC=1: todos os vizinhos já se conhecem (nó dispensável). **CC perto de 0: vizinhos só se conectam por meio dele → ele é muito importante para a rede dele** (se sai, a rede deixa de se conectar). Atenção: CC = 0 com degree 1 não significa importância |
| **Closeness (proximidade)** | **média dos caminhos mais curtos** do nó até todos os outros | proximidade ~ tempo para **difundir uma informação** a partir do nó; **menor média de passos = nó mais central** (contamina mais rápido). Com peso: decidir se peso alto = mais perto ou mais longe e **inverter o peso se preciso** |
| **Betweenness (intermediação)** | **nº de vezes que o nó aparece nos menores caminhos** entre outros pares | Cb(u) = Σ σst(u)/σst. Nós com alta betweenness são os **"porteiros" / conduítes da informação** (pontes). Ex. jogador no menor caminho até o gol |

**Estatísticas gerais da rede:** nº de nós; nº de arestas; **densidade** = links existentes / links possíveis (grafo completo); **comprimento médio do caminho** (soma dos menores caminhos / quantidade deles; se =2, em média 2 passos); **excentricidade** (distância do nó ao mais distante); **raio** (menor excentricidade); **diâmetro** (maior excentricidade).

## 4. Detecção de comunidades
- **Modularidade (Q)** = métrica mais popular: fração dos links **dentro** das comunidades **menos** a fração esperada se os links fossem aleatórios; mede a **qualidade da divisão**. Algoritmo de Louvain-like: cada nó começa sendo uma comunidade; iterativamente avalia ganho de modularidade e funde.
- **Resolution (resolução):** controla o tamanho das comunidades. **Valor menor → mais comunidades, menores; valor maior (> 1) → menos comunidades, maiores.** Escolher por **tentativa e erro conforme a necessidade do negócio** (o "maior" modularidade nem sempre atende).
- Tamanhos de comunidade tendem a seguir **lei de potência** (poucas muito grandes, muitas pequenas).
- **Algoritmos (igraph):** modularidade ótima (<100 vértices), edge betweenness (melhor resultado, grafos até ~700 vértices/3.500 arestas), fast greedy, walktrap (primeira tentativa), leading eigenvector, spinglass, label propagation, multilevel, **info map (para grafos direcionados)**.
- Um nó pode ser **ponte dentro da comunidade, mas não na rede inteira**. Nós isolados: vale perguntar se fazem sentido na rede (custo computacional).

## 5. Ferramentas
- **Gephi:** software livre (Java; Win/Linux/Mac) de visualização e análise de redes. CSV de **links precisa de colunas `Source` e `Target` (e opcional `weight` numérico)**; importar como **tabela de links**; outros formatos .net, .gdf, .gephi. Janelas: visão geral, laboratório de dados, visualização, partição/classificação (colorir por modularidade/degree), layout, estatísticas.
- **Python/igraph** (biblioteca mais usada para grafos): scripts da aula (comunidades da base **Karate Club** — 34 nós e 78 ligações, rede clássica de teste). Referências: Pinheiro (SNA in Telecommunications), Newman (Networks).
- Dica: usar a **estatística descritiva** para entender a rede quando não dá para visualizar o grafo.

## Pergunta típica
Calcular CC de um nó em um grafo pequeno; diferença entre in-degree e out-degree; o que significa closeness/betweenness alto; o que muda quando Resolution aumenta; por que SNA ≠ mídia social; qual aplicação de SNA reduz churn; papéis (líder, seguidor, bridge, outlier).
