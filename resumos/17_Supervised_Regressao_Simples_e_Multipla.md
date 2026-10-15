# 17 · Supervised ML — Análise de Regressão Simples e Múltipla (OLS)
**Prof. Dr. Luiz Paulo Fávero · 4 aulas · Prioridade: máxima — é o tema com mais destaques de avaliação do curso**

> **Destaques do professor (perguntas de avaliação).** (1) os **nomes do R²**; (2) **interpretar uma saída/tabela**; (3) **calcular o R² da regressão simples a partir da correlação**; (4) **prever Y com dummies, somando betas**; (5) **a diferença entre F, t e R²**; (6) **por que não usar pesos arbitrários em categorias**.

## O fio condutor deste capítulo

Você quer prever o tempo de entrega a partir da distância. Ao desenhar os pontos (distância × tempo), uma reta que passa "no meio da nuvem" resume a relação. A **regressão por mínimos quadrados (OLS)** escolhe a reta que **minimiza a soma dos erros ao quadrado**, isto é, as distâncias verticais de cada ponto à reta. A partir daí surgem as perguntas de qualidade, que organizam o capítulo: *quanto a reta explica?* (R²), *existe modelo?* (teste F), *cada variável pesa?* (teste t) e *os pressupostos valem?* (diagnósticos).

```mermaid
flowchart LR
  A["Estimar o modelo por OLS"] --> B["R²: quanto explica?"]
  B --> C["Teste F: existe modelo?"]
  C --> D["Teste t: cada variável importa?"]
  D --> E["Diagnósticos: normalidade, multicolinearidade, heterocedasticidade"]
  E --> F["Prever dentro da faixa de X"]
```

## 1. Contexto: onde a regressão se encaixa

A regressão é um modelo **supervisionado**, do tipo **GLM**. **A escala de Y define o modelo:** Y contínuo → regressão (OLS); Y binário ou categórico → logística (capítulo 18); contagem → Poisson e afins (19); dados aninhados → multinível (20). O modelo estima \(Y = f(X_1, \ldots, X_k)\), é **confirmatório** e permite **previsão e inferência fora da amostra** (dentro da faixa de X usada no treino). Lembre-se de Box: *"todos os modelos estão errados, mas alguns são úteis"*, e de que **correlação não implica causalidade**.

## 2. Regressão linear simples

O modelo é \(Y_i = \alpha + \beta X_i + u_i\): \(\alpha\) é o intercepto, \(\beta\) a inclinação e \(u\) o **resíduo** (\(Y\) real − \(\hat{Y}\) previsto). O OLS escolhe \(\alpha\) e \(\beta\) de modo que \(\sum u = 0\) e \(\sum u^2\) seja o **mínimo possível**.

![A reta OLS e os resíduos (linhas pontilhadas)](img/17_regressao.png)

> **Exemplo resolvido.** \(X = 1, 2, 3, 4, 5\) e \(Y = 2, 4, 5, 4, 5\). Médias: \(\bar{X} = 3\), \(\bar{Y} = 4\). \(\sum (x-\bar{x})(y-\bar{y}) = 6\); \(\sum (x-\bar{x})^2 = 10\); \(\sum (y-\bar{y})^2 = 6\).
> \[ \beta = \frac{6}{10} = 0{,}6 \qquad \alpha = 4 - 0{,}6\times 3 = 2{,}2 \qquad \hat{Y} = 2{,}2 + 0{,}6\,X \qquad R^2 = \frac{6^2}{10\times 6} = 0{,}60 \]
> Interpretação: cada unidade a mais de X aumenta Y em média 0,6; X explica 60% da variância de Y. Previsão para \(X = 6\): \(2{,}2 + 3{,}6 = 5{,}8\), mas isso está **fora** da faixa 1–5 (extrapolação).

O **R²** (também chamado **coeficiente de ajuste, de explicação ou de determinação**) é o **percentual da variância de Y explicado pelas variáveis explicativas**. Varia de 0 a 1 e, **na regressão simples, \(R^2 = r^2\)** (o quadrado da correlação de Pearson).

## 3. F, t e R² não são a mesma coisa

| Medida | Responde | Hipótese | Decisão |
|---|---|---|---|
| **R²** | quanto da variância de Y é explicada? | — | descritivo, não decide se há modelo |
| **Teste F** | o modelo **como um todo** existe? | H0: \(\beta_1 = \ldots = \beta_k = 0\) | **p < 5% → existe modelo** |
| **Teste t** | **cada** parâmetro é significante? | H0: \(\beta_j = 0\); \(t = \hat\beta / EP\) | \(\lvert t\rvert > 1{,}96\) (p < 0,05) → significante |

> **Atenção.** **Quem decide se há modelo é o F, não o R².** Pode haver modelo com R² baixo (baixo poder preditivo). Se o intervalo de confiança de um parâmetro contém o zero, ele não é significante. **Nunca exclua o intercepto \(\alpha\)** só porque não é significante: forçar \(\alpha = 0\) vicia os betas.

## 4. Regressão múltipla

