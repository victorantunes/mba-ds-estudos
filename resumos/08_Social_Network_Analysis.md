# 08 · Social Network Analysis (SNA)
**Profa. Adriana Silva · 2 aulas · Prioridade: ALTA (métricas de centralidade e cálculo "na mão" são cobráveis)**

> **Em uma frase:** SNA mede **a importância de cada nó** olhando para **como ele se conecta** aos outros — quem influencia, quem faz ponte, quem está isolado.

**Pré-requisitos:** noção de grafos (nós e arestas). **Vem depois:** aplicações em churn e marketing.

> **Atenção:** SNA **não é** análise de mídias sociais (Instagram/Facebook): é análise de **relacionamentos entre entidades** (ligações telefônicas, e-mails, transações). Também **não é análise de cluster**, embora comunidade lembre cluster.

## Por que isso importa (intuição)
Dois clientes têm o mesmo gasto e a mesma idade, mas um liga para 50 pessoas e o outro para 2. Se o primeiro cancelar, **arrasta amigos junto**. Tabelas comuns não enxergam isso; a rede enxerga. É a lógica de "retenha o líder e a rede toda fica".

## 1. Conceitos
- **Grafo:** **nós** (vértices; pessoas ou entidades) ligados por **links/arestas** (e-mail, ligação, transação).
- **Direcionada × não direcionada:** direcionada quando a direção importa (A liga para B ≠ B liga para A). **Peso** quando a intensidade importa (coluna `weight`).
- **Seis graus de separação (Milgram):** em média, ~6 passos separam duas pessoas quaisquer.
- **Comunidade:** grupo de nós **mais ligado entre si do que ao resto da rede**.
- **Papéis dos nós:** **Líder** (central na comunidade), **Seguidor** (ligado ao líder), **Marginal**, **Outlier** (poucas conexões), **Bridge/ponte** (conecta comunidades).
- **Aplicações (marketing/telecom):** segmentação; **retenção de líderes** (reduz churn); **cross-sell/up-sell em líderes (efeito viral)**; incluir a métrica de rede no **modelo de churn**.

## 2. Processo de SNA
1) obter acesso ao contexto → 2) extrair dados e definir **links (A→B) e forças** → 3) montar a base → 4) **detectar comunidades** → 5) **estipular papéis** → aplicar. **SNA propriamente dito = passos 4 e 5.**

## 3. Métricas de centralidade (muito cobradas)
- **Degree (grau):** nº de links do nó. Em redes direcionadas: **out-degree** (saem), **in-degree** (chegam); **degree = in + out**. *Degree ponderado* soma os pesos.
- **Clustering Coefficient (CC):** **CC = ligações existentes entre os vizinhos ÷ ligações possíveis entre eles.** Mede o quanto os **vizinhos** do nó se conhecem entre si. **CC alto** (perto de 1) = os vizinhos já se conectam sem o nó (ele é "dispensável"). **CC perto de 0** = os vizinhos só se ligam **através dele** → ele é **importante para a rede dele**.
- **Closeness (proximidade):** **média dos caminhos mais curtos** do nó até todos os outros. **Menor média = mais central** = difunde uma informação mais rápido.
- **Betweenness (intermediação):** nº de vezes que o nó aparece nos **menores caminhos entre outros pares**. Alto = **"porteiro"/ponte** da informação.

**Exemplo resolvido (CC).** O nó A tem 4 vizinhos (B, C, D, E). Pares possíveis entre eles = 4·3/2 = **6**. Existem só 2 ligações entre os vizinhos (B–C e D–E). **CC = 2/6 = 0,33** → seus vizinhos pouco se conectam sem A; ele é uma peça importante da vizinhança.
**Exemplo (in/out).** A liga 5 vezes para B e B liga 1 para A: out-degree de A = 5 (ou 1 link com peso 5), in-degree de A = 1.

### Estatísticas gerais da rede
- **Densidade** = links existentes ÷ links possíveis. **Comprimento médio do caminho**; **excentricidade** (distância ao nó mais distante); **raio** (menor excentricidade); **diâmetro** (maior).

## 4. Detecção de comunidades
- **Modularidade (Q):** fração dos links **dentro** das comunidades **menos** a fração esperada se os links fossem aleatórios — mede a **qualidade da divisão** (algoritmo tipo Louvain: cada nó começa sozinho e se funde quando a modularidade melhora).
- **Resolution (resolução):** **menor valor → mais comunidades e menores; maior (> 1) → menos comunidades e maiores.** Escolha por tentativa e erro conforme o negócio.
- Algoritmos (igraph): edge betweenness, fast greedy, walktrap, label propagation, multilevel, **info map (grafos direcionados)**.
- Tamanhos de comunidade tendem à **lei de potência** (poucas grandes, muitas pequenas).

## 5. Ferramentas
- **Gephi:** visualização e análise. CSV de links precisa das colunas **`Source` e `Target`** (e `weight` numérico opcional).
- **Python/igraph:** base **Karate Club** (34 nós, 78 ligações) como exemplo clássico.

## Armadilhas e confusões comuns
| Confusão | O correto |
|---|---|
| SNA = análise de redes sociais | SNA = análise de **relações entre entidades** |
| CC alto = nó importante | CC alto = vizinhos já ligados (nó **dispensável**); **CC baixo** = nó importante para a vizinhança |
| Degree alto = intermediação alta | são métricas diferentes (grau local × posição nos caminhos) |
| Closeness alto = muita média de passos | **menor** média de passos = mais central |
| Aumentar resolution gera mais comunidades | gera **menos e maiores** |
| Modularidade alta resolve tudo | o melhor Q nem sempre atende o negócio |

## Resumo-relâmpago
- Degree = nº de links; CC = ligações entre vizinhos ÷ possíveis; closeness = menor média de caminhos; betweenness = presença nos menores caminhos.
- Comunidades: modularidade mede qualidade; resolution maior = comunidades maiores e menos numerosas.
- Aplicação: reter líderes reduz churn.

## Teste-se
1. Um nó tem 3 vizinhos e há 1 ligação entre eles. Qual o CC?
<details markdown="1"><summary>Ver resposta</summary>Pares possíveis = 3; existem 1 → CC = 1/3 ≈ 0,33.</details>

2. O que significa betweenness alta?
<details markdown="1"><summary>Ver resposta</summary>O nó aparece em muitos dos menores caminhos entre outros pares: é ponte/porteiro da informação.</details>

3. O que acontece ao aumentar a resolution na detecção de comunidades?
<details markdown="1"><summary>Ver resposta</summary>Há menos comunidades, e maiores.</details>

4. Por que SNA não é análise de mídia social?
<details markdown="1"><summary>Ver resposta</summary>Porque analisa relacionamentos entre quaisquer entidades (ligações, e-mails, transações), não só redes sociais online.</details>

## Pergunta típica
Calcular o CC de um nó em um grafo pequeno · diferença entre in-degree e out-degree · o que significa closeness ou betweenness alto · o que muda quando a resolution aumenta · por que SNA não é mídia social · qual aplicação de SNA reduz churn · papéis (líder, seguidor, bridge, outlier)
