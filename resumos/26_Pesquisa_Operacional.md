# 26 · Pesquisa Operacional e Modelos de Otimização (I, II, III)
**Prof. Cassiano Augusto Isler · 3 aulas · Prioridade: MÉDIA-ALTA (saber MODELAR um enunciado em variáveis/objetivo/restrições é o que cai)**

## 1. Ideia central
- **Pesquisa Operacional (PO) / programação matemática:** transformar um **problema real de decisão** em um **modelo matemático** e resolvê-lo para achar a solução **ótima** (boa e rápida). "O segredo é interpretar o problema" — o modelo é consequência da interpretação (converse com quem vive o problema).
- **Os 3 componentes de todo modelo de otimização:**
  1. **Variáveis de decisão** — o que posso escolher (as respostas que busco).
  2. **Função objetivo** — a meta: **maximizar** (lucro, receita, nota, itens entregues) ou **minimizar** (custo, tempo).
  3. **Restrições** — condições de contorno; sempre **comparam duas quantidades mensuráveis** (≤, ≥, =).
- **Programação Linear (PL):** função objetivo e restrições **todas lineares** (soma de termos constante × variável; **nunca x²**). Se há variáveis inteiras → **PLI**; se há inteiras **e** contínuas → **PLIM (mista)**.
- **Passo a passo de modelagem (da aula):** (1) entender o problema; (2) coletar dados/evidências; (3) **em palavras**: identificar variáveis, objetivo e restrições; (4) escrever as equações; (5) resolver e **validar** se o modelo resolve o problema real. **Defina a função objetivo ANTES das restrições** (senão você pode olhar para o ator errado — ex.: livraria em vez do centro de distribuição).
- **Minimizar f = maximizar −f.** Restrição **flexível** (pode ser violada a um custo): modela-se a **folga/diferença como variável** e **penaliza-se na função objetivo**; restrição **absoluta (hard)** nunca pode ser violada.
- Aplicações citadas: filas, pátios/fábricas, teoria dos jogos, localização de instalações (*facility location*), precificação, gestão de estoques, corte de bobinas, entrega de pizzas (precisa de solução **imediata** → modelo rápido; planejamento semanal tolera horas).

## 2. Solução gráfica e Simplex (2 variáveis)
- **Região factível:** conjunto de pontos que satisfazem **todas** as restrições ao mesmo tempo. A função objetivo vira **retas paralelas** (isoquantas: mesmo valor de Z); desloca-se a reta na direção de crescimento (máx.) até o **último ponto** de contato com a região factível → **ótimo está em um vértice**.
- **Exemplo da média ponderada (estudo):** variáveis H1, H2 (horas por disciplina); objetivo maximizar a nota ponderada (ex.: 15·H1 + 20·H2, dividido por 8); restrições de **tempo total disponível** e **nota mínima**. Reta Z = 60 passando pelos pontos (H1=0, H2=20) e (H1=10, H2=12,5) etc.
- **Simplex:** não percorre todos os vértices; **caminha de vértice em vértice** na direção de maior crescimento de Z e, em cada vértice, testa se algum movimento ainda melhora; quando nenhum melhora, **garante** o ótimo. Modelos reais têm muitas variáveis → não dá para resolver graficamente; usa-se software.
- Ferramentas: **Solver do Excel** (indicar célula objetivo, células variáveis, restrições; resultado pode depender de "chute inicial" em modelos não lineares) e **Python PuLP** (`LpProblem`, `LpVariable`, soma de objetivo, restrições, `prob.solve()`; **sempre a mesma lógica: variáveis → objetivo → restrições → resolver**).

## 3. Programação Linear Inteira — exemplo "Venda de Livros"
- **Enunciado-resumo:** centro de distribuição envia caixas **Leves (L)** e **Mistas (M)** à livraria; máximo de **10 caixas** (L + M ≤ 10); restrição de tipos de livros (6L + 2M ≥ 40); **maximizar Q = 6L + 7M** (livros entregues); L, M **inteiros ≥ 0** (não existe meia caixa).
- **Solução ótima: (L, M) = (5, 5), Q = 65.**
- **Por que o Simplex "puro" não basta:** a solução do simplex pode ser **fracionária** (ex.: L = 5,7; M = 3 → Q = 55,2... no exemplo da aula, **relaxada**). Para variáveis inteiras usa-se **Branch-and-Bound**:
  1. **Solução inicial relaxada** (trata as variáveis como contínuas);
  2. **Ramificação (branching):** se L = 5,7 não é inteiro, cria dois subproblemas: **L ≤ 5** e **L ≥ 6**; resolve cada um;
  3. **Limitação (bounding):** toda solução **inteira** achada é **candidata**; compara-se o valor da função objetivo com a **melhor já encontrada**; ramos que não podem superá-la são **podados** (não se ramifica mais). Exemplo: 2.1 → (5,5), Q = 65; 2.2 → (6,4), Q = 64 → vence 2.1.
  - **Se a solução ótima relaxada já for inteira, não precisa ramificar** (foi o caso de (5,5)). O **valor da relaxação é um limite superior** (maximização) para o ótimo inteiro.
  - No PuLP, declarar `cat="Integer"` faz o solver usar Branch-and-Bound automaticamente.
