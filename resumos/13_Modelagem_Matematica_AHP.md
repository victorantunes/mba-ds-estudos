# 13 · Modelagem Matemática e Estruturação de Problemas Complexos (AHP)
**Prof. Dr. Marcos dos Santos (Marinha, IME/ITA/UFF) · 2 aulas · Prioridade: ALTA (cálculo passo a passo de AHP e AHP-Gaussiano; destaque do professor sobre a matriz de julgamentos)**

> **Em uma frase:** quando há várias alternativas e vários critérios conflitantes, o AHP transforma **julgamentos par a par** em **pesos e notas** que levam a um ranking transparente e justificável.

**Pré-requisitos:** média e desvio padrão (01). **Vem depois:** 26 (otimização) usa outra face da pesquisa operacional.

> **Destaque do professor:** *"na matriz de ponderações, a diagonal principal tem valores sempre 1"* e *"se estou comparando custo com custo, o grau tem que ser um."*

## Por que isso importa (intuição)
Comprar um celular: o mais barato tem a pior câmera; o melhor tem preço alto. Você pesa critérios **de cabeça**. O AHP organiza isso: compare **dois critérios por vez** ("custo é moderadamente mais importante que câmera?"), calcule os pesos e some as notas. É mais fácil julgar pares do que ponderar tudo de uma vez.

## 1. Contexto
- **Pesquisa Operacional (PO):** abordagem científica para **ajudar quem decide a decidir melhor** (otimização, simulação, apoio multicritério à decisão).
- **Decisão multicritério (MCDM):** descrita por uma **matriz de decisão** (alternativas × critérios) com pesos dos critérios. Métodos: **AHP, ANP, PROMETHEE, ELECTRE, TOPSIS**…
- Para cada critério informe se é **de lucro** (maior é melhor) ou **de custo** (menor é melhor).

## 2. AHP (Analytic Hierarchy Process — Saaty, anos 1970)
- Método **simples e flexível**, baseado em matemática e **psicologia (escala psicométrica)**; aceita julgamentos subjetivos; garante **transparência e rastreabilidade**.
- **Hierarquia:** objetivo → critérios → alternativas.
- **Escala de Saaty:** 1 = igual; 3 = moderadamente mais importante; 5 = mais importante; 7 = muito mais; 9 = extremamente mais; 2, 4, 6, 8 = intermediários; **recíprocos** (1/3, 1/5…).
- **Matriz de julgamentos:** quadrada; **diagonal principal = 1**; **reciprocidade:** se a₍ᵢⱼ₎ = 3, então a₍ⱼᵢ₎ = 1/3; nº de comparações = **n(n−1)/2**.

### Passo a passo
1. **Normalizar:** dividir cada elemento pela **soma da sua coluna**.
2. **Vetor de prioridades (pesos) = média de cada linha** da matriz normalizada.
3. **Consistência:** calcular λmax; **CI = (λmax − n)/(n − 1)**; **CR = CI ÷ RI**. **RI** (aleatório de Saaty): n=3 → 0,58; 4 → 0,90; 5 → 1,12; 6 → 1,24; 7 → 1,32. **CR < 10% → consistente.**
4. Julgar as **alternativas em cada critério** (ou normalizar dados quantitativos) → prioridades locais.
5. **Agregar:** nota global = Σ (peso do critério × prioridade da alternativa).

### Exemplo resolvido (3 critérios)
Matriz (linhas/colunas: A, B, C): [[1, 3, 5], [1/3, 1, 3], [1/5, 1/3, 1]].
- **Somas das colunas:** 1,533 · 4,333 · 9.
- **Normalizada:** linha A = 0,652 · 0,692 · 0,556; linha B = 0,217 · 0,231 · 0,333; linha C = 0,130 · 0,077 · 0,111.
- **Pesos (médias das linhas):** A = **0,633**, B = **0,260**, C = **0,106** (somam 1).
- **Consistência:** multiplicar a matriz pelo vetor de pesos e dividir cada resultado pelo peso respectivo dá ≈ 3,07; 3,03; 3,01 → **λmax ≈ 3,04**. CI = (3,04 − 3)/2 ≈ **0,019**; CR = 0,019 ÷ 0,58 ≈ **0,033 (3,3% < 10%) → consistente.**