Com várias variáveis: \(Y = \alpha + \beta_1 X_1 + \cdots + \beta_k X_k + u\), ou, em forma matricial, \(b = (X'X)^{-1}X'Y\). Cada beta é o efeito da variável **mantendo as demais constantes** (*ceteris paribus*). Para **comparar modelos com números diferentes de variáveis**, usa-se o **R² ajustado**, que penaliza variáveis inúteis:

\[ R^2_{aj} = 1 - (1 - R^2)\,\frac{n-1}{n-k-1} \]

> **Exemplo.** \(R^2 = 0{,}60\), \(n = 5\), \(k = 1\): \(R^2_{aj} = 1 - 0{,}4\times\frac{4}{3} \approx 0{,}47\).

## 5. Variáveis qualitativas: as dummies (cai sempre)

O erro clássico é a **ponderação arbitrária**: codificar categorias como 1, 2, 3. Isso supõe que o efeito entre categorias é **linear**, o que quase nunca é verdade. A solução é a **dummização**: para n categorias criam-se **n − 1 dummies** (0/1); a categoria omitida é a **referência** (evita multicolinearidade perfeita), e o beta de cada dummy é a diferença média de Y **em relação à referência**. Para **prever**, soma-se \(\alpha\) mais os betas das dummies que valem 1.

> **Exemplo resolvido.** Índice = 40 + 12·Europa − 6·África (referência: Ásia). Ásia = **40**; Europa = 40 + 12 = **52**; África = 40 − 6 = **34**.

## 6. Pressupostos e diagnósticos

| Diagnóstico | O que verifica | Teste e decisão |
|---|---|---|
| **Normalidade dos resíduos** | base da inferência e dos IC | **Shapiro-Francia**; H0: normais; queremos **p > 0,05** (não rejeitar) |
| **Multicolinearidade** | alta correlação entre as explicativas | **VIF = 1/Tolerance**, com Tolerance = \(1 - R^2_{aux}\); **VIF > 10** é alerta |
| **Heterocedasticidade** | variância dos erros **não constante** (cone no gráfico) | **Breusch-Pagan**; H0: homocedasticidade; **p < 0,05 → problema** |

**Se os resíduos não são normais**, a forma funcional é inadequada. Uma saída é a **transformação de Box-Cox**, \(Y^* = (Y^\lambda - 1)/\lambda\), em que se escolhe o \(\lambda\) que melhor aproxima a normalidade: \(\lambda = 1\) é linear, 2 quadrática, 0,5 raiz, −1 inversa e **\(\lambda = 0\) equivale a \(\ln Y\)**. Os betas do modelo transformado **não são comparáveis** com os do linear, porque a métrica de Y mudou.

**O procedimento stepwise** remove passo a passo as variáveis **não significantes** e ajuda na multicolinearidade, mas **não corrige** heterocedasticidade nem forma funcional. A **multicolinearidade** causa sinais invertidos e **t baixo com F significante e R² alto**; as saídas são o stepwise, remover a variável ou usar **PCA** (capítulo 15). A **heterocedasticidade** costuma vir de **variável relevante omitida** e se mitiga incluindo preditores ou usando modelos multinível.

> **Exemplo (VIF).** A regressão auxiliar de \(X_2\) nas demais dá \(R^2 = 0{,}90\) → Tolerance = 0,10 → \(VIF = 10\): colinearidade problemática.

**Roteiro da aula:** explorar correlações → estimar OLS (com dummies) → stepwise a 95% → Shapiro-Francia dos resíduos → se não normal, Box-Cox em Y e repetir → VIF e Breusch-Pagan → prever dentro da faixa de X.

## O que levar daqui

O OLS minimiza a soma dos resíduos ao quadrado. R² mede a variância explicada (na simples, \(R^2 = r^2\)); o F decide se há modelo; o t avalia cada variável; o R² ajustado compara modelos. Categorias viram n − 1 dummies, e o beta é a diferença à referência. Diagnósticos: Shapiro-Francia (p > 0,05), VIF < 10, Breusch-Pagan (p > 0,05).

## Erros que todo mundo comete

| Erro | Correção |
|---|---|
| "R² baixo = não há modelo" | quem decide é o **F** |
| "No Shapiro-Francia queremos p < 0,05" | queremos **p > 0,05** (normalidade) |
| "Breusch-Pagan com p > 0,05 indica problema" | p **< 0,05** = heterocedasticidade |
| "Para n categorias, n dummies" | **n − 1** (uma é a referência) |
| Codificar categorias como 1, 2, 3 | ponderação arbitrária: use dummies |
| "Excluir o intercepto se não for significante" | **não exclua** |
| "Os betas do Box-Cox são comparáveis" | a métrica de Y mudou: **não comparáveis** |
| "O stepwise resolve a heterocedasticidade" | só variáveis não significantes e multicolinearidade |

## Teste-se

1. A correlação entre X e Y é 0,5. Qual o R² da regressão simples?
<details markdown="1"><summary>Ver resposta</summary>R² = 0,5² = 0,25 (25%).</details>

2. O F é significativo e o R² é 0,08. Existe modelo?
<details markdown="1"><summary>Ver resposta</summary>Sim, existe modelo (ao menos uma variável explica Y), mas com baixa capacidade preditiva.</details>

3. Uma variável qualitativa tem 5 categorias. Quantas dummies?
<details markdown="1"><summary>Ver resposta</summary>4; a quinta é a referência.</details>

4. O que se espera do Shapiro-Francia dos resíduos?
<details markdown="1"><summary>Ver resposta</summary>Não rejeitar H0 (p > 0,05): resíduos normais.</details>

5. Cite duas consequências da multicolinearidade.
<details markdown="1"><summary>Ver resposta</summary>Sinais invertidos ou instáveis nos betas, e t baixo com F significante e R² alto (erros de predição).</details>

## Pergunta típica
Nomes do R² e o que mede · diferença entre F, t e R² (há modelo ≠ R² alto) · hipóteses do F e do t · por que usar o R² ajustado · n−1 dummies e por que não usar pesos 1, 2, 3 · calcular valor previsto com dummies · R² na simples = r² · o que testa o Shapiro-Francia e qual resultado se espera · Box-Cox (λ = 0 → ln) · stepwise · multicolinearidade (VIF/Tolerance) · heterocedasticidade (causas, Breusch-Pagan) · por que não excluir o intercepto
