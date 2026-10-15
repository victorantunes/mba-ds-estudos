# 05 · Metodologias Ágeis I e II
**Prof. Gino Terentim · 2 aulas · Prioridade: ALTA para o vocabulário (vira questão conceitual fácil de pontuar)**

> Ideia central: **a abordagem de gestão (preditiva ou ágil) depende da natureza do problema** que você está tentando resolver — não do gosto do gestor.

## 1. Projeto × processo; mudança
| | **Projeto** | **Processo** ("run the business") |
|---|---|---|
| Natureza | cria algo **único**, **finito**, muda o negócio, tende a **modificar o status quo**, equipes transversais | contínuo/recorrente, ambiente controlado, variáveis conhecidas, tende a **manter o status quo** e aprimorar, equipes funcionais |
- **Mudança** = passagem/transição de um estado para outro diferente. Estágios: **incremental** (modificação de si mesmo, melhoria contínua), **transformacional** (redefinição de si mesmo), **disruptiva** (inovação). "Projetos direcionam mudanças."
- Gestão de **portfólios** (benefícios), **mudanças** (capacidades/novo comportamento) e **projetos** (entregas dentro das restrições). **Projeto** = organização temporária criada para entregar produtos conforme um **business case** aprovado.
- **Business Case Canvas:** justificativa (qual problema? por que agora?), opções de negócio, benefícios e desbenefícios, principais entregas e marcos, riscos, custos e **avaliação do investimento** (retorno esperado qualitativo/quantitativo), como medir o sucesso (indicadores). Sem consenso sobre o problema, não há como todos concordarem que o projeto foi um sucesso.

## 2. D.I.C.E. — chance de sucesso do projeto
Fatores: **D**uração (tempo até a conclusão: <2 meses=1; 2–4=2; 4–8=3; >8=4) · **I**ntegridade (desempenho/capacidade da equipe, incluindo liderança) · **C**ompromisso (C1 = gestão sênior; C2 = pessoas envolvidas/local) · **E**sforço (esforço **além** das responsabilidades habituais: <10%=1 … >40%=4).
**Pontuação = D + 2·I + 2·C1 + C2 + E.** Zonas: **7–14 = WIN** (altas chances de sucesso) · **15–17 = WORRY** (preocupante) · **18–28 = WOE** (alto risco).

## 3. Natureza dos problemas → abordagem
- **Problemas conhecidos** (olham o passado): resposta já existe → **processo preditivo** (planejar → executar → monitorar). Escopo fixo; incertezas acomodadas em **prazo e custo**.
- **Problemas conhecíveis** (presente): precisam de análise/experimentação; **adaptativo/empírico** ("frio/quente"): incertezas acomodadas no **escopo**; prazo e custo com tolerância zero.
- **Incognoscíveis** (futuro): impossível saber antes; **a resposta provavelmente está errada → dê um passo para descobrir**. "Lance logo."
- Conhecimento **a priori** (razão, dedução) × **a posteriori** (experiência, experimentação).
- **Não priorize o projeto; priorize o problema.** ("Não há nada tão inútil quanto fazer com eficiência o que não deveria ser feito." — Drucker.)
- Dica de aplicação em Data Science: pegar o problema, dividir em **microproblemas** e ver quais você já sabe resolver (preditivo) e quais exigem experimentação (ágil).

## 4. Origem do ágil e Manifesto
- **Takeuchi e Nonaka (1986, "The New New Product Development Game")**: empresas de sucesso (Fuji-Xerox, Canon, Honda, NEC…) usavam abordagem "**rugby**" em vez da "corrida de revezamento" sequencial. **6 características:** instabilidade embutida; equipes de projeto **auto-organizadas**; fases de desenvolvimento **sobrepostas**; **"multiaprendizagem"**; **controle sutil**; **transferência organizacional de aprendizado**. O termo **Scrum** vem do rugby.
- **Manifesto Ágil — 4 valores** ("valorizamos mais os itens da esquerda"): **indivíduos e interações** sobre processos e ferramentas · **software funcionando** sobre documentação extensa · **colaboração com o cliente** sobre negociação de contratos · **responder a mudanças** sobre seguir um plano. "Ágil é antes de tudo ser **leve e adaptável**."
- Em problemas **conhecíveis**: pessoas e interações > processos e ferramentas. Em problemas **conhecidos**: eficiência é métrica importante; em complexos, **eficácia** primeiro.

