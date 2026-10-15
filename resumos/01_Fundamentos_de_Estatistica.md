# 01 · Fundamentos de Estatística
**Prof. Wilson Tarantin Jr. · 3 aulas · Prioridade: ALTA — base de regressão, logística, contagem, multinível, PCA e séries temporais**

> **Em uma frase:** estatística é o conjunto de regras para **resumir dados** (descritiva) e para **decidir com segurança a partir de uma amostra** (inferência), sabendo o quanto você pode errar.

**Pré-requisitos:** nenhum. **Vem depois:** todo o resto de modelagem (17–20, 14–16, 22).

## Por que isso importa (intuição)
Você nunca vê a população inteira (todos os clientes, todas as peças); vê uma **amostra**. Duas perguntas guiam o capítulo:
1. *Como descrevo bem o que eu tenho?* → medidas de posição, dispersão e forma.
2. *Posso generalizar para o que não vi?* → distribuições de probabilidade e testes de hipóteses.

Para quem programa: pense em **variável = coluna tipada**. O tipo da coluna decide quais operações fazem sentido (não se faz `mean()` de uma coluna categórica).

---

## 1. Tipos de variável — a primeira decisão sempre
- **Qualitativa (categórica):** categorias sem valor numérico real (estado civil, cor, "aprovado/reprovado", faixa de renda, escala Likert). Só admite **tabela de frequências**, gráficos de barras e a **moda**.
- **Quantitativa (métrica):** número com significado (idade, renda em R$, retorno). Admite tudo: posição, dispersão, forma. Pode ser **discreta** (contagem: nº de filhos) ou **contínua** (altura, salário).

**Exemplo.** "Faixa de renda" (0–2 mil, 2–4 mil…) é qualitativa; "renda em reais" é quantitativa. Transformar a segunda na primeira perde informação — por isso só se agrupa em faixas quando for preciso montar tabela de frequências.

**Armadilha clássica — ponderação arbitrária:** codificar cores (azul=1, verde=2, …) e calcular a média ("cor média = 5,68") **não significa nada**, porque os números são rótulos, não quantidades.

## 2. Estatística descritiva (uma variável)

### Tabela de frequências
Conta quantas vezes cada valor/classe aparece. Quatro versões: **absoluta**, **relativa (%)**, **absoluta acumulada** e **relativa acumulada**. Variável contínua precisa ser agrupada em classes antes.

### Medidas de posição — "onde está o centro?"
- **Média:** soma ÷ n. Usa todos os valores, mas é **puxada por extremos (outliers)**.
- **Mediana:** valor do meio (com n par, média dos dois centrais). **Robusta a outliers.**
- **Moda:** valor mais frequente; pode não existir ou haver várias; é **a única que serve para qualitativas**.
- **Percentis/quartis:** P25 = 179 significa "25% dos valores são ≤ 179". Q1 = P25, Q2 = mediana = P50, Q3 = P75.

**Exemplo resolvido.** Salários (mil R$): 3; 3,2; 3,5; 4; 30.
Média = 43,7 ÷ 5 = **8,74**; mediana = **3,5**. Um único salário alto arrasta a média para um valor que **ninguém ganha** — por isso em dados com cauda longa a mediana descreve melhor.

### Medidas de dispersão — "o quanto os dados se espalham?"
- **Amplitude:** máx − mín (muito sensível a outlier). **AIQ** (amplitude interquartil) = Q3 − Q1.
- **Variância amostral:** Σ(Xi − X̄)² ÷ (n−1). Mede o desvio médio ao quadrado (unidade ao quadrado). Divide por **n−1** porque a média da amostra já "gastou" um grau de liberdade.
- **Desvio padrão:** √variância; **mesma unidade** da variável.
- **Erro padrão:** S ÷ √n = desvio padrão **da média**. Mostra o quanto a média amostral variaria entre amostras.
- **Coeficiente de variação (CV):** (S ÷ X̄) × 100 = dispersão **relativa**, serve para comparar variáveis de escalas diferentes.

