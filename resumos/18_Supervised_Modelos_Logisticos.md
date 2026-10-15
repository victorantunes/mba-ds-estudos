# 18 · Supervised ML — Modelos Logísticos Binários e Multinomiais
**Prof. Dr. Luiz Paulo Fávero · 2 aulas · Prioridade: ALTA (classificação; "qual distribuição/modelo", logito, cutoff e ROC)**
*Itens marcados com (†) são padrão da disciplina e complementam o que o professor mostrou nas lousas.*

> **Em uma frase:** a regressão logística modela a **probabilidade** de um evento (sim/não, ou uma entre várias categorias) usando uma curva em "S" que nunca sai de 0 a 1.

**Pré-requisitos:** regressão (17), Bernoulli e odds (01). **Vem depois:** 19 (contagem) e 20 (multinível).

## Por que isso importa (intuição)
Se Y é "cliente deu calote (1) ou não (0)", uma reta de regressão pode prever −0,3 ou 1,4 — probabilidades impossíveis. A solução: modelar não p, mas o **logito = ln[p/(1−p)]**, que é linear em X e pode ir de −∞ a +∞; depois a **função logística** converte de volta para uma probabilidade entre 0 e 1.

## 1. Quando usar
- **Supervisionada**, para **explicar/predizer a probabilidade** de um evento. **Y qualitativa:** **binária** (2 categorias) → logística **binária**; **3 ou mais** → **multinomial**. **X** pode ser métrica ou qualitativa (dummies n−1).
- **Objetivos:** atribuir probabilidades e **classificar** observações.
- **Erros a evitar:** usar OLS quando Y é qualitativa e usar pesos arbitrários nas X qualitativas.
- **Não é necessário** balancear classes nem separar treino/teste (todos os dados estimam o modelo).
- Aplicações: atraso, falha de componente (Challenger × temperatura), recuperação judicial, **crédito e default**, fidelidade.

## 2. Probabilidade, chance (odds) e logito
- **Chance (odds) = p ÷ (1 − p).** p = 0,50 → chance 1; p = 0,75 → chance 3; p = 0,25 → chance 1/3.
- **Logito (Z) = ln[p ÷ (1 − p)] = α + β₁X₁ + … + βₖXₖ** (linear nas X).
- **Função logística (sigmoide):** **p = 1 ÷ (1 + e⁻ᶻ)** — sempre entre 0 e 1. Curva em S.
- (†) **Razão de chances:** **eᵝ** = quanto a chance do evento **multiplica** quando X sobe 1 unidade. β > 0 aumenta a probabilidade; β < 0 diminui.

**Exemplo resolvido.** Z = −2 + 0,5·X, com X = 6 → Z = **1** → p = 1 ÷ (1 + e⁻¹) = **0,73**. eᵝ = e⁰·⁵ ≈ **1,65**: cada unidade a mais de X multiplica a chance por 1,65 (aumento de ~65% na chance).

## 3. Estimação — máxima verossimilhança
- **Y segue Bernoulli**; a **função objetivo é maximizar o log da verossimilhança (LL)**, processo **iterativo**. Python: `smf.logit('y ~ x1 + x2', data=df).fit()`; Y precisa ser **numérica 0/1**.
- **Teste χ² (razão de verossimilhança):** compara com o **modelo nulo** (só intercepto); **p < 5% → ao menos um β ≠ 0** (equivale ao F). **Teste z de Wald:** cada parâmetro (equivale ao t).
- **Pseudo-R² de McFadden = 1 − LL ÷ LL₀.** **Não é variância explicada.**

**Exemplo.** LL do modelo = −60; LL do nulo = −100 → McFadden = 1 − (−60 ÷ −100) = **0,40**.

