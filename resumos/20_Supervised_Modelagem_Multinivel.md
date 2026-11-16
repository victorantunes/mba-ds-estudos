# 20 · Supervised ML — Modelagem Multinível (HLM / GLMM)
**Prof. Dr. Luiz Paulo Fávero · 2 aulas · Prioridade: alta (destaque explícito: "vai cair esse tipo de pergunta": prever valores, ICC, efeito escola × efeito estudante)**

## O fio condutor deste capítulo

Alunos da mesma escola se parecem entre si: compartilham professores, estrutura e vizinhança. Suas notas **não são independentes**. A regressão comum trata todos como um único grupo e ignora isso. O **modelo multinível** reconhece que os dados são **aninhados** (alunos dentro de escolas, empresas dentro de países) e diz: *cada escola tem seu próprio nível médio de desempenho (um intercepto que varia) e, às vezes, sua própria relação entre horas de estudo e nota (uma inclinação que varia)*. Assim, é possível medir **quanto da diferença vem da escola e quanto vem do aluno**.

O capítulo apresenta primeiro a ideia e o vocabulário (e por que OLS e dummies não bastam); depois os componentes (**efeitos fixos e aleatórios**); em seguida as **equações** do modelo de dois níveis, o **ICC** e a **previsão** passo a passo; e termina com o modelo de **três níveis** para medidas repetidas.

```mermaid
flowchart TD
  M["Município (nível 3)"] --> E["Escola (nível 2)"]
  E --> A["Aluno (nível 1)"]
  A --> T["Medidas repetidas no tempo (nível 1 do growth model)"]
```

## 1. Ideia e vocabulário

Um modelo multinível reconhece **estruturas hierárquicas**: observações (nível 1) dentro de grupos (nível 2), dentro de grupos maiores (nível 3). Seus sinônimos são **HLM** (modelos hierárquicos lineares), modelos mistos, aninhados, de coeficientes aleatórios e **GLMM**; é o modelo supervisionado **mais geral**. Quando não há hierarquia explícita, cria-se um **contexto latente**: faz-se um **cluster** da amostra e usa-se o cluster como nível (a saída do não supervisionado vira entrada do supervisionado).

**Por que não OLS nem OLS com dummies de grupo?** O OLS ignora os efeitos contextuais; as dummies não separam efeitos observáveis dos não observáveis nem modelam a **variância entre contextos**. Existe ainda o **paradoxo de Simpson**: uma tendência presente dentro dos grupos pode **inverter ou desaparecer** quando os grupos são combinados.

## 2. Efeitos fixos e aleatórios

| Componente | O que é | Exemplo |
|---|---|---|
| **Efeitos fixos (γ)** | parâmetros comuns a toda a população | intercepto e inclinação "médios" |
| **\(\nu_{0j}\)** | variação do **intercepto** entre grupos | escolas com médias diferentes |
| **\(\nu_{1j}\)** | variação da **inclinação** entre grupos | o efeito das horas de estudo difere entre escolas |
| **\(\varepsilon_{ij}\)** | erro do nível 1 | variação individual do aluno |

O **primeiro passo** é testar se as **variâncias dos efeitos aleatórios são diferentes de zero**: se forem, o OLS **não é adequado**; se não, o multinível não agrega. Grupos com uma única observação são descartados. Para **comparar modelos** usa-se o **teste de razão de verossimilhança (LR)**, com o log-likelihood, e também o gráfico de valores previstos × reais (quanto mais perto da reta de 45°, melhor).

## 3. As equações do modelo de dois níveis (HLM2)

**Modelo nulo (intercepto aleatório):** nível 1: \(desempenho_{ij} = \beta_{0j} + \varepsilon_{ij}\); nível 2: \(\beta_{0j} = \gamma_{00} + \nu_{0j}\). Juntando:

\[ desempenho_{ij} = \gamma_{00} + \nu_{0j} + \varepsilon_{ij} \]

**Com inclinação aleatória e variável de nível 2** (por exemplo, `texp` = experiência média dos professores da escola):

\[ desempenho_{ij} = \gamma_{00} + \gamma_{10}\,horas_{ij} + \gamma_{01}\,texp_j + \gamma_{11}\,texp_j\,horas_{ij} + \nu_{0j} + \nu_{1j}\,horas_{ij} + \varepsilon_{ij} \]

Note o termo \(\gamma_{11}\,texp\cdot horas\): uma **interação entre níveis**.

### O ICC: efeito escola × efeito estudante

\[ ICC = \frac{\text{variância entre grupos}}{\text{variância entre grupos} + \text{variância do erro}} \]

