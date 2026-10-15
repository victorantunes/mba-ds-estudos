# 01 · Fundamentos de Estatística
**Prof. Wilson Tarantin Jr. · 3 aulas (09, 14 e 16/05/2025) · Base de TODO o resto do curso (ML, regressão, testes)**
**Prioridade de estudo: ALTA** (é pré-requisito de Regressão, Logística, Contagem, Multinível, PCA e Séries Temporais).

> Para quem programa: pense em "variável" como uma coluna tipada. A primeira decisão em qualquer análise é **o tipo da coluna**, porque ele define quais ferramentas são válidas.

---
## 1. Tipos de variável (primeira decisão sempre)
| Tipo | Também chamada | Exemplos | O que pode calcular |
|---|---|---|---|
| **Qualitativa** | categórica, não métrica | país, estado civil, cor, faixa de renda, escala Likert, "crédito aprovado ou não" | só **tabela de frequências** e gráficos. Moda é a única medida de posição possível |
| **Quantitativa** | métrica | idade, renda em R$, peso, retorno de ação, nº de filhos | tudo: posição, dispersão, forma |

- Quantitativa **discreta** = contagem (nº de filhos). **Contínua** = qualquer valor real (altura, salário).
- **Armadilha clássica: "ponderação arbitrária"** → transformar categoria em número (primavera=1, verão=2…) e tirar a média. É **errado**: a "média 5,68" de cores de carro não significa nada. Isso não deve ser feito.
- Faixa de renda é qualitativa; renda em reais é quantitativa.

## 2. Estatística descritiva univariada
**Tabela de frequências** (4 tipos): absoluta, relativa (%), absoluta acumulada, relativa acumulada. Variável contínua → precisa agrupar em classes/faixas antes.

**Medidas de posição**
- **Média** = soma / n. Sensível a valores extremos (outliers).
- **Mediana** = valor central (n ímpar: posição (n+1)/2; n par: média dos dois centrais). Robusta a outliers.
- **Moda** = mais frequente; pode não existir; **única que serve para qualitativas**.
- **Percentis** dividem em 100 partes, **quartis** em 4 (Q1=P25, Q2=mediana=P50, Q3=P75), **decis** em 10. Interpretação: P25 = 179 → 25% dos valores são ≤ 179 e 75% são ≥ 179. Percentil pode ser **interpolado** (um valor que nem existe na amostra).

**Medidas de dispersão**
| Medida | Fórmula/ideia | Nota |
|---|---|---|
| Amplitude | máx − mín | muito sensível a outlier |
| Amplitude interquartil (AIQ) | Q3 − Q1 | base do boxplot |
| **Variância amostral** | Σ(Xi − X̄)² / (n−1) | unidade ao quadrado |
| **Desvio padrão** | √variância | mesma unidade da variável |
| **Erro padrão** | S / √n | desvio padrão **da média**. Maior n → menor erro → média mais precisa. É insumo do intervalo de confiança |
| **Coeficiente de variação** | (S / X̄) × 100 | dispersão **relativa**: permite comparar variáveis com escalas diferentes. Menor CV = mais homogêneo |

**Outlier univariado (regra de Tukey):** valor < Q1 − 1,5·AIQ  ou  > Q3 + 1,5·AIQ.

**Medidas de forma**
- Assimetria (g1 de Fisher): g1 = 0 simétrica (média = mediana = moda); g1 > 0 cauda longa à direita (**média > mediana**); g1 < 0 cauda à esquerda (média < mediana).
- Curtose (g2 de Fisher): g2 = 0 normal (mesocúrtica); g2 > 0 alongada/pontuda (leptocúrtica); g2 < 0 achatada (platicúrtica).

## 3. Distribuições de probabilidade (teóricas, populacionais)
Regras gerais: probabilidades entre 0 e 1; soma = 1. **Distribuições são para variáveis quantitativas.**

**Discretas** (e a conexão com os modelos que vêm depois):
| Distribuição | Quando | Fórmula | Vira base de… |
|---|---|---|---|
| Uniforme discreta | todos os resultados equiprováveis (dado) | P = 1/n | — |
| **Bernoulli** | 1 experimento, 2 resultados (sucesso x=1 prob p; fracasso x=0 prob 1−p) | p^x · (1−p)^(1−x) | **Regressão logística binária** |
| **Binomial** | n repetições independentes de Bernoulli, p constante; conta nº de sucessos k | C(n,k)·p^k·(1−p)^(n−k) | **Regressão logística multinomial** |
| **Binomial negativa** | nº de ensaios x até obter k sucessos | | **Modelo de contagem binomial negativo** (dados com superdispersão/cauda longa) |
| **Poisson** | nº de sucessos k numa **exposição** (tempo, área); λ = taxa média | e^(−λ)·λ^k / k! | **Modelo de contagem Poisson** (equidispersão: média ≈ variância) |

Exemplos resolvidos em aula: Bernoulli com p=0,48 → P(1)=48%, P(0)=52%. Binomial p=6,5%, n=12 lotes: P(k=2)=14,24%; P(k=4)=0,52%. Poisson λ=2/ano: P(1 paciente)=27,07%; P(6)=1,2%.

