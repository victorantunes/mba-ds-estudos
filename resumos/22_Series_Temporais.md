# 22 · Séries Temporais (I, II, III + Aula Extra de Exercícios)
**Prof. Fabiano Guasti Lima · 3 aulas + extra · Prioridade: alta (muitos conceitos curtos e fórmulas)**
*Referência do professor: Hyndman, "Forecasting: Principles and Practice" (otexts.com/fpp3).*

## O fio condutor deste capítulo

Em dados de vendas mensais, o valor de hoje **depende do que aconteceu antes**: por isso não se podem embaralhar as linhas nem tratar as observações como independentes. A estratégia é **decompor** a série (o que é nível ou tendência, o que se repete todo ano, o que é puro acaso) e usar esses padrões para **prever**. Métodos simples (repetir o último valor, tirar a média) servem de **linha de base**: um modelo sofisticado só vale se **os vencer**.

O capítulo percorre esse caminho: primeiro *o que é* uma série e seus **componentes**; depois os **métodos simples** e a **suavização exponencial**; em seguida como **medir o erro** das previsões; e, por fim, a **estacionariedade** e os modelos **ARIMA**, que exigem que a série seja "estável".

```mermaid
flowchart LR
  A["Série temporal"] --> B["Decompor: T, S, C, E"]
  B --> C["Métodos simples e suavização exponencial"]
  C --> D["Medir o erro: MAE, RMSE, MAPE"]
  D --> E["Estacionariedade: teste ADF, log e diferença"]
  E --> F["ARIMA: p, d, q via ACF e PACF"]
  F --> G["Resíduos: ruído branco?"]
```

## 1. O que é uma série temporal

É um conjunto de observações **\(X_t\) ordenadas no tempo** (t = 1…n) e **igualmente espaçadas**; **a ordem importa**, e o desejável é ter **n ≥ 50**. Seus ingredientes são a medida, a unidade de tempo e a fonte. Pode ser **univariada** ou **multivariada**, **determinística** (fórmula exata) ou **estocástica** (probabilística). Os objetivos são prever, entender o mecanismo gerador, descrever e achar periodicidades; e **previsões mais longas são menos confiáveis**, porque o erro se propaga e o intervalo de confiança se abre.

## 2. Componentes e decomposição

| Componente | O que é |
|---|---|
| **Tendência (T)** | direção de longo prazo |
| **Sazonalidade (S)** | padrão que se repete em **período fixo** (mês, semana) |
| **Ciclo (C)** | ondas longas **sem período fixo** |
| **Erro (E)** | o que sobra, imprevisível |

![Decomposição aditiva: série = tendência + sazonalidade + erro](img/22_decomposicao.png)

A decomposição pode ser **aditiva**, \(Y = T + C + S + E\), quando a sazonalidade tem **tamanho constante**, ou **multiplicativa**, \(Y = T\times C\times S\times E\), quando a sazonalidade **cresce com o nível** da série. No multiplicativo, os índices sazonais somam o número de períodos.

## 3. Métodos simples e suavização exponencial

As **linhas de base** são o **naive** (último valor), o **naive sazonal** (valor do mesmo período do ano anterior), a **média** e o **drift** (reta do primeiro ao último ponto). A **média móvel** faz a média dos vizinhos em uma janela: janela pequena segue a série; grande suaviza.

> **Exemplo.** Valores 10, 12, 14 e 16. A média móvel de 3 períodos no final é \(\frac{12 + 14 + 16}{3} = 14\).

A **suavização exponencial** dá **peso maior às observações recentes**, que decai exponencialmente. A escolha do método depende dos componentes presentes:

| Método | Quando | Parâmetros |
|---|---|---|
| **SES** (simples) | sem tendência e sem sazonalidade | **α** (0 a 1) |
| **Holt** | com **tendência** | α e **β** |
| **Holt-Winters** | com **tendência e sazonalidade** (aditivo ou multiplicativo) | α, β e **γ** |
| **ETS** | escolhe automaticamente: **A** (aditivo), **M** (multiplicativo), **N** (nenhum), **Ad** (tendência amortecida) | — |

Um α alto reage rápido; um α baixo suaviza. Para a SES, o nível é atualizado por \(L_t = \alpha X_t + (1-\alpha)L_{t-1}\), e os parâmetros são escolhidos **minimizando um erro** (por exemplo, o MSE).

> **Exemplo resolvido (SES).** \(\alpha = 0{,}3\) e \(L_0 = 100\). \(X_1 = 110\): \(L_1 = 0{,}3\cdot110 + 0{,}7\cdot100 = 103\). \(X_2 = 120\): \(L_2 = 0{,}3\cdot120 + 0{,}7\cdot103 = 36 + 72{,}1 = 108{,}1\). A previsão para os próximos períodos é **108,1**.

## 4. Medindo o erro (erro = real − previsto)

| Medida | Fórmula/ideia | Observação |
|---|---|---|
| **ME** | média dos erros | positivos e negativos **se anulam**: enganosa |
| **MAE** | média dos erros absolutos | na unidade original |
| **MSE** | média dos erros ao quadrado | penaliza erros grandes |
| **RMSE** | \(\sqrt{MSE}\) | na unidade original |
| **MAPE** | erro percentual absoluto médio | **sem unidade**; explode com valores perto de zero |
| **Theil's U** | ajuste da previsão | **menor é melhor, zero é ideal** |

Em todas, **menor é melhor**. Um bom modelo deixa **resíduos que são ruído branco**: média zero, variância constante e **sem autocorrelação**. Os testes são o **Ljung-Box** (H0: sem autocorrelação; queremos **p > 0,05**), o Breusch-Pagan/ARCH (homocedasticidade) e o Jarque-Bera (normalidade).