**Exemplo resolvido.** Dados 2, 4, 6 → média 4; desvios −2, 0, 2; quadrados 4, 0, 4 (soma 8). Variância = 8 ÷ 2 = **4**; desvio padrão = **2**.
**Erro padrão:** com S = 10, n = 100 → 1; com n = 400 → 0,5. **Quadruplicar a amostra só dobra a precisão** (por causa da raiz).
**CV:** A (média 100, S 10) → 10%; B (média 5, S 2) → 40%. B é **4× mais heterogênea**, embora seu desvio padrão seja menor.

**Outlier (regra de Tukey):** valor < Q1 − 1,5·AIQ ou > Q3 + 1,5·AIQ. Com Q1 = 10 e Q3 = 20 (AIQ = 10) os limites são −5 e 35; um valor 40 é outlier.

### Medidas de forma
- **Assimetria (g1):** 0 = simétrica; **> 0 = cauda longa à direita (média > mediana)**; < 0 = cauda à esquerda.
- **Curtose (g2):** 0 = como a normal (mesocúrtica); > 0 = pontuda/caudas pesadas (leptocúrtica); < 0 = achatada (platicúrtica).

## 3. Distribuições de probabilidade — o "molde" teórico
Uma distribuição descreve **quais valores uma variável pode assumir e com que probabilidade**. Probabilidades ficam entre 0 e 1 e somam 1.

### Discretas (contagens e sim/não) — e onde cada uma reaparece no curso
- **Bernoulli:** **um** ensaio, dois resultados (sucesso com prob. p, fracasso 1−p). **Base da regressão logística binária.**
- **Binomial:** **n** ensaios Bernoulli independentes com p constante; conta o **nº de sucessos** k. P(k) = C(n,k)·pᵏ·(1−p)ⁿ⁻ᵏ. Base da logística multinomial.
- **Binomial negativa:** nº de ensaios até obter k sucessos; base do **modelo de contagem binomial negativo** (dados com superdispersão).
- **Poisson:** nº de eventos numa **janela** (tempo/área) com taxa média λ. P(k) = e⁻ˡ·λᵏ ÷ k! (com e⁻ˡ = e elevado a −λ). Base do **modelo de contagem Poisson** (média ≈ variância).

**Como escolher:** *conto sucessos em n tentativas?* → Binomial. *Conto eventos soltos numa janela contínua, sem "n" definido?* → Poisson.

**Exemplos resolvidos.**
- Binomial: 3 lançamentos de moeda, P(exatamente 2 caras) = C(3,2)·0,5²·0,5 = 3 × 0,125 = **0,375**.
- Poisson: λ = 2 pacientes/ano → P(1 paciente) = e⁻²·2 = **27,07%** (valor visto em aula).

### Contínuas
- **Normal:** curva em sino, simétrica, definida por μ e σ. **Regra empírica:** ±1σ ≈ 68%, ±2σ ≈ 95%, ±3σ ≈ 99,7%.
- **Normal padrão / Z-score:** Z = (X − μ) ÷ σ → média 0, desvio 1. **Muda a escala, não a forma.** Responde "a quantos desvios padrão do centro este valor está?". Ex.: retorno médio 2,8%, σ 1,2%; P(retorno > 4%) = P(Z > 1) = **15,87%**.
- **Qui-quadrado (χ²):** assimétrica à direita; usada em testes de **associação entre categóricas**.
- **t de Student:** parece a normal com **caudas mais pesadas** (mais chance de extremos) — compensa a incerteza de **σ desconhecido em amostras pequenas**. Com mais graus de liberdade, converge para a normal.
- **F de Snedecor:** **razão de variâncias**; assimétrica à direita; tem dois graus de liberdade.
- **Graus de liberdade (gl):** nº de valores que podem variar livremente. Se 5 números devem somar 18, quatro são livres e o quinto fica determinado → gl = 4 = n−1.

