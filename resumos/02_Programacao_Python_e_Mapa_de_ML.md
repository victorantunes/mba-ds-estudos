# 02 · Programação em Python + Mapa do Machine Learning
**Prof. Wilson Tarantin Jr. · 3 aulas · Prioridade: BAIXA para o Python em si (você já domina); ALTA para o "mapa" de ML — ele organiza todo o curso**

> **Em uma frase:** antes de escolher uma técnica, responda duas perguntas — *existe uma variável a prever (Y)?* e *de que tipo são as variáveis?* — e o mapa abaixo indica a família de modelos.

**Pré-requisitos:** nenhum. **Vem depois:** as disciplinas 14–20 (cada uma é uma "caixa" deste mapa).

## Por que isso importa (intuição)
O curso tem dezenas de técnicas, mas elas se organizam em um **mapa de decisão**. Se você decorar o mapa, cada nova técnica vira "mais uma casinha" em vez de um assunto isolado. Python é só a ferramenta para executar.

## 1. Conceitos de base
- **Machine learning:** usar dados e algoritmos (que contêm métodos estatísticos) para gerar informação útil à decisão — entender como variáveis se relacionam e/ou construir modelos de previsão.
- **Banco de dados:** **observações** (linhas: pessoa, país, empresa) × **variáveis** (colunas: atributos). Quase sempre é uma **amostra** da população.
- **Variável métrica (quantitativa):** discreta (contagem: 0, 1, 2…) ou contínua (números reais). **Não métrica (qualitativa):** dicotômica (2 categorias) ou policotômica (>2); nominal (sem ordem) ou ordinal (com ordem).
- **Regra de ouro:** o **tipo da variável determina o modelo e a distribuição de probabilidade** adequados.

## 2. O mapa: supervisionado × não supervisionado
**Ideia:** no **supervisionado** existe uma resposta Y que você quer prever/explicar a partir de X (há "professor" dando o gabarito). No **não supervisionado** não existe Y: você explora a estrutura dos dados.

| | **Não supervisionado** | **Supervisionado** |
|---|---|---|
| Também chamado | exploratório; técnicas de **interdependência** | confirmatório; técnicas de **dependência** |
| Objetivo | descobrir relações/agrupamentos, **sem** modelo preditivo | estimar **Y = f(X1, …, Xk)** para prever |
| Inferência fora da amostra? | **Não** | **Sim** |
| Tarefas | reduzir dados, agrupar observações, associar categorias | prever ou explicar Y |

### Qual técnica? (depende do tipo de variável)
**Não supervisionado:**
- Variáveis **quantitativas** → **Clustering** (agrupa observações: K-Means, hierárquico) e **PCA/análise fatorial** (reduz variáveis).
- Variáveis **qualitativas** → **ANACOR** (2 variáveis) e **ACM/MCA** (3 ou mais). Base: teste qui-quadrado.

**Supervisionado (olhe o tipo de Y):**
- Y quantitativo contínuo → **regressão linear/não linear**.
- Y de **contagem** (inteiro ≥ 0) → **Poisson / Binomial negativo** (e *zero-inflated* se há excesso de zeros).
- Y com 2 categorias → **logística binária**; com mais de 2 → **logística multinomial**.
- Dados **aninhados** (alunos dentro de escolas) → **multinível/hierárquico**.
- Famílias genéricas que servem a vários casos: **árvores, bagging/random forest, boosting, SVM, redes neurais**.

**Exemplo de uso do mapa.** "Quero prever se o cliente vai cancelar (sim/não) com base em idade e renda." Há Y (cancelar) → supervisionado; Y tem 2 categorias → **logística binária** (ou uma árvore).
"Quero agrupar clientes em perfis, sem rótulo prévio" → não supervisionado, variáveis quantitativas → **clustering**.

## 3. Python no curso (só o que vale lembrar)
- Ambiente **Spyder via Anaconda**; bibliotecas: **pandas** (dados), **numpy** (matemática), **matplotlib/seaborn/plotly** (gráficos).
- **DataFrame** é a estrutura padrão. Funções vistas: `info()`, `describe()` (50% = mediana), `iloc[linhas, colunas]` (índice começa em 0), filtros booleanos, `groupby`, `sort_values`, `reset_index`.
- **Histograma:** distribuição de uma variável métrica. **Boxplot:** mín, Q1, mediana, Q3, máx e outliers (regra 1,5·AIQ).

## Armadilhas e confusões comuns
| Confusão | O correto |
|---|---|
| Clustering é supervisionado | **Não**: não há Y; é exploratório |
| PCA serve para variáveis categóricas | PCA/fatorial = **quantitativas**; categóricas → ANACOR/ACM |
| Técnica não supervisionada "prevê" fora da amostra | **não há inferência** para observações fora da amostra |
| Qualquer Y numérico usa regressão linear | Y de **contagem** pede Poisson/Binomial negativa |
| Árvore/Random Forest só serve a um tipo de Y | servem a **vários** casos (classificação e regressão) |

## Resumo-relâmpago
- Supervisionado = dependência (há Y, há previsão); não supervisionado = interdependência (sem Y).
- Quantitativas → clustering e PCA; qualitativas → ANACOR/ACM.
- Y contínuo → regressão; contagem → Poisson/BN; binário → logística; aninhado → multinível.

## Teste-se
1. Qual a diferença entre modelo supervisionado e não supervisionado?
<details markdown="1"><summary>Ver resposta</summary>Supervisionado tem variável dependente Y, estima uma equação e permite inferência/previsão fora da amostra (dependência). Não supervisionado não tem Y e só explora relações dentro da amostra (interdependência).</details>

2. Que técnica usar para associar 3 variáveis categóricas?
<details markdown="1"><summary>Ver resposta</summary>ACM (análise de correspondência múltipla); a simples (ANACOR) é para 2 variáveis.</details>

3. Y = número de acidentes por dia. Qual família de modelos?
<details markdown="1"><summary>Ver resposta</summary>Modelos de contagem: Poisson (média ≈ variância) ou Binomial negativa (superdispersão).</details>

## Pergunta típica
Quais as diferenças entre modelo supervisionado e não supervisionado · para qual tipo de variável serve ANACOR/ACM e para qual PCA/clustering · como escolher o modelo conforme o tipo de Y