> **Exemplo resolvido.** Reais: 100 e 110; previstos: 90 e 120; erros: +10 e −10. **ME = 0** (enganoso!), **MAE = 10**, **MSE = 100**, **RMSE = 10**, **MAPE** = \(\frac{10/100 + 10/110}{2} \approx 9{,}5\%\).

## 5. Estacionariedade

Uma série é **estacionária** quando **média e variância são constantes** no tempo e a covariância depende apenas da defasagem. O ARIMA exige isso, e a causa mais comum de não estacionariedade é a **tendência**.

| Teste | H0 | Decisão |
|---|---|---|
| **ADF** (Dickey-Fuller aumentado) | a série **não** é estacionária (raiz unitária) | **p ≤ 0,05 → estacionária**; p > 0,05 → transformar |
| **KPSS** | a série **é** estacionária | hipóteses **invertidas** em relação ao ADF |

Quando a série não é estacionária, aplica-se o **log** (estabiliza a **variância**; transforma sazonalidade multiplicativa em aditiva) e/ou a **diferenciação** (subtrai o valor anterior; remove a **tendência**, \(d = 1\)) e testa-se de novo.

## 6. ARIMA (Box-Jenkins)

O **ARIMA(p, d, q)** combina três ideias: **p** termos **autorregressivos (AR)**, em que o valor depende de valores passados; **d** **diferenças** (a integração); **q** termos de **média móvel (MA)**, em que o valor depende de erros passados. **Como escolher:** o **p vem da PACF**, o **q vem da ACF** e o **d vem dos testes de estacionariedade**.

| Modelo | ACF | PACF |
|---|---|---|
| **AR(p)** | decai gradualmente | **corta no lag p** |
| **MA(q)** | **corta no lag q** | decai gradualmente |
| **ARMA** | decai | decai |

![Padrões de ACF e PACF para AR(1) e MA(1)](img/22_acf_pacf.png)

As etapas de **Box-Jenkins** são: identificação (ACF/PACF) → estimação → checagem dos resíduos (ruído branco); se falhar, recomeça. A **seleção** entre modelos usa **AIC/BIC** (menor é melhor). O **SARIMA(p,d,q)(P,D,Q)\(_s\)** acrescenta termos sazonais (s = 12 para dados mensais). Outros temas citados: causalidade de Granger, modelos de volatilidade (ARCH/GARCH) e cenários (otimista, pessimista, provável).

> **Exemplo de leitura.** Correlograma com PACF cortando após o lag 2 e ACF decaindo gradualmente sugere **AR(2)**. Se a ACF decai muito lentamente por muitos lags, a série provavelmente **não é estacionária**: diferencie antes.

## O que levar daqui

Uma série tem tendência, sazonalidade, ciclo e erro (aditivo ou multiplicativo). Compare qualquer modelo com os métodos simples. SES, Holt e Holt-Winters adicionam parâmetros α, β e γ. Avalie com MAE, RMSE e MAPE; o resíduo deve ser ruído branco. ADF: p ≤ 0,05 → estacionária. ARIMA: p → PACF, q → ACF, d → diferenças.

## Erros que todo mundo comete

| Erro | Correção |
|---|---|
| "No ADF queremos não rejeitar H0" | queremos **rejeitar** H0 (estacionária) |
| ADF e KPSS têm a mesma H0 | as hipóteses são **invertidas** |
| "ME baixo = modelo bom" | os erros se anulam; olhe **MAE/RMSE/MAPE** |
| Aditivo × multiplicativo | sazonalidade **constante** × que **cresce com o nível** |
| "O p vem da ACF" | **p → PACF; q → ACF** |
| "Diferenciar remove a sazonalidade" | remove a **tendência**; a sazonal pede diferença sazonal (D) |
| "Ljung-Box com p < 0,05 é bom" | queremos **p > 0,05** |

## Teste-se

1. Qual a H0 do teste ADF e o que fazer se p = 0,40?
<details markdown="1"><summary>Ver resposta</summary>H0: a série não é estacionária. Com p = 0,40 não rejeita: aplique log e/ou diferenciação e teste novamente.</details>

2. Como escolher p e q em um ARIMA?
<details markdown="1"><summary>Ver resposta</summary>p pela PACF (corta no lag p em um AR) e q pela ACF (corta no lag q em um MA); d pelos testes de estacionariedade.</details>

3. Quando usar modelo multiplicativo?
<details markdown="1"><summary>Ver resposta</summary>Quando a amplitude da sazonalidade cresce junto com o nível da série.</details>

4. Reais 100 e 110; previstos 90 e 120. Quanto vale o MAE?
<details markdown="1"><summary>Ver resposta</summary>Erros absolutos 10 e 10 → MAE = 10.</details>

5. O que deve acontecer com os resíduos de um bom modelo?
<details markdown="1"><summary>Ver resposta</summary>Ser ruído branco: média zero, variância constante e sem autocorrelação (Ljung-Box com p > 0,05).</details>

## Pergunta típica
Componentes e diferença aditivo × multiplicativo · qual método de suavização para cada caso (SES, Holt, HW) e o papel de α/β/γ · definir ME, MAE, RMSE, MAPE e interpretar Theil · H0 do ADF × KPSS · como estacionarizar (log e diferença) · o que significam p, d, q e qual gráfico define p e q · padrões de ACF/PACF para AR e MA · critério AIC/BIC · o que deve ocorrer com os resíduos · por que previsões longas perdem confiabilidade
