# 06 · Computação Evolucionária
**Profs. Renata da Encarnação Onety e Rubelmar Maia de Azevedo Cruz Neto · 2 aulas · Prioridade: ALTA (algoritmos genéticos têm vocabulário fixo e é cobrado)**
*Complementa: Pesquisa Operacional (resumo 26), que usa a mesma modelagem.*

> **Em uma frase:** algoritmos genéticos resolvem problemas de otimização **imitando a evolução** — uma população de soluções que se cruzam, mutam e sobrevivem conforme a qualidade — para achar uma **boa** solução quando testar todas é impossível.

**Pré-requisitos:** noção de função objetivo e restrições (26). **Vem depois:** aplicações em seleção de variáveis e carteiras.

## Por que isso importa (intuição)
Alguns problemas têm tantas combinações que **força bruta é inviável**. Exemplo: o caixeiro-viajante com 20 cidades tem ~6,1×10¹⁶ rotas — a 1 milhão de rotas por segundo levaria ≈ 1.900 anos. Em vez de testar tudo, o algoritmo genético **faz uma busca inteligente**: mantém várias soluções, favorece as melhores e sorteia variações — como a seleção natural. Em troca, **não garante o ótimo**, só uma solução satisfatória ("o bom é inimigo do ótimo").

## 1. Contexto: otimização, heurística e meta-heurística
- **Todo modelo de ML é um problema de otimização:** a regressão linear minimiza a **SSE** (soma dos quadrados dos resíduos); a logística **maximiza a verossimilhança**.
- **Heurística:** regra/intuição para achar uma **boa** solução (ex.: *greedy*, que escolhe o melhor passo local).
- **Meta-heurística:** combina **intensificação** (refinar o que é bom) e **diversificação** (explorar novas áreas) para **escapar de ótimos locais** e chegar perto do global, **sem garantia de otimalidade**. O AG é uma meta-heurística.
- **Computação evolucionária** faz parte da inteligência computacional (inspirada na natureza), junto com inteligência de enxame, redes neurais e lógica fuzzy. Família: algoritmos genéticos (Holland, anos 60), estratégias evolutivas, programação evolutiva, programação genética.
- **Problemas difíceis:** não lineares, **multimodais** (vários máximos/mínimos locais) e **combinatórios**.

### Caixeiro-viajante (TSP)
Menor rota que visita cada cidade uma vez e volta à origem. **Nº de rotas = (n−1)!/2:** n=4 → 3; n=5 → 12; n=10 → 181.440; n=20 → 6,1×10¹⁶. **Não existe algoritmo exato eficiente conhecido.** Aplicações: logística, circuitos, sequenciamento de DNA.

## 2. Modelagem matemática (base de qualquer otimização)
1. **Variáveis de decisão:** o que o modelo escolhe.
2. **Função objetivo:** o que **maximizar** (lucro) ou **minimizar** (custo, tempo).
3. **Restrições:** limites que definem as soluções viáveis (capacidade, tempo). **Fortes** (inegociáveis) × **fracas** (desejáveis; só em meta-heurísticas).
- Primeiro passo prático: **ouvir quem vive o problema**.

**Exemplo — mochila:** maximizar o valor dos itens com **limite de peso 5 kg**; variável binária xᵢ (1 = leva o item). Ótimo da aula: Z = 41.
**Exemplo — mistura (ração):** minimizar custo Z = 0,56x₁ + 0,81x₂ + 0,46x₃ sujeito a mínimos de proteína e cálcio e x₁+x₂+x₃ = 1; ótimo: ½ kg de osso + ½ kg de peixe → **R$ 0,51/kg**.

## 3. Algoritmo genético — vocabulário (muito cobrado)
- **Gene:** elemento básico do cromossomo (na mochila, um item). **Alelo:** valor que o gene assume (0/1 ou real).
- **Cromossomo/Indivíduo:** uma solução completa. **População:** conjunto de indivíduos. **Geração:** um ciclo de evolução.
- **Genótipo:** representação codificada (ex.: sequência binária). **Fenótipo:** como o genótipo é interpretado no problema (ex.: valor total da mochila).
- **Fitness (aptidão):** qualidade do indivíduo, calculada pela **função objetivo**.
- **Seleção:** escolhe os pais — **roleta** (chance proporcional ao fitness) ou **torneio** (sorteia alguns e fica o melhor).
- **Cruzamento (crossover):** combina genes de dois pais em filhos; **explora** o espaço (1 ou 2 pontos de corte).
- **Mutação:** altera genes aleatoriamente; **mantém diversidade e evita ótimos locais**.
- **Elitismo:** preserva os melhores indivíduos intactos na geração seguinte.
- **Taxas de cruzamento e de mutação:** probabilidades de cada operador.

