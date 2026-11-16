# 26 · Pesquisa Operacional e Modelos de Otimização (I, II, III)
**Prof. Cassiano Augusto Isler · 3 aulas · Prioridade: média-alta (saber MODELAR um enunciado em variáveis, objetivo e restrições é o que se cobra)**

## O fio condutor deste capítulo

Um centro de distribuição precisa decidir quantas caixas de cada tipo enviar, quanto transportar por cada rota, quais terminais ativar. São decisões com muitas combinações e restrições. A **pesquisa operacional (PO)** ensina a **transformar um problema real em um modelo matemático** e a resolvê-lo para obter a melhor decisão. Todo o capítulo gira em torno de um único hábito: *ler o problema em palavras e traduzi-lo em três peças*: **variáveis de decisão, função objetivo e restrições**.

A progressão é esta: primeiro a **modelagem** em si; depois como se **resolve** um modelo pequeno (graficamente e pelo Simplex); em seguida o caso em que as variáveis precisam ser **inteiras** (Branch-and-Bound); e por fim o **modelo misto**, com variáveis contínuas, inteiras e binárias, onde aparecem os padrões mais úteis de modelagem.

```mermaid
flowchart LR
  A["Problema em palavras"] --> B["Variáveis de decisão"]
  A --> C["Função objetivo: max ou min"]
  A --> D["Restrições"]
  B --> E["Modelo matemático"]
  C --> E
  D --> E
  E --> F["Resolver: Simplex, Branch-and-Bound, Solver ou PuLP"]
  F --> G["Interpretar e validar"]
```

## 1. As três peças de todo modelo

| Peça | Pergunta | Exemplo (caixas de livros) |
|---|---|---|
| **Variáveis de decisão** | o que posso escolher? | \(L\) = caixas leves, \(M\) = caixas mistas |
| **Função objetivo** | o que quero maximizar ou minimizar? | maximizar \(Q = 6L + 7M\) (livros entregues) |
| **Restrições** | quais limites existem? (sempre comparam **duas quantidades mensuráveis**) | \(L + M \leq 10\); \(6L + 2M \geq 40\) |

Quando todas as equações são **lineares** (soma de termos "constante × variável", nunca \(x^2\)), tem-se **programação linear (PL)**. Se há variáveis inteiras, é **PLI**; se há inteiras e contínuas juntas, **PLIM (mista)**. O roteiro de modelagem é: entender o problema (conversando com quem o vive) → escrever **em palavras** variáveis, objetivo e restrições → traduzir em equações → resolver → **validar**. **Defina o objetivo antes das restrições**; senão você pode olhar para o ator errado (a livraria, em vez do centro de distribuição).

> **Dica.** **Minimizar \(f\) equivale a maximizar \(-f\).** Uma restrição **flexível** (que pode ser violada a um custo) modela-se com uma variável de folga **penalizada na função objetivo**; uma restrição **absoluta (hard)** nunca pode ser violada.

## 2. Resolvendo um modelo pequeno

Com duas variáveis, o problema se desenha. A **região factível** é o conjunto de pontos que satisfazem **todas** as restrições ao mesmo tempo. A função objetivo vira uma família de **retas paralelas** (todas com o mesmo valor de \(Q\)): desliza-se a reta na direção em que \(Q\) cresce, até o **último ponto de contato** com a região, e esse ponto é um **vértice**.

### Exemplo completo (da aula): as caixas de livros

**O enunciado.** Uma livraria vai vender um livro novo, em duas versões: **capa mole** (estoque inicial de **40** cópias) e **capa dura** (estoque de **65**). Ela precisa de **pelo menos 80 cópias de cada versão** para atender pedidos já feitos e, se possível, de cópias adicionais. Um centro de distribuição planeja as entregas e pode enviar **até 10 caixas**: a caixa **leve** tem **6 livros de capa mole**; a caixa **mista** tem **5 de capa dura e 2 de capa mole**, e há **7 caixas mistas** disponíveis.

**Passo 1: entender o enfoque.** Quem toma a decisão é o **centro de distribuição**, e a meta é entregar "da melhor forma possível", isto é, **o máximo de livros**.

**Passo 2: variáveis de decisão.** \(L\) = nº de caixas **leves** enviadas e \(M\) = nº de caixas **mistas** enviadas (não são "livros vendidos", são caixas).

**Passo 3: função objetivo.** Cada caixa leve tem 6 livros e cada mista tem 5 + 2 = 7. **Maximizar** o total de livros entregues: \(Q = 6L + 7M\). (A composição entre capa mole e dura entra nas restrições, não na função objetivo.)

**Passo 4: restrições.**

| Restrição | Como sai do enunciado | Equação |
|---|---|---|
| Total de caixas | no máximo 10 caixas | \(L + M \leq 10\) |
| Caixas mistas | só há 7 | \(M \leq 7\) |
| Capa mole | estoque 40 + 6 por leve + 2 por mista, e o mínimo é 80: \(40 + 6L + 2M \geq 80\) | \(6L + 2M \geq 40\) |
| Capa dura | estoque 65 + 5 por mista, mínimo 80: \(65 + 5M \geq 80\) | \(M \geq 3\) |
| Domínio | não existe caixa negativa | \(L, M \geq 0\) |

