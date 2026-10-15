# 18 · Supervised ML — Modelos Logísticos Binários e Multinomiais
**Prof. Dr. Luiz Paulo Fávero · 2 aulas (10 e 17/03/2026) · Prioridade: ALTA (classificação; "qual distribuição/modelo", logito, cutoff e ROC)**
*Itens marcados com (†) são padrão da disciplina e complementam o que o professor mostrou nas lousas/planilhas.*

## 1. Quando usar
- Técnica **supervisionada** para **explicar ou predizer a probabilidade de ocorrência de um evento** em função de variáveis X. **Y é qualitativa**: **binária** (2 categorias → logística **binária**) ou **policotômica** (3+ categorias → logística **multinomial**). **X podem ser métricas ou não métricas** (qualitativas viram dummies, n−1).
- **Objetivos:** **atribuir probabilidades** (0–1) e **classificar** observações em categorias.
- São modelos de **classificação, não de "regressão" com erro de média zero**: aqui não faz sentido falar de termo de erro, e sim de acerto/erro de classificação. **Erros a evitar:** estimar OLS quando Y é qualitativa (**escolha errada do modelo**) e usar **pesos arbitrários** nas X qualitativas.
- **Não precisa balancear** (downsampling/oversampling) como alguns *ensemble models*; **não precisa separar treino e teste** nem definir hiperparâmetros (todos os dados são "treino"; separar penaliza a estimação). Eventos **raros**: modelos de contagem/inflação de zeros (resumo 19).
- Aplicações: chegar atrasado, falha de componente (Challenger × temperatura), **recuperação judicial**, probabilidade de **crédito e de default**, fidelidade do cliente.

## 2. Probabilidade, chance (odds) e logito
- **p** = probabilidade do evento (Y=1); **1 − p** = não evento.
- **Chance (odds) = p / (1 − p)**. p=0,50 → chance 1 (1 para 1); p=0,75 → chance 3; p=0,25 → chance 1/3.
- **Logito (Z) = ln(chance) = ln[p/(1−p)] = α + β1X1 + β2X2 + … + βkXk** (função **linear** nas X → "modelo linear generalizado").
- **Isolando p (função logística/sigmoide):** **p = 1 / (1 + e^(−Z))** = e^Z/(1 + e^Z) — assume valores entre **0 e 1** para qualquer Z de −∞ a +∞. Curva em "S".
- (†) **Interpretação do beta:** e^β = **razão de chances (odds ratio)** — quanto a chance do evento multiplica quando X aumenta 1 unidade. β>0 aumenta a probabilidade; β<0 diminui.

## 3. Estimação — Máxima Verossimilhança (MLE)
- **Y segue distribuição de Bernoulli** (binária) — **a função densidade de probabilidade de Y define a função objetivo**. **Função objetivo = maximizar o logaritmo da função de verossimilhança (LL)**: processo **iterativo** que ajusta α e βs para maximizar o acerto entre a probabilidade prevista e o que de fato ocorreu. (Aula: feito na mão por **otimização/Solver** no Excel.) Python: `smf.logit('y ~ x1 + x2', data=df).fit()` (statsmodels); **Y precisa estar numérica 0/1** (se for texto, converter). `.predict()` já aplica 1/(1+e^−Z).
- **Modelo nulo:** só intercepto (LL do modelo nulo). Teste **χ² (razão de verossimilhança)**: compara o modelo com preditoras × nulo; **p < 5% → pelo menos um β ≠ 0** (equivale ao teste F da regressão). **Teste z de Wald** para **cada parâmetro** (equivale ao t): p < 0,05 → significante.
- **Pseudo-R² de McFadden** = 1 − LL/LL₀ = incremento percentual do log-likelihood em relação ao modelo nulo. **Não é a variância explicada** como o R² da regressão (o nome "variância" é inadequado aqui).
- Cuidado com **overfitting** (não treinar demais algoritmos fortes como LightGBM); no logístico a estimação é por MLE (determinística).

## 4. Eficiência: cutoff, matriz de confusão, sensibilidade, especificidade e curva ROC
- **Cutoff (ponto de corte):** probabilidade a partir da qual se classifica como evento (**p̂ ≥ cutoff → 1**; padrão 0,5). **Mudar o cutoff muda os acertos**: baixar o cutoff aumenta a **sensibilidade** (mais verdadeiros positivos) mas inclui **falsos positivos** (observações antes corretas passam a erro).
- **Matriz de confusão (tabela de classificação):** verdadeiros positivos (VP), falsos positivos (FP), verdadeiros negativos (VN), falsos negativos (FN).
- (†) **Acurácia** = (VP+VN)/total. **Sensibilidade (recall)** = VP/(VP+FN) = acerto entre os que **tiveram** o evento. **Especificidade** = VN/(VN+FP) = acerto entre os que **não tiveram**.
- **Curva ROC:** plota **sensibilidade × (1 − especificidade)** para **todos os cutoffs**; **área sob a curva (AUC)** mede o poder de discriminação (0,5 = aleatório; 1 = perfeito). Exemplo da aula: só com a idade, **AUC ≈ 70%**; incluindo 15–16 dummies, **AUC ≈ 95%** (+25 pontos percentuais) e acurácia de **86%** — dummies melhoram muito mesmo sem variáveis métricas.
- Exemplo: Challenger — com 70 °F (21 °C), probabilidade de falha ≈ 13,7%.

## 5. Regressão logística multinomial
- **Y policotômica** com M categorias → **M − 1 logitos** (compara cada categoria à **categoria de referência**, escolhida pelo pesquisador). Para 3 categorias (0=referência, 1, 2): Z1 = α1 + β11X1 + …; Z2 = α2 + β12X1 + …
- **Probabilidades:** **P0 = 1/(1 + e^Z1 + e^Z2); P1 = e^Z1/(1 + e^Z1 + e^Z2); P2 = e^Z2/(1 + e^Z1 + e^Z2)** — **mesmo denominador; P0 + P1 + P2 = 100%** em cada linha.
- **Distribuição de Y:** (na lousa do professor) **a Y policotômica segue distribuição binomial/multinomial**, base da função de verossimilhança do modelo (Bernoulli no binário).
- **Interpretação:** parâmetros **sempre em relação à categoria de referência**; eficiência global: teste **χ²** do modelo e testes **z** dos parâmetros.
- **Classificação:** a observação vai para a categoria de **maior probabilidade estimada** — **não faz sentido definir cutoff/threshold** no multinomial.

## Pergunta típica
Por que logística e não OLS quando Y é qualitativa · logito, chance e probabilidade (converter p ↔ chance) · fórmula p = 1/(1+e^−Z) · por que MLE e qual a função objetivo · χ² × z de Wald · para que serve cutoff · sensibilidade × especificidade × ROC/AUC · quantos logitos no multinomial (M−1) · por que não há cutoff no multinomial · por que não balancear nem separar treino/teste aqui.
