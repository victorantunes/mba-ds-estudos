# 10 · Analytics e Gestão de Riscos
**Prof. Fabiano Guasti Lima · 2 aulas · Prioridade: alta (tem cálculo: treine as fórmulas)**
*Referências do professor: Fávero & Belfiore (Manual de análise de dados); Lima (Análise de Riscos).*

## O fio condutor deste capítulo

Dois investimentos podem ter o mesmo retorno médio e oscilar de formas muito diferentes; o mais volátil é o mais arriscado. **Risco é a incerteza sobre resultados**, e a gestão de riscos faz três coisas: **mede** essa incerteza (desvio padrão, perda esperada, VaR), **reduz** o que dá para reduzir (diversificação, capital) e **decide** com base nos números.

O capítulo avança do mais simples ao mais complexo: o risco de **um ativo**; o risco de **uma carteira** (por que combinar ativos reduz risco); o **risco de crédito** (perder porque o cliente não paga); a **regulação bancária** (Basileia, que exige capital proporcional ao risco); o **risco operacional**; e, por fim, o risco em **projetos** (fluxo de caixa, sensibilidade e Monte Carlo).

```mermaid
flowchart LR
  A["Risco de um ativo: desvio padrão dos retornos"] --> B["Carteira: correlação reduz o risco"]
  B --> C["Crédito: PD x EC x LGD"]
  C --> D["Basileia: capital sobre APR"]
  D --> E["Operacional: frequência x severidade"]
  E --> F["Projetos: VPL, sensibilidade, Monte Carlo"]
```

## 1. Retorno e risco de um ativo

O **retorno** de um período pode ser **discreto** ou **contínuo** (logarítmico):

\[ R_t = \frac{P_t}{P_{t-1}} - 1 \qquad\qquad R_t = \ln\left(\frac{P_t}{P_{t-1}}\right) \]

O primeiro período não tem retorno, pois falta o preço anterior. O **risco** é a **volatilidade**, medida pelo **desvio padrão dos retornos** (e não dos preços). O **coeficiente de variação** (desvio ÷ média) expressa o risco por unidade de retorno.

### Exemplo completo (da aula): PETR4, VALE3 e EMBR3

A aula usa as **cotações de fechamento** de **PETR4, VALE3 e EMBR3** (84 pregões, de 26/05/2025 a 19/09/2025, arquivo `COTACOES.xlsx`). As primeiras duas linhas são:

| Data | PETR4 | VALE3 | EMBR3 |
|---|---|---|---|
| 26/05/2025 | 29,710381 | 52,179024 | 67,000000 |
| 27/05/2025 | 29,928699 | 52,014786 | 68,400002 |

**Retorno de um dia (PETR4).** De 29,710381 para 29,928699:

\[ \text{discreto} = \frac{29{,}928699}{29{,}710381} - 1 = 0{,}007348 = 0{,}735\% \qquad \text{contínuo} = \ln\frac{29{,}928699}{29{,}710381} = 0{,}007321 = 0{,}732\% \]

Para retornos pequenos os dois são quase iguais (0,735% × 0,732%). O retorno **contínuo (log)** tem a vantagem de ser **aditivo no tempo**: o retorno de uma semana é a soma dos retornos diários. A aula usa o retorno discreto (`pct_change`), obtendo **83 retornos diários** por ativo.


Há dois tipos de risco: o **diversificável** (específico do ativo) e o **sistemático** (político, guerra, clima, mercado), que **não some** com diversificação. "O risco pode ser mitigado, nunca eliminado."

## 2. Carteiras: Markowitz (Nobel 1990)

O retorno de uma carteira é a **média ponderada** dos retornos: \(R_c = W_A R_A + W_B R_B\). O risco, porém, **não** é a média dos riscos: depende também de **como os ativos se movem juntos** (a covariância):

\[ \sigma_c^2 = W_A^2\sigma_A^2 + W_B^2\sigma_B^2 + 2\,W_A W_B\,\text{cov}(A,B), \qquad \text{cov}(A,B) = \rho_{AB}\,\sigma_A\sigma_B \]

