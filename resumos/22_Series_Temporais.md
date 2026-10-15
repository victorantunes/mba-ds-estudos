# 22 · Séries Temporais (I, II, III + Aula Extra de Exercícios)
**Prof. Fabiano Guasti Lima · 3 aulas + extra · Prioridade: ALTA (muitos conceitos curtos e fórmulas; cai bastante)**
*Referência: Hyndman, "Forecasting: Principles and Practice" (otexts.com/fpp3).*

## 1. O que é uma série temporal
- **Conjunto de observações ordenadas no tempo**: X_t, t = 1..n; **a ordem importa** (cada valor depende do que veio antes) e o **espaçamento é regular** (diário, mensal…). **n ≥ 50 = "sucessão cronológica".** Três ingredientes: **medida** (o quê) · **unidade de tempo** (quando) · **fato/fonte**. Exemplos: IBOVESPA diário, inflação mensal, câmbio, passageiros por mês.
- **Univariada** (uma variável × tempo) × **multivariada** (duas ou mais). **Discreta** (observações em intervalos fixos) × **contínua**. **Determinística** (função matemática exata) × **estocástica** (valores futuros só em termos probabilísticos: modelo com termo aleatório).
- **Objetivos:** (1) **prever** valores futuros; (2) investigar o **mecanismo gerador**; (3) **descrever** o comportamento da série; (4) procurar **periodicidades**. Previsões longas → **o erro se propaga** (intervalo de confiança se abre); com série curta, prever passo a passo.
- Limpeza: dados faltantes, erros de medida, acumulados (pandemia).

## 2. Componentes
- **Tendência (T)**: direção de longo prazo (crescente/decrescente). **Sazonalidade (S)**: padrão que se repete em **período fixo** (dia, semana, mês). **Ciclo (C)**: ondas longas, **sem período fixo** (ciclos econômicos). **Aleatório/erro (E)**: o resto imprevisível.
- **Modelo aditivo: Y = T + C + S + E** (sazonalidade de **mesmo tamanho** ao longo do tempo). **Multiplicativo: Y = T × C × S × E** (sazonalidade **cresce com o nível**). No multiplicativo, os índices sazonais somam o nº de períodos (ex.: 4 trimestres somam 4).
- **Decomposição:** estimar a tendência (média móvel; com janela **ímpar** já fica centrada), remover T (Y − T ou Y / T) → S + E; calcular a sazonalidade média por período; o que sobra = ciclo + erro.
- **Diagnóstico visual primeiro:** sobe/desce → tendência; repete padrão em período fixo → sazonalidade; oscila em torno de média fixa → estacionária.

## 3. Métodos simples (baselines — qualquer modelo mais sofisticado precisa vencê-los)
- **Naive:** último valor. **Naive sazonal:** último valor do mesmo período sazonal. **Média:** média histórica. **Drift:** reta do primeiro ao último ponto (acompanha a tendência).
- **Média móvel:** média dos vizinhos numa janela n (remove ruído); janela pequena segue de perto, grande suaviza; o melhor n minimiza o erro nas previsões passadas.

## 4. Suavização exponencial (SES, Holt, Holt-Winters) e ETS
| Modelo | Quando | Ideia |
|---|---|---|
| **SES** (simples) | sem tendência e sem sazonalidade ("andando de lado") | peso maior nas observações recentes, **decaindo exponencialmente**; **α entre 0 e 1** (α alto reage rápido; baixo = previsão suave); previsão = último valor suavizado (linha reta) |
| **Holt (SEH)** | **tendência** linear, sem sazonalidade | acrescenta o parâmetro **β** (tendência) |
| **Holt-Winters** | **tendência + sazonalidade** (período c) | parâmetros **α, β, γ** (nível, tendência, sazonal); **aditivo** (sazonal constante) ou **multiplicativo** (sazonal cresce) |
- Fórmulas (aditivo): X̂t = L̂t−1 + T̂t−1 + Ŝt−c; Lt = α(Xt − St−c) + (1−α)(Lt−1 + Tt−1); Tt = β(Lt − Lt−1) + (1−β)Tt−1; St = γ(Xt − Lt−1) + (1−γ)St−c. Previsão h passos: Lt + h·Tt + St+h−c. Intervalo: X̂t(h) ± Zα/2·SE(h) (cresce com h). (Multiplicativo: usa produto e divisão.)
- **ETS (Error, Trend, Seasonal):** escolhe automaticamente o melhor modelo; códigos **A** (aditivo), **M** (multiplicativo), **N**/Z (nenhum/automático); tendência **Ad / Md** = amortecida; ex.: "AAA". Se não há tendência/sazonalidade, β e γ são zero.
- Os parâmetros (α, β, γ) são escolhidos **minimizando uma medida de erro** (ex.: MSE) — no Excel, com o Solver variando α.