## 4. Testes de hipóteses — a lógica

**Ideia central (analogia do tribunal):** presume-se "inocente" (H0) até a evidência ser forte o bastante para rejeitá-la. Você **nunca prova** H0; só decide se os dados são **incompatíveis** com ela.

**Passo a passo (sempre igual):**
1. **H0** = "não há efeito/diferença" (sempre com igualdade). **H1** = o que você quer mostrar.
2. O sinal de H1 define o tipo: **bilateral** (≠), **unilateral à esquerda** (<) ou **à direita** (>).
3. Escolha **α** (1%, 5% ou 10%) = probabilidade máxima de rejeitar H0 **sendo ela verdadeira**. Nível de confiança = 1 − α.
4. Calcule a **estatística de teste** e compare com o **valor crítico**; ou use o **p-valor**: **p < α → rejeita H0**.

**O que é o p-valor:** *se H0 fosse verdadeira, quão raro seria observar um resultado ao menos tão extremo quanto o meu?* p pequeno → resultado raro sob H0 → desconfia de H0.

- **Erro tipo I:** rejeitar H0 sendo verdadeira (probabilidade = **α**) — "alarme falso".
- **Erro tipo II:** não rejeitar H0 sendo falsa — "deixar o culpado passar".

### Qual teste usar?
| Situação | Teste | Estatística |
|---|---|---|
| 2 variáveis **qualitativas** (associação?) | **Qui-quadrado de associação** | χ² = Σ(obs − esp)² ÷ esp; gl = (L−1)(C−1) |
| 2 variáveis **quantitativas** (correlação?) | **r de Pearson + teste t** | r = cov(X,Y) ÷ (Sx·Sy); t = r ÷ √[(1−r²)÷(n−2)]; gl = n−2 |
| Média de 1 amostra, σ conhecido (ou n grande) | **Teste Z** | Z = (X̄ − μ0) ÷ (σ/√n) |
| Média de 1 amostra, σ desconhecido | **Teste t** | t = (X̄ − μ0) ÷ (S/√n); gl = n−1 |
| 1 variável categórica: observado × esperado | **χ² de aderência** | χ² = Σ(O−E)²÷E; gl = k−1 |
| Variâncias de 2 amostras | **Teste F** | F = S²maior ÷ S²menor |
| Médias de 2 amostras independentes | **t de duas amostras** | faça antes o teste F: variâncias iguais → variância combinada; diferentes → Welch |

**Intervalo de confiança da média:** X̄ ± (Z ou t) × erro padrão. Um IC de 95% que **não contém** o valor de H0 equivale a rejeitar H0 a 5%.

### Exemplos resolvidos
**(a) Teste t, 1 amostra.** Um fabricante afirma μ = 100. Amostra: n = 25, X̄ = 104, S = 10. H0: μ = 100; H1: μ ≠ 100.
t = (104 − 100) ÷ (10/√25) = 4 ÷ 2 = **2,0**; gl = 24. O valor crítico bilateral a 5% é ≈ **2,064**. Como 2,0 < 2,064 → **não rejeita H0** (evidência insuficiente a 5%, mesmo a diferença parecendo grande).

**(b) Qui-quadrado de associação.** Tabela 2×2 (sexo × comprou?): observados [[30, 20], [10, 40]]; N = 100. Totais: linhas 50/50; colunas 40/60.
Esperados = (total linha × total coluna) ÷ N → 20, 30, 20, 30. χ² = 100/20 + 100/30 + 100/20 + 100/30 ≈ **16,7**; gl = (2−1)(2−1) = 1; crítico a 5% = 3,84 → **rejeita H0**: há associação.

**(c) Correlação.** r = 0,5 com n = 27 → t = 0,5 ÷ √(0,75/25) ≈ **2,89**; gl = 25 → significativa a 5%.

