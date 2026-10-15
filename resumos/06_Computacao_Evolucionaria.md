# 06 · Computação Evolucionária
**Profs. Renata da Encarnação Onety e Rubelmar Maia de Azevedo Cruz Neto · 2 aulas (05 e 12/08/2025) · Prioridade: ALTA (algoritmos genéticos têm vocabulário fixo e cai em prova)**
*Complementa: Pesquisa Operacional (resumo 26), que usa a mesma modelagem.*

## 1. Contexto: otimização, heurística e meta-heurística
- **Todo modelo de ML envolve um problema de otimização:** regressão linear minimiza a **SSE** (soma dos quadrados dos resíduos, método dos mínimos quadrados); rede neural de regressão também minimiza SSE; **regressão logística maximiza a verossimilhança**.
- **Heurística** (do grego "descobrir"): busca guiada por intuição/regras para achar uma **boa solução** (ex.: *greedy*). **Meta-heurística:** combina **intensificação** e **diversificação** para **escapar de ótimos locais** e chegar perto do **ótimo global, mas sem garantia de otimalidade** (ex.: **algoritmos genéticos**).
- **Computação evolucionária** é parte da **Inteligência Computacional** (técnicas inspiradas na natureza), junto com inteligência de enxame, redes neurais e lógica fuzzy. Família: **algoritmos genéticos (Holland, anos 60)**, estratégias evolutivas (Rechenberg), programação evolutiva (Fogel), programação genética (Koza).
- **"O bom é inimigo do ótimo":** não testa todas as soluções, não garante ótimo, busca solução **satisfatória**.
- Problemas difíceis: **não lineares**, **multimodais** (vários máximos/mínimos), **combinatórios**.

### Caixeiro-viajante (TSP)
Achar a rota mais curta visitando cada cidade uma vez e voltando à origem. Nº de rotas = **(n−1)!/2** (n=4 → 3 rotas; n=5 → 12; n=10 → 181.440; n=20 → 6,1×10¹⁶). **Não se conhece algoritmo exato eficiente (polinomial)**; força bruta fica inviável (20 cidades a 1 milhão de rotas/s ≈ 1.900 anos). Aplicações: logística, circuitos eletrônicos, sequenciamento de DNA, setup de máquinas, solda em placas.

## 2. Modelagem matemática (base para qualquer otimização)
1. **Variáveis de decisão** — o que o modelo calcula (escolhas controláveis; ficam claras lendo a pergunta do problema).
2. **Função objetivo** — equação que quantifica o desempenho: **maximizar** (lucro) ou **minimizar** (custo, tempo).
3. **Restrições** — condições que delimitam as soluções viáveis (igualdades/desigualdades; capacidade, disponibilidade, tempo). Restrições **fortes** (inegociáveis) × **fracas** (desejáveis; só possíveis em meta-heurísticas).
- Primeiro passo prático: **ouvir quem vive o problema**. "Modelo não é a realidade, mas é similar o suficiente."

**Problema da mistura (ração):** min Z = 0,56x1 + 0,81x2 + 0,46x3 s.a. proteína 0,2x1+0,5x2+0,4x3 ≥ 0,3; cálcio 0,6x1+0,4x2+0,4x3 ≥ 0,5; x1+x2+x3 = 1; xi ≥ 0. Ótimo: ½ kg de osso + ½ kg de peixe, **R$ 0,51/kg**.
**Problema da mochila:** maximizar valor com **limite de peso** (5 kg). Variáveis binárias xi (1 = leva o item). Ótimo: Z = 41.

