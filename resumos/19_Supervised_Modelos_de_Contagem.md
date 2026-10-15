# 19 · Supervised ML — Modelos para Dados de Contagem (Poisson, Binomial Negativo, Inflacionados de Zeros)
**Prof. Dr. Luiz Paulo Fávero · 2 aulas · Prioridade: ALTA (destaque explícito do professor: "o que caracteriza um dado de contagem?")**

> **Em uma frase:** quando Y é uma **contagem** (0, 1, 2, … eventos numa exposição), usa-se Poisson; se a variância for maior que a média, **binomial negativo**; se houver zeros demais, **modelos inflacionados de zeros**.

**Pré-requisitos:** Poisson e Bernoulli (01), regressão (17), logística (18). **Vem depois:** 20 (multinível).

## Por que isso importa (intuição)
Número de idas ao médico por ano, de acidentes por mês, de falhas por lote: **não é contínuo** e **nunca é negativo**, então OLS falha. A Poisson é a distribuição "natural" de contagens, mas assume algo restritivo — **média = variância**. Dados reais costumam ter **caudas longas** (poucos casos com contagens muito altas) e **muitos zeros**; os outros modelos corrigem isso.

> **Destaque do professor:** *"o que caracteriza um dado de contagem? Quatro coisinhas."*

## 1. As 4 características do dado de contagem (muito cobradas)
1. **Quantidade** (Y quantitativa); 2. **valores discretos (inteiros)**; 3. **não negativos** (0, 1, 2…); 4. **exposição definida** (tempo, área, região — "se mudar a exposição, muda a contagem").
Exemplos: consultas por ano, IPOs por ano, infrações por mês, falhas de fabricação.

## 2. Modelo Poisson
- **p(Y = m) = e^(−λ)·λᵐ ÷ m!**, com **λ = taxa média** na exposição.
- **Característica central: média = variância = λ (equidispersão).** Um só parâmetro.
- **Modelo:** **ln(λ) = α + β₁X₁ + … + βₖXₖ** (ligação logarítmica); estimado por **máxima verossimilhança**. Python: `smf.poisson`.
- (†) **eᵝ** = razão entre taxas esperadas por unidade de X.

**Exemplo resolvido.** λ = 3 consultas/ano. **P(0) = e⁻³ ≈ 0,050**; **P(2) = e⁻³·3² ÷ 2 ≈ 0,224** (22,4%). Se a exposição passa de 1 ano para 6 meses, λ cai para ≈ 1,5 — por isso a exposição precisa estar definida.

## 3. Superdispersão e o teste de Cameron e Trivedi
- **Superdispersão:** **variância > média** (cauda longa). **Subdispersão:** variância < média. Diagnóstico inicial: compare média e variância.
- **Teste (4 passos):** (1) estimar a **Poisson**; (2) criar **Y\* = [(Y − λ̂)² − Y] ÷ λ̂**; (3) regressão auxiliar OLS de Y\* sobre λ̂, **sem intercepto** (é um teste de variância, não preditivo); (4) olhar o **β**: **p < 0,05 → há superdispersão**. Se não significante → equidispersão → Poisson serve.

## 4. Binomial Negativo (Poisson-Gama)
- **Quando:** superdispersão. **Variância = λ + φ·λ²** (quadrática), com **φ = 1/θ** (o **"alfa"** do statsmodels). **Dois parâmetros:** θ (forma) e δ (decaimento).
- **Decisão Poisson × NB:** **alfa significante (p < 0,05) → superdispersão → NB melhor**; se alfa não é significante, o NB equivale à Poisson (o NB nunca é pior). Também há o **teste de razão de verossimilhança (LR)** e o NB prevê melhor valores altos.

**Exemplo resolvido.** Média = 2 e variância = 10. Em Poisson a variância seria 2 (equidispersão). No NB: 10 = 2 + φ·2² → **φ = 2** → o modelo reproduz a cauda longa que a Poisson não captura.

