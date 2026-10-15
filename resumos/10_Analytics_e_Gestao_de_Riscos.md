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

> **Exemplo resolvido.** PETR4 vai de R$ 36,77 para R$ 37,50. Discreto: \(37{,}50/36{,}77 - 1 = 1{,}99\%\). Contínuo: \(\ln(1{,}0199) = 1{,}97\%\).

Há dois tipos de risco: o **diversificável** (específico do ativo) e o **sistemático** (político, guerra, clima, mercado), que **não some** com diversificação. "O risco pode ser mitigado, nunca eliminado."

## 2. Carteiras: Markowitz (Nobel 1990)

O retorno de uma carteira é a **média ponderada** dos retornos: \(R_c = W_A R_A + W_B R_B\). O risco, porém, **não** é a média dos riscos: depende também de **como os ativos se movem juntos** (a covariância):

\[ \sigma_c^2 = W_A^2\sigma_A^2 + W_B^2\sigma_B^2 + 2\,W_A W_B\,\text{cov}(A,B), \qquad \text{cov}(A,B) = \rho_{AB}\,\sigma_A\sigma_B \]

Quanto **menor a correlação** \(\rho\), maior a redução de risco; com \(\rho = +1\) não há ganho. Para N ativos usa-se a **matriz de covariância**: risco = \(\sqrt{W'\Sigma W}\).

> **Exemplo resolvido.** Ativo A (retorno 8%, risco 5%) e B (25%, 12%), 50/50, \(\rho = -0{,}60\). Retorno = \(0{,}5\cdot 8 + 0{,}5\cdot 25 = 16{,}5\%\). \(\text{cov} = -0{,}6\cdot5\cdot12 = -36\). Variância = \(0{,}25\cdot25 + 0{,}25\cdot144 + 2\cdot0{,}25\cdot(-36) = 6{,}25 + 36 - 18 = 24{,}25\) → risco ≈ **4,9%**. A carteira tem risco **menor que o de A** e retorno muito maior, porque a correlação negativa faz as oscilações se compensarem.

## 3. Risco de crédito

É o risco de **perda econômica por não cumprimento de obrigações pela contraparte**. A perda pode ser **incorrida** (já ocorreu) ou **esperada** (provável no futuro). No Brasil, a Res. CMN **2.682/99** (classificação AA–H) foi substituída pela **4.966/21**, baseada em **perda esperada** e em **3 estágios** (1 normal; 2 aumento significativo do risco; 3 ativo problemático).

A perda esperada é construída por três direcionadores: a **PD** (probabilidade de default), a **EAD/EC** (exposição ao crédito no default) e a **LGD** (perda dado o default = 1 − taxa de recuperação):

\[ \text{Perda esperada} = PD \times EC \times LGD \]

> **Exemplo resolvido.** Carteira de R$ 100 mil: A (R$ 10 mil, PD 2%), B (R$ 20 mil, 5%), C (R$ 70 mil, 10%), recuperação 0 (LGD = 1). Perdas esperadas: 0,2 + 1 + 7 = **R$ 8,2 mil**. É o valor **provisionado**; a **perda excepcional** vem da cauda da distribuição de perdas.

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

> **Exemplo resolvido.** Ativos: 1.000 (0%), 50.000 (20%), 200.000 (50%), 300.000 (100%). APR = 0 + 10.000 + 100.000 + 300.000 = **410.000**. PR = Nível 1 (40.000) + Nível 2 (30.000) = 70.000. Índice = 70.000 ÷ 410.000 = **17,1% ≥ 8%** → instituição adequada.

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

Um projeto com **VPL positivo** é viável (no exemplo da aula, investimento de R$ 200 mil à taxa de 14% a.a. deu VPL ≈ R$ 62,9 mil). Para medir o risco usam-se duas técnicas:

| Técnica | Como funciona |
|---|---|
| **Análise de sensibilidade** | varia **um parâmetro por vez** e mede o impacto no VPL; se muda muito, o projeto é muito sensível àquele parâmetro |
| **Simulação de Monte Carlo** | sorteia **todas** as variáveis segundo suas **distribuições** (Normal, Triangular, PERT) muitas vezes e obtém a **distribuição do VPL** |

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
