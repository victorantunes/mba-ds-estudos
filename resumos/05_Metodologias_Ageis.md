# 05 · Metodologias Ágeis I e II
**Prof. Gino Terentim · 2 aulas · Prioridade: ALTA para o vocabulário (vira questão conceitual fácil de pontuar)**

> **Em uma frase:** a forma de gerir um trabalho (planejar tudo antes ou aprender no caminho) deve ser escolhida pela **natureza do problema**, não pelo gosto do gestor.

**Pré-requisitos:** nenhum. **Vem depois:** 11 (liderança) e 30 (gestão da mudança).

## Por que isso importa (intuição)
Construir uma ponte com projeto pronto é um problema **conhecido**: planeje e execute. Descobrir um produto que o cliente ainda nem sabe que quer é um problema **incognoscível**: você só aprende **fazendo e testando**. Usar o método errado custa caro — planejar demais o incerto, ou improvisar no que já se sabe fazer.

## 1. Projeto, processo e mudança
- **Projeto:** cria algo **único e finito**, muda o negócio, equipes transversais. **Processo:** contínuo e recorrente, mantém/aprimora o *status quo*, equipes funcionais.
- **Mudança:** transição entre estados — **incremental** (melhoria contínua), **transformacional** (redefinição) ou **disruptiva** (inovação). Projeto = organização temporária criada para entregar conforme um **business case** aprovado.
- **Business Case Canvas:** problema e justificativa, opções, benefícios/desbenefícios, entregas e marcos, riscos, custos e avaliação do investimento, indicadores de sucesso.

## 2. D.I.C.E. — chance de sucesso de um projeto
- **D**uração (<2 meses = 1; 2–4 = 2; 4–8 = 3; >8 = 4) · **I**ntegridade (capacidade da equipe/liderança) · **C**ompromisso (C1 = gestão sênior; C2 = equipe/local) · **E**sforço adicional (<10% = 1 … >40% = 4).
- **Pontuação = D + 2·I + 2·C1 + C2 + E.** Zonas: **7–14 = WIN** · **15–17 = WORRY** · **18–28 = WOE** (alto risco). *Nota baixa é boa.*

**Exemplo.** D=2, I=1, C1=2, C2=2, E=1 → 2 + 2 + 4 + 2 + 1 = **11 → WIN**.

## 3. Natureza do problema → abordagem
| Tipo de problema | Característica | Abordagem | Onde acomoda a incerteza |
|---|---|---|---|
| **Conhecido** (passado) | já existe resposta | **preditiva**: planejar → executar → monitorar | prazo e custo |
| **Conhecível** (presente) | exige análise/experimentação | **adaptativa/empírica** | escopo (prazo e custo rígidos) |
| **Incognoscível** (futuro) | impossível saber antes | **experimentar**: "dê um passo para descobrir" | — |

- Conhecimento **a priori** (razão/dedução) × **a posteriori** (experiência).
- **Priorize o problema, não o projeto.** Em Data Science: divida o problema em **microproblemas** e veja quais você já sabe resolver (preditivo) e quais exigem experimentação (ágil).

## 4. Origem do ágil e Manifesto
- **Takeuchi e Nonaka (1986):** empresas de sucesso trabalhavam como no **rugby** (equipe junta, passando a bola) e não como **corrida de revezamento**. 6 características: instabilidade embutida; equipes **autoorganizadas**; fases **sobrepostas**; **multiaprendizagem**; **controle sutil**; **transferência de aprendizado**. O nome **Scrum** vem do rugby.
- **Manifesto Ágil — valorizamos mais:** **indivíduos e interações** (sobre processos e ferramentas) · **software funcionando** (sobre documentação extensa) · **colaboração com o cliente** (sobre negociação de contratos) · **responder a mudanças** (sobre seguir um plano). Ágil = **leve e adaptável**. *Os itens da direita ainda têm valor; só valem menos.*