## 5. Inflacionados de zeros (ZIP e ZINB) — eventos raros
- **Excesso de zeros** (ex.: 5.000 residências e só 4 com violência doméstica): combina **modelo de contagem + modelo binário (logístico)**.
- **ZIP = logit + Poisson; ZINB = logit + binomial negativo** (Lambert, 1992).
- **Dois tipos de zero:** **estruturais** (componente dicotômico: o evento **nunca** ocorreria) e **amostrais** (componente de contagem: **poderia** ocorrer, mas não ocorreu).
- **P(Y=0) = p_logit + (1 − p_logit)·P_contagem(0)**; **P(Y=m) = (1 − p_logit)·P_contagem(m)** para m ≥ 1.
- **Teste de Vuong (1989):** indica se **há inflação de zeros** (modelo inflacionado × convencional). Significante → use o inflacionado.

**Exemplo resolvido.** p_logit = 0,7 e P_Poisson(0) = 0,2 → **P(Y=0) = 0,7 + 0,3 × 0,2 = 0,76**; **P(Y=1) = 0,3 × P_Poisson(1)**.

## 6. Roteiro de escolha
1. Y é contagem (4 características)? → 2. estimar **Poisson** → 3. **Cameron-Trivedi / alfa**: superdispersão? → **NB** → 4. **Vuong**: zeros em excesso? → **ZIP/ZINB** → 5. comparar por **log-likelihood** e testes (LR, Wald, Vuong) → só então interpretar eᵝ.
- Heterocedasticidade/termo de erro não se aplicam como em OLS; vale a dispersão da própria distribuição.

## Armadilhas e confusões comuns
| Confusão | O correto |
|---|---|
| Qualquer Y numérico → OLS | contagem: inteiro, ≥ 0, com exposição → **Poisson/NB** |
| Poisson aceita variância maior que a média | exige **média = variância** |
| NB piora a Poisson quando não há superdispersão | com alfa não significante, equivale à Poisson |
| Zeros em excesso = superdispersão | são problemas **diferentes**; o ZIP/ZINB trata zeros |
| Cameron-Trivedi usa intercepto | a regressão auxiliar é **sem intercepto** |
| Zeros estruturais = amostrais | estruturais: **nunca** ocorreria; amostrais: poderia, mas não ocorreu |
| Vuong detecta superdispersão | detecta **inflação de zeros** |

## Resumo-relâmpago
- Contagem: quantidade, discreta, não negativa, com exposição.
- Poisson: média = variância = λ. NB: var = λ + φλ², alfa = φ. ZIP/ZINB: logit + contagem; Vuong.
- Cameron-Trivedi: β da auxiliar sem intercepto significante → superdispersão.

## Teste-se
1. Quais as 4 características de um dado de contagem?
<details markdown="1"><summary>Ver resposta</summary>Quantidade, valores discretos, não negativos e exposição definida.</details>

2. Média = 4 e variância = 20. Qual o modelo mais adequado?
<details markdown="1"><summary>Ver resposta</summary>Binomial negativo (superdispersão: variância muito maior que a média).</details>

3. O que o teste de Vuong detecta?
<details markdown="1"><summary>Ver resposta</summary>Inflação de zeros (modelo inflacionado × convencional).</details>

4. Diferencie zero estrutural e zero amostral.
<details markdown="1"><summary>Ver resposta</summary>Estrutural: o evento nunca ocorreria (componente logit). Amostral: poderia ocorrer mas não ocorreu naquele período (componente de contagem).</details>

## Pergunta típica
As 4 características de dado de contagem · equidispersão × superdispersão × subdispersão · o que faz o teste de Cameron e Trivedi (e por que sem intercepto) · quando usar binomial negativo e o que é o alfa · diferença Poisson × NB · zeros estruturais × amostrais · qual teste detecta inflação de zeros · ZIP × ZINB
