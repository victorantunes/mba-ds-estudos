# 02 · Programação em Python + Mapa do Machine Learning
**Prof. Wilson Tarantin Jr. · 3 aulas · Prioridade: baixa para o Python em si (você já domina); alta para o "mapa" de ML, que organiza o curso inteiro**

## O fio condutor deste capítulo

Este capítulo tem duas partes de pesos muito diferentes. Python, aqui, é só a ferramenta: pandas para tabelas, numpy para contas, gráficos para olhar os dados. Como você já programa, basta lembrar o essencial. O que realmente importa para o resto do curso é o **mapa**: uma forma de responder, diante de qualquer problema com dados, *"que família de técnica devo usar?"*. Quase todas as disciplinas seguintes são uma "casinha" desse mapa, e ele evita que você as veja como assuntos soltos.

> **Memorize.** Duas perguntas resolvem a escolha da técnica: **(1)** existe uma variável que quero prever (Y)? **(2)** de que tipo são as variáveis? O resto do curso é detalhar as respostas.

## 1. O que é Machine Learning e como é o dado

Chamamos de **machine learning** o uso de dados e algoritmos (que contêm métodos estatísticos) para produzir informação útil na tomada de decisão. Há duas finalidades: entender como os dados se relacionam entre si e construir modelos que **prevejam** algo.

O dado chega como uma tabela. Cada **linha** é uma *observação* (um cliente, um país, uma empresa) e cada **coluna** é uma *variável* (um atributo). Quase sempre a tabela é uma **amostra**, isto é, uma parte da população. Isso importa porque só alguns modelos permitem tirar conclusões para além da amostra.

As colunas são de dois tipos, e a tabela abaixo organiza os nomes que o curso usa:

| Tipo | Subtipos | Exemplos |
|---|---|---|
| **Métrica** (quantitativa) | **discreta** (contagem: 0, 1, 2…) · **contínua** (qualquer valor real) | nº de filhos · renda em R$ |
| **Não métrica** (qualitativa) | **dicotômica** (2 categorias) · **policotômica** (mais de 2) · **nominal** (sem ordem) · **ordinal** (com ordem) | sim/não · cor · baixo/médio/alto |

> **Regra de ouro.** O **tipo da variável determina o modelo e a distribuição de probabilidade** adequados. Quase todo erro de modelagem começa em ignorar isso.

## 2. A primeira bifurcação: existe uma resposta a prever?

Diante de um problema, a primeira pergunta é: *eu tenho uma variável que quero prever ou explicar?* Se sim, há um "gabarito" (Y) e o problema é **supervisionado**. Se não, você só quer explorar a estrutura dos dados e o problema é **não supervisionado**.

| | **Supervisionado** | **Não supervisionado** |
|---|---|---|
| Também chamado | técnicas de **dependência**, confirmatório | técnicas de **interdependência**, exploratório |
| Existe Y? | **sim** | **não** |
| O que se estima | uma equação \(Y = f(X_1, X_2, \ldots, X_k)\) | agrupamentos, fatores, associações |
| Inferência para fora da amostra | **sim** (previsão) | **não**; se entram novas observações, refaz-se |
| Tarefas | prever ou explicar Y | reduzir variáveis, agrupar observações, associar categorias |

## 3. A segunda bifurcação: de que tipo são as variáveis?

Dentro de cada ramo a escolha da técnica segue o tipo de variável, e é por isso que o curso parece tão longo: cada tipo pede um modelo.

```mermaid
flowchart TD
  P["Problema com dados"] --> Q{"Há Y para prever?"}
  Q -->|"Não"| N["Não supervisionado"]
  Q -->|"Sim"| S["Supervisionado"]
  N --> N1["Variáveis quantitativas"]
  N --> N2["Variáveis qualitativas"]
  N1 --> C1["Clustering: agrupa observações"]
  N1 --> C2["PCA/fatorial: agrupa variáveis"]
  N2 --> C3["ANACOR (2 variáveis) ou ACM (3 ou mais)"]
  S --> Y{"Tipo de Y"}
  Y --> Y1["Contínuo: regressão linear"]
  Y --> Y2["Contagem: Poisson, binomial negativa, inflacionados"]
  Y --> Y3["Categórico: logística binária ou multinomial"]
  Y --> Y4["Dados aninhados: multinível"]
```

Além dessas técnicas, há famílias flexíveis que servem a vários casos: **árvores, random forest, boosting, SVM e redes neurais**.

### Exemplo completo: o mapa de ML aplicado aos problemas reais do curso

Cada capítulo seguinte resolve um problema real da aula. Usando as duas perguntas ("há um Y a prever?" e "de que tipo é o Y ou são as variáveis?"), o mapa leva à técnica certa:

| Problema da aula | Há Y? | Tipo de Y / variáveis | Técnica | Capítulo |
|---|---|---|---|---|
| Agrupar **5 candidatos do vestibular** e **660 clientes de cartão** em perfis | não | variáveis quantitativas (linhas = observações) | **Cluster** | 14 |
| Resumir 9 indicadores dos **distritos de São Paulo** em um indicador socioeconômico | não | variáveis quantitativas (colunas) | **PCA** | 15 |
| Associar **perfil de investidor × tipo de aplicação** | não | variáveis **categóricas** | **ANACOR / ACM** | 16 |
| Prever o **tempo de viagem** pela distância; a **percepção de corrupção** pelo país | **sim** | contínuo | **Regressão linear (OLS)** | 17 |
| Prever se o estudante **chega atrasado** (sim/não) | **sim** | binário | **Logística binária** | 18 |
| Prever em qual aula o estudante **se atrasa** (nenhuma, 1ª, 2ª) | **sim** | categórico com 3 níveis | **Logística multinomial** | 18 |
| Prever o **número de multas** de estacionamento | **sim** | **contagem** (0, 1, 2…, muitos zeros) | **Poisson / binomial negativa / ZINB** | 19 |
| Prever o **desempenho** de estudantes **dentro de escolas** | **sim** | contínuo, com dados **aninhados** | **Multinível (HLM)** | 20 |
| Prever **doença cardíaca** e **churn** de clientes | **sim** | categórico, muitas variáveis e interações | **Árvores / Random Forest** | 27 |