## 5. Cynefin (Dave Snowden)
| Domínio | Natureza | O que fazer |
|---|---|---|
| **Claro** | causa-efeito óbvia | **melhores práticas**, checklist; eficiência |
| **Complicado** | exige análise/especialista | boas práticas e análise |
| **Complexo** | causa-efeito só visível depois | **experimentos seguros** (*probe → sense → respond*); eficácia |
| **Caótico** | crise | **agir primeiro** para estabilizar |
| **Confuso** | não se sabe o domínio | descobrir onde está |
- **Número de Dunbar:** rede social estável de ~100–150 pessoas.

## 6. PMRL — 9 estágios em 3 fases
- **Exploration (Problem-Solution Fit):** 1 *Discovery* · 2 *Prototyping* · 3 *Validation*.
- **Delivery (Product-Market Fit):** 4 **MVP** · 5 *Iteration* · 6 *Market Testing*.
- **Exploitation (Scale):** 7 *Optimization* · 8 *Expansion* · 9 *Scaling*.
- Exploração → ágil/empírico; exploração do que já funciona (escalar) → processo conhecido/preditivo.

## 7. Scrum
- **Sprint:** ciclo de **no máximo 30 dias**.
- **Papéis:** **Product Owner** (prioriza o backlog, maximiza valor) · **Scrum Master** (líder-servidor, remove impedimentos) · **Desenvolvedores** (time multidisciplinar e autogerenciável).
- **Eventos:** Sprint Planning · Daily · Sprint Review · Retrospective.
- **Artefatos ↔ compromissos:** Product Backlog → **Meta do Produto**; Sprint Backlog → **Meta da Sprint**; Incremento → **Definição de Pronto (DoD)**.

## 8. Lean e Kanban
- **8 desperdícios (Lean):** superprodução · espera · transporte · processamento excessivo · inventário excessivo · movimentação · defeitos · talento não utilizado.
- **Kanban:** visualizar o trabalho em colunas, **limitar o trabalho em progresso (WIP)**, o fluxo revela **gargalos**; "pare de começar, comece a terminar".
- **Scrum é framework; Kanban é método.**

## Armadilhas e confusões comuns
| Confusão | O correto |
|---|---|
| Ágil = sem planejamento/documentação | valoriza **mais** pessoas e software funcionando, mas planeja e documenta o necessário |
| Quanto maior a nota DICE, melhor | **menor** é melhor (7–14 = WIN) |
| Scrum e Kanban são o mesmo | Scrum = framework com papéis e eventos; Kanban = método de fluxo |
| Preditivo sempre errado | é ótimo para problemas **conhecidos** |
| Scrum Master = chefe do time | é **líder-servidor** que remove impedimentos |
| Problema complexo se resolve por checklist | exige **experimentação** |

## Resumo-relâmpago
- Conhecido → preditivo; conhecível → adaptativo; incognoscível → experimentar.
- DICE = D + 2I + 2C1 + C2 + E; ≤14 = WIN.
- Manifesto: 4 valores; Scrum: 3 papéis, 4 eventos, 3 artefatos; Kanban: WIP.
- Cynefin: claro, complicado, complexo, caótico, confuso.

## Teste-se
1. Diferencie projeto e processo.
<details markdown="1"><summary>Ver resposta</summary>Projeto: único, finito, muda o negócio. Processo: contínuo e recorrente, mantém/aprimora o status quo.</details>

2. Onde cada abordagem acomoda a incerteza?
<details markdown="1"><summary>Ver resposta</summary>Preditiva: em prazo e custo (escopo fixo). Adaptativa: no escopo (prazo e custo rígidos).</details>

3. Calcule DICE: D=3, I=2, C1=3, C2=2, E=2.
<details markdown="1"><summary>Ver resposta</summary>3 + 4 + 6 + 2 + 2 = 17 → WORRY.</details>

4. Cite os 8 desperdícios do Lean.
<details markdown="1"><summary>Ver resposta</summary>Superprodução, espera, transporte, processamento excessivo, inventário excessivo, movimentação, defeitos, talento não utilizado.</details>

## Pergunta típica
Diferença entre projeto e processo · entre abordagem preditiva e adaptativa (onde cada uma acomoda incerteza) · valores do Manifesto Ágil · papéis, eventos e artefatos do Scrum · o que é WIP limit · domínios do Cynefin · fórmula e zonas do DICE · os 8 desperdícios
