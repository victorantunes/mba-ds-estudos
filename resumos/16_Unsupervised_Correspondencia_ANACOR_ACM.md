# 16 · Unsupervised ML — Análise de Correspondência (ANACOR e ACM) + Exercícios Aplicados
**Prof. Wilson Tarantin Jr. · 3 aulas · Prioridade: ALTA (fecha o bloco não supervisionado; "qual técnica para qual tipo de variável" é cobrado sempre)**

> **Em uma frase:** a análise de correspondência mostra, em um **mapa**, **quais categorias de variáveis qualitativas "andam juntas"** — categorias próximas no mapa estão associadas.

**Pré-requisitos:** tabela de contingência e teste qui-quadrado (01); cluster e PCA (14, 15). **Vem depois:** regressões (17+).

## Por que isso importa (intuição)
PCA e cluster exigem números. Mas muitos dados são categorias (escola pública/privada, perfil do investidor, tipo de aplicação). **Não dá para tirar média de "pública"** — e codificar categorias como 1, 2, 3 cria uma **ponderação arbitrária**. A correspondência usa **contagens** para ver se há associação e desenhar um mapa onde **proximidade = associação**.

## 1. Objetivo
- Para **variáveis categóricas**; verifica **associação significativa entre variáveis e entre suas categorias** e gera o **mapa perceptual**. Variável métrica entra se for **categorizada** antes (faixas).
- **Exploratória/não supervisionada** (interdependência), **sem inferência** fora da amostra; se entrarem observações, refaz.
- **ANACOR (simples)** = **2** variáveis; **ACM/MCA (múltipla)** = **3 ou mais**.

## 2. ANACOR — duas etapas
**Etapa 1 — há associação? (teste qui-quadrado)**
1. Tabela de contingência (frequências observadas).
2. **Esperada** de cada célula = (total da linha × total da coluna) ÷ N.
3. **Resíduo** = observada − esperada; χ² da célula = resíduo² ÷ esperada; **χ² total = soma**.
4. **H0: independentes (associação aleatória); H1: há dependência.** gl = (I−1)(J−1). **p < α → rejeita H0 → há associação.** (`scipy.stats.chi2_contingency`.)
- O teste é **global**. Só vá à etapa 2 se houver associação.

**Etapa 2 — quais categorias se associam? Mapa perceptual**
- **Resíduo padronizado ajustado > 1,96 (5%) → associação significativa entre aquelas duas categorias** (excesso de ocorrências no cruzamento).
- **Dimensões do mapa:** m = **mín(I−1, J−1)**. **Autovalores = inércias principais parciais**; **inércia total = Σλ = χ² ÷ N**; **% da inércia por dimensão = λ ÷ inércia total**. Maior inércia/χ² = associação mais forte.
- **Massa:** peso (representatividade) de cada categoria na sua variável. **Coordenadas** das categorias formam o mapa.
- **Leitura:** **categorias próximas = associadas**.

**Exemplo resolvido.** Escola (pública/privada) × aprovação (sim/não), N = 200. Observados: pública 30 sim/70 não; privada 60 sim/40 não. Totais: linhas 100/100; colunas 90 (sim)/110 (não).
- **Esperados:** 45; 55; 45; 55. **Resíduos:** −15; +15; +15; −15.
- **χ² = 225/45 + 225/55 + 225/45 + 225/55 ≈ 5 + 4,09 + 5 + 4,09 = 18,2**, gl = 1 → rejeita H0: **há associação**.
- Resíduo padronizado ajustado da célula (pública, sim) ≈ −15 ÷ 3,52 ≈ **−4,3** → |4,3| > 1,96: pública está **menos** associada a "sim"; privada, **mais**.
- Dimensões = mín(1, 1) = **1**; inércia total = 18,2 ÷ 200 ≈ **0,09**.

