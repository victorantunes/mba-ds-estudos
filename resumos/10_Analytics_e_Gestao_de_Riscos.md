# 10 · Analytics e Gestão de Riscos
**Prof. Fabiano Guasti Lima · 2 aulas (30/09 e 07/10/2025) · Prioridade: ALTA (tem cálculo — treine as fórmulas)**
*Referências do professor: Fávero & Belfiore (Manual de análise de dados); Lima (Análise de Riscos).*

## 1. Retorno e risco de um ativo
- **Retorno discreto:** Rt = Pt / Pt−1 − 1. Ex.: PETR4 jan R$ 36,77 → fev R$ 37,50: **+1,99%**.
- **Retorno contínuo (log):** Rt = ln(Pt / Pt−1). Mesmo exemplo: **1,97%**. Para o 1º mês não há retorno (precisa do preço anterior).
- **Risco = volatilidade = desvio padrão dos retornos.** "Quem oscilou mais?" não se responde com o preço, e sim com o desvio padrão dos **retornos** (estimar com ≥ 6 meses; nem dados muito antigos nem poucos recentes).
- **Coeficiente de variação** (desvio/média) = **risco por unidade de retorno** (compara ativos de escalas diferentes).
- Variância de N períodos = soma das variâncias (desvio padrão cresce com a raiz do tempo).
- **Risco diversificável × sistemático:** o risco **sistemático** (político, guerra, clima, mercado) **não é eliminado** por diversificação ("o risco pode ser mitigado, nunca eliminado"). Correlação −1 não zera o risco porque nem todo risco é diversificável.

## 2. Carteiras — Markowitz (Nobel 1990)
- **Retorno da carteira:** Rc = Wa·Ra + Wb·Rb (média ponderada).
- **Risco da carteira (2 ativos):** **σc² = Wa²·σa² + Wb²·σb² + 2·Wa·Wb·cov(Ra,Rb)**, com **cov = corr(Ra,Rb)·σa·σb**. Covariância tem unidade ao quadrado (difícil de interpretar); correlação é padronizada (−1 a 1).
- **Efeito da correlação:** quanto **menor a correlação**, **maior a redução de risco** (diversificação). Exemplo (Ibovespa × dólar: corr −0,627; PETR4 × VALE3: corr +0,532).
- **Exemplo:** A (retorno 8%, risco 5%) e B (retorno 25%, risco 12%), 50/50, correlação −0,60 → **retorno 16,5%** e risco ≈ **4,9%** (menor que o de A!, porque a correlação é negativa).
- **N ativos:** Rc = Σ Wi·Ri; risco = √( W′ · Σ · W ) com **matriz de covariância** (no Excel: Análise de Dados → Covariância).

