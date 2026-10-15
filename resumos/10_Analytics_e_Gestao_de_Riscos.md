# 10 · Analytics e Gestão de Riscos
**Prof. Fabiano Guasti Lima · 2 aulas · Prioridade: ALTA (tem cálculo — treine as fórmulas)**
*Referências do professor: Fávero & Belfiore (Manual de análise de dados); Lima (Análise de Riscos).*

> **Em uma frase:** risco é a **incerteza sobre resultados**; a gestão de riscos mede essa incerteza (desvio padrão, perda esperada, VaR), reduz o que dá para reduzir (diversificação, capital) e decide com base nos números.

**Pré-requisitos:** desvio padrão, correlação e VPL (01). **Vem depois:** aplica-se a carteiras, crédito, bancos e projetos.

## Por que isso importa (intuição)
Dois investimentos podem ter o mesmo retorno médio e oscilar de formas muito diferentes; o mais volátil é o mais arriscado. Já **combinar ativos que não andam juntos** (correlação baixa ou negativa) faz as oscilações se compensarem — é a ideia da diversificação (Markowitz). No crédito, você aceita que alguns clientes não pagarão e **provisiona essa perda esperada**; o que excede isso exige **capital** (Basileia).

## 1. Retorno e risco de um ativo
- **Retorno discreto:** Rₜ = Pₜ ÷ Pₜ₋₁ − 1. **Retorno contínuo (log):** Rₜ = ln(Pₜ ÷ Pₜ₋₁). O 1º período não tem retorno (falta o preço anterior).
- **Risco = volatilidade = desvio padrão dos retornos** (não do preço).
- **Coeficiente de variação** (desvio ÷ média) = **risco por unidade de retorno**.
- **Risco diversificável × sistemático:** o sistemático (político, guerra, clima, mercado) **não some** com diversificação — "o risco pode ser mitigado, nunca eliminado".

**Exemplo resolvido.** PETR4: R$ 36,77 → R$ 37,50. Discreto: 37,50 ÷ 36,77 − 1 = **1,99%**; contínuo: ln(1,0199) = **1,97%**.

## 2. Carteiras — Markowitz (Nobel 1990)
- **Retorno da carteira:** média ponderada R_c = W_A·R_A + W_B·R_B.
- **Risco (2 ativos):** **σ_c² = W_A²σ_A² + W_B²σ_B² + 2·W_A·W_B·cov(A,B)**, com **cov = ρ·σ_A·σ_B**.
- **Quanto menor a correlação ρ, maior a redução de risco.** Com ρ = +1 não há ganho de diversificação.
- **Com N ativos:** retorno = ΣWᵢRᵢ; risco = √(W′ΣW), com matriz de covariância Σ.

**Exemplo resolvido.** A (retorno 8%, risco 5%) e B (25%, 12%), 50/50, ρ = −0,60.
Retorno = 0,5·8 + 0,5·25 = **16,5%**. cov = −0,6·5·12 = −36. Variância = 0,25·25 + 0,25·144 + 2·0,25·(−36) = 6,25 + 36 − 18 = 24,25 → risco = **≈ 4,9%**. A carteira tem **risco menor que o de A** e retorno bem maior, porque a correlação negativa compensa as oscilações.

## 3. Risco de crédito
- **Risco de crédito:** perda econômica por **não cumprimento** de obrigações pela contraparte. Perda **incorrida** (já ocorreu) × **esperada** (provável no futuro).
- **Regulação no Brasil:** Res. CMN **2.682/99** (classificação AA–H) → Res. CMN **4.966/21** (**perda esperada**, em **3 estágios**: 1 normal, 2 aumento significativo do risco, 3 ativo problemático).
- **Direcionadores:** **PD** (probabilidade de default), **EAD/EC** (exposição no default) e **LGD** (perda dado o default = 1 − taxa de recuperação).
- **Perda esperada = PD × EC × LGD.**