O ICC é a **fração da variância total atribuível ao contexto** (a escola); o restante é o efeito do indivíduo. Quanto maior o ICC, mais importante o contexto.

### Exemplo completo (da aula): desempenho de 358 estudantes em 10 escolas

Dados reais: cada linha é um **estudante** (nível 1) que pertence a uma de **10 escolas** (nível 2, de 20 a 48 estudantes cada). A variável dependente é o **desempenho** (média 41,6; de 6,5 a 100). As explicativas são as **horas de estudo por semana** (nível 1, média de 19) e o **tempo médio de experiência dos professores da escola**, **texp** (nível 2, em anos, de 1,9 a 13).

**O desempenho muda muito de escola para escola.** As médias por escola vão de **18,6** (escola 9) a **75,4** (escola 8):

| Escola | 9 | 5 | 2 | 6 | 1 | 10 | 4 | 7 | 3 | 8 |
|---|---|---|---|---|---|---|---|---|---|---|
| Desempenho médio | 18,6 | 19,3 | 21,4 | 34,0 | 36,8 | 38,6 | 55,3 | 57,5 | 67,1 | 75,4 |

**Passo 1: o modelo nulo** (só intercepto, mas **aleatório por escola**). Ele separa a variação em duas partes:

| Componente | Estimativa |
|---|---|
| Intercepto geral \(\gamma_{00}\) (efeito fixo) | **42,39** |
| Variância **entre escolas** (efeito aleatório do intercepto, \(\tau_{00}\)) | **414,07** |
| Variância **residual** (entre estudantes da mesma escola, \(\sigma^2\)) | **142,92** |

**Passo 2: o ICC** (correlação intraclasse): a fração da variância total que está **entre escolas**.

\[ ICC = \frac{\tau_{00}}{\tau_{00} + \sigma^2} = \frac{414{,}07}{414{,}07 + 142{,}92} = \frac{414{,}07}{556{,}99} = \mathbf{0{,}743} \]

**74,3% da variação no desempenho é "efeito escola"** e só 25,7% é "efeito estudante" dentro da escola. É um ICC enorme: ignorar a estrutura hierárquica seria um erro grave. O **teste de razão de verossimilhança** (como feito na aula) confirma: a LL do modelo nulo multinível (−1.416,0) é bem maior que a do OLS sem estrutura (−1.633,5), com \(\chi^2 = 2(−1.416{,}0 + 1.633{,}5) = 435\): **os efeitos aleatórios de escola são necessários**.


### Exemplo completo (continuação): o modelo final e a previsão

O modelo final tem **interceptos e inclinações aleatórios** por escola, com as horas de estudo (nível 1), o texp (nível 2) e a **interação** entre os dois:

\[ \widehat{\text{desemp}}_{ij} = \underbrace{\gamma_{00} + \gamma_{10}\,\text{horas}_{ij} + \gamma_{01}\,\text{texp}_j + \gamma_{11}\,\text{horas}_{ij}\,\text{texp}_j}_{\text{efeitos fixos}} + \underbrace{\nu_{0j} + \nu_{1j}\,\text{horas}_{ij}}_{\text{efeitos aleatórios da escola }j} \]

**Efeitos fixos estimados:**

| Termo | Coeficiente | p-valor | Leitura |
|---|---|---|---|
| \(\gamma_{00}\) Intercepto | −0,850 | 0,777 | não significante |
| \(\gamma_{10}\) horas | **0,713** | 0,026 | cada hora de estudo a mais eleva o desempenho em 0,71 ponto (quando texp = 0) |
| \(\gamma_{01}\) texp | **1,585** | 0,001 | cada ano a mais de experiência dos professores eleva o desempenho em 1,59 ponto |
| \(\gamma_{11}\) horas × texp | **0,232** | < 0,001 | **interação:** o efeito das horas de estudo **cresce** em escolas com professores mais experientes |

**Efeitos aleatórios (variâncias):** do intercepto, \(\tau_{00} = 24{,}3\); da inclinação das horas, \(\tau_{11} = 0{,}31\); e a residual \(\sigma^2 = 7{,}04\). Para ter uma ideia: no modelo nulo a variância entre escolas era **414**; no modelo final, com as horas e o texp, a variância do intercepto é **24**. Os modelos não são idênticos (o final tem inclinação aleatória), mas a queda sugere que o tempo de experiência dos professores explica boa parte do "efeito escola".

**Previsão passo a passo.** Qual o desempenho previsto do **estudante 1**, da **escola 1**, que estuda **11 horas** por semana, numa escola com **texp = 3,6**?