## 3. Risco de crédito
- **Definição:** risco de **perda econômica por não cumprimento de obrigações pela contraparte**. Perda **incorrida** (evento já ocorreu) × perda **esperada** (probabilidade de evento futuro).
- **Regulação (Brasil):** **CMN 2.682/99** (modelo antigo, classificação AA–H em níveis) → **Resolução CMN 4.966/21** (**perda esperada**, classificação em **3 estágios**: 1 = normal; 2 = aumento significativo do risco; **3 = ativo problemático**) e BCB 352/23.
- **Direcionadores:** **PD** (probability of default), **EAD/EC** (exposição ao crédito no default) e **LGD** (perda dado o default = **1 − taxa de recuperação**).
- **Perda esperada = PD × EC × LGD** (= p × EC × (1 − t)). Ex. carteira de R$ 100 mil: A (10 mil, 2%), B (20 mil, 5%), C (70 mil, 10%), recuperação 0, defaults independentes → perda esperada = 0,2 + 1 + 7 = **R$ 8.200**. A **perda excepcional/inesperada** vem da cauda da distribuição de perdas (ex.: R$ 61.800 acima da esperada no nível de confiança escolhido).
- Distribuição das perdas: **perda esperada** (provisionada) + **perda não esperada** (exige capital) + **excepcional** (cauda, falha extrema). Modelos de **ML** (probabilidade de inadimplência) e **ratings** (Moody's, Fitch, S&P; risco soberano e privado) são usados para estimar PD.

## 4. Basileia (regulação de capital bancário)
- **BIS** (Bank for International Settlements, Basileia, Suíça, fundado em 1930; "banco dos bancos centrais"; ~55 bancos centrais); **Comitê de Basileia (BCBS)** sobre supervisão bancária: **solvência, liquidez e estabilidade** do sistema.
- **Basileia I (1988):** capital para **risco de crédito**; **1996:** risco de **mercado**; **Basileia II (2004):** risco **operacional**; **2009:** Basileia 2,5 (securitizações); **Basileia III (2010):** gestão integrada de riscos.
- **Regra central:** **Capital (Patrimônio de Referência, PR) / Ativos Ponderados pelo Risco (APR) ≥ 8%** (no Brasil, patamar maior com adicionais).
- **Ponderação (Basileia I):** 0% (países e bancos centrais), 20% (bancos multilaterais/bancos), 50% (financiamento imobiliário/garantia residencial), 100% (empresas e demais).
- **Exemplo:** ativos 1.000 (0%) + 50.000 (20%) + 200.000 (50%) + 300.000 (100%) → APR = 0 + 10.000 + 100.000 + 300.000 = **410.000**. PR = Nível 1 (40.000: capital social, reservas, lucros) + Nível 2 (30.000: reavaliação, dívidas subordinadas, híbridos) = 70.000 → **Índice = 70.000/410.000 = 17,1%** → **instituição adequada** (≥ 8%).

## 5. Risco operacional
- Mede-se pela **distribuição de perdas = frequência × severidade**, com dados históricos, estimativas subjetivas ou distribuições teóricas (frequência: **Poisson**).
- Passo a passo: tabular **nº de eventos (probabilidade)** e **magnitude (probabilidade)** → combinar para gerar **distribuição empírica de perdas** → ordenar pela perda e acumular probabilidade → **VaR operacional = pior perda no nível de confiança desejado − perda esperada média**.
- Exemplo de severidade: $500 (60%), $10.000 (30%), $50.000 (10%); nº de perdas: nenhuma 70%, 1 = 20%, 2 = 10%.

## 6. Risco em fluxos de caixa / projetos
- **Fluxo de caixa operacional:** Receita − Despesas operacionais = **EBITDA**; − Depreciação = **EBIT (LAIR)**; − IR = **NOPAT**; **+ Depreciação = entrada de caixa operacional** (a depreciação é despesa não desembolsável).
- Exemplo da aula: investimento 200 mil; receitas 170/145/125/100; desp. operacionais 23/23/20/20; depreciação 50/ano; IR 40%; taxa 14% a.a. → fluxos ≈ 108,2 / 93,2 / 83,0 / 68,0 → **VPL ≈ R$ 62,9 mil** (positivo → projeto viável).
- **Análise de sensibilidade:** variar **um parâmetro por vez** e ver o impacto no VPL/rentabilidade; se muda muito, o projeto é **muito sensível** àquele parâmetro → vale obter dados menos incertos (no Excel: "Atingir meta").
- **Simulação de Monte Carlo:** sorteia valores das variáveis segundo suas **distribuições de probabilidade** (**Normal, Triangular, PERT**) ao longo da vida do projeto → distribuição do VPL (risco). Perguntas de risco: economia, preços, novos concorrentes, prazos e custos, eficiência.

## Pergunta típica
Calcular retorno discreto/contínuo · risco de carteira de 2 ativos com correlação dada · perda esperada = PD×EC×LGD · índice de Basileia (APR e PR/APR ≥ 8%) · diferença entre risco diversificável e sistemático · o que é VaR · sensibilidade × Monte Carlo · EBITDA→NOPAT→caixa.