**Contínuas:**
- **Normal:** sino, simétrica, parâmetros μ e σ. Regra empírica: μ±1σ → 68,26%; ±2σ → 95,44%; ±3σ → 99,74%.
- **Normal padrão (Z-score):** Z = (X − μ)/σ → média 0 e desvio 1. A padronização muda a escala, **não** a forma da distribuição. Ex.: retorno médio 2,8%, desvio 1,2%: P(retorno > 4%) = P(Z > 1) = 15,87%.
- **Qui-quadrado (χ²):** assimétrica positiva; com mais graus de liberdade fica mais simétrica. Usada em **testes de associação** de variáveis categóricas.
- **t de Student:** parecida com a normal, **caudas mais longas** → mais prob. de valores extremos; para **pequenas amostras**/variância desconhecida; com mais graus de liberdade → tende à normal.
- **F de Snedecor:** razão de variâncias; assimétrica positiva; graus de liberdade no numerador e no denominador.
- **Graus de liberdade** = "quantas observações podem variar livremente". Ex.: 5 números somando 18: 4 livres, o 5º é determinado → 4 = n−1 gl. Cada teste tem seu cálculo; **mudam o valor crítico**.

## 4. Testes de hipóteses (a estrutura é sempre a mesma)
1. **H0 (nula)** = "não há efeito / não há diferença / está no padrão" (sempre com igualdade). **H1 (alternativa)** = o que você investiga.
2. Tipo do teste decorre de H1: **bilateral** (H1: θ ≠ θ0, região crítica nas 2 caudas), **unilateral à esquerda** (H1: θ < θ0), **unilateral à direita** (H1: θ > θ0).
3. Escolher **α** (nível de significância; usuais 1%, 5%, 10%). **Nível de confiança = 1 − α.** α define o tamanho da **região crítica (RC)**.
4. Calcular a **estatística de teste**. Se cair na RC → **rejeita H0** (H1 plausível). Se cair na RN (região de não rejeição) → **não rejeita H0**.
5. Equivalente via **p-valor**: **p < α → rejeita H0**; p > α → não rejeita.

**Erros:** **Tipo I** = rejeitar H0 sendo verdadeira (prob. = **α**). **Tipo II** = não rejeitar H0 sendo falsa.

**Qual teste usar?**
| Situação | Teste | Estatística / distribuição |
|---|---|---|
| 2 variáveis **qualitativas** (há associação?) | **Qui-quadrado de associação** | tabela de contingência → freq. esperada = (total linha × total coluna)/N → resíduo = obs − esp → χ² = Σ resíduo²/esp; gl = (I−1)(J−1). H0: associação aleatória |
| 2 variáveis **quantitativas** (correlação) | **r de Pearson** + teste t | r = cov(X,Y)/(Sx·Sy), vai de −1 a 1; t = r / √((1−r²)/(n−2)), gl = n−2. H0: r = 0 (bicaudal) |
| Média de 1 amostra, **σ populacional conhecido** (ou n grande, normal) | **Teste Z** | Z = (X̄ − μ0)/(σ/√n) |
| Média de 1 amostra, **σ desconhecido** | **Teste t** | t = (X̄ − μ0)/(S/√n), gl = n−1 |
| Frequências observadas vs esperadas (1 variável categórica) | **χ² de uma amostra** | χ² = Σ(O−E)²/E, gl = k−1 |
| Comparar **variâncias** de 2 amostras | **Teste F** | F = S²maior / S²menor, gl n−1 e n−1; decisão na cauda direita |
| Comparar **médias** de 2 amostras independentes | **t de duas amostras** | antes faça o teste F: variâncias iguais → usa variância combinada Sp, gl = n1+n2−2; diferentes → gl de Welch |

**Intervalo de confiança da média:** IC = X̄ ± Z·(erro padrão) (n grande/σ conhecido) ou X̄ ± t·(erro padrão) (n pequeno/σ desconhecido, gl = n−1).

Exemplos feitos em aula (úteis para treinar): caixas de papelão (Z, H1: μ>100, rejeita H0, p≈0,01); tempo de processamento (t, 25 obs, média 16,808 vs 18, α=1%, **não rejeita**); rotas de entrega (F, rota B tem variância maior, rejeita H0, p=0,005); fornos A e B (t de 2 amostras, médias diferentes); correlação notas: só matemática–física foi significativa.

---
## O que mais cai (dicas do professor e do estilo da prova)
- "Para variável qualitativa, qual medida de posição posso usar?" → **moda** (e tabela de frequências). Média/mediana/desvio **não**.
- Rejeitar H0 quando p < α. α = prob. do **erro tipo I**. Nível de confiança = 1 − α.
- Média > mediana → assimetria à **direita**.
- Mais amostra → **menor erro padrão** → estimativa mais precisa.
- CV compara dispersão entre variáveis com escalas diferentes.
- Associação entre 2 categóricas = **qui-quadrado**; entre 2 métricas = **Pearson**.
- Bernoulli → logística binária; Binomial → logística multinomial; Poisson e Binomial negativa → modelos de contagem.

## Mini-quiz (responda sem consultar)
1. Por que "média da cor do carro = 5,68" não faz sentido?
2. A distribuição t tem caudas mais longas ou mais curtas que a normal? Por que isso importa em amostras pequenas?
3. Em um teste com α = 5% e p-valor = 0,03, qual a decisão? E se α = 1%?
4. Quantos graus de liberdade tem um χ² de associação com tabela 3×4?
5. Qual teste faço antes de comparar médias de dois grupos, e para quê?

**Respostas:** 1) ponderação arbitrária de categoria; 2) mais longas, evita subestimar a variabilidade; 3) rejeita H0; com 1% não rejeita; 4) (3−1)(4−1)=6; 5) teste F de variâncias, para escolher entre variâncias iguais/diferentes no t.

*Fonte: slides do Prof. Tarantin (baseados em Fávero e Belfiore, "Manual de análise de dados") e transcrições das 3 aulas. Planilhas de apoio (Excel) estão em `aulas\2025-05-09 …\Materiais\`.*