**Passo 5: a região factível e os vértices.** Os pontos que respeitam **todas** as restrições formam o triângulo azul da figura. Em PL, o ótimo está sempre em um **vértice**, então basta testar os vértices (cada um é o encontro de duas retas de restrição):

![Região factível e retas de Q = 6L + 7M](img/26_regiao_factivel.png)

| Vértice | Encontro de | \(Q = 6L + 7M\) |
|---|---|---|
| \((5{,}67;\ 3)\) | \(M = 3\) com \(6L + 2M = 40\) | \(34 + 21 = 55\) |
| \((7;\ 3)\) | \(M = 3\) com \(L + M = 10\) | \(42 + 21 = 63\) |
| **\((5;\ 5)\)** | \(L + M = 10\) com \(6L + 2M = 40\) | \(30 + 35 = \mathbf{65}\) |

(O ponto \((3; 7)\), que o Solver chegou a mostrar na aula no meio da construção do modelo, **viola** \(6L + 2M \geq 40\), pois \(6\cdot 3 + 2\cdot 7 = 32\).)

**Passo 6: a resposta.** O máximo está em **\((L, M) = (5, 5)\)**: enviar **5 caixas leves e 5 mistas**, totalizando **65 livros**. Conferindo o enunciado: capa mole = 40 + 6·5 + 2·5 = **80** (exatamente o mínimo) e capa dura = 65 + 5·5 = **90** (acima do mínimo). Como L e M já saíram **inteiros**, não é preciso nenhum método para variáveis inteiras.


Em problemas reais há muitas variáveis e não dá para desenhar nem visitar todos os vértices. O **Simplex** caminha de vértice em vértice na direção de maior crescimento da função objetivo e, em cada vértice, testa se algum movimento ainda melhora; quando nenhum melhora, **garante o ótimo**. As ferramentas são o **Solver do Excel** e a biblioteca **PuLP** do Python, com a mesma lógica: *variáveis → objetivo → restrições → resolver*.

## 3. Variáveis inteiras: Branch-and-Bound

Não existe "meia caixa". Quando as variáveis precisam ser inteiras, o Simplex puro pode devolver soluções fracionárias (ex.: \(L = 5{,}7\)). O **Branch-and-Bound** resolve isso em três ideias:

1. **Solução relaxada:** resolve-se primeiro o problema tratando as variáveis como contínuas (isso dá um **limite superior** para o ótimo inteiro).
2. **Ramificação (branching):** se \(L = 5{,}7\), criam-se dois subproblemas, \(L \leq 5\) e \(L \geq 6\), e resolve-se cada um.
3. **Limitação (bounding):** toda solução **inteira** encontrada é **candidata**; ramos que não podem superar a melhor candidata são **podados**.

> **Exemplo (da aula): o caso dos livros.** A solução relaxada (tratando L e M como contínuos) já foi **(5, 5)**, **inteira**: **não é preciso ramificar**. É isso que acontece quando as restrições "encaixam" nos números inteiros.
>
> **Exemplo didático completo (não é da aula; criado para mostrar o Branch-and-Bound).** Maximizar \(Z = 5x + 4y\) com \(6x + 4y \leq 24\), \(x + 2y \leq 6\), \(x, y\) inteiros e \(\geq 0\).
>
> 1. **Relaxação** (sem exigir inteiros): ótimo em \((x, y) = (3; 1{,}5)\), com \(Z = 21\). Como \(y = 1{,}5\) não é inteiro, é preciso ramificar. **O 21 é um limite superior** para qualquer solução inteira.
> 2. **Ramificar em \(y\):** subproblema **A** (\(y \leq 1\)) e subproblema **B** (\(y \geq 2\)).
>    - **B** dá \((2; 2)\), inteira, \(Z = 18\): é a **primeira candidata** (18).
>    - **A** dá \((3{,}33; 1)\), \(Z = 20{,}67\): **fracionária** (x), mas o 20,67 **supera 18**, então continua a investigar.
> 3. **Ramificar A em \(x\):** \(x \leq 3\) dá \((3; 1)\), \(Z = 19\) (inteira, **nova melhor candidata**, 19); \(x \geq 4\) dá \((4; 0)\), \(Z = 20\) (inteira, **melhor ainda**).
> 4. **Poda:** nenhum ramo restante pode superar 20, então a solução ótima inteira é **\((x, y) = (4; 0)\) com \(Z = 20\)**. Note que ela **não** é o arredondamento da relaxada \((3; 1{,}5)\): arredondar poderia dar \((3; 1)\) (Z = 19) ou \((3; 2)\) (inviável).


Outro exemplo é a **nova ala hospitalar**: variáveis \(q_1, q_2, q_3\) (quartos de 1, 2 e 3 leitos); maximizar a receita \(R = 7500q_1 + 6000q_2 + 4500q_3\) com restrições de **área** (\(10q_1 + 15q_2 + 18q_3 \leq 1200\)), de **capacidade** (\(q_1 + q_2 + q_3 \leq 70\)), de **limite de individuais** (\(q_1 \leq 30\)), de **mínimo de leitos** (\(q_1 + 2q_2 + 3q_3 \geq 120\)) e de **domínio** (inteiros ≥ 0).

