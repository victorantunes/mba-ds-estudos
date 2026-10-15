# 02 · Introdução à Programação com Python + Mapa do Machine Learning
**Prof. Wilson Tarantin Jr. · 3 aulas · Prioridade: BAIXA para o Python em si (você já domina); ALTA para o "mapa" de ML abaixo.**

> A parte de código é só pandas/numpy/matplotlib/seaborn no Spyder. A parte que importa para avaliação é **o mapa conceitual** que o professor apresenta na aula 1: ele organiza todo o curso.

## 1. Conceitos de base
- **Machine learning** = usar dados + algoritmos (que contêm métodos estatísticos) para produzir informação útil à tomada de decisão: analisar a interdependência entre dados e/ou criar modelos preditivos. Envolve coletar, tratar dados brutos e escolher a técnica adequada.
- **Banco de dados** = **observações** (linhas: unidades analisadas, ex. pessoa, país, empresa) × **variáveis** (colunas: atributos). Muitas vezes é uma **amostra** (subconjunto da população).
- Variáveis **métricas** (quantitativas) × **não métricas** (qualitativas/categóricas).
  - Qualitativas: **dicotômica** (2 categorias, binária) × **policotômica** (>2); **nominal** (sem ordem) × **ordinal** (com ordem).
  - Quantitativas: **discretas** (contagem, 0,1,2…) × **contínuas** (números reais).
- **O tipo de variável determina o modelo e a distribuição de probabilidade adequados.**

## 2. O mapa: supervisionado × não supervisionado (CAI MUITO)
| | **Não supervisionados** | **Supervisionados** |
|---|---|---|
| Também chamados | exploratórios, **técnicas de interdependência** | confirmatórios, **técnicas de dependência** |
| Objetivo | estudar relação entre variáveis **sem** intenção de criar modelo preditivo; **não há inferência** para observações fora da amostra | estimar uma equação **Y = f(X1, X2, …, Xk)** para **previsão**; **há inferência** para fora da amostra |
| Tarefas | redução de dados, **agrupamento** de observações, correlação/associação entre variáveis | prever/explicar uma variável dependente Y |

**Qual técnica? Depende do tipo de variável:**
- **Não supervisionados com variáveis quantitativas:** **Clustering** (K-Means, hierárquico) para agrupar observações; **PCA / análise fatorial** para reduzir variáveis.
- **Não supervisionados com variáveis qualitativas:** **ANACOR** (correspondência simples, 2 variáveis) e **MCA** (múltipla, 3+ variáveis). (Base: teste qui-quadrado da aula de estatística.)
- **Supervisionados, Y quantitativo (métrico):** **regressões lineares e não lineares**; Y de **contagem** (discreto, ≥0): **modelos para dados de contagem** (Poisson, binomial negativo) e **zero-inflated** (excesso de zeros); dados aninhados: **multinível/hierárquicos (GLMM)**.
- **Supervisionados, Y qualitativo:** **regressão logística binária** (Y com 2 categorias) e **multinomial** (Y com >2 categorias).
- **Famílias que servem para vários casos:** **árvores (CART)**, **bagging e random forest**, **boosting**, **SVM**, **redes neurais**.

## 3. Python no curso (só o essencial para lembrar)
- IDE **Spyder**, via **Anaconda**; trabalha-se com **projects** (abrir a pasta do projeto). Pacotes: **pandas** (dados), **numpy** (matemática), **matplotlib/seaborn** (gráficos), **plotly** (interativo).
- Tudo que aparece no console não é erro; se nada apareceu, **executou**.
- **DataFrame** = estrutura padrão para bancos de dados. Variável categórica: `dtype="category"`.
- Funções que apareceram: `info()`, `describe()` (para variáveis métricas; 50% = mediana), `iloc[linhas, colunas]` (índice começa em 0), filtros booleanos combinados, `groupby`, `sort_values(by=…)`, `reset_index()`.
- Gráficos: **histograma** (distribuição de frequências de variável métrica), **boxplot** (mín, Q1, mediana, Q3, máx e outliers pela regra 1,5·AIQ; "lower fence" = limite inferior).
- Função definida pelo usuário (`def`) com condições no corpo — os professores usam isso nos scripts de ML.

## Pergunta típica
- "Quais são as diferenças entre modelo supervisionado e não supervisionado?" → dependência × interdependência; com × sem Y; com × sem inferência/previsão fora da amostra.
- "Para qual tipo de variável serve ANACOR/MCA?" → qualitativas. PCA/clustering → quantitativas.
