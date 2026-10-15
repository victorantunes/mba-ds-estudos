# 20 · Supervised ML — Modelagem Multinível (HLM / GLMM)
**Prof. Dr. Luiz Paulo Fávero · 2 aulas · Prioridade: ALTA (destaque explícito: "vai cair esse tipo de pergunta": prever valores, ICC, efeito escola × efeito estudante)**

> **Em uma frase:** quando os dados são **aninhados** (alunos dentro de escolas, empresas dentro de países), o modelo multinível separa o que vem do **indivíduo** do que vem do **contexto**, deixando interceptos e inclinações variarem entre os grupos.

**Pré-requisitos:** regressão (17) e noção de variância (01). **Vem depois:** os modelos de classificação/contagem também aceitam versões multinível (GLMM).

## Por que isso importa (intuição)
Alunos da mesma escola se parecem entre si (professores, estrutura, vizinhança): suas notas **não são independentes**. A regressão comum trata todos como um único grupo e subestima isso. O multinível diz: *"cada escola tem seu nível médio de desempenho (intercepto aleatório) e, às vezes, sua própria relação entre horas de estudo e nota (inclinação aleatória)"*. Assim você mede **quanto da diferença é da escola e quanto é do aluno**.

## 1. Ideia e vocabulário
- **Estrutura hierárquica:** observações (nível 1) dentro de grupos (nível 2), dentro de grupos maiores (nível 3). Ex.: **alunos → escolas → municípios**; **empresas → países**; **medidas repetidas → indivíduos → grupos**.
- **Sinônimos:** HLM (modelos hierárquicos lineares), modelos mistos, modelos aninhados, coeficientes aleatórios, **GLMM** — o modelo supervisionado mais geral.
- **Sem hierarquia explícita?** Crie **contextos latentes**: faça um **cluster** da amostra e use-o como nível (a saída do não supervisionado vira entrada do supervisionado).
- **Por que não OLS nem dummies de grupo?** O OLS ignora efeitos contextuais; as dummies não separam efeitos observáveis dos não observáveis nem modelam a variância entre contextos.
- **Paradoxo de Simpson:** uma tendência dentro dos grupos pode **inverter ou sumir** quando os grupos são combinados.

## 2. Componentes
- **Efeitos fixos (γ):** parâmetros comuns da população (intercepto e inclinação "médios").
- **Efeitos aleatórios:** **ν₀ⱼ** = variação do **intercepto** entre grupos (escolas com médias diferentes); **ν₁ⱼ** = variação da **inclinação** (o efeito das horas de estudo difere entre escolas); **εᵢⱼ** = erro do nível 1.
- **Primeiro passo:** testar se as **variâncias dos efeitos aleatórios são diferentes de zero**; se forem, o OLS **não é adequado**; se não, o multinível não agrega. Grupos com uma observação são descartados.
- **Comparar modelos:** **teste de razão de verossimilhança (LR)** com o log-likelihood; compare também os valores previstos × reais (quanto mais perto da reta de 45°, melhor).

## 3. Equações do HLM2 (2 níveis)
- **Modelo nulo (intercepto aleatório):** N1: **desempenhoᵢⱼ = β₀ⱼ + εᵢⱼ**; N2: **β₀ⱼ = γ₀₀ + ν₀ⱼ** → **desempenho = γ₀₀ + ν₀ⱼ + εᵢⱼ**.
- **Interceptos e inclinações aleatórios:** desempenho = γ₀₀ + γ₁₀·horas + ν₀ⱼ + ν₁ⱼ·horas + εᵢⱼ.
- **Com variável de nível 2** (texp = experiência média dos professores): desempenho = γ₀₀ + γ₁₀·horas + γ₀₁·texp + **γ₁₁·texp·horas** + ν₀ⱼ + ν₁ⱼ·horas + εᵢⱼ (há **interação entre níveis**).
- **ICC (correlação intraclasse)** = **variância do grupo ÷ (variância do grupo + variância do erro)** — fração da variância total atribuível ao **contexto**; o restante é efeito do indivíduo.

**Exemplo resolvido (ICC).** Variância entre escolas = 20; variância residual = 80 → **ICC = 20 ÷ 100 = 0,20**: 20% da variação no desempenho é "efeito escola"; **80% é "efeito estudante"**.