- **Exemplo "Nova Ala Hospitalar":** variáveis q1, q2, q3 = quartos de 1, 2 e 3 leitos. **Maximizar R = 7500·q1 + 6000·q2 + 4500·q3** sujeito a: **área** 10q1 + 15q2 + 18q3 ≤ 1200; **capacidade** q1 + q2 + q3 ≤ 70; **limite de individuais** q1 ≤ 30; **mínimo de leitos** q1 + 2q2 + 3q3 ≥ 120; q ∈ ℤ⁺. Com 3 variáveis não há solução gráfica (espaço 3D) → só analítica via software.

## 4. Programação Linear Inteira Mista (PLIM)
- **Mista** = o modelo tem **mais de um tipo de variável**: **contínuas** + **inteiras** e/ou **binárias** (0/1). Resolve-se com **Branch-and-Bound** (ramifica só nas inteiras).
- **Exemplo — Transporte:** 2 centros (CD1: 40 t; CD2: 60 t) e 3 lojas (L1: 30 t; L2: 35 t; L3: 25 t); custo $/t entre CDs e lojas; **minimizar custo total** com restrições de **oferta (≤)** por CD e **demanda (=)** por loja.
  - **Regra especial:** o trecho **CD2→L2 só por caminhões de 7 t** → **x_cd2,l2 = 7k, k inteiro** (x ∈ {0, 7, 14, …, 35}); demais variáveis contínuas ≥ 0. No ótimo da aula, **k = 3** (x_cd2,l2 = 21).
  - Dica de modelagem: variável "k" (nº de caminhões) é inteira e a quantidade transportada é **7·k**.
- **Exemplo — Transporte e Transbordo com Ativação de Terminais:** adiciona **2 terminais de transbordo (T1, T2)** entre CDs e lojas, **capacidade 50 t** cada, **custo fixo de ativação ($10 cada)**; ainda é possível transporte direto. 
  - **Variáveis:** fluxos CD→loja, CD→terminal, terminal→loja (contínuas ≥ 0), **k** (caminhões, inteira) e **binárias y_T1, y_T2** (1 = terminal ativado).
  - **Objetivo:** custo de transporte (todos os arcos) **+ 10·y_T1 + 10·y_T2** (custos fixos).
  - **Restrições-chave:** oferta dos CDs (≤); demanda das lojas (= soma dos fluxos diretos + via terminais); **equilíbrio de fluxo no transbordo** (**tudo que entra no terminal = tudo que sai**); **capacidade condicionada à ativação: (entradas em T) ≤ 50·y_T** (se y = 0, nada passa; se y = 1, até 50 t) — a clássica ligação **binária × capacidade**; múltiplo de 7 em CD2→L2.
  - Ótimo do exemplo ≈ **custo total 330** (com terminais ativados), resolvido no Solver e no PuLP.
- **Padrões de modelagem para memorizar:** **decisão sim/não (ativar, abrir, escolher) = variável binária**; **custo fixo** entra no objetivo multiplicado pela binária; **capacidade só se ativado** = x ≤ Cap·y; **conservação de fluxo** em nós de transbordo; **quantidade em lotes** = x = lote·k com k inteiro.

## 5. Resumo de classificação
| Tipo | Variáveis | Método |
|---|---|---|
| PL | contínuas | Simplex |
| PLI | todas inteiras | Branch-and-Bound |
| PLIM | contínuas + inteiras/binárias | Branch-and-Bound |
| Não linear | termos x², produtos… | **fora do escopo** (resultado pode depender do chute inicial) |

## Pergunta típica
Os 3 componentes de um modelo de otimização e o que é PL · dado um enunciado, escrever variáveis de decisão, função objetivo e restrições (ex.: quartos de hospital, caixas de livros, transporte) · o que é região factível e por que o ótimo está em um vértice · como funciona o Simplex vs. Branch-and-Bound (branching, bounding, solução relaxada, poda) · quando o modelo é inteiro, binário ou misto · como representar "múltiplo de 7", "terminal só se ativado" e conservação de fluxo · Solver × PuLP.
