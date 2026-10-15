# 23 · Data Wrangling (pandas) — Tratamento e Preparação de Dados
**Prof. Wilson Tarantin Jr. · 4 aulas · Prioridade: MÉDIA (para você é prática de pandas; fixe os conceitos e o vocabulário)**

## 1. O que é Data Wrangling
- **Transformar a base de dados da estrutura original (dados brutos) para uma estrutura mais adequada** à extração de informações. É **preparação, organização e manipulação** dos bancos de dados; **ocorre antes da análise exploratória, da criação de gráficos e da modelagem**. **Quanto melhor, melhores os dados e a qualidade da análise** (modelos refletem a má qualidade dos dados). **Não é atividade padronizada** — depende do contexto.
- **Etapas comuns:**
  1. **Coleta e importação** (XLSX, CSV, Parquet, sites, **APIs**, ERPs/CRMs via **SQL**); atenção a **encoding** (ex.: `latin1`).
  2. **Junção** (combinar fontes) — exige **variável "chave"** com o **mesmo nome** nas duas tabelas.
  3. **Transformação**: **limpeza** (remover variáveis/observações irrelevantes, erros, faltantes, duplicados), **criação e alteração de variáveis**, **seleção de observações**, **agregações e resumos**.
- Vai-e-volta constante com a entendimento dos dados; já nessa etapa se calculam **estatísticas descritivas** para acompanhar a qualidade/consistência.

## 2. CRISP-DM (ciclo de vida do projeto de DS) — CAI
**Cross-Industry Standard Process for Data Mining.** Etapas: **1) Business Understanding** (entender o negócio, problema e objetivo; ex.: instituição financeira quer reduzir inadimplência) → **2) Data Understanding** (coletar e explorar dados; descoberta/qualidade — **data wrangling começa aqui**) → **3) Data Preparation** (limpeza, seleção, criação de variáveis, integração — **o grosso do wrangling**) → **4) Modeling** (modelos de ML/DL) → **5) Evaluation** (avaliar; volta ao negócio se não resolve) → **6) Deployment** (colocar em produção). É **iterativo** (setas de volta). Seleção de variáveis com critérios de modelagem pertence à **modelagem**.
- Fases de data wrangling (Harvard Business School): **descoberta** (se familiarizar com os dados), **estruturação**, **limpeza (cleaning)**, **enriquecimento**, **validação**, **publicação** (disponibilizar para modelagem).

## 3. pandas — operações-chave
| Tarefa | Função / conceito |
|---|---|
| Ler | `pd.read_csv`, `pd.read_excel` (parâmetro `encoding`) |
| Conhecer | `.info()` (tipos e nulos), `.describe()` (estatísticas das métricas), `.head()/.tail()`, `.unique()` (categorias únicas), `.nunique()`, `.value_counts()` (tabela de frequências) |
| Tipos | `.astype(...)` — variável **categórica** (`category`) × texto (`object`); `pd.to_datetime` |
| Selecionar | `.loc` (rótulos), `.iloc` (posição; **índices começam em 0**), **`.query('x > 5 and y == "a"')`** (texto com aspas internas diferentes; menos repetição do nome do DataFrame), `.isin()`, `.between()`; referenciar colunas **pelo nome** (mais seguro que pela posição) |
| Renomear / remover | `.rename()`, `.drop()`, `.drop_duplicates()`, `.dropna()` (`how='all'`), `.fillna()` / `.isna()` |
| Criar variáveis | `.assign()`, **`np.where(cond, a, b)`** (condicional), `pd.qcut` (categorizar em quantis/faixas), `.cumsum()`, `.shift()` |
| Texto | `.str.slice()`, `.str.split()`, `.str.startswith/endswith`, `.str.rstrip`, `.str.extractall` |
| Resumir | **`.groupby(var).agg(...)`** (agrupa por critério **qualitativo**; **salve o resultado em outro objeto**: o objeto agrupado tem estrutura diferente do DataFrame), `.sort_values()`, `.reset_index()`, `pd.crosstab` (tabela de contingência → ponto de partida do **teste qui-quadrado**) |
| Reestruturar | **`.melt()`** (de **wide** para **long**; "derrete": variáveis em colunas viram linhas) e **`.pivot()`/`pivot_table`** (long → wide; variáveis nas linhas viram colunas). **Formato wide** = variáveis em colunas (adequado para estatística/modelos); **long** = variáveis empilhadas em linhas |
| Combinar | **`.concat()`** (empilhar linhas ou colar colunas) e **`.merge(how=…)`** |

### Tipos de merge (junção) — CAI
Mantém no resultado: **`left`** = todas as observações do **DataFrame principal à esquerda** (+ correspondentes da direita); **`right`** = todas as da direita; **`inner`** = só as que aparecem **nas duas**; **`outer`** = **todas** (união). **Chave:** variável com o mesmo nome nos dois DataFrames (se não houver chave única, usa-se combinação de variáveis). Exemplo: `left merge` leva informações de `dados_grupo` (income group) para `dados_saude`. Faltantes resultantes de joins precisam de tratamento.

## 4. Boas práticas e armadilhas
- **Salvar banco agrupado em separado**; checar **tipos** após importar; **variável categórica ≠ média** (não tirar média de categoria); índices começam em 0; usar `.copy()` ao extrair cópia.
- **Setores/grupos com poucas observações enviesam médias** (média representa poucas empresas).
- Em **Big Data** muda-se de biblioteca (Spark/Dask/etc.) por eficiência — o ciclo é o mesmo.
- **Git e GitHub:** **Git = controle de versão** (rastreia e armazena versões dos arquivos; histórico do projeto; `commit` a cada mudança importante, versões 1, 2, 3…); **GitHub = plataforma/"rede social" de desenvolvedores** para repositórios públicos ou privados (compartilhar, colaborar, divulgar). Repositório local (pasta do projeto) × remoto.
- **Pipeline de construção de variável (exemplo do futebol):** `np.where` encadeado para definir o "vencedor" a partir de gols e para classificar "acerto/erro" da previsão (vencedor previsto × real; o mandante com maior probabilidade prevista vs. visitante), depois `groupby` pela fase.
- Fontes: Banco Mundial (indicadores em formato wide/long), CVM (dados contábeis, contas e códigos), dados meteorológicos ("dados tempo").

## Pergunta típica
O que é data wrangling e quando ocorre · etapas do CRISP-DM (e onde entra o wrangling) · diferença entre left/right/inner/outer join · wide × long (melt e pivot) · para que serve `groupby` · como o `.query` funciona · como tratar variável categórica no pandas (não calcular média) · Git × GitHub.