## 3. ACM (múltipla)
- **1º passo:** χ² **para cada par** de variáveis; **só entram na ACM variáveis associadas a pelo menos uma outra**.
- O **input é o banco de dados** (não uma tabela de contingência só).
- **Matriz binária (indicadora) Z:** 0/1 por categoria; **dimensões = J − Q** (J = total de categorias; Q = nº de variáveis); inércia total = (J − Q) ÷ Q.
- **Matriz de Burt B = Z′Z:** cruza todos os pares; aplica-se a ANACOR → coordenadas principais.
- Python: **`prince.MCA`**. Plote as dimensões com autovalor acima da média.

**Exemplo.** 3 variáveis com 3, 2 e 4 categorias → J = 9, Q = 3 → **6 dimensões**; inércia total = (9 − 3) ÷ 3 = **2**.

## 4. Visão integrada das técnicas não supervisionadas
| Técnica | Agrupa | Variáveis | Base | Saída |
|---|---|---|---|---|
| **Cluster** | **observações** | métricas | **distâncias** (padronizar) | clusters |
| **PCA** | **variáveis** | métricas | **correlações** | fatores ortogonais, índices |
| **Correspondência** | **categorias** | categóricas | **qui-quadrado** | mapa perceptual |
- **Podem se combinar:** cluster → ANACOR; cluster com os fatores da PCA; coordenadas do mapa → cluster ou PCA. Com variáveis mistas use **mais de uma técnica**.
- Cuidados: remover faltantes; **nunca tirar média de categórica**; ANOVA para ver quais variáveis formaram clusters; selecionar fatores sempre **perde informação**.

## Armadilhas e confusões comuns
| Confusão | O correto |
|---|---|
| ANACOR serve para variáveis métricas | para **categóricas** (métricas só após categorizar) |
| Associação global = todas as categorias associadas | o χ² é **global**; o resíduo ajustado mostra **quais pares** |
| Resíduo ajustado > 1,96 é "forte" | indica **significância a 5%** entre aquelas categorias |
| ACM aceita qualquer variável | só as **associadas** a ao menos uma outra |
| Dimensões = nº de categorias | ANACOR: **mín(I−1, J−1)**; ACM: **J − Q** |
| Categorias distantes no mapa são associadas | **próximas** = associadas |
| Técnicas não supervisionadas preveem | **não** têm caráter preditivo |

## Resumo-relâmpago
- χ²: esperada = (linha × coluna) ÷ N; gl = (I−1)(J−1); p < α → associação.
- Resíduo ajustado > 1,96 → par significativo. Inércia total = χ² ÷ N. Dimensões: mín(I−1, J−1).
- ACM: filtrar variáveis; matriz binária (J − Q dimensões) ou Burt (Z′Z).
- Cluster/PCA = métricas; correspondência = categóricas.

## Teste-se
1. Qual a hipótese nula do qui-quadrado de associação?
<details markdown="1"><summary>Ver resposta</summary>As variáveis são independentes (associação aleatória).</details>

2. Quantos graus de liberdade tem uma tabela 4×5?
<details markdown="1"><summary>Ver resposta</summary>(4−1)(5−1) = 12.</details>

3. O que significa resíduo padronizado ajustado de 2,8?
<details markdown="1"><summary>Ver resposta</summary>Excesso de ocorrências no cruzamento (> 1,96): associação significativa entre aquelas categorias.</details>

4. Por que remover variáveis sem associação na ACM?
<details markdown="1"><summary>Ver resposta</summary>Porque uma variável que não se associa a nenhuma outra não tem o que mostrar no mapa e só adiciona ruído.</details>

5. Diferença entre ANACOR e ACM?
<details markdown="1"><summary>Ver resposta</summary>ANACOR usa 2 variáveis categóricas; ACM usa 3 ou mais.</details>

## Pergunta típica
Qual técnica usar para cada tipo de variável/objetivo · hipóteses do χ² e gl · significado do resíduo padronizado ajustado > 1,96 · quantas dimensões tem a ANACOR/ACM · o que mede a inércia · diferença ANACOR × ACM · por que remover variável sem associação na ACM · matriz binária × matriz de Burt · por que as técnicas não supervisionadas não preveem
