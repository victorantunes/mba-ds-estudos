# 13 · Modelagem Matemática e Estruturação de Problemas Complexos (AHP)
**Prof. Dr. Marcos dos Santos (Marinha, IME/ITA/UFF) · 2 aulas · Prioridade: alta (cálculo passo a passo de AHP e AHP-Gaussiano)**

> **Destaque do professor.** *"Na matriz de ponderações, a diagonal principal tem valores sempre: 1"* e *"se estou comparando custo com custo, o grau tem que ser um."*

## O fio condutor deste capítulo

Comprar um celular: o mais barato tem a pior câmera; o melhor tem preço alto. Você pesa critérios de cabeça e, no fim, não sabe justificar a escolha. A **decisão multicritério** organiza esse raciocínio. O **AHP** faz isso de um jeito intuitivo: em vez de ponderar tudo ao mesmo tempo, você **compara critérios dois a dois** ("o custo é moderadamente mais importante que a câmera?") e o método converte esses julgamentos em **pesos** e **notas**, levando a um ranking transparente e justificável.

O capítulo apresenta o problema da decisão multicritério, o AHP clássico (com um exemplo numérico completo, incluindo a checagem de consistência) e o **AHP-Gaussiano**, uma variante que dispensa as comparações par a par ao tirar os pesos dos próprios dados.

```mermaid
flowchart TD
  O["Objetivo: escolher o celular"] --> C1["Critério: Custo"]
  O --> C2["Critério: Câmera"]
  O --> C3["Critério: Armazenamento"]
  O --> C4["Critério: Bateria"]
  C1 --> A1["Alternativas: Xiaomi, Samsung, iPhone"]
  C2 --> A1
  C3 --> A1
  C4 --> A1
```

## 1. O problema da decisão multicritério

A pesquisa operacional é a abordagem científica para **ajudar quem decide a decidir melhor**. Há decisão sempre que existe um problema com **mais de uma alternativa**, e toda decisão tem ganho e perda. O problema é descrito por uma **matriz de decisão** (alternativas × critérios) acompanhada dos **pesos dos critérios**. Métodos conhecidos: **AHP, ANP, PROMETHEE, ELECTRE, TOPSIS**. Para cada critério é preciso informar se é **de lucro** (quanto maior, melhor) ou **de custo** (quanto menor, melhor).

## 2. AHP (Analytic Hierarchy Process, Saaty, anos 1970)

O AHP é simples e flexível, baseado em matemática e **psicologia (escala psicométrica)**; aceita julgamentos subjetivos e garante **transparência e rastreabilidade**. O primeiro passo é montar a **hierarquia**: objetivo → critérios → alternativas. Os julgamentos usam a **escala de Saaty**:

| Valor | Significado |
|---|---|
| 1 | igual importância |
| 3 | moderadamente mais importante |
| 5 | mais importante |
| 7 | muito mais importante |
| 9 | extremamente mais importante |
| 2, 4, 6, 8 | valores intermediários |
| 1/3, 1/5, 1/7, 1/9 | **recíprocos** (o inverso do julgamento) |

A **matriz de julgamentos** é quadrada; a **diagonal principal vale sempre 1**; vale a **reciprocidade** (se \(a_{ij} = 3\), então \(a_{ji} = 1/3\)); e o número de comparações é \(\frac{n(n-1)}{2}\).

### O passo a passo

1. **Normalizar** a matriz: dividir cada elemento pela **soma da sua coluna**.
2. **Vetor de prioridades (pesos)** = **média de cada linha** da matriz normalizada.
3. **Consistência:** calcular \(\lambda_{max}\) e depois
\[ CI = \frac{\lambda_{max} - n}{n-1} \qquad\qquad CR = \frac{CI}{RI} \]
com o índice aleatório de Saaty \(RI\): 0,58 (n = 3), 0,90 (n = 4), 1,12 (n = 5), 1,24 (n = 6), 1,32 (n = 7). **CR < 10% = consistente.**
4. Julgar as **alternativas em cada critério** (ou normalizar dados quantitativos).
5. **Agregar:** nota global = soma de (peso do critério × prioridade da alternativa).

