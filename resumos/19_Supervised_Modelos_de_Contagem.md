# 19 · Supervised ML — Modelos para Dados de Contagem (Poisson, Binomial Negativo, Inflacionados de Zeros)
**Prof. Dr. Luiz Paulo Fávero · 2 aulas · Prioridade: ALTA (dica explícita: "se cair uma pergunta na avaliação… o que caracteriza um dado de contagem?")**

## 1. O que é dado de contagem — 4 características (CAI NA AVALIAÇÃO)
O professor: *"se cair uma pergunta na avaliação, só estou dando spoiler: o que caracteriza um dado de contagem? Quatro coisinhas."*
1. **Quantidade** (variável dependente quantitativa);
2. **Valores discretos** (inteiros);
3. **Não negativos** (0, 1, 2, …);
4. **Precisa ser definida uma exposição** (unidade temporal, espacial ou social — mês, ano, área, região…; "se mudar a exposição, muda a contagem").
Exemplos: idas ao médico por ano (idade, sexo, plano), nº de IPOs por ano em países emergentes, violações de trânsito por mês, falhas em manufatura, ecologia, mercado imobiliário. **Y define a classe de modelo (pela distribuição de Y).**

## 2. Modelo Poisson
- **Distribuição:** p(Y = m) = e^(−λ)·λ^m / m!, em que **λ = taxa média esperada** de ocorrências em dada exposição.
- **Característica central: média = variância = λ → EQUIDISPERSÃO.** Só um parâmetro (λ).
- **Modelo:** **ln(λi) = α + β1X1i + … + βkXki** (ligação logarítmica; λ = e^(α+βX)). Estimado por **máxima verossimilhança** (função objetivo: maximizar o **logaritmo da função de verossimilhança** da distribuição Poisson). Python: `smf.poisson('y ~ x1 + x2', data).fit()`.
- (†) **Interpretação:** e^β = razão entre taxas esperadas por unidade de X.

## 3. Superdispersão e Teste de Cameron e Trivedi (1990)
- **Superdispersão:** **variância > média** (cauda longa; a Poisson não captura valores altos). Diagnóstico preliminar: comparar média e variância (ex.: variância ≈ 50× a média). **Subdispersão:** variância < média (a OLS com Box-Cox não resolve; ainda há cauda longa/normalidade dos erros).
- **Teste (4 passos):** 1) estimar o modelo **Poisson**; 2) criar **Y\* = [(Y − λ̂poisson)² − Y] / λ̂poisson**; 3) estimar um **modelo auxiliar OLS de Y\* em função de λ̂poisson, SEM intercepto** (único caso conhecido sem alfa: é um teste de variância, não preditivo); 4) olhar o **β**: **se for estatisticamente diferente de zero (p < 0,05) → há superdispersão** (variância estatisticamente maior que a média). Se β não significante → **equidispersão** → usar Poisson.

## 4. Modelo Binomial Negativo (Poisson-Gama, NB2)
- **Quando:** quando há **superdispersão** (cauda longa). **Dois parâmetros:** **θ (parâmetro de forma)** e **δ (taxa de decaimento)**. **Média = λ_bneg; variância = λ + φ·λ²** com **φ = 1/θ** ("**alfa**" no output do statsmodels = **inverso do parâmetro de forma**). A variância é **quadrática**.
- **Modelo:** ln(λbneg) = α + β1X1 + … ; Y segue **Poisson-Gama**; função objetivo = **log da verossimilhança da distribuição binomial negativa**. Python: `smf.negativebinomial(...)`.
- **Como decidir entre os dois:** **teste do parâmetro alfa (z de Wald):** se **alfa for estatisticamente significante (p < 0,05) → há superdispersão e o binomial negativo é o melhor**; **se alfa não for significante, o output é idêntico ao da Poisson** (equidispersão) — o NB nunca é pior. **Teste de razão de verossimilhança (LR)** entre Poisson e NB compara os log-likelihoods: o de maior LL, com diferença significante, é melhor; o NB também **prevê melhor valores altos** (ex.: 22 × 17).
- **Caudas longas:** Poisson não consegue; NB sim.

## 5. Modelos Inflacionados de Zeros (ZIP e ZINB) — eventos raros
- **Excesso de zeros** (ex.: 5.000 residências e só 4 com violência doméstica): combinação de **modelo para dados de contagem + modelo binário (logístico)** — investigam **as razões da contagem** *e* **as razões de o fenômeno ocorrer ou não**.
- **ZIP = Bernoulli (logit) + Poisson**; **ZINB = Bernoulli (logit) + Poisson-Gama (binomial negativo)** (Lambert, 1992).
- **Dois processos geradores de zeros:** **zeros estruturais** (componente dicotômico: o evento nunca ocorreria) e **zeros amostrais** (componente de contagem: poderia ocorrer, mas não ocorreu naquele período). **P(Y=0) = p_logit + (1 − p_logit)·P_contagem(0)**; **P(Y=m) = (1 − p_logit)·P_contagem(m)**, m ≥ 1. Ex.: p_logit = 0,7 → 70% dos zeros vêm da inflação e 30% da própria Poisson.
- **Teste de Vuong (1989):** define se **há inflação de zeros** (compara o modelo inflacionado × o convencional, não aninhados). Significante → usar modelo inflacionado. O ZINB consegue reduzir o efeito de variáveis (ex.: impacto do "enforcement legal").

## 6. Roteiro de escolha (resumo prático)
1. Y é contagem? (4 características) → modelos de contagem. 2. Estimar **Poisson**; 3. **Cameron-Trivedi** (superdispersão?) e olhar alfa do NB; 4. **Teste de Vuong** (zeros excessivos?); 5. Escolher **Poisson / NB / ZIP / ZINB** pelo **log-likelihood**, testes (LR, Wald, Vuong) e interpretar e^β.
- **Heterocedasticidade e termo de erro não fazem sentido** em modelos binários/multinomiais (Y quali; previsto = probabilidade). Para contagem, a análise é por dispersão da própria distribuição.
- Os coeficientes só são interpretados após garantir que o **modelo certo** (equi × superdispersão × zeros) foi escolhido — "não transformem ciência de dados em *self-service data science*".

## Pergunta típica
As 4 características de dado de contagem · equidispersão × superdispersão × subdispersão · o que faz o teste de Cameron e Trivedi (e por que sem intercepto) · quando usar binomial negativo e o que é o parâmetro alfa · diferença Poisson × NB (1 × 2 parâmetros; var = λ × λ + φλ²) · o que são zeros estruturais × amostrais · qual teste detecta inflação de zeros (Vuong) · ZIP × ZINB.