**Exemplo resolvido.** Carteira de R$ 100 mil: A (R$ 10 mil, PD 2%), B (R$ 20 mil, 5%), C (R$ 70 mil, 10%), recuperação 0 (LGD = 1). Perdas esperadas = 0,2 + 1 + 7 = **R$ 8,2 mil** (8.200). Esse valor é **provisionado**; a **perda excepcional** vem da cauda da distribuição de perdas.
- **Tipos de perda:** esperada (provisão), **não esperada** (capital) e **excepcional** (cauda). ML e ratings (Moody's, S&P, Fitch) ajudam a estimar PD.

## 4. Basileia — regulação de capital bancário
- **BIS** ("banco dos bancos centrais", Basileia, Suíça, 1930); **Comitê de Basileia** trata de **solvência, liquidez e estabilidade**.
- **Evolução:** **Basileia I (1988)** risco de crédito → 1996 risco de mercado → **Basileia II (2004)** risco operacional → **Basileia III (2010)** gestão integrada.
- **Regra central:** **Patrimônio de Referência (PR) ÷ Ativos Ponderados pelo Risco (APR) ≥ 8%.**
- **Ponderações (Basileia I):** 0% (países e BCs), 20% (bancos), 50% (financiamento imobiliário), 100% (empresas e demais).

**Exemplo resolvido.** Ativos: 1.000 (0%), 50.000 (20%), 200.000 (50%), 300.000 (100%).
APR = 0 + 10.000 + 100.000 + 300.000 = **410.000**. PR = Nível 1 (40.000) + Nível 2 (30.000) = 70.000. **Índice = 70.000 ÷ 410.000 = 17,1% ≥ 8% → adequado.**

## 5. Risco operacional
- **Perda = frequência × severidade.** Frequência costuma seguir **Poisson**.
- **Passo a passo:** tabular nº de eventos e magnitudes (com probabilidades) → combinar para obter a **distribuição empírica de perdas** → ordenar e acumular → **VaR operacional = pior perda no nível de confiança − perda esperada média**.

## 6. Risco em fluxos de caixa e projetos
- **Fluxo operacional:** Receita − Despesas operacionais = **EBITDA**; − Depreciação = **EBIT**; − IR = **NOPAT**; **+ Depreciação** (despesa não desembolsável) = **entrada de caixa**.
- **VPL positivo → projeto viável.** Exemplo da aula: investimento 200 mil, taxa 14% a.a. → **VPL ≈ R$ 62,9 mil**.
- **Análise de sensibilidade:** varia **um parâmetro por vez** e mede o impacto no VPL (se muda muito, o projeto é muito sensível àquele parâmetro).
- **Simulação de Monte Carlo:** sorteia as variáveis segundo suas **distribuições** (Normal, Triangular, PERT) muitas vezes → obtém a **distribuição do VPL** (o risco).

## Armadilhas e confusões comuns
| Confusão | O correto |
|---|---|
| Risco se mede pelo preço | mede-se pelo desvio padrão dos **retornos** |
| Diversificar elimina todo o risco | elimina o diversificável, **não o sistemático** |
| Covariância e correlação são equivalentes | cov tem unidade²; correlação é padronizada (−1 a 1) |
| Perda esperada = perda máxima | é o valor **médio** esperado; o resto é perda não esperada/excepcional |
| LGD = taxa de recuperação | **LGD = 1 − recuperação** |
| Basileia exige 8% do ativo total | 8% sobre os **ativos ponderados pelo risco (APR)** |
| Sensibilidade e Monte Carlo são iguais | sensibilidade varia **um parâmetro por vez**; Monte Carlo varia **todos**, com distribuições |

## Resumo-relâmpago
- Retorno: P_t/P_{t−1} − 1 (ou ln). Risco = desvio padrão dos retornos; CV = risco por retorno.
- Carteira: variância com covariância; menor correlação = mais diversificação.
- Perda esperada = PD × EC × LGD. Basileia: PR/APR ≥ 8%.
- Operacional: frequência × severidade; VaR. Projeto: VPL, sensibilidade, Monte Carlo.

## Teste-se
1. Calcule o retorno discreto de um ativo que foi de R$ 50 para R$ 52.
<details markdown="1"><summary>Ver resposta</summary>52 ÷ 50 − 1 = 4%.</details>

2. Cliente com EC = R$ 20 mil, PD = 5% e recuperação de 40%. Qual a perda esperada?
<details markdown="1"><summary>Ver resposta</summary>LGD = 1 − 0,4 = 0,6; perda = 0,05 × 20.000 × 0,6 = R$ 600.</details>

3. Por que a correlação negativa reduz o risco de uma carteira?
<details markdown="1"><summary>Ver resposta</summary>Porque o termo de covariância fica negativo, reduzindo a variância total: um ativo sobe quando o outro cai.</details>

4. PR = 90.000 e APR = 1.000.000. O banco está adequado?
<details markdown="1"><summary>Ver resposta</summary>Índice = 9% ≥ 8%, sim.</details>

## Pergunta típica
Calcular retorno discreto/contínuo · risco de carteira de 2 ativos com correlação dada · perda esperada = PD×EC×LGD · índice de Basileia (APR e PR/APR ≥ 8%) · diferença entre risco diversificável e sistemático · o que é VaR · sensibilidade × Monte Carlo · EBITDA → NOPAT → caixa
