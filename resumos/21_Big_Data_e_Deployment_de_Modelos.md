# 21 · Big Data e Deployment de Modelos (MLOps)
**Prof. Helder Prado Santos · 2 aulas · Prioridade: MÉDIA (você, como dev, já conhece APIs/versionamento; foque nos termos de ML)**

## 1. Ciclo de vida de modelos e deployment
- **Modelo em desenvolvimento × em produção.** Na modelagem há input (dados preparados) e output; em produção chegam **dados novos o tempo todo** e a acurácia medida no treino **pode não se manter**.
- **Ciclo de vida:** **1) coleta e preparação de dados → 2) treinamento e validação → 3) deploy em produção → 4) monitoramento contínuo → 5) atualização e re-treinamento → 6) aposentadoria de modelos desatualizados** (ex.: regra de negócio mudou ou eficiência caiu).
- **Desafios do deployment:** **data drift** (mudança na distribuição dos dados/da variável alvo afeta a performance; a distribuição de Y mudou), **diferença entre ambiente de desenvolvimento e produção**, **monitoramento de performance pós-deploy**, **gerenciamento de múltiplas versões**, e adoção correta de **MLOps**.
- **Equipe (workflow):** cientistas de dados (treinam), engenheiros (colocam em produção), negócio. Um mesmo modelo pode ter 30 versões; é preciso promover versões sem "derrubar e subir" (o usuário usa o modelo hoje e, depois, o novo automaticamente).

## 2. MLOps e MLflow
- **MLOps = práticas de DevOps + Machine Learning**: automatiza o ciclo completo (treinamento, validação, deploy, monitoramento) com **eficiência, reprodutibilidade e rastreabilidade** dos experimentos, e facilita a colaboração entre cientistas de dados e engenheiros.
- **Frameworks:** **MLflow**, Kubeflow, Weights & Biases, Neptune.ai, Seldon, Polyaxon.
- **MLflow — 4 componentes principais:**
  - **MLflow Tracking:** gerencia **experimentos**, rastreando **parâmetros, métricas e artefatos** (`autolog` registra parâmetros de entrada e saída automaticamente; salva gráficos, summary do modelo, tempo de `fit` e `predict`);
  - **MLflow Projects:** padroniza o código para reprodutibilidade;
  - **MLflow Models:** **formato unificado** para salvar e implantar modelos (modelo + **metadados, dependências** — pacotes e versão da linguagem — e **assinatura/signature** = esquema do input/output, exemplos de requisição); `log_model` registra o modelo e sua assinatura;
  - **MLflow Model Registry:** **controle de versões** e estágios (ex.: promover a versão 3 para produção e arquivar a 2).
- **Benefícios:** rastreabilidade e controle de versões automatizados, integração com vários frameworks/linguagens, simplifica deploy/monitoramento, facilita re-treinamento e atualização contínua.
- **Servindo o modelo:** via **API REST** (o usuário se comunica com uma URL; a **API cria uma barreira entre as regras de negócio e o usuário**); MLflow serve o modelo como endpoint.

## 3. Big Data
- **Definição:** conjuntos de dados **extremamente grandes e complexos** que **não podem ser facilmente processados ou gerenciados com ferramentas tradicionais**. Escala: **1 ZB = 1.024 EB**; 1 EB = 1.073.741.824 GB (padrão binário). O boom de **IA generativa/LLMs** e de **dados sintéticos** acelera o crescimento; o custo de armazenamento em nuvem (S3, Blob, GCS) tornou viável guardar históricos grandes.
- **Os 5 Vs:** **Volume** (quantidade), **Velocidade** (rapidez com que são gerados/processados/disponibilizados), **Variedade** (estruturados, semi e não estruturados), **Veracidade** (confiabilidade/qualidade) e **Valor** (insights úteis). Na prática, os frameworks entregam **volume, velocidade e variedade**.
- **Cluster:** vários computadores em rede; o software precisa ser feito para rodar em **ambiente distribuído**.

### Hadoop MapReduce
- **HDFS** (armazenamento distribuído em clusters) + **MapReduce** (modelo de programação para **processamento paralelo** dividindo tarefas entre nós). **Escalável horizontalmente** (adiciona servidores). Processa **em disco**.

### Apache Spark
- **Processamento in-memory** (não grava em disco entre as etapas → muito mais rápido que o MapReduce).
- **DAG (grafo acíclico dirigido)** das operações: **direcionado** (arestas têm direção), **acíclico** (sem ciclos); permite otimização, dividir em **estágios** e paralelismo.
- **RDD (Resilient Distributed Dataset):** coleção **distribuída**, **resiliente** (recupera de falhas recomputando a partir da origem) e **imutável** (transformações geram novos RDDs). **Transformações** (map, filter) são **lazy** (só executam quando uma **ação** é chamada) × **ações** (count, collect) retornam valor ao driver.
- **DataFrames e Spark SQL** (colunas/linhas; `select/filter/groupBy`; **Catalyst Optimizer**); **MLlib** (ML distribuído); **Spark Streaming** (tempo real); formatos: parquet, avro, orc, json, csv. Clusters: **standalone (1 nó), Hadoop YARN, Kubernetes**; no **Databricks** o cluster é gerenciado (plug and play).
- Estratégias com muito dado: **amostragem** para exploração inicial; **ferramenta distribuída** quando o pandas não cabe em memória.

### Arquiteturas e otimização
- **Data Warehouse → Data Lake → Data Lakehouse** (jornada de arquiteturas). **Arquitetura Medalhão (bronze → silver → gold):** camada **bruta**, dados **limpos**, dados **agregados/prontos**.
- **Compressão** (CSV → **Parquet**: até **87%** de redução, ~34× mais rápido para carregar, até 99% de redução de custos de consulta).
- **Particionamento dos dados** (ex.: por ano/mês) — "quebra" o problema da variável tempo para acessar dados mais rápido; cuidado com particionar por uma chave que não combine com as consultas.

## Pergunta típica
Etapas do ciclo de vida de um modelo · o que é data drift · o que é MLOps · componentes do MLflow (Tracking, Projects, Models, Registry) · o que é a assinatura de um modelo · Hadoop × Spark (disco × memória) · RDD (resiliente, distribuído, imutável) e DAG · transformação (lazy) × ação · os 5 Vs · arquitetura medalhão · por que Parquet/particionamento.
