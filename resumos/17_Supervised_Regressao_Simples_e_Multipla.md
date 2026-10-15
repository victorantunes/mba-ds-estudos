# 17 · Supervised ML — Análise de Regressão Simples e Múltipla (OLS)
**Prof. Dr. Luiz Paulo Fávero · 4 aulas · Prioridade: MÁXIMA — é o tema com mais destaques de avaliação do curso**

> **Em uma frase:** a regressão encontra a **reta (ou plano) que melhor descreve como Y varia com X**, escolhendo os coeficientes que minimizam a soma dos quadrados dos erros — e depois testa se o modelo e cada variável realmente contam.

**Pré-requisitos:** correlação, testes t e F, distribuições (01). **Vem depois:** 18–20 (outros tipos de Y) e 22 (séries).

> **O que o professor destacou como pergunta de avaliação:** (1) **nomes do R²**; (2) **interpretar uma saída/tabela**; (3) **calcular o R² da regressão simples a partir da correlação**; (4) **prever Y com dummies (somando betas)**; (5) **diferença entre F, t e R²**; (6) **por que não usar pesos arbitrários em categorias**.

## Por que isso importa (intuição)
Você quer prever o tempo de entrega a partir da distância. Se desenhar os pontos (distância × tempo), a reta que passa "no meio da nuvem" resume a relação. O **OLS** escolhe a reta que **minimiza os erros ao quadrado** (distância vertical de cada ponto à reta). Depois vêm as perguntas de qualidade: *a reta explica quanto?* (R²), *existe modelo?* (F), *cada variável pesa?* (t), *os pressupostos valem?* (diagnósticos).

## 1. Contexto
- Dentro de *Machine Learning → Supervised → modelos GLM*. **A escala de Y define o modelo:** contínua → **OLS**; binária/multinomial → logística (18); contagem → Poisson/BN (19); dados aninhados → multinível (20).
- Supervisionado: **Y = f(X₁, …, Xₖ)**, confirmatório, com **previsão e inferência fora da amostra** (dentro da faixa de X do treino). *"Todos os modelos estão errados, mas alguns são úteis"* (Box).
- **Correlação não implica causalidade.**

## 2. Regressão linear simples
- **Yᵢ = α + β·Xᵢ + uᵢ:** α = intercepto; β = inclinação; **u = resíduo = Y real − Ŷ** (valor previsto/"fitted").
- **OLS/MQO:** escolhe α e β com **Σu = 0** e **Σu² mínima**. Python: `smf.ols('y ~ x', data=df).fit()`.
- **R² (coeficiente de ajuste = de explicação = de determinação):** **percentual da variância de Y explicado pelas variáveis explicativas**; vai de 0 a 1. **Na regressão simples, R² = r²** (correlação de Pearson ao quadrado).

**Exemplo resolvido.** X = 1, 2, 3, 4, 5; Y = 2, 4, 5, 4, 5. Médias: X̄ = 3; Ȳ = 4.
Σ(x−X̄)(y−Ȳ) = 4 + 0 + 0 + 0 + 2 = **6**; Σ(x−X̄)² = **10**; Σ(y−Ȳ)² = **6**.
**β = 6 ÷ 10 = 0,6**; **α = 4 − 0,6 × 3 = 2,2** → Ŷ = 2,2 + 0,6X. **R² = 6² ÷ (10 × 6) = 0,60** (r = √0,6 ≈ 0,77). Previsão para X = 6: 2,2 + 3,6 = **5,8** (fora da faixa 1–5: extrapolação, cuidado).
**Interpretação:** cada unidade a mais de X aumenta Y em média 0,6; X explica 60% da variância de Y.

## 3. F, t e R² não são a mesma coisa
- **Teste F (modelo como um todo):** **H0: β₁ = … = βₖ = 0; H1: ao menos um β ≠ 0.** **p < 5% → existe modelo.** **Quem diz se há modelo é o F, não o R².** Pode haver modelo com R² baixo (baixo poder preditivo); gl: k e n−k−1.
- **Teste t (cada parâmetro):** H0: βⱼ = 0; **t = estimativa ÷ erro padrão**; |t| < 1,96 → não significante a 95%. Na simples, t e F concluem o mesmo.
- **Intervalo de confiança:** se contém zero, o parâmetro não é significante.
- **Nunca exclua o intercepto α** só por não ser significante: forçar α = 0 **vicia os betas**.

## 4. Regressão múltipla
- **Y = α + β₁X₁ + … + βₖXₖ + u**; forma matricial b = (X′X)⁻¹X′Y. O beta é o efeito de Xⱼ com **as demais constantes (ceteris paribus)**.
- **R² ajustado = 1 − (1 − R²)(n − 1)/(n − k − 1):** **compara modelos com números diferentes de variáveis** (penaliza variáveis inúteis).

**Exemplo.** R² = 0,60, n = 5, k = 1 → R² ajustado = 1 − 0,4 × (4 ÷ 3) ≈ **0,47**.