**Exemplo resolvido (previsão — pergunta de avaliação).** γ₀₀ = 50; γ₁₀ = 2; γ₀₁ = 1,5; γ₁₁ = 0,3. Escola 1 com ν₀ = 3 e ν₁ = 0,5; aluno que estuda **11 horas** em escola com **texp = 3,6**.
- **Parte fixa:** 50 + 2·11 + 1,5·3,6 + 0,3·3,6·11 = 50 + 22 + 5,4 + 11,88 = **89,28**.
- **Parte aleatória da escola 1:** 3 + 0,5·11 = **8,5**.
- **Previsto = 89,28 + 8,5 = 97,78.** (O `fittedvalues` do statsmodels já inclui os efeitos aleatórios.)

## 4. HLM3 com medidas repetidas (growth model)
- **Níveis:** N1 = **tempo (medidas repetidas)**; N2 = **indivíduo**; N3 = **grupo (escola)**.
- **Modelo nulo:** desempenho = δ₀₀₀ + ν₀ⱼₖ + τ₀₀ₖ + εₜⱼₖ.
- **Tendência linear (growth model):** desempenho = δ₀₀₀ + δ₁₀₀·mês + ν₀ⱼₖ + τ₀₀ₖ + τ₁₀ₖ·mês + εₜⱼₖ; variáveis de N2 e N3 podem interagir com o tempo.

## 5. Python e aplicações
- **`statsmodels.mixedlm`:** `smf.mixedlm('desempenho ~ horas', data, groups=df['escola'], re_formula='~horas')`; HLM3 usa `vc_formula`. Variáveis `object` precisam virar dummies/numéricas.
- **Aplicações:** estrutura de capital de empresas por país (Rajan & Zingales), escolas × alunos, crédito e risco. "Qualquer modelo supervisionado ganha capacidade preditiva ao incorporar contexto."

## Armadilhas e confusões comuns
| Confusão | O correto |
|---|---|
| Dummies de escola equivalem ao multinível | dummies **não** modelam a variância entre contextos |
| Efeito fixo = efeito aleatório | fixo = comum à população; aleatório = **varia entre grupos** |
| ICC alto = pouco efeito do contexto | ICC alto = **muito** efeito do contexto |
| Previsão usa só os γ | some também **ν₀ⱼ e ν₁ⱼ·x** do grupo |
| Multinível exige hierarquia explícita | pode-se criar **contexto latente** via cluster |
| Grupo com 1 observação ajuda | é **descartado** (sem variância) |
| ν₀ⱼ = diferença nas inclinações | ν₀ⱼ = interceptos; **ν₁ⱼ = inclinações** |

## Resumo-relâmpago
- Nível 1 dentro de nível 2 (e 3). Efeitos fixos (γ) + aleatórios (ν, τ) + erro (ε).
- Primeiro teste: variâncias aleatórias ≠ 0. Comparar com LR. ICC = var grupo ÷ (var grupo + var erro).
- Previsão = parte fixa + efeitos aleatórios do grupo.

## Teste-se
1. Variância entre grupos = 12 e residual = 28. Qual o ICC?
<details markdown="1"><summary>Ver resposta</summary>12 ÷ (12 + 28) = 0,30 (30% de efeito do contexto).</details>

2. O que ν₁ⱼ representa?
<details markdown="1"><summary>Ver resposta</summary>A variação da inclinação entre grupos (o efeito de X difere entre contextos).</details>

3. Por que não usar OLS com dummies de escola?
<details markdown="1"><summary>Ver resposta</summary>Porque não separam efeitos observáveis dos não observáveis nem capturam a variância entre contextos.</details>

4. Quais são os níveis de um modelo de medidas repetidas de alunos em escolas?
<details markdown="1"><summary>Ver resposta</summary>Tempo (N1) → aluno (N2) → escola (N3).</details>

## Pergunta típica
Definição e sinônimos de modelagem multinível · por que não OLS nem dummies · efeito fixo × aleatório · primeira verificação (variância dos efeitos aleatórios) · como comparar modelos (LR, log-likelihood) · calcular ICC · interpretar ν₀ⱼ e ν₁ⱼ · montar a previsão com a equação final · níveis em medidas repetidas · paradoxo de Simpson · cluster como contexto latente
