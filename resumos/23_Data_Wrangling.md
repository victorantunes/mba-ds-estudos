# 23 · Data Wrangling (pandas) — Tratamento e Preparação de Dados
**Prof. Wilson Tarantin Jr. · 4 aulas · Prioridade: MÉDIA (para você é prática de pandas; fixe os conceitos e o vocabulário)**

> **Em uma frase:** data wrangling é **transformar dados brutos em uma estrutura adequada à análise** — importar, juntar, limpar, criar variáveis e resumir — antes de qualquer gráfico ou modelo.

**Pré-requisitos:** Python/pandas básico (02). **Vem depois:** todos os modelos (14–20, 27–28).

## Por que isso importa (intuição)
**Modelo é tão bom quanto os dados.** Uma coluna com datas como texto, duplicados ou faltantes mal tratados produzem conclusões erradas sem nenhum erro de execução. Wrangling é o trabalho de "arrumar a casa" que ocupa a maior parte do tempo de um projeto de dados.

## 1. O que é data wrangling
- Preparar, organizar e manipular a base **antes da análise exploratória, dos gráficos e da modelagem**; **não é padronizado**: depende do contexto.
- **Etapas comuns:** (1) **coleta/importação** (CSV, XLSX, Parquet, APIs, bancos via SQL; cuidado com **encoding**, ex. `latin1`); (2) **junção** (precisa de uma **variável-chave** com o mesmo nome nas duas tabelas); (3) **transformação**: **limpeza** (faltantes, erros, duplicados), **criação/alteração de variáveis**, **seleção de observações**, **agregações**.
- **Fases (Harvard):** descoberta, estruturação, limpeza, enriquecimento, validação, publicação.

## 2. CRISP-DM
**Cross-Industry Standard Process for Data Mining**, **iterativo:** 1) **Business Understanding** (objetivo do negócio) → 2) **Data Understanding** (coleta e exploração; o wrangling começa aqui) → 3) **Data Preparation** (limpeza, seleção, criação, integração — o grosso) → 4) **Modeling** → 5) **Evaluation** (volta ao negócio se não resolve) → 6) **Deployment**.

## 3. pandas — operações-chave
- **Ler e conhecer:** `pd.read_csv/read_excel`, `.info()` (tipos e nulos), `.describe()`, `.head()`, `.unique()`, `.nunique()`, `.value_counts()`.
- **Tipos:** `.astype()`; `category`; `pd.to_datetime`.
- **Selecionar:** `.loc` (rótulos), `.iloc` (posição, **começa em 0**), **`.query('x > 5 and y == "a"')`**, `.isin()`, `.between()`.
- **Limpar:** `.rename()`, `.drop()`, `.drop_duplicates()`, `.dropna()`, `.fillna()`.
- **Criar variáveis:** `.assign()`, **`np.where(cond, a, b)`**, `pd.qcut` (faixas por quantis), `.cumsum()`, `.shift()`.
- **Resumir:** **`.groupby(var).agg(...)`**, `.sort_values()`, `.reset_index()`, `pd.crosstab` (tabela de contingência → qui-quadrado).
- **Reestruturar:** **`.melt()`** (largo → **longo**) e **`.pivot()`** (longo → largo). **Wide** = variáveis em colunas; **long** = empilhadas em linhas.
- **Combinar:** `.concat()` e **`.merge(how=…)`**.

### Tipos de merge
- **`left`:** todas as linhas da esquerda + correspondentes da direita. **`right`:** todas da direita. **`inner`:** só as que aparecem **nas duas**. **`outer`:** **todas**.

**Exemplo resolvido.** Clientes: {1, 2, 3}; Compras: {2, 3, 4}. `inner` → {2, 3}; `left` (clientes à esquerda) → {1, 2, 3} (cliente 1 com compra = NaN); `right` → {2, 3, 4}; `outer` → {1, 2, 3, 4}.
**Exemplo (melt).** Tabela larga com colunas `ano_2022`, `ano_2023` → `.melt()` gera colunas `ano` e `valor`, uma linha por país e ano (formato longo, útil para gráficos e `groupby`).

## 4. Boas práticas e armadilhas
- **Salve o resultado do `groupby` em outro objeto**; confira **tipos** após importar; **não calcule média de variável categórica**; use `.copy()` para cópias.
- Grupos com **poucas observações** distorcem médias.
- Em **Big Data** troca-se a biblioteca (Spark/Dask), mas o ciclo é o mesmo.
- **Git × GitHub:** Git = **controle de versão** (histórico, commits); GitHub = **plataforma** para hospedar e colaborar em repositórios.

## Armadilhas e confusões comuns
| Confusão | O correto |
|---|---|
| `inner` mantém todas as linhas | só as que existem **nas duas** tabelas |
| `left` mantém as da tabela da direita | mantém **todas as da esquerda** |
| `iloc` usa rótulos | usa **posição** (começa em 0); `loc` usa rótulos |
| Wide e long são o mesmo | wide: variáveis em colunas; long: empilhadas |
| `merge` não precisa de chave | precisa de **variável-chave** em comum |
| Wrangling vem depois da modelagem | vem **antes** (CRISP-DM: preparação) |
| Git = GitHub | Git é a **ferramenta de versão**; GitHub é a **plataforma** |

## Resumo-relâmpago
- Wrangling = preparar dados antes de explorar/modelar. CRISP-DM: 6 fases, iterativo.
- merge: left, right, inner, outer. melt (wide → long), pivot (long → wide).
- groupby/agg para resumir; np.where e qcut para criar variáveis; Git ≠ GitHub.

## Teste-se
1. Em que fase do CRISP-DM acontece o grosso do wrangling?
<details markdown="1"><summary>Ver resposta</summary>Data Preparation (começa em Data Understanding).</details>

2. Qual a diferença entre `inner` e `outer` merge?
<details markdown="1"><summary>Ver resposta</summary>Inner mantém só as chaves presentes nas duas tabelas; outer mantém todas as chaves das duas.</details>

3. O que faz `.melt()`?
<details markdown="1"><summary>Ver resposta</summary>Converte o formato largo em longo: variáveis em colunas viram linhas.</details>

4. Por que não calcular média de uma variável categórica?
<details markdown="1"><summary>Ver resposta</summary>Porque os números são rótulos de categoria (ponderação arbitrária); só frequências e moda fazem sentido.</details>

## Pergunta típica
O que é data wrangling e quando ocorre · etapas do CRISP-DM (e onde entra o wrangling) · diferença entre left/right/inner/outer · wide × long (melt e pivot) · para que serve groupby · como o `.query` funciona · como tratar variável categórica no pandas · Git × GitHub