## 5. Variáveis qualitativas → dummies (cai sempre)
- **Erro clássico: ponderação arbitrária** (Europa = 1, Ásia = 2, …): supõe efeito **linear** entre categorias, o que quase nunca é verdade.
- **Solução:** **n − 1 dummies** (0/1) para n categorias; a omitida é a **referência/baseline** (evita multicolinearidade perfeita). O beta da dummy = diferença média de Y **em relação à referência**.
- **Previsão com dummies:** some **α + betas das dummies que valem 1**.

**Exemplo resolvido.** Índice = 40 + 12·Europa − 6·África (referência: Ásia). Ásia = **40**; Europa = 40 + 12 = **52**; África = 40 − 6 = **34**.

## 6. Pressupostos e diagnósticos
**a) Normalidade dos resíduos (para inferência/IC).** Teste **Shapiro-Francia**; **H0: normais; queremos p > 0,05 (não rejeitar)** — o oposto dos testes F/t. Se não normal, a forma funcional é inadequada.
**b) Box-Cox:** Y* = (Yλ − 1) ÷ λ; escolhe-se o **λ** que mais aproxima a normalidade. **λ = 1** linear; 2 quadrática; 0,5 raiz; −1 inversa; **λ = 0 → ln(Y)**. Os betas do modelo transformado **não são comparáveis** aos do linear.
**c) Stepwise:** remove variáveis **não significantes** passo a passo (p ex. 0,05) e ajuda na multicolinearidade; **não conserta** heterocedasticidade nem forma funcional.
**d) Multicolinearidade:** alta correlação entre explicativas → **sinais invertidos, t baixo com F significante e R² alto**. **Tolerance = 1 − R²ₐᵤₓ; VIF = 1 ÷ Tolerance** (VIF > 10 = alerta). Solução: stepwise, remover variável ou **PCA**.
**e) Heterocedasticidade:** variância dos erros **não constante** (gráfico em cone). Causas: **variável relevante omitida** e forma funcional errada. **Breusch-Pagan: H0 = homocedasticidade; p < 0,05 → heterocedasticidade.**

**Exemplo (VIF).** Regressão auxiliar de X₂ nas outras dá R² = 0,90 → Tolerance = 0,10 → **VIF = 10**: colinearidade problemática.

## 7. Roteiro de estimação (script da aula)
1) explorar correlações/gráficos → 2) estimar OLS (com dummies) → 3) **stepwise** (95%) → 4) **Shapiro-Francia** dos resíduos → 5) se não normal, **Box-Cox** em Y e repetir → 6) **VIF** e **Breusch-Pagan** → 7) prever com `.predict()` **dentro da faixa de X**.

## Armadilhas e confusões comuns
| Confusão | O correto |
|---|---|
| R² baixo = não há modelo | quem decide é o **F** |
| Shapiro-Francia: queremos p < 0,05 | queremos **p > 0,05** (normalidade) |
| Breusch-Pagan: p > 0,05 indica problema | p **< 0,05** = heterocedasticidade |
| Para n categorias, n dummies | **n − 1** (uma é referência) |
| Codificar 1, 2, 3 para categorias | é **ponderação arbitrária**; use dummies |
| Excluir o intercepto se não significante | **não exclua** (vicia os betas) |
| Betas Box-Cox comparáveis ao linear | a métrica de Y mudou: **não comparáveis** |
| Stepwise resolve heterocedasticidade | só variáveis não significantes/multicolinearidade |
| R² simples ≠ correlação | R² simples = **r²** |

## Resumo-relâmpago
- OLS: Σu = 0, Σu² mínimo. R² = variância de Y explicada; simples: R² = r².
- F: existe modelo? t: variável significante? R² ajustado compara modelos.
- Dummies: n − 1, beta = diferença à referência. Shapiro-Francia p > 0,05; BP p < 0,05 = heterocedástico; VIF > 10.

## Teste-se
1. Correlação entre X e Y é 0,5. Qual o R² da regressão simples?
<details markdown="1"><summary>Ver resposta</summary>R² = 0,5² = 0,25 (25%).</details>

2. O F é significativo e o R² é 0,08. Existe modelo?
<details markdown="1"><summary>Ver resposta</summary>Sim, existe modelo (ao menos uma variável explica Y), mas com baixa capacidade preditiva.</details>

3. Uma variável qualitativa tem 5 categorias. Quantas dummies?
<details markdown="1"><summary>Ver resposta</summary>4; a quinta é a referência.</details>

4. O que se espera do Shapiro-Francia dos resíduos?
<details markdown="1"><summary>Ver resposta</summary>Não rejeitar H0 (p > 0,05): resíduos normais.</details>

5. Cite duas consequências da multicolinearidade.
<details markdown="1"><summary>Ver resposta</summary>Sinais invertidos/instáveis nos betas e t baixo com F significante e R² alto (erros de predição).</details>

## Pergunta típica
Nomes do R² e o que mede · diferença entre F, t e R² (há modelo ≠ R² alto) · hipóteses do F e do t · por que usar o R² ajustado · n−1 dummies e por que não usar pesos 1, 2, 3 · calcular valor previsto com dummies · R² na simples = r² · o que testa o Shapiro-Francia e qual resultado se espera · Box-Cox (λ = 0 → ln) · stepwise · multicolinearidade (VIF/Tolerance) · heterocedasticidade (causas, Breusch-Pagan) · por que não excluir o intercepto