## 4. Eficiência: cutoff, matriz de confusão, sensibilidade, especificidade, ROC
- **Cutoff:** p̂ ≥ cutoff → classe 1 (padrão 0,5). **Baixar o cutoff aumenta a sensibilidade** e traz mais falsos positivos.
- **Matriz de confusão:** VP, FP, VN, FN. **Acurácia** = (VP+VN) ÷ total. **Sensibilidade (recall)** = VP ÷ (VP+FN) (acerto entre os que **tiveram** o evento). **Especificidade** = VN ÷ (VN+FP) (acerto entre os que **não tiveram**).
- **Curva ROC:** **sensibilidade × (1 − especificidade)** para todos os cutoffs; **AUC** mede a discriminação (**0,5 = aleatório; 1 = perfeito**). Na aula: só com idade, AUC ≈ 70%; com dummies, ≈ 95% e acurácia 86%.

**Exemplo resolvido.** 200 casos: VP = 40, FN = 10, FP = 20, VN = 130.
Acurácia = 170 ÷ 200 = **85%**; sensibilidade = 40 ÷ 50 = **80%**; especificidade = 130 ÷ 150 ≈ **86,7%**.

## 5. Logística multinomial
- **Y com M categorias → M − 1 logitos**, cada um comparando uma categoria à **categoria de referência**. Para 3 categorias: Z₁ e Z₂.
- **Probabilidades:** P₀ = 1 ÷ (1 + e^Z₁ + e^Z₂); P₁ = e^Z₁ ÷ (1 + e^Z₁ + e^Z₂); P₂ = e^Z₂ ÷ (1 + e^Z₁ + e^Z₂) — **mesmo denominador, somam 100%**.
- **Classificação:** categoria de **maior probabilidade**; **não há cutoff** no multinomial.

**Exemplo resolvido.** Z₁ = 0,5 e Z₂ = −0,2 → e^0,5 = 1,649; e^−0,2 = 0,819; denominador = 3,467. **P₀ = 0,288; P₁ = 0,476; P₂ = 0,236** (soma = 1). Classificada na categoria 1.

## Armadilhas e confusões comuns
| Confusão | O correto |
|---|---|
| OLS serve para Y binária | probabilidades fora de 0–1; use **logística** |
| Pseudo-R² de McFadden = variância explicada | **não**; compara log-likelihoods |
| β = variação da probabilidade | β é variação do **logito**; **eᵝ** é razão de chances |
| Multinomial tem 1 logito | **M − 1** logitos |
| Multinomial usa cutoff | **não**: vai para a categoria de maior probabilidade |
| Baixar o cutoff aumenta a especificidade | aumenta a **sensibilidade** (e os falsos positivos) |
| Precisa balancear e separar treino/teste | **não precisa** nesta disciplina |
| AUC = 0,5 é bom | 0,5 = **aleatório** |

## Resumo-relâmpago
- odds = p/(1−p); logito = ln(odds) = α + βX; p = 1/(1+e⁻ᶻ); eᵝ = razão de chances.
- MLE: maximizar LL. χ² (modelo) e z (parâmetros). McFadden = 1 − LL/LL₀.
- Sensibilidade = VP/(VP+FN); especificidade = VN/(VN+FP); ROC/AUC. Multinomial: M−1 logitos, sem cutoff.

## Teste-se
1. Converta p = 0,8 em chance.
<details markdown="1"><summary>Ver resposta</summary>0,8 ÷ 0,2 = 4 (4 para 1).</details>

2. β = 0,7. O que significa eᵝ ≈ 2,01?
<details markdown="1"><summary>Ver resposta</summary>Cada unidade a mais de X aproximadamente dobra a chance do evento.</details>

3. Quantos logitos tem um Y com 4 categorias?
<details markdown="1"><summary>Ver resposta</summary>3 (M − 1), cada um contra a referência.</details>

4. Por que baixar o cutoff aumenta a sensibilidade?
<details markdown="1"><summary>Ver resposta</summary>Mais observações passam a ser classificadas como evento, capturando mais verdadeiros positivos (ao custo de mais falsos positivos).</details>

## Pergunta típica
Por que logística e não OLS quando Y é qualitativa · logito, chance e probabilidade (converter p ↔ chance) · fórmula p = 1/(1+e⁻ᶻ) · por que MLE e qual a função objetivo · χ² × z de Wald · para que serve o cutoff · sensibilidade × especificidade × ROC/AUC · quantos logitos no multinomial · por que não há cutoff no multinomial · por que não balancear nem separar treino/teste aqui