**Resultado do exemplo da ala hospitalar (resolvido).** Resolvendo a relaxação (variáveis contínuas), a solução é \((q_1, q_2, q_3) = (30,\ 30,\ 10)\), com **receita mensal de R$ 450.000**: 30 quartos individuais (o limite), 30 duplos e 10 triplos. Conferindo as restrições: área = \(10\cdot 30 + 15\cdot 30 + 18\cdot 10 = 930 \leq 1200\); total de quartos = 30 + 30 + 10 = **70** (no limite); leitos = 30 + 60 + 30 = **120** (exatamente o mínimo). Como a solução já saiu **inteira**, o Branch-and-Bound não precisa ramificar. Existe ainda **outra solução ótima** com a mesma receita, \((20,\ 50,\ 0)\) (20 individuais e 50 duplos): é o caso de **múltiplas soluções ótimas**, em que o modelo é indiferente entre elas.

## 4. Modelos mistos e os padrões de modelagem

No **PLIM** há variáveis contínuas, inteiras e binárias. O exemplo da aula é um problema de **transporte e transbordo com ativação de terminais**: dois centros (CD1 com 40 t e CD2 com 60 t) abastecem três lojas (30, 35 e 25 t), com a possibilidade de passar por dois terminais de transbordo (T1 e T2), de capacidade 50 t e **custo fixo de ativação de $ 10** cada. Além disso, o trecho CD2 → L2 só pode ser feito em **caminhões de 7 t**. Os padrões para traduzir cada regra são:

| Regra do problema | Como modelar |
|---|---|
| **Oferta** de um centro | soma do que sai ≤ oferta |
| **Demanda** de uma loja | soma do que chega **=** demanda |
| **Conservação de fluxo** no terminal | tudo que **entra** = tudo que **sai** |
| **Decisão sim/não** (ativar um terminal) | variável **binária** \(y\) (0 ou 1) |
| **Custo fixo** | somar \(10\,y\) na função objetivo |
| **Capacidade só se ativado** | \(\text{entrada no terminal} \leq 50\,y\) (com \(y=0\), nada passa; com \(y=1\), até 50 t) |
| **Quantidade em lotes** (caminhões de 7 t) | \(x = 7k\) com \(k\) **inteiro** |

> **Exemplo resolvido (lote).** Se \(x_{CD2,L2} = 7k\), os valores possíveis são 0, 7, 14, 21, 28 e 35. No ótimo da aula, \(k = 3\) e \(x_{CD2,L2} = 21\).

O ótimo do exemplo com terminais custou cerca de **330**, com os dois terminais ativados.

## O que levar daqui

PO transforma problemas em modelos com **variáveis, objetivo e restrições**. PL só tem equações lineares; o Simplex acha o ótimo andando pelos vértices. Para variáveis inteiras usa-se Branch-and-Bound (relaxar, ramificar, limitar, podar). No modelo misto, decisão sim/não vira binária; custo fixo entra multiplicado pela binária; capacidade condicionada vira \(x \leq \text{Cap}\cdot y\); lotes viram \(x = \text{lote}\cdot k\).

## Erros que todo mundo comete

| Erro | Correção |
|---|---|
| "O ótimo está dentro da região" | em PL, está num **vértice** |
| "O Simplex testa todos os vértices" | caminha e para quando nada melhora |
| "Branch-and-Bound sempre ramifica" | se a relaxada já é inteira, **não ramifica** |
| "Variável binária = inteira qualquer" | só pode ser **0 ou 1** |
| Esquecer a conservação de fluxo no terminal | entrada = saída |
| Definir restrições antes do objetivo | defina o **objetivo primeiro** |

## Teste-se

1. Quais os três componentes de um modelo de otimização?
<details markdown="1"><summary>Ver resposta</summary>Variáveis de decisão, função objetivo e restrições.</details>

2. Como modelar "um terminal só pode receber carga se estiver ativado, com capacidade de 50 t"?
<details markdown="1"><summary>Ver resposta</summary>Com uma binária \(y\): entrada no terminal ≤ 50·y.</details>

3. Como representar um trecho que só aceita caminhões de 7 t?
<details markdown="1"><summary>Ver resposta</summary>\(x = 7k\), com \(k\) inteiro não negativo.</details>

4. O que é a solução relaxada no Branch-and-Bound?
<details markdown="1"><summary>Ver resposta</summary>A solução do problema tratando as variáveis inteiras como contínuas; dá um limite superior (em maximização) para o ótimo inteiro.</details>

## Pergunta típica
Os 3 componentes de um modelo de otimização e o que é PL · dado um enunciado, escrever variáveis, função objetivo e restrições (quartos de hospital, caixas de livros, transporte) · o que é região factível e por que o ótimo está em um vértice · Simplex × Branch-and-Bound (branching, bounding, solução relaxada, poda) · quando o modelo é inteiro, binário ou misto · como representar "múltiplo de 7", "terminal só se ativado" e conservação de fluxo · Solver × PuLP