Repare como o **tipo do Y** manda: contínuo → OLS; binário → logística; contagem → Poisson e afins; categorias sem Y → correspondência; e, quando os dados têm **níveis** (estudantes em escolas), multinível.

## 4. Python no curso, só o que vale lembrar

O ambiente é o Spyder, via Anaconda. A estrutura central é o **DataFrame** do pandas.

| Para quê | Função |
|---|---|
| ver tipos e nulos | `info()` |
| estatísticas descritivas (o "50%" é a mediana) | `describe()` |
| selecionar por posição (índice começa em 0) | `iloc[linhas, colunas]` |
| agregar e ordenar | `groupby`, `sort_values`, `reset_index` |
| olhar a distribuição de uma métrica | histograma |
| mínimo, quartis, mediana, máximo e outliers | boxplot (outlier pela regra de 1,5 × AIQ) |

### Exemplo completo (da aula): as notas do PISA com o pandas

A aula usa a base de **notas do PISA** (Programa Internacional de Avaliação de Alunos): **96 países** (38 da OCDE e 58 parceiros) e 8 colunas: `country`, `group`, e as notas de matemática, leitura e ciências em **2022** e em **2018**. Veja as operações, na ordem em que aparecem na aula:

| Operação | O que faz neste exemplo | Resultado |
|---|---|---|
| `pisa.shape` | linhas e colunas | **(96, 8)** |
| `pisa.info()` | tipos e nulos | cada nota de 2022 tem **15 valores ausentes** (o arquivo traz "—") |
| `pisa.iloc[46, 2]` | linha 46, coluna 2 (a contagem começa em **0**) | nota de **matemática 2022 do Brasil: 378,7** |
| `pisa.iloc[19, ]` | a linha 19 inteira | o **Japão**: OCDE, matemática 2022 = **535,6** |
| `pisa.iloc[:, [0, 2, 5]]` | só as colunas país, matemática 2022 e 2018 | uma tabela de 3 colunas |
| `pisa.drop(columns=[...])` | remove as colunas de 2018 | base só com 2022 |
| `describe()` | estatísticas das 81 notas disponíveis | média de matemática **437,6**, mediana **440,8**, mínimo 336,4 e máximo 574,7 |
| `pisa.groupby('group')` | resumo por grupo | OCDE: média **472,4** (37 países); parceiros: média **408,4** (44 países) |
| `sort_values('mathematics_2022', ascending=False)` | ranking | 1º **Singapura (575)**, 2º Macau (552), 3º Taipé (547); último, Camboja (336) |

**Como ler.** O "**50%**" do `describe()` é a **mediana** (440,8). O **Brasil (378,7)** está **abaixo da média dos 81 países (437,6)**: 64 dos 81 países têm nota maior. E o `groupby` mostra a diferença entre os grupos (472 contra 408), que o `describe()` geral esconde. **Cuidado com o erro clássico de índice:** `iloc[46, 2]` é a **47ª linha** (começa em zero) e a **3ª coluna**.

## O que levar daqui

Todo problema começa com duas perguntas: *há um Y a prever?* (supervisionado × não supervisionado) e *de que tipo são as variáveis?* (define a técnica). Com Y contínuo, regressão; com contagem, Poisson e afins; com categorias, logística; com dados aninhados, multinível. Sem Y, clustering e PCA para variáveis métricas, correspondência para categóricas.

## Erros que todo mundo comete

| Erro | Correção |
|---|---|
| Achar que clustering é supervisionado | não há Y; é exploratório |
| Usar PCA com variáveis categóricas | PCA exige **métricas**; categóricas → ANACOR/ACM |
| Esperar que técnicas não supervisionadas prevejam novas observações | não há inferência fora da amostra |
| Usar regressão linear para uma contagem | contagem pede Poisson/binomial negativa |

## Teste-se

1. Qual a diferença entre modelo supervisionado e não supervisionado?
<details markdown="1"><summary>Ver resposta</summary>O supervisionado tem uma variável dependente Y, estima uma equação e permite previsão e inferência fora da amostra (dependência). O não supervisionado não tem Y e só explora relações dentro da amostra (interdependência).</details>

2. Que técnica usar para associar três variáveis categóricas?
<details markdown="1"><summary>Ver resposta</summary>ACM (análise de correspondência múltipla). A ANACOR serve para duas variáveis.</details>

3. Y = número de acidentes por dia. Qual família de modelos?
<details markdown="1"><summary>Ver resposta</summary>Modelos de contagem: Poisson (média ≈ variância) ou binomial negativa (variância maior que a média).</details>

## Pergunta típica
Quais as diferenças entre modelo supervisionado e não supervisionado · para qual tipo de variável serve ANACOR/ACM e para qual PCA/clustering · como escolher o modelo conforme o tipo de Y