> **Exemplo resolvido (3 critérios).** Matriz de julgamentos entre A, B e C: \(\begin{pmatrix}1&3&5\\1/3&1&3\\1/5&1/3&1\end{pmatrix}\).
> **Soma das colunas:** 1,533 · 4,333 · 9.
> **Normalizada:** linha A = 0,652 · 0,692 · 0,556; linha B = 0,217 · 0,231 · 0,333; linha C = 0,130 · 0,077 · 0,111.
> **Pesos (médias das linhas):** A = **0,633**, B = **0,260**, C = **0,106** (somam 1).
> **Consistência:** multiplicando a matriz pelo vetor de pesos e dividindo cada resultado pelo peso respectivo obtém-se ≈ 3,07; 3,03; 3,01, logo \(\lambda_{max} \approx 3{,}04\). \(CI = (3{,}04-3)/2 \approx 0{,}019\) e \(CR = 0{,}019/0{,}58 \approx 0{,}033\) (3,3%), **abaixo de 10%: consistente**.

### Dados quantitativos e critérios de custo

Quando os dados são números (preço, GB, horas de bateria), **não é preciso comparar par a par**: **normaliza-se** a coluna dividindo cada valor pela soma. Para um critério de **custo**, usa-se o **inverso (1/x)** antes de normalizar (preços 1500, 1800 e 5000 viram 0,469; 0,391; 0,141). Normalizar torna a matriz **adimensional**, o que permite somar critérios de unidades diferentes.

**Limitações:** funciona bem até cerca de **7 critérios**; o número de comparações cresce rápido; há **desgaste cognitivo** do decisor e **é difícil obter CR < 10%**.

## 3. AHP-Gaussiano (Santos et al., 2020/2021)

Nasceu de um problema real da **Marinha do Brasil** (escolha de um navio). A ideia: os **pesos dos critérios saem dos próprios dados**, pela **dispersão**, **sem comparação par a par**. Isso reduz o esforço cognitivo e a subjetividade e serve para muitas alternativas e critérios.

> **Intuição.** Um critério em que todas as alternativas são parecidas **não ajuda a decidir** (peso baixo). Um critério em que elas **diferem muito** discrimina mais (peso alto).

| Passo | O que se faz |
|---|---|
| 1 | montar a matriz de decisão |
| 2 | normalizar (custo: inverso; lucro: ÷ soma) |
| 3 | calcular a média de cada critério (sempre \(1/n\)) |
| 4 | calcular o **desvio padrão** de cada critério |
| 5 | **fator gaussiano = desvio padrão ÷ média** (o coeficiente de variação) |
| 6 | **normalizar os fatores** (÷ soma): o resultado é o **peso** do critério |
| 7–8 | agregar (peso × valor normalizado) e ranquear |

## O que levar daqui

O AHP converte comparações par a par em pesos, checados por consistência. A matriz tem diagonal 1 e reciprocidade; os pesos são a média das linhas da matriz normalizada; CR < 10% é consistente. Critérios de custo usam o inverso. O AHP-Gaussiano obtém os pesos do coeficiente de variação dos dados, sem comparação par a par.

## Erros que todo mundo comete

| Erro | Correção |
|---|---|
| "A diagonal da matriz pode variar" | é **sempre 1** |
| "Se \(a_{ij} = 3\), então \(a_{ji} = 3\)" | \(a_{ji} = 1/3\) (reciprocidade) |
| "CR alto é aceitável" | o limite é **CR < 10%** |
| "Peso = soma das linhas" | peso = **média das linhas** da matriz normalizada |
| "Critério de custo normaliza direto" | custo usa o **inverso** antes de normalizar |
| "O AHP-Gaussiano pede comparação par a par" | **não**: o peso vem do CV dos dados |

## Teste-se

1. Quantas comparações par a par para 5 critérios?
<details markdown="1"><summary>Ver resposta</summary>5·4/2 = 10.</details>

2. Se \(a_{ij} = 5\), quanto vale \(a_{ji}\)?
<details markdown="1"><summary>Ver resposta</summary>1/5.</details>

3. CI = 0,06 com n = 4 (RI = 0,90). A matriz é consistente?
<details markdown="1"><summary>Ver resposta</summary>CR = 0,06/0,90 ≈ 0,067 (6,7%) < 10%: sim.</details>

4. Como o AHP-Gaussiano obtém os pesos?
<details markdown="1"><summary>Ver resposta</summary>Pelo fator gaussiano (desvio padrão ÷ média) de cada critério, normalizado pela soma, sem comparação par a par.</details>

## Pergunta típica
Calcular o vetor de prioridades (normalizar pela soma da coluna e tirar a média das linhas) · calcular CI/CR com RI dado e decidir se é consistente · aplicar reciprocidade e identificar a diagonal (=1) · critério de custo × lucro · o que muda no AHP-Gaussiano · limitações do AHP