### O ciclo
1) definir variáveis e limites → 2) criar o fitness → 3) escolher a codificação → 4) configurar parâmetros → 5) gerar **população inicial** → 6) **repetir:** avaliar fitness → selecionar pais → cruzar → mutar → preservar elite → nova população → 7) **parar** (nº máximo de gerações, convergência, sem melhora em N gerações) → 8) devolver o melhor indivíduo.

**Parâmetros típicos:** população 50–200 (≈ 10 × nº de variáveis); gerações 100–1000; **cruzamento 70–90%**; **mutação 1–5% por gene**. População pequena converge cedo para **ótimo local**. Escolher parâmetros é **outro problema de otimização** (ajustável por **DoE**). **Restrições:** indivíduos que as violam são **penalizados** ou descartados.
**Métricas do AG:** melhor fitness, fitness médio, taxa de convergência, **desvio padrão do fitness = diversidade** (alto no início, baixo no fim), tempo.

**Exemplo de uma rodada (mochila).** Cromossomo 1 0 1 1 0 = leva os itens 1, 3 e 4. Fitness = valor total (se passar de 5 kg, penaliza). Seleção por torneio escolhe dois pais; cruzamento troca a "cauda" entre eles; mutação inverte um bit com probabilidade pequena; o melhor da geração passa direto (elitismo).

## 4. Casos aplicados
- **TSP:** xᵢⱼ = 1 se vai da cidade i para j; cada cidade entra e sai uma vez; **eliminação de sub-rotas**.
- **Carteira de investimentos:** maximizar retorno com risco ≤ limite e máx. 30% por ação; com covariâncias vira não linear.
- **Seleção de variáveis em regressão:** AG no lugar do stepwise (fitness = R² ajustado ou SSE), porque com 20–30 variáveis o stepwise pode não achar o melhor modelo.

## 5. Multiobjetivo e outros algoritmos
- **Ponderação:** Σ wᵢ·fᵢ(x) transforma vários objetivos em um.
- **Fronteira de Pareto:** soluções **não dominadas** (nenhuma melhor em todos os objetivos). **NSGA-II** (2–3 objetivos), **NSGA-III** (4+), **SPEA2**.
- Outros: colônia de formigas, enxame de partículas (PSO), recozimento simulado, busca tabu, sistemas imunológicos artificiais.

## Armadilhas e confusões comuns
| Confusão | O correto |
|---|---|
| AG garante o ótimo global | **não**; busca uma boa solução |
| Genótipo = fenótipo | genótipo é a **codificação**; fenótipo é a **interpretação** no problema |
| Mutação serve para melhorar o melhor indivíduo | serve para **diversidade** e escapar de ótimos locais |
| Elitismo reduz a qualidade | **preserva** os melhores |
| Mais população é sempre melhor | aumenta o custo; é um **trade-off** |
| Heurística = meta-heurística | meta-heurística **combina intensificação e diversificação** |

## Resumo-relâmpago
- Heurística = boa solução guiada por regra; meta-heurística escapa de ótimos locais; sem garantia de ótimo.
- AG: população → fitness → seleção (roleta/torneio) → cruzamento → mutação → elitismo → parada.
- Cruzamento ≈ 70–90%; mutação ≈ 1–5%; diversidade = desvio padrão do fitness.
- TSP: (n−1)!/2 rotas; multiobjetivo: Pareto, NSGA-II.

## Teste-se
1. Qual a diferença entre genótipo e fenótipo?
<details markdown="1"><summary>Ver resposta</summary>Genótipo é a representação codificada (ex.: bits); fenótipo é como ela é interpretada no problema (ex.: valor total da mochila).</details>

2. Para que servem mutação e elitismo?
<details markdown="1"><summary>Ver resposta</summary>Mutação mantém a diversidade e evita ótimos locais; elitismo preserva os melhores indivíduos entre gerações.</details>

3. Quantas rotas distintas tem o TSP com 5 cidades?
<details markdown="1"><summary>Ver resposta</summary>(5−1)!/2 = 24/2 = 12.</details>

4. Por que o AG não garante o ótimo?
<details markdown="1"><summary>Ver resposta</summary>Porque não testa todas as soluções; é estocástico e meta-heurístico, busca uma solução satisfatória.</details>

## Pergunta típica
Heurística × meta-heurística · o que é fitness · papel de cruzamento, mutação e elitismo · genótipo × fenótipo · por que o AG não garante o ótimo · quantas rotas tem o TSP · critérios de parada · roleta × torneio
