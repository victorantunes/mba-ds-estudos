# 21 · Big Data e Deployment de Modelos (MLOps)
**Prof. Helder Prado Santos · 2 aulas · Prioridade: MÉDIA (você, como dev, já conhece APIs e versionamento; foque nos termos de ML)**

> **Em uma frase:** um modelo só gera valor quando **vai para produção e continua funcionando**; MLOps é a disciplina que automatiza e monitora esse ciclo, e Big Data são as ferramentas para fazê-lo com volumes que não cabem em uma máquina.

**Pré-requisitos:** noção de modelos (17–20, 27), APIs (29) e cloud (07). **Vem depois:** 22 (séries) usa previsão em produção.

## Por que isso importa (intuição)
Treinar um bom modelo no notebook é metade do caminho. Na produção, **os dados mudam** (clientes novos, outro comportamento), o modelo envelhece e é preciso **versionar, monitorar e retreinar**. Pense em MLOps como **DevOps para modelos**: cada versão tem registro, métricas e um caminho seguro até a produção.

## 1. Ciclo de vida do modelo
1. coleta e preparação → 2. treinamento e validação → 3. **deploy** → 4. **monitoramento contínuo** → 5. atualização/retreinamento → 6. **aposentadoria** de modelos desatualizados.
- **Desafios:** **data drift** (a distribuição dos dados ou de Y muda e a performance cai), diferença entre **ambiente de desenvolvimento e produção**, monitoramento pós-deploy, **versionamento**.
- **Equipe:** cientistas de dados (treinam), engenheiros (colocam em produção), negócio. É preciso **promover versões** sem "derrubar e subir" o serviço.

**Exemplo (data drift).** Um modelo de crédito é treinado com clientes de 2022. Em 2025 a renda média e o perfil mudaram e a taxa de default subiu: a **acurácia medida no treino não se mantém**. O monitoramento detecta a queda e dispara o retreinamento.

## 2. MLOps e MLflow
- **MLOps = DevOps + Machine Learning:** automatiza treino, validação, deploy e monitoramento, com **reprodutibilidade e rastreabilidade**. Frameworks: **MLflow**, Kubeflow, Weights & Biases, Seldon.
- **MLflow — 4 componentes:**
  - **Tracking:** registra **experimentos** (parâmetros, métricas, artefatos); `autolog` faz isso automaticamente.
  - **Projects:** padroniza o código para reprodutibilidade.
  - **Models:** **formato unificado** do modelo, com **metadados, dependências e assinatura (signature)** = esquema de entrada e saída.
  - **Model Registry:** **versões e estágios** (ex.: promover a versão 3 para produção e arquivar a 2).
- **Servir o modelo:** por **API REST** (a API é uma barreira entre as regras de negócio e o usuário).

**Exemplo (fluxo).** Você treina 5 variações → o **Tracking** registra parâmetros e métricas de cada uma → a melhor vai para o **Registry** como versão 4 → promovida a **Production** → o **Model** é servido como endpoint REST com a **signature** validando a entrada.

## 3. Big Data
- **Big Data:** dados **grandes e complexos demais** para ferramentas tradicionais.
- **5 Vs:** **Volume, Velocidade, Variedade, Veracidade** (qualidade) e **Valor** (insights úteis). Na prática, os frameworks entregam volume, velocidade e variedade.
- **Cluster:** vários computadores em rede; o software precisa ser **distribuído**.

### Hadoop MapReduce
- **HDFS** (armazenamento distribuído) + **MapReduce** (processamento paralelo dividido entre nós). **Escala horizontal** e processa **em disco**.

### Apache Spark
- **Em memória** → muito mais rápido que o MapReduce.
- **DAG (grafo acíclico dirigido):** o plano das operações — direcionado e **sem ciclos**; permite otimizar e paralelizar.
- **RDD:** coleção **distribuída, resiliente (recupera por recomputação) e imutável**. **Transformações** (`map`, `filter`) são **lazy**; só executam quando uma **ação** (`count`, `collect`) é chamada.
- **DataFrames/Spark SQL** (otimizador **Catalyst**), **MLlib**, **Streaming**. Clusters: standalone, YARN, Kubernetes; no **Databricks** o cluster é gerenciado.
- Com muito dado: **amostre** para explorar; use ferramenta **distribuída** quando o pandas não cabe em memória.

**Exemplo (lazy).** `df.filter(preco > 100).select("id")` **não faz nada** ainda; só ao chamar `df.count()` o Spark monta o DAG e executa tudo de uma vez.

### Arquiteturas e otimização
- **Data Warehouse → Data Lake → Data Lakehouse.** **Medalhão:** **bronze** (bruto) → **silver** (limpo) → **gold** (agregado/pronto).
- **Parquet** (colunar, compactado): reduz muito o tamanho e acelera consultas. **Particionamento** (por ano/mês) acelera leituras; cuidado com chaves que não combinam com as consultas.

## Armadilhas e confusões comuns
| Confusão | O correto |
|---|---|
| Acurácia do treino vale para sempre | **data drift** a degrada; monitore |
| MLOps = só deploy | cobre **todo o ciclo** (treino, validação, deploy, monitoramento) |
| Spark e MapReduce processam do mesmo jeito | Spark: **memória**; MapReduce: **disco** |
| Transformação executa na hora | é **lazy**; só a **ação** dispara |
| RDD é mutável | é **imutável** |
| Big Data = só volume | são **5 Vs** (volume, velocidade, variedade, veracidade, valor) |
| MLflow Registry registra experimentos | experimentos → **Tracking**; versões → **Registry** |

## Resumo-relâmpago
- Ciclo: coleta → treino → deploy → monitoramento → retreino → aposentadoria. Drift derruba o modelo.
- MLflow: Tracking, Projects, Models (signature), Registry.
- 5 Vs. Spark em memória; RDD resiliente e imutável; lazy × ação; DAG.
- Medalhão bronze/silver/gold; Parquet e particionamento.

## Teste-se
1. O que é data drift?
<details markdown="1"><summary>Ver resposta</summary>Mudança na distribuição dos dados (ou de Y) em produção que reduz a performance do modelo.</details>

2. Cite os 4 componentes do MLflow.
<details markdown="1"><summary>Ver resposta</summary>Tracking, Projects, Models e Model Registry.</details>

3. Qual a diferença entre transformação e ação no Spark?
<details markdown="1"><summary>Ver resposta</summary>Transformação (map, filter) é lazy e só planeja; ação (count, collect) dispara a execução e retorna valor ao driver.</details>

4. O que são as camadas bronze, silver e gold?
<details markdown="1"><summary>Ver resposta</summary>Bronze: dados brutos; silver: dados limpos; gold: dados agregados e prontos para consumo.</details>

## Pergunta típica
Etapas do ciclo de vida de um modelo · o que é data drift · o que é MLOps · componentes do MLflow · o que é a assinatura de um modelo · Hadoop × Spark (disco × memória) · RDD (resiliente, distribuído, imutável) e DAG · transformação (lazy) × ação · os 5 Vs · arquitetura medalhão · por que Parquet e particionamento