Quanto **menor a correlação** \(\rho\), maior a redução de risco; com \(\rho = +1\) não há ganho. Para N ativos usa-se a **matriz de covariância**: risco = \(\sqrt{W'\Sigma W}\).

> **Exemplo (da aula): o erro de achar que o risco da carteira é a média dos riscos.** Dois ativos: **A** (retorno 8%, risco 5%) e **B** (retorno 25%, risco 12%), com **metade do dinheiro em cada** (50/50). O **retorno** da carteira é a média ponderada: \(0{,}5\times 8 + 0{,}5\times 25 = \) **16,5%**. Até 1952 se acreditava que o risco seria igual: \(0{,}5\times 5 + 0{,}5\times 12 = \) **8,5%**. **Markowitz mostrou que não é assim**, porque os ativos se influenciam: o risco usa a **correlação** entre eles,
>
> \[ \sigma_p^2 = w_A^2\sigma_A^2 + w_B^2\sigma_B^2 + 2\,w_A w_B\,\rho_{AB}\,\sigma_A\sigma_B \]
>
> Com uma correlação **negativa** (por exemplo \(\rho = -0{,}60\), valor escolhido para a conta): \(\sigma_p^2 = 0{,}25(25) + 0{,}25(144) + 2(0{,}25)(-0{,}60)(5)(12) = 6{,}25 + 36 - 18 = 24{,}25\), logo \(\sigma_p = \) **4,9%**, **menor que o risco do ativo A sozinho (5%)**, e não 8,5%. O exemplo que a aula dá de correlação negativa é **Ibovespa × dólar**: quando muitos estrangeiros trazem dólares para comprar ações, o dólar cai e a Bolsa sobe; quando saem, o dólar sobe e a Bolsa cai (no slide, correlação de **−0,627**). Por isso Markowitz ganhou o **Nobel de 1990**, e até hoje o risco de carteira se calcula assim.
>
> **Exemplo completo (da aula): risco e retorno dos três ativos.** Com os 83 retornos diários:
>
> | | PETR4 | VALE3 | EMBR3 |
> |---|---|---|---|
> | Retorno médio **diário** | 0,063% | 0,134% | 0,196% |
> | Desvio padrão **diário** (risco) | 1,36% | 1,31% | 2,56% |
> | Retorno esperado **anual** (× 252 pregões) | 15,8% | 33,9% | 49,3% |
> | Volatilidade **anual** (× √252) | 21,6% | 20,9% | 40,6% |
> | Retorno ÷ risco (sem descontar a taxa livre de risco) | 0,73 | 1,62 | 1,21 |
>
> A EMBR3 deu o **maior retorno** no período, mas com o **maior risco** (quase o dobro das outras). **A anualização:** a média diária é multiplicada por 252 (dias úteis do ano) e o desvio padrão por \(\sqrt{252}\) (a variância cresce linearmente com o tempo).
>
> **Correlações entre os retornos diários:** PETR4 × VALE3 = **−0,10**; PETR4 × EMBR3 = **−0,05**; VALE3 × EMBR3 = **0,00**. Correlações perto de zero (ou negativas) significam **bom potencial de diversificação**.


> **Exemplo completo (da aula): a carteira de duas ações e o efeito da diversificação.** Carteira **50% PETR4 e 50% VALE3**. O **retorno** é a média ponderada: \(0{,}5\times 15{,}8\% + 0{,}5\times 33{,}9\% = \) **24,8% ao ano**. O **risco não é a média ponderada dos riscos**: é preciso incluir a covariância (anualizada: \(\text{cov} = -0{,}0045\)):
>
> \[ \sigma_p^2 = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2w_1w_2\,\text{cov}_{12} = 0{,}25(0{,}0465) + 0{,}25(0{,}0435) + 2(0{,}25)(-0{,}0045) = 0{,}0203 \]
>
> \[ \sigma_p = \sqrt{0{,}0203} = \mathbf{14{,}2\%} \]
>
> A média ponderada dos riscos seria \(0{,}5\times 21{,}6\% + 0{,}5\times 20{,}9\% = 21{,}2\%\), mas a carteira tem risco de só **14,2%**, **menor que o de qualquer um dos dois ativos**. Essa é a **diversificação**: a correlação é negativa (−0,10), então as oscilações **se compensam**. Quanto menor a correlação, maior o ganho.
>
> **Fronteira de Markowitz com os 3 ativos** (pesos entre 0 e 100%, sem vender a descoberto; taxa livre de risco de 14,5% ao ano):
>
> | Carteira | PETR4 | VALE3 | EMBR3 | Retorno anual | Risco anual | Sharpe |
> |---|---|---|---|---|---|---|
> | **Pesos iguais** | 33,3% | 33,3% | 33,3% | 33,0% | 16,3% | 1,14 |
> | **Mínimo risco** | 43,3% | 45,0% | 11,7% | 27,9% | **13,3%** | 1,01 |
> | **Tangente (máx. Sharpe)** | 11,9% | 60,0% | 28,1% | 36,1% | 16,9% | **1,28** |
>
> O **Sharpe** = \((\text{retorno} - \text{taxa livre de risco})/\text{risco}\) mede o **retorno extra por unidade de risco**. A carteira de **mínimo risco** tem o menor desvio padrão possível (13,3%, menor que o de qualquer ativo sozinho); a **tangente** tem o **melhor Sharpe** (1,28, contra 0,06 da PETR4, 0,93 da VALE3 e 0,86 da EMBR3 sozinhas, já descontada a taxa livre de risco). Na aula, a nuvem de milhares de carteiras aleatórias (**Monte Carlo**) mostra que as melhores ficam na borda superior: a **fronteira eficiente**.
>
> **VaR (valor em risco) histórico.** Para a carteira de pesos iguais, o 5º percentil dos 83 retornos diários é −1,46%: com **95% de confiança**, a perda em **1 dia** não deve passar de **1,46%** (da PETR4 sozinha, 1,67%). Pela distribuição normal, o VaR paramétrico dá 1,55%.


## 3. Risco de crédito

É o risco de **perda econômica por não cumprimento de obrigações pela contraparte**. A perda pode ser **incorrida** (já ocorreu) ou **esperada** (provável no futuro). No Brasil, a Res. CMN **2.682/99** (classificação AA–H) foi substituída pela **4.966/21**, baseada em **perda esperada** e em **3 estágios** (1 normal; 2 aumento significativo do risco; 3 ativo problemático).

A perda esperada é construída por três direcionadores: a **PD** (probabilidade de default), a **EAD/EC** (exposição ao crédito no default) e a **LGD** (perda dado o default = 1 − taxa de recuperação):

\[ \text{Perda esperada} = PD \times EC \times LGD \]

> **Exemplo (dos slides da aula).** Carteira de R$ 100 mil: A (R$ 10 mil, PD 2%), B (R$ 20 mil, 5%), C (R$ 70 mil, 10%), recuperação 0 (LGD = 1). Perdas esperadas: 0,2 + 1 + 7 = **R$ 8,2 mil**. É o valor **provisionado**; a **perda excepcional** vem da cauda da distribuição de perdas.

| Tipo de perda | Tratamento |
|---|---|
| **Esperada** | provisionada |
| **Não esperada** | exige **capital** |
| **Excepcional** (cauda) | falha extrema |

## 4. Basileia: capital proporcional ao risco

O **BIS** ("banco dos bancos centrais", Basileia, Suíça, 1930) abriga o **Comitê de Basileia**, que cuida da **solvência, liquidez e estabilidade** do sistema. A evolução: **Basileia I (1988)** risco de crédito → **1996** risco de mercado → **Basileia II (2004)** risco operacional → **Basileia III (2010)** gestão integrada.

A regra central é:

\[ \frac{\text{Patrimônio de Referência (PR)}}{\text{Ativos Ponderados pelo Risco (APR)}} \geq 8\% \]

Cada ativo é ponderado pelo risco: **0%** (países e bancos centrais), **20%** (bancos), **50%** (financiamento imobiliário), **100%** (empresas e demais).

> **Exemplo (dos slides da aula).** Ativos: 1.000 (0%), 50.000 (20%), 200.000 (50%), 300.000 (100%). APR = 0 + 10.000 + 100.000 + 300.000 = **410.000**. PR = Nível 1 (40.000) + Nível 2 (30.000) = 70.000. Índice = 70.000 ÷ 410.000 = **17,1% ≥ 8%** → instituição adequada.

## 5. Risco operacional

A perda operacional é o produto de **frequência × severidade**, e a frequência costuma seguir uma **Poisson**. O passo a passo é: tabular o nº de eventos e as magnitudes (com probabilidades) → combiná-los em uma **distribuição empírica de perdas** → ordenar e acumular as probabilidades → obter o **VaR operacional**, a pior perda ao nível de confiança escolhido menos a perda esperada média.

## 6. Risco em projetos: fluxo de caixa

O fluxo de caixa operacional parte da receita e vai descontando:

| Passo | Cálculo |
|---|---|
| Receita − despesas operacionais | **EBITDA** |
| − depreciação | **EBIT (LAIR)** |
| − imposto de renda | **NOPAT** |
| **+ depreciação** (despesa que não sai do caixa) | **entrada de caixa operacional** |

Um projeto com **VPL positivo** é viável (no exemplo da aula, mais abaixo, o VPL foi de R$ 13,9 mil). Para medir o risco usam-se duas técnicas:

| Técnica | Como funciona |
|---|---|
| **Análise de sensibilidade** | varia **um parâmetro por vez** e mede o impacto no VPL; se muda muito, o projeto é muito sensível àquele parâmetro |
| **Simulação de Monte Carlo** | sorteia **todas** as variáveis segundo suas **distribuições** (Normal, Triangular, PERT) muitas vezes e obtém a **distribuição do VPL** |

### Exemplo completo (da aula): o VPL de um projeto, da planilha à simulação

O script da aula analisa um projeto de **4 anos**, com **imposto de renda de 40%** e **depreciação linear** do investimento. As premissas estão em três valores (**pessimista, mais provável e otimista**):

| Variável | Pessimista | **Mais provável** | Otimista |
|---|---|---|---|
| Preço de venda (R$/unid) | 49 | **51** | 55 |
| Quantidade (unid/ano) | 990 | **1.100** | 1.200 |
| Custo unitário (R$/unid) | 32 | **29,5** | 28 |
| Despesa operacional (R$/ano) | 6.500 | **6.000** | 5.000 |
| Investimento no ano 0 (R$) | 20.800 | **20.000** | 19.000 |
| Taxa de desconto (a.a.) | 19% | **18%** | 17% |

**Passo 1: o fluxo de caixa com os valores mais prováveis.**

| Linha | Cálculo | R$/ano |
|---|---|---|
| Receita | 51 × 1.100 | 56.100 |
| − Custos | 29,5 × 1.100 | −32.450 |
| − Despesas operacionais | | −6.000 |
| **EBITDA** | | **17.650** |
| − Depreciação | 20.000 ÷ 4 | −5.000 |
| **EBIT** | | **12.650** |
| − Imposto de renda (40%) | 0,40 × 12.650 | −5.060 |
| **NOPAT** | | **7.590** |
| **+ Depreciação** (não sai do caixa) | | +5.000 |
| **Fluxo de caixa operacional (FCO)** | | **12.590** |

**Passo 2: o VPL.** \(VPL = -\text{Investimento} + \sum_{t=1}^{4}\frac{FCO}{(1+r)^t} = -20.000 + 12.590\times 2{,}690 = \) **R$ 13.867,88** (o fator 2,690 é a soma dos fatores de desconto a 18% em 4 anos). VPL positivo: o projeto **é viável** nas condições mais prováveis. Mas esse número supõe que **todas** as variáveis serão exatamente as mais prováveis.

**Passo 3: análise de sensibilidade.** Varia-se **uma variável por vez** entre o pessimista e o otimista, mantendo as outras no mais provável:

| Variável | VPL (pessimista) | VPL (otimista) | Amplitude |
|---|---|---|---|
| **Preço de venda** | 10.317 | 20.970 | **10.653** |
| Quantidade | 10.051 | 17.338 | 7.287 |
| Custo unitário | 9.429 | 16.531 | 7.102 |
| Despesa operacional | 13.061 | 15.482 | 2.421 |
| Taxa de desconto | 13.220 | 14.537 | 1.318 |
| Investimento | 13.283 | 14.599 | 1.316 |

O projeto é **mais sensível ao preço de venda**, depois à quantidade e ao custo unitário; a taxa de desconto e o investimento pouco mexem no resultado. Isso diz **onde** concentrar a atenção (por exemplo, garantir o preço).

**Passo 4: simulação de Monte Carlo.** Sorteia-se **todas as variáveis ao mesmo tempo**, 10.000 vezes, com distribuição **triangular** (pessimista, mais provável e otimista), e calcula-se o VPL de cada sorteio. O resultado é uma **distribuição** de VPL:

| Estatística do VPL (10.000 simulações) | Valor |
|---|---|
| Média | R$ 14.645 |
| Mediana | R$ 14.584 |
| Desvio padrão | R$ 3.134 |
| **P5** (pior 5%) | R$ 9.653 |
| **P95** (melhor 5%) | R$ 19.939 |
| Mínimo e máximo | R$ 4.815 e R$ 25.511 |
| **Probabilidade de VPL > 0** | **100%** |

**Leitura.** Em **90% dos cenários** o VPL fica entre R$ 9,7 mil e R$ 19,9 mil, e **em nenhum dos 10.000** ele é negativo (o pior é +R$ 4,8 mil): o projeto é **robusto** às incertezas consideradas. A sensibilidade mostrou *qual* variável pesa mais; o Monte Carlo mostra *o risco do conjunto*, em forma de probabilidades.

## O que levar daqui

Risco = desvio padrão dos retornos. Em carteiras, **menor correlação = menor risco**. Perda esperada = PD × EC × LGD. Basileia exige PR/APR ≥ 8%. Risco operacional = frequência × severidade. Em projetos, VPL e a comparação entre sensibilidade (um parâmetro por vez) e Monte Carlo (todos, com distribuições).

## Erros que todo mundo comete

| Erro | Correção |
|---|---|
| Medir risco pelo preço | usa-se o desvio padrão dos **retornos** |
| "Diversificar elimina todo o risco" | elimina o diversificável, **não o sistemático** |
| Covariância = correlação | cov tem unidade²; correlação é padronizada (−1 a 1) |
| Perda esperada = perda máxima | é o valor **médio**; o resto é perda não esperada/excepcional |
| LGD = taxa de recuperação | **LGD = 1 − recuperação** |
| Basileia = 8% do ativo total | 8% dos **ativos ponderados pelo risco (APR)** |

## Teste-se

1. Calcule o retorno discreto de um ativo que foi de R$ 50 para R$ 52.
<details markdown="1"><summary>Ver resposta</summary>52 ÷ 50 − 1 = 4%.</details>

2. Cliente com EC = R$ 20 mil, PD = 5% e recuperação de 40%. Qual a perda esperada?
<details markdown="1"><summary>Ver resposta</summary>LGD = 1 − 0,4 = 0,6; perda = 0,05 × 20.000 × 0,6 = R$ 600.</details>

3. Por que a correlação negativa reduz o risco de uma carteira?
<details markdown="1"><summary>Ver resposta</summary>O termo de covariância fica negativo e reduz a variância total: um ativo sobe quando o outro cai.</details>

4. PR = 90.000 e APR = 1.000.000. O banco está adequado?
<details markdown="1"><summary>Ver resposta</summary>Índice = 9% ≥ 8%, sim.</details>

## Pergunta típica
Calcular retorno discreto/contínuo · risco de carteira de 2 ativos com correlação dada · perda esperada = PD×EC×LGD · índice de Basileia (APR e PR/APR ≥ 8%) · diferença entre risco diversificável e sistemático · o que é VaR · sensibilidade × Monte Carlo · EBITDA → NOPAT → caixa