## 3. Algoritmos genéticos (AG) — vocabulário (CAI MUITO)
| Termo | Significado |
|---|---|
| **Gene** | elemento básico do cromossomo (um traço da solução; na mochila = um item; na mistura = um ingrediente) |
| **Alelo** | valor que o gene pode assumir (0/1, ou valor real) |
| **Cromossomo / Indivíduo** | uma solução completa (vetor de genes) |
| **População** | conjunto de indivíduos em uma geração |
| **Geração** | um ciclo de evolução |
| **Genótipo** | representação interna codificada (ex.: sequência binária) |
| **Fenótipo** | como o genótipo é interpretado no problema (ex.: valor total da mochila) |
| **Fitness (aptidão)** | qualidade do indivíduo, vem da **função objetivo** |
| **Seleção** | escolher pais (sobrevivência do mais apto): **roleta** (probabilidade proporcional ao fitness) ou **torneio** (sorteia 2+ e fica o melhor) |
| **Cruzamento (crossover)** | combina genes de 2 pais → filhos; **explora** o espaço (ex.: 1 ponto de corte, 2 pontos) |
| **Mutação** | altera genes aleatoriamente; **aumenta diversidade**, evita **ótimos locais** |
| **Elitismo** | preserva os melhores indivíduos intactos para a geração seguinte |
| **Codificação / decodificação** | binária ou real ↔ solução do problema |
| **Taxa de cruzamento / de mutação** | probabilidades de cruzar / mutar |

**Passo a passo do AG:** 1) definir variáveis e limites; 2) criar função de fitness; 3) escolher codificação; 4) configurar parâmetros; 5) gerar população inicial (pseudo-aleatória, ou semeada por outra heurística); 6) **loop**: avaliar fitness → selecionar pais → cruzar → mutar → preservar elite → nova população = filhos + elite; 7) **critério de parada** (nº máximo de gerações, convergência, fitness sem melhora em N gerações); 8) devolve o melhor indivíduo.
**Parâmetros típicos:** população 50–200 (regra: ~10 × nº de variáveis), gerações 100–1000, **cruzamento 70–90%**, **mutação 1–5% por gene**. Mais variáveis/restrições → populações maiores; espaço maior → mais gerações; população pequena converge rápido para **ótimo local**. **Escolher esses parâmetros já é um problema de otimização** (como hiperparâmetros de rede neural/árvore). **Ajuste via DoE (Design of Experiments).**
**Restrição em AG:** indivíduos que violam a restrição são penalizados (método das penalidades) ou descartados.

**Métricas de avaliação do AG:** melhor fitness; fitness médio; **taxa de convergência**; **desvio padrão do fitness** = diversidade (alto no início = bom; baixo no fim = convergiu); tempo de execução.

## 4. Casos aplicados
- **Mochila e mistura em Python** (também em **Excel Solver**).
- **Função x² com AG** (limites −5 a 5): minimização, ponto de mínimo onde derivada = 0 — didático; funções multimodais mostram o poder do AG.
- **TSP:** variável xij = 1 se vai da cidade i para j; restrições: cada nó entra e sai uma vez + **eliminação de sub-rotas**; solução da aula: 1→4→5→3→2 (Z = 217,21).
- **Otimização de carteira de investimentos:** maximizar retorno com risco (desvio padrão) ≤ 2,5% e máx. 30% por ação; é linear. Com **variância e covariância** vira não linear. Pode combinar **previsão (séries temporais, redes recorrentes, XGBoost) + otimização**.
- **Seleção de variáveis em regressão** com AG no lugar do stepwise (R² ajustado ou SSE como fitness), porque stepwise com 20–30 variáveis pode não achar o melhor modelo (problema combinatório).

## 5. Multiobjetivo e outros algoritmos
- **Método das penalidades / ponderação:** transforma multiobjetivo em objetivo único com pesos wᵢ: Σ wᵢ·fᵢ(x).
- **Fronteira de Pareto:** conjunto de soluções **não dominadas** (nenhuma é melhor em todos os objetivos). **NSGA-II** (2–3 objetivos), **NSGA-III** (4+), **SPEA2**.
- Outros: **colônia de formigas, enxame de abelhas, voo dos pássaros (PSO), sistemas imunológicos artificiais, simulated annealing, busca tabu**, híbridos. AG foi escolhido por ser pioneiro e clássico.
- Pergunta interativa da aula: "qual operador é mais importante: seleção, cruzamento ou mutação?" (resposta: depende; os três se complementam — exploração × intensificação).

## Pergunta típica
- Heurística × meta-heurística; o que é fitness; papel de cruzamento, mutação e elitismo; genótipo × fenótipo; por que AG não garante ótimo; fórmula/ordem de grandeza das rotas do TSP; critérios de parada; roleta × torneio.