---

## Armadilhas e confusões comuns
| Confusão | O correto |
|---|---|
| "p = 0,03 significa 3% de chance de H0 ser verdadeira" | p é a probabilidade dos **dados** (ou mais extremos) **se H0 for verdadeira**, não de H0 |
| "Não rejeitei H0, logo H0 é verdadeira" | só significa **evidência insuficiente** para rejeitar |
| α e p-valor são a mesma coisa | α é **escolhido antes** (tolerância ao erro tipo I); p é **calculado dos dados** |
| Tirar média/mediana de variável qualitativa | só **moda** e frequências |
| Usar desvio padrão para comparar variáveis com escalas diferentes | use o **CV** |
| Média = mediana sempre | **média > mediana** indica cauda à direita |
| Binomial × Poisson | Binomial: nº **fixo** de tentativas; Poisson: eventos numa janela, **sem teto** natural |
| Mais amostra faz o desvio padrão diminuir | diminui o **erro padrão** (o desvio padrão da variável não muda) |

## Resumo-relâmpago
- Tipo da variável decide a ferramenta. Qualitativa → frequência e moda.
- Média é sensível a outliers; mediana não. Média > mediana → cauda à direita.
- Variância usa n−1; erro padrão = S/√n; CV compara escalas diferentes.
- Bernoulli → logística binária; Binomial → logística multinomial; Poisson e Binomial negativa → contagem.
- Teste: H0 com igualdade; **p < α → rejeita H0**; α = prob. do erro tipo I.
- Associação entre categóricas = χ²; entre métricas = Pearson; médias = Z/t; variâncias = F.

## Teste-se (responda antes de abrir a resposta)
1. Por que "média da cor do carro = 5,68" não faz sentido?
<details markdown="1"><summary>Ver resposta</summary>Porque os números são apenas rótulos de categorias (ponderação arbitrária); a média só vale para variável quantitativa. Para cor, use frequências e moda.</details>

2. Em um teste com α = 5% e p = 0,03, qual a decisão? E com α = 1%?
<details markdown="1"><summary>Ver resposta</summary>Com 5%: p < α → rejeita H0. Com 1%: p > α → não rejeita H0.</details>

3. Quantos graus de liberdade tem o χ² de associação de uma tabela 3×4?
<details markdown="1"><summary>Ver resposta</summary>(3−1)(4−1) = 6.</details>

4. A distribuição t tem caudas mais longas ou mais curtas que a normal? Por que isso importa?
<details markdown="1"><summary>Ver resposta</summary>Mais longas. Em amostras pequenas com σ desconhecido, há mais incerteza; as caudas pesadas evitam subestimar a variabilidade (valores críticos maiores).</details>

5. Qual teste fazer antes de comparar as médias de dois grupos, e para quê?
<details markdown="1"><summary>Ver resposta</summary>O teste F de variâncias, para escolher entre o t com variâncias iguais (variância combinada) ou com variâncias diferentes (Welch).</details>

6. Dados 2, 4, 6: quanto vale a variância amostral?
<details markdown="1"><summary>Ver resposta</summary>Média 4; soma dos quadrados dos desvios = 8; 8 ÷ (3−1) = 4.</details>

## Pergunta típica
Para variável qualitativa, qual medida de posição posso usar · o que significa p < α · α é a probabilidade de qual erro · média > mediana indica qual assimetria · por que mais amostra reduz o erro padrão · quando usar o CV · qual teste para associação entre categóricas e qual para duas métricas · qual distribuição está na base de cada modelo (Bernoulli, Binomial, Poisson, Binomial negativa) · diferença entre Z e t

*Fonte: slides do Prof. Tarantin (baseados em Fávero e Belfiore, "Manual de análise de dados") e transcrições das 3 aulas. Exercícios: lista complementar e planilha de suporte da aula.*