## 5. Cynefin (Dave Snowden) — estilo de liderança por domínio
| Domínio | Natureza | Prática | Liderança/métrica |
|---|---|---|---|
| **Claro (simples)** | causa-efeito óbvia, passado | **melhores práticas**, checklist, única resposta | forte dependência de liderança formal; **eficiência**; cultura de seguir regras |
| **Complicado** | requer análise/especialista; várias respostas boas | boas práticas, análise | especialistas |
| **Complexo** | causa-efeito só visível depois; incognoscível a priori | **experimentação** ("experimentos seguros para falha": *probe → sense → respond*) | liderança que cria ambiente seguro; **eficácia** |
| **Caótico** | crise; sem relação clara | agir primeiro para estabilizar | liderança direta |
| **Confuso** | não se sabe em qual domínio está | | |
- "A habilidade-chave de um líder é gerenciar o ambiente para que as pessoas tomem as decisões corretas" (Snowden). **Número de Dunbar:** rede social estável de ~100–150 pessoas (≤5 íntimos, ≤150 conhecidos). Tomada de decisão baseada em dados; **vieses** (Kahneman: muita aleatoriedade nas decisões).
- **Falhar em planejar é planejar para falhar** (Franklin), mas **experimentação segura** é essencial em ambiente complexo ("se fracasso não é opção, sucesso também não").

## 6. PMRL (Product–Market / Problem–Solution) — 9 estágios em 3 fases
- **Estágios 1–3 → Problem-Solution Fit (Exploration):** 1 *Discovery* (validar o problema com usuários; Design Thinking, entrevistas) · 2 *Prototyping* (protótipos baixa fidelidade) · 3 *Validation* (testes de usabilidade).
- **Estágios 4–6 → Product-Market Fit (Delivery):** 4 **MVP** (produto mínimo viável; lançar e coletar feedback; Lean Startup) · 5 *Iteration* (refinar com feedback) · 6 *Market Testing* (testar aceitação do mercado).
- **Estágios 7–9 → Scale (Exploitation):** 7 *Optimization* (eficiência, Lean/Six Sigma) · 8 *Expansion* (novos mercados/segmentos) · 9 *Scaling* (crescer base de usuários).
- Exploration → abordagem ágil/empírica; Exploitation → preditiva/processo conhecido.

## 7. Scrum (framework) — visão geral
- **Sprint:** ciclo de **no máximo 30 dias** (curto o suficiente para aprender rápido).
- **Papéis:** **Product Owner** (representa clientes/usuários, prioriza o **Product Backlog**, maximiza valor) · **Scrum Master** (líder-servidor/mentor da equipe autogerenciável, **remove impedimentos**, foco em processo e pessoas) · **Desenvolvedores** (time **multidisciplinar, autogerenciável**, tomam decisões e assumem responsabilidade pelas entregas).
- **Eventos:** **Sprint Planning** · **Daily** · **Sprint Review** · **Retrospective** (e a própria Sprint).
- **Artefatos e compromissos:** **Product Backlog → Meta do Produto**; **Sprint Backlog → Meta da Sprint**; **Incremento → Definição de Pronto (DoD)**.

## 8. Lean e Kanban
- **8 desperdícios (Lean):** 1 **superprodução** · 2 **espera** · 3 **transporte** · 4 **processamento excessivo** · 5 **inventário excessivo** · 6 **movimentação** · 7 **defeitos** (retrabalho) · 8 **talento não utilizado**. Multitarefa também gera perdas (exercício de contar múltiplos de 4 e consoantes ao mesmo tempo × em sequência).
- **Kanban** (método, "placa de sinalização"): visualizar o trabalho em colunas (A fazer → Análise → Execução → Conclusão → Feito); **limitar o trabalho em progresso (WIP limits)**; o fluxo **revela gargalos**; **"Pare de começar, comece a terminar!"** (sistema puxado); raias para classes de serviço/prioridade.
- Scrum é **framework**; Kanban é **método**.

## Pergunta típica
- Diferença entre projeto e processo; entre abordagem preditiva e adaptativa (onde cada uma acomoda incerteza). · Valores do Manifesto Ágil. · Papéis/eventos/artefatos do Scrum. · O que é WIP limit. · Domínios do Cynefin. · Fórmula e zonas do DICE. · Os 8 desperdícios.
