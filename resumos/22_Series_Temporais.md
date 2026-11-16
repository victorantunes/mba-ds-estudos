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

### Exemplo completo (da aula): decomposição de uma série trimestral

A aula usa uma série de **16 trimestres** (do 1º trimestre de 2019 ao 4º de 2022):

| | 2019 | 2020 | 2021 | 2022 |
|---|---|---|---|---|
| **1º tri** | 10 | 16 | 15 | 28 |
| **2º tri** | 14 | 22 | 27 | 40 |
| **3º tri** | 8 | 14 | 18 | 25 |
| **4º tri** | 25 | 35 | 40 | 65 |

O 4º trimestre é sempre o mais alto e o 3º o mais baixo: há **sazonalidade** (período de 4). Também há **tendência de alta**. Vamos separar os componentes pelo modelo **aditivo**, \(Y = T + S + E\).

**Passo 1: tendência (média móvel centrada de 4 períodos).** Como o período é par, usa-se uma média móvel **centrada**, com peso 1/2 nas pontas. Para o **3º tri de 2019**:

\[ T = \frac{0{,}5\cdot 10 + 14 + 8 + 25 + 0{,}5\cdot 16}{4} = \frac{60}{4} = 15{,}0 \]

Repetindo para os demais trimestres: 16,75; 18,5; 20,5; 21,6; 22,1; 23,3; 24,4; 26,6; 29,9; 32,4; 36,4 (os dois primeiros e os dois últimos não têm tendência calculada, pela falta de vizinhos).

**Passo 2: o que sobra** \(Y - T\) (sazonalidade + erro). Para o 3º tri de 2019: \(8 - 15 = -7\). Para cada trimestre, tira-se a média das sobras de todos os anos:

| Trimestre | Sobras \(Y - T\) | Média |
|---|---|---|
| 1º | −2,50; −8,25; −4,38 | −5,04 |
| 2º | 1,50; 2,63; 3,63 | 2,58 |
| 3º | −7,00; −7,63; −8,63 | −7,75 |
| 4º | 8,25; 12,88; 10,13 | 10,42 |

**Passo 3: centrar os índices** para somarem zero. A soma das médias é 0,21, então subtrai-se \(0{,}21/4 = 0{,}05\) de cada uma. **Índices sazonais finais:** **1º tri = −5,09; 2º = +2,53; 3º = −7,80; 4º = +10,36.**

**Interpretação.** Em média, o 4º trimestre fica **10,4 acima** da tendência e o 3º **7,8 abaixo**. O **erro** é o que resta: \(E = Y - T - S\). No 3º tri de 2019: \(E = 8 - 15 - (-7{,}80) = +0{,}80\). Os erros ficam entre −3,2 e +2,6, pequenos perto da amplitude da série.

**Aditivo × multiplicativo.** No modelo **multiplicativo** (\(Y = T\times S\times E\)), os índices são **razões**: 1º tri = 0,80; 2º = 1,10; 3º = 0,62; 4º = 1,48. Ele é mais adequado quando a **amplitude sazonal cresce com o nível** da série, como aqui (o 4º tri pula de 25 para 65).

A decomposição pode ser **aditiva**, \(Y = T + C + S + E\), quando a sazonalidade tem **tamanho constante**, ou **multiplicativa**, \(Y = T\times C\times S\times E\), quando a sazonalidade **cresce com o nível** da série. No multiplicativo, os índices sazonais somam o número de períodos.

## 3. Métodos simples e suavização exponencial

As **linhas de base** são o **naive** (último valor), o **naive sazonal** (valor do mesmo período do ano anterior), a **média** e o **drift** (reta do primeiro ao último ponto). A **média móvel** faz a média dos vizinhos em uma janela: janela pequena segue a série; grande suaviza.

> **Exemplo (média móvel).** Na série da aula `[3, 5, 9, 20, 12, 17, 22, 23, 51, 41, 56, 75, 60, 75, 88]` (15 períodos), a média móvel de **3 períodos** ao final é \(\frac{60 + 75 + 88}{3} = 74{,}3\). Repare que o último valor foi 88: a média móvel **fica para trás** quando há tendência de alta, porque dá o mesmo peso a valores velhos.


A **suavização exponencial** dá **peso maior às observações recentes**, que decai exponencialmente. A escolha do método depende dos componentes presentes:

| Método | Quando | Parâmetros |
|---|---|---|
| **SES** (simples) | sem tendência e sem sazonalidade | **α** (0 a 1) |
| **Holt** | com **tendência** | α e **β** |
| **Holt-Winters** | com **tendência e sazonalidade** (aditivo ou multiplicativo) | α, β e **γ** |
| **ETS** | escolhe automaticamente: **A** (aditivo), **M** (multiplicativo), **N** (nenhum), **Ad** (tendência amortecida) | — |

Um α alto reage rápido; um α baixo suaviza. Para a SES, o nível é atualizado por \(L_t = \alpha X_t + (1-\alpha)L_{t-1}\), e os parâmetros são escolhidos **minimizando um erro** (por exemplo, o MSE).

### Exemplo completo (da aula): suavização exponencial na série `[3, 5, 9, …, 88]`

A série da aula tem **15 valores** com forte tendência de alta: 3, 5, 9, 20, 12, 17, 22, 23, 51, 41, 56, 75, 60, 75, 88. A suavização exponencial simples (**SES**) atualiza um **nível** \(L_t = \alpha X_t + (1-\alpha)L_{t-1}\). Com \(\alpha = 0{,}3\) e partindo de \(L_1 = X_1 = 3\):

| t | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| \(X_t\) | 3 | 5 | 9 | 20 | 12 | 17 | 22 | 23 |
| \(L_t\) | 3,00 | 3,60 | 5,22 | 9,65 | 10,36 | 12,35 | 15,25 | 17,57 |