### Dados quantitativos e critérios de custo
- Com valores numéricos (preço, GB, horas de bateria) **não precisa comparar par a par:** **normaliza-se** a coluna (÷ soma). Para critério de **custo**, use o **inverso (1/x)** e depois normalize (preços 1500, 1800, 5000 → 0,469; 0,391; 0,141). **Normalizar** deixa a matriz **adimensional**, para somar critérios de unidades diferentes.

### Limitações
Funciona bem até **~7 critérios**; o nº de comparações cresce rápido; **desgaste cognitivo** do decisor; **difícil obter CR < 10%**.

## 3. AHP-Gaussiano (Santos et al., 2020/2021)
- Nasceu de um problema da **Marinha do Brasil** (escolha de navio). **Ideia:** os **pesos dos critérios saem dos próprios dados**, pela **dispersão**, **sem comparação par a par** → menos esforço cognitivo e menos subjetividade; serve para **muitas alternativas e critérios**.
- **Passos:** (1) matriz de decisão → (2) normalização (custo: inverso; lucro: ÷ soma) → (3) média de cada critério (**1/n**) → (4) **desvio padrão** de cada critério → (5) **fator gaussiano = desvio padrão ÷ média (= coeficiente de variação)** → (6) **fator normalizado (÷ soma dos fatores) = peso do critério** → (7–8) agregação e ranking.
- **Intuição:** um critério em que todas as alternativas são parecidas **não ajuda a decidir** (peso baixo); um critério em que elas **diferem muito** discrimina mais (peso alto).

## Armadilhas e confusões comuns
| Confusão | O correto |
|---|---|
| Diagonal da matriz pode variar | é **sempre 1** (comparar com si mesmo) |
| Se aᵢⱼ = 3 então aⱼᵢ = 3 | aⱼᵢ = **1/3** (reciprocidade) |
| CR alto é aceitável | **CR < 10%** é o limite |
| Peso = soma das linhas | peso = **média das linhas** da matriz normalizada |
| Critério de custo normaliza direto | custo usa o **inverso** antes de normalizar |
| AHP-Gaussiano pede comparação par a par | **não**; o peso vem do CV dos dados |
| Muito critério melhora o AHP | acima de ~7 piora (comparações e cansaço) |

## Resumo-relâmpago
- AHP: normalizar por coluna → média das linhas = pesos → CI, CR (RI) → agregar.
- Matriz: diagonal 1, recíproca, n(n−1)/2 comparações.
- Custo: inverso. Gaussiano: peso = CV normalizado, sem par a par.

## Teste-se
1. Quantas comparações par a par para 5 critérios?
<details markdown="1"><summary>Ver resposta</summary>5·4/2 = 10.</details>

2. Se aᵢⱼ = 5, quanto vale aⱼᵢ?
<details markdown="1"><summary>Ver resposta</summary>1/5.</details>

3. CI = 0,06 com n = 4 (RI = 0,90). A matriz é consistente?
<details markdown="1"><summary>Ver resposta</summary>CR = 0,06/0,90 ≈ 0,067 (6,7%) < 10% → sim.</details>

4. Como o AHP-Gaussiano obtém os pesos?
<details markdown="1"><summary>Ver resposta</summary>Pelo fator gaussiano (desvio padrão ÷ média) de cada critério, normalizado pela soma — sem comparação par a par.</details>

## Pergunta típica
Calcular o vetor de prioridades (normalizar pela soma da coluna e tirar a média das linhas) · calcular CI/CR com RI dado e decidir se é consistente · aplicar reciprocidade e identificar a diagonal (=1) · critério de custo × lucro · o que muda no AHP-Gaussiano · limitações do AHP