1. **Parte fixa:** \(-0{,}850 + 0{,}713\times 11 + 1{,}585\times 3{,}6 + 0{,}232\times 11\times 3{,}6 = -0{,}850 + 7{,}843 + 5{,}706 + 9{,}187 = \mathbf{21{,}89}\).
2. **Efeitos aleatórios da escola 1** (estimados pelo modelo): \(\nu_{01} = -0{,}211\) (intercepto) e \(\nu_{11} = +0{,}439\) (inclinação).
3. **Previsão completa:** \(21{,}89 + (-0{,}211) + 0{,}439\times 11 = 21{,}89 - 0{,}21 + 4{,}83 = \mathbf{26{,}50}\).

O desempenho observado desse estudante foi **25,0**. A previsão só com a parte fixa (21,89) ficaria mais longe; **somar os efeitos aleatórios da escola** aproxima a previsão da realidade (26,50), porque ela reconhece que a escola 1 tem uma inclinação das horas um pouco acima da média das escolas.


## 4. Três níveis e medidas repetidas (growth model)

Quando o mesmo aluno é medido várias vezes, os níveis são: **nível 1 = tempo (medidas repetidas)**, **nível 2 = indivíduo**, **nível 3 = grupo (escola)**. O **modelo de tendência linear** com interceptos e inclinações aleatórios fica:

\[ desempenho = \delta_{000} + \delta_{100}\,m\hat{e}s + \nu_{0jk} + \tau_{00k} + \tau_{10k}\,m\hat{e}s + \varepsilon_{tjk} \]

Variáveis de nível 2 e 3 podem interagir com o tempo.

## 5. Python e aplicações

Em Python usa-se `statsmodels.mixedlm`: `smf.mixedlm('desempenho ~ horas', data, groups=df['escola'], re_formula='~horas')` (para três níveis, `vc_formula`). Variáveis `object` precisam virar dummies ou numéricas. Aplicações: estrutura de capital de empresas por país (Rajan e Zingales), escolas × alunos, crédito e risco. Em geral, "qualquer modelo supervisionado pode ganhar capacidade preditiva ao incorporar contexto".

## O que levar daqui

Multinível lida com dados aninhados separando efeito do indivíduo e do contexto. Efeitos fixos (γ) são comuns; aleatórios (ν, τ) variam por grupo; ε é o erro. O primeiro teste é se as variâncias aleatórias diferem de zero; compara-se modelos por LR. ICC = variância do grupo ÷ (variância do grupo + variância do erro). A previsão soma a parte fixa e os efeitos aleatórios do grupo.

## Erros que todo mundo comete

| Erro | Correção |
|---|---|
| "Dummies de escola equivalem ao multinível" | dummies **não** modelam a variância entre contextos |
| "Efeito fixo = efeito aleatório" | fixo = comum à população; aleatório = **varia entre grupos** |
| "ICC alto = pouco efeito do contexto" | ICC alto = **muito** efeito do contexto |
| "A previsão usa só os γ" | some também \(\nu_{0j}\) e \(\nu_{1j}\cdot x\) do grupo |
| "Multinível exige hierarquia explícita" | pode-se criar **contexto latente** via cluster |
| "\(\nu_{0j}\) é a diferença nas inclinações" | \(\nu_{0j}\) = interceptos; **\(\nu_{1j}\) = inclinações** |

## Teste-se

1. Variância entre grupos = 12 e residual = 28. Qual o ICC?
<details markdown="1"><summary>Ver resposta</summary>12 ÷ (12 + 28) = 0,30 (30% de efeito do contexto).</details>

2. O que \(\nu_{1j}\) representa?
<details markdown="1"><summary>Ver resposta</summary>A variação da inclinação entre grupos (o efeito de X difere entre contextos).</details>

3. Por que não usar OLS com dummies de escola?
<details markdown="1"><summary>Ver resposta</summary>Porque não separam efeitos observáveis dos não observáveis nem capturam a variância entre contextos.</details>

4. Quais são os níveis de um modelo de medidas repetidas de alunos em escolas?
<details markdown="1"><summary>Ver resposta</summary>Tempo (nível 1) → aluno (nível 2) → escola (nível 3).</details>

## Pergunta típica
Definição e sinônimos de modelagem multinível · por que não OLS nem dummies · efeito fixo × aleatório · primeira verificação (variância dos efeitos aleatórios) · como comparar modelos (LR, log-likelihood) · calcular ICC · interpretar ν₀ⱼ e ν₁ⱼ · montar a previsão com a equação final · níveis em medidas repetidas · paradoxo de Simpson · cluster como contexto latente