| t | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|
| \(X_t\) | 51 | 41 | 56 | 75 | 60 | 75 | 88 |
| \(L_t\) | 27,60 | 31,62 | 38,93 | 49,75 | 52,83 | 59,48 | **68,04** |

Por exemplo, \(L_2 = 0{,}3\times 5 + 0{,}7\times 3 = 3{,}6\) e \(L_3 = 0{,}3\times 9 + 0{,}7\times 3{,}6 = 5{,}22\). A previsão do SES para **qualquer período futuro** é o último nível: **68,04**.

**O problema.** O último valor real foi **88**, mas o SES prevê 68. Com \(\alpha = 0{,}3\) o nível **demora a subir**; mesmo se o \(\alpha\) for otimizado pelo software (\(\alpha \approx 0{,}84\), que dá a previsão plana de ≈ **85,6**), a previsão continua **horizontal**, enquanto a série claramente sobe. **O SES não captura tendência.** O **modelo de Holt** acrescenta um segundo componente, a **tendência**, e suas previsões acompanham a subida: para os 3 períodos seguintes, ≈ **85,7; 91,7; 97,8** (+6,1 por período; valores com parâmetros otimizados pelo `statsmodels`, que podem variar um pouco entre versões).

**Com sazonalidade: Holt-Winters.** Para a série trimestral da seção de decomposição (16 trimestres, com tendência e sazonalidade crescente), ajustam-se as duas versões. Os erros dentro da amostra:

| Modelo | MAE | RMSE | MAPE | Previsão dos 4 próximos trimestres |
|---|---|---|---|---|
| Holt-Winters **aditivo** | 3,70 | 4,69 | 17,1% | 44,1; 55,3; 48,2; 75,5 |
| Holt-Winters **multiplicativo** | **1,97** | **2,39** | **10,3%** | 37,2; 55,9; 34,1; 86,1 |

O **multiplicativo ajusta bem melhor** (todos os erros caem quase pela metade), pelo mesmo motivo visto na decomposição: a amplitude sazonal cresce junto com o nível. (Os parâmetros ajustados e as previsões podem variar um pouco conforme a versão do pacote `statsmodels`.)


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

> **Exemplo completo: os erros do Holt-Winters multiplicativo na série trimestral.** Erro = real − previsto (ajustado).
>
> | Trimestre | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
> |---|---|---|---|---|---|---|---|---|
> | Real | 10 | 14 | 8 | 25 | 16 | 22 | 14 | 35 |
> | Ajustado | 8,88 | 15,81 | 9,77 | 23,27 | 14,19 | 23,42 | 14,10 | 36,06 |
> | Erro | +1,12 | −1,81 | −1,77 | +1,73 | +1,81 | −1,42 | −0,10 | −1,06 |
>
> | Trimestre | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
> |---|---|---|---|---|---|---|---|---|
> | Real | 15 | 27 | 18 | 40 | 28 | 40 | 25 | 65 |
> | Ajustado | 20,33 | 25,07 | 15,12 | 41,44 | 22,87 | 38,46 | 24,23 | 63,36 |
> | Erro | −5,33 | +1,93 | +2,88 | −1,44 | +5,13 | +1,54 | +0,77 | +1,64 |
>
> Somando as 16 observações: **ME** (erro médio) = **+0,35** (enganoso: erros positivos e negativos se compensam); **MAE** (erro absoluto médio) = **1,97**; **MSE** (erro quadrático médio) = **5,73**; **RMSE** = \(\sqrt{5{,}73} = \) **2,39** (na mesma unidade da série, e pune mais os erros grandes, como o −5,33 e o +5,13); **MAPE** (erro percentual absoluto médio) = **10,3%**. O MAPE permite comparar séries de escalas diferentes.


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

![ACF e PACF das séries simuladas na aula: AR(1) com φ = 0,8 e MA(1) com θ = −0,3](img/22_acf_pacf.png)

As etapas de **Box-Jenkins** são: identificação (ACF/PACF) → estimação → checagem dos resíduos (ruído branco); se falhar, recomeça. A **seleção** entre modelos usa **AIC/BIC** (menor é melhor). O **SARIMA(p,d,q)(P,D,Q)\(_s\)** acrescenta termos sazonais (s = 12 para dados mensais). Outros temas citados: causalidade de Granger, modelos de volatilidade (ARCH/GARCH) e cenários (otimista, pessimista, provável).

> **Exemplo (da aula): lendo ACF e PACF em séries simuladas.** A aula simula 500 pontos de um **AR(1) com φ = 0,8** e de um **MA(1) com θ = −0,3** e olha os correlogramas. No **AR(1)**, a **ACF decai gradualmente** (0,78; 0,61; 0,47; 0,35; 0,29; 0,22 nos lags 1 a 6, aproximadamente \(0{,}8^k\)) e a **PACF corta depois do lag 1** (0,78; depois valores em torno de zero). No **MA(1)**, é o contrário: a **ACF corta depois do lag 1** (−0,28; depois ≈ 0) e a **PACF decai**. Regra: **PACF corta após o lag p → AR(p); ACF corta após o lag q → MA(q).**
>
> Se a ACF decai muito lentamente por muitos lags, a série provavelmente **não é estacionária**: diferencie antes. Um exemplo com a série real de passageiros aéreos (144 meses): o **teste de Dickey-Fuller aumentado (ADF)**, com H0 de raiz unitária (não estacionária), dá **p = 0,99** para a série original (não rejeita H0: **não estacionária**) e **p = 0,054** após **uma diferenciação** (já bem próximo de 0,05); por isso se diferencia, aqui possivelmente também com a parte sazonal.


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
