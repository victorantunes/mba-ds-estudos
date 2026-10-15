# 20 · Supervised ML — Modelagem Multinível (HLM / GLMM)
**Prof. Dr. Luiz Paulo Fávero · 2 aulas (07 e 14/04/2026) · Prioridade: ALTA (dica explícita: "vai cair esse tipo de pergunta na prova": prever valores, ICC, efeito escola × efeito estudante)**

## 1. Ideia e vocabulário
- **Modelo multinível** = modelo que **reconhece estruturas de dados aninhadas/hierárquicas**: observações (nível 1) dentro de grupos (nível 2) dentro de grupos maiores (nível 3). Ex.: **alunos → escolas → municípios**; **empresas → países**; **medidas repetidas no tempo → indivíduos → grupos**.
- **Sinônimos** (todos significam modelagem multinível): **hierarchical linear models (HLM)**, **mixed models**, **nested models**, **random coefficients models**, **GLMM** (Generalized Linear Mixed Models). É o **modelo supervisionado mais geral**, do qual os outros derivam. Pouco usado por: estrutura dos dados, não considerar a natureza multinível, e **capacidade computacional** em interações profundas.
- Quando **não há hierarquia explícita**, é possível criar **contextos latentes**: **clusterizar a amostra** e usar o **cluster como o nível/contexto** (output da técnica não supervisionada vira input do supervisionado).
- **Por que não usar OLS ou OLS com dummies de grupo?** OLS ignora os efeitos contextuais; **dummies de grupo não separam efeitos observáveis dos não observáveis** nem capturam variância entre contextos. Os modelos tradicionais **ignoram as interações entre variáveis de níveis diferentes (efeitos fixos) e entre termos de erro e variáveis (efeitos aleatórios)**.
- **Paradoxo de Simpson:** uma tendência presente dentro dos grupos pode **se inverter ou desaparecer** quando os dados são combinados.

## 2. Componentes
- **Efeitos fixos:** parâmetros comuns (γ) para toda a população (intercepto e inclinação "médios").
- **Efeitos aleatórios:** termos que variam entre grupos: **ν0j = variância dos interceptos aleatórios** (diferença nas **médias**/desempenho inicial entre escolas) e **ν1j = variância das inclinações aleatórias** (diferença na **taxa de variação**, ex.: o efeito de estudar mais difere entre escolas). Há também o **erro idiossincrático de nível 1 (εij)**.
- **Primeiro passo:** **testar se as variâncias dos efeitos aleatórios são estatisticamente diferentes de zero**; se forem, OLS **não é adequado**; se não forem, o modelo multinível não agrega. **Grupos com uma única observação são descartados** (não há variância).
- **Comparação de modelos: teste de razão de verossimilhança (LR)** — ganho de **log-likelihood** (ex.: 2018 × 2 = 4036 a favor do modelo com maior LL); gl = nº de efeitos aleatórios adicionais. Compara-se também com **fitted values do GLM sem multinível** vs. multinível (gráfico real × previsto; quanto mais próximo da reta de 45°, melhor).

## 3. Modelos HLM2 (2 níveis) — equações
- **Modelo nulo/intercepto aleatório:** Nível 1: **desempenhoij = β0j + εij**; Nível 2: **β0j = γ00 + ν0j** → **desempenhoij = γ00 + ν0j + εij**.
- **Interceptos e inclinações aleatórios:** N1: desempenhoij = β0j + β1j·horasij + εij; N2: β0j = γ00 + ν0j; β1j = γ10 + ν1j → desempenhoij = γ00 + γ10·horasij + ν0j + ν1j·horasij + εij.
- **Modelo final com variável de nível 2 (ex.: texp = tempo médio de experiência dos professores da escola):** β0j = γ00 + γ01·texpj + ν0j; β1j = γ10 + γ11·texpj + ν1j → **desempenhoij = γ00 + γ10·horasij + γ01·texpj + γ11·texpj·horasij + ν0j + ν1j·horasij + εij** (aparece **interação entre níveis** texp × horas).
- **ICC (coeficiente de correlação intraclasse)** (dica de prova: "qual é o efeito escola, qual é o efeito estudante, dado esse output") = **variância do nível grupo / (variância do nível grupo + variância do erro)** — **proporção da variância total atribuível ao contexto (escola)**; o restante é efeito do estudante. Quanto maior o ICC, mais importante o contexto.
- **Previsão manual (PERGUNTA DE PROVA):** "valor previsto do desempenho do aluno da escola 1, que estuda 11 horas/semana e cuja escola tem texp = 3,6" → substituir na equação final **os γ do efeito fixo** e **somar os efeitos aleatórios ν0j e ν1j·horas da escola 1** (a função `fittedvalues` já inclui os efeitos aleatórios). Também há gráficos "tapinhas para cima ou para baixo" = **efeito aleatório de cada escola** (qual escola tem desempenho acima/abaixo da média).

## 4. HLM3 com medidas repetidas (growth model)
- **Níveis:** **N1 = tempo (medidas repetidas)**, **N2 = indivíduo (aluno)**, **N3 = grupo (escola)**.
- **Modelo nulo:** desempenho_tjk = β0jk + εtjk; β0jk = γ00k + ν0jk; γ00k = δ000 + τ00k → **= δ000 + ν0jk + τ00k + εtjk**.
- **Modelo de tendência linear com interceptos e inclinações aleatórios (growth model):** N1: desempenho_tjk = β0jk + β1jk·mês + εtjk; N2: β0jk = γ00k + ν0jk, β1jk = γ10k; N3: γ00k = δ000 + τ00k, γ10k = δ100 + τ10k → **desempenho = δ000 + δ100·mês + ν0jk + τ00k + τ10k·mês + εtjk**. Com **variáveis de nível 2 (ativ)** e **de nível 3 (texp)** interagindo com o tempo (ex.: δ110·ativ·mês, δ101·texp·mês).
- Painel/efeitos aleatórios no tempo: diferentes de **efeito fixo (dummies)** e de **efeito aleatório só de intercepto**.

## 5. Python e prática
- **statsmodels `MixedLM`/`mixedlm`** (`smf.mixedlm('desempenho ~ horas', data, groups=df['escola'], re_formula='~horas')`); para HLM3 usa-se `vc_formula` (variance components; ex.: `0 + C(estudante)` para intercepto aleatório por estudante, nível 2). **Variáveis `object` precisam virar dummy/numéricas** antes de entrar no modelo.
- **Aplicações:** Rajan & Zingales (1995) — alavancagem (Leverage) de 4.557 empresas em 7 países com variáveis de nível 1 (ativos tangíveis, market-to-book, log vendas, ROA) e coeficientes aleatórios por país; escolas × estudantes; modelos de **crédito/risco**; "qualquer modelo supervisionado pode ganhar capacidade preditiva ao incorporar contexto".
- Desafios: capacidade de processamento, **clusterização da amostra** para contextos latentes, métodos de estimação (REML/ML).

## Pergunta típica
Definição e sinônimos de modelagem multinível · por que não OLS nem dummies · o que é efeito fixo × aleatório · qual a primeira verificação (variância dos efeitos aleatórios) · como comparar modelos (LR, log-likelihood) · calcular ICC · interpretar ν0j e ν1j · montar a previsão com a equação final · níveis de um modelo de medidas repetidas (tempo → indivíduo → grupo) · paradoxo de Simpson · uso de cluster como contexto latente.