## 5. Estatísticas de erro de previsão (erro = real − previsto)
**ME** (erro médio; positivos e negativos se anulam) · **MAE** (média do valor absoluto; na unidade original) · **MSE** (média dos quadrados) · **RMSE** (raiz do MSE; penaliza erros grandes) · **MPE** (erro percentual médio) · **MAPE** (erro percentual absoluto médio; **sem unidade**, bom para comparar séries) · **Theil's U / TIC** (grau de ajuste da previsão; **quanto menor melhor, zero é ideal**; "quase um R² invertido") · **ACF1** (autocorrelação de 1ª ordem dos resíduos). **Em todas: quanto menor, melhor** (mesma base de comparação). MAPE explode quando há valores próximos de zero (use MAE).
- **Resíduos de um bom modelo:** **ruído branco** = **média zero, variância constante e sem autocorrelação** (se o erro de hoje prevê o de amanhã, o modelo não extraiu toda a estrutura). Testes: **Ljung-Box** (H0: sem autocorrelação nos resíduos; **p > 0,05 desejável**), **Breusch-Pagan/ARCH** (H0: homocedasticidade), **Jarque-Bera** (H0: normalidade; JB ~ χ²(2); assimetria 0 e curtose 3 na normal).

## 6. Estacionariedade
- **Estacionária:** **média e variância constantes** no tempo e covariância dependendo só da defasagem. A maioria dos modelos (ARIMA) exige. Tendência é a causa mais comum de não estacionariedade.
- **Teste ADF (Dickey-Fuller Aumentado):** **H0: a série NÃO é estacionária (tem raiz unitária)**; **p ≤ 0,05 → estacionária**; **p > 0,05 → não estacionária** → aplicar **log** e/ou **diferenciação** e testar de novo. **KPSS** tem a hipótese invertida: **H0: a série é estacionária** (H1: possui raiz unitária). **Phillips-Perron (PP)**: H0 raiz unitária.
- **Log** estabiliza a **variância** (transforma sazonalidade multiplicativa em aditiva); **diferenciação** (subtrair o valor anterior) **remove a tendência**; d = 1 (primeira ordem), d = 2 (rara). Sazonal: diferenciação sazonal (D).

## 7. ARIMA (Box-Jenkins)
- **ARIMA(p, d, q):** **p** = ordem **autorregressiva (AR)** (valor depende de p valores passados); **d** = grau de **diferenciação (I, integrado)**; **q** = ordem da **média móvel (MA)** (depende dos **erros/choques** passados). AR(1)=ARIMA(1,0,0); MA(1)=ARIMA(0,0,1); ARMA(1,1)=ARIMA(1,0,1). Ex.: Xt = 0,8·Xt−1 + εt.
- **Como definir p, d, q:** **p → PACF**, **q → ACF**, **d → testes de estacionariedade**. **Padrões:** **AR(p): ACF decai exponencialmente/senoide amortecida; PACF corta (significativa até o lag p)**. **MA(q): ACF corta no lag q; PACF decai**. **ARMA: ambas decaem.**
- **Autocorrelação (FAC/ACF):** correlação entre observações defasadas k períodos (−1 a 1); **correlograma** = gráfico FAC × k (1ª autocorrelação = 1). **FACP/PACF:** autocorrelação "parcial" (retira o efeito dos lags intermediários). Série não estacionária: **ACF decai lentamente**.
- **Etapas Box-Jenkins:** **Identificação** (ACF/PACF) → **Estimação** → **Checagem dos resíduos (ruído branco)**; se não for, recomeça.
- **Seleção de modelo:** **AIC** (informação perdida; **menor = melhor**) e **BIC** (menor = melhor ajuste).
- **SARIMA(p,d,q)(P,D,Q)s:** acrescenta termos **sazonais** com ciclo s (ex.: s = 12 para mensal), P/Q = AR/MA sazonais, D = diferenças sazonais. Ex.: SARIMA(1,0,2)(0,1,1)12.
- Outros citados: **teste de causalidade de Granger** (se X passa, não pôr em MQO/XGBoost como se fosse exógena sem cuidado), modelos de **volatilidade (ARCH/GARCH)**, **redes neurais** e cenários (otimista, pessimista, provável) para orçamento.

## Pergunta típica
Componentes e diferença aditivo × multiplicativo · qual método de suavização para cada caso (SES, Holt, HW) e o papel de α/β/γ · definir ME, MAE, RMSE, MAPE e interpretar Theil · H0 do ADF × KPSS · como estacionarizar (log e diferença) · o que significam p, d, q e qual gráfico determina p e q · padrões de ACF/PACF para AR e MA · critério AIC/BIC · o que deve ocorrer com os resíduos (ruído branco, Ljung-Box) · por que previsões longas perdem confiabilidade.
