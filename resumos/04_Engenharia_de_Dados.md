# 04 · Engenharia de Dados
**Prof. Guilherme Lima · 3 aulas · Prioridade: MÉDIA (você, como dev, já domina boa parte; foque nos conceitos e no vocabulário)**

> **Em uma frase:** engenharia de dados constrói e mantém a "tubulação" que coleta, limpa, organiza e entrega dados confiáveis para analistas, BI e modelos de ML.

**Pré-requisitos:** noção de SQL. **Vem depois:** 21 (Big Data/MLOps), 23 (wrangling).

> **Destaque do professor:** *"O que é engenharia de dados?"* e *"O que é uma view?"* — entenda o papel, não decore a definição.

## Por que isso importa (intuição)
Cientistas de dados gastam cerca de **80% do tempo preparando dados** e só ~20% modelando. O engenheiro de dados **automatiza essa preparação** (coleta, limpeza, transformação) para inverter a proporção. Pense em uma fábrica: o engenheiro cuida da linha de produção; o cientista usa o produto final.

## 1. O que é engenharia de dados
- **Definição:** desenvolvimento e manutenção de sistemas que **coletam, organizam e processam dados** — movimentação, manipulação e gerenciamento. Fluxo: **dados brutos → engenharia (coleta, armazenamento, transformação, entrega) → ciência de dados/BI/ML**.
- **Normalmente NÃO faz:** modelos de ML, dashboards/relatórios, análises, KPIs ou aplicativos de software.
- **Ferramentas do dia a dia:** SQL e Python; cloud em projetos maiores.
- **Problemas típicos dos dados:** valores ausentes, duplicados e formatos despadronizados.

### ETL e pipeline
- **ETL (Extract–Transform–Load):** **extrair** de fontes (CSV, API, bancos) → **transformar** (limpar, padronizar, tratar nulos: remover linhas ou preencher com média/mediana/regra de negócio) → **carregar** no destino estruturado (banco/DW).
- **Pipeline de dados** = a automação desse fluxo.

**Exemplo.** Vendas chegam por API (JSON), por planilha (CSV) e do ERP (SQL). O pipeline: lê as três fontes → padroniza datas e moedas → remove duplicados → grava em uma tabela única no DW. Os analistas consultam só essa tabela.

### Big Data
- Termo popularizado em **1998 (John Mashey)**; em **2001** surgem os **3 Vs: Volume, Velocidade e Variedade**. A resposta histórica foi dividir dados em **clusters** com hardware comum (origem do Hadoop).
- **Maturidade:** poucos dados **não precisam** de microsserviços nem cluster — o engenheiro não deve criar problemas que não existem.

## 2. Bancos relacionais e SQL (revisão)
- **Banco relacional:** dados em **tabelas** que se relacionam. **Chave primária (PK)** identifica cada linha; **chave estrangeira (FK)** liga tabelas.
- **Comandos:** `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE … SET … WHERE`, `DELETE … WHERE` (**sempre `WHERE` em UPDATE/DELETE**), `JOIN`, `GROUP BY`.
- **String vazia ≠ NULL.** Nulos impedem cálculos estatísticos.
- **Por que centralizar em um banco?** performance e **consistência** (um único ID por autor, mesmo que o nome apareça escrito de formas diferentes), em vez de depender de planilhas e APIs soltas.

## 3. Modelagem: MER
- **Entidade:** elemento do mundo real (cliente, produto). **Atributo:** propriedade da entidade (nome, preço).
- **Entidade forte:** existe por si só, com chave primária própria.
- **Entidade fraca:** depende de outra e **não tem chave primária completa sem a chave da entidade da qual depende** (ex.: **itens de pedido** dependem de **pedido**).
- **Entidade associativa:** representa um **relacionamento com atributos próprios** (ex.: **vendas** liga clientes e produtos e guarda data e quantidade).
- **Operacional × analítico:** operacional = aplicação/backend, muitas **escritas**; analítico = analistas e cientistas, muita **leitura**, atualiza com menos frequência.

## 4. View × Stored Procedure
- **View:** **consulta salva** que se comporta como tabela virtual; **não altera** dados; sem lógica de programação. Serve para reaproveitar consultas complexas e simplificar relatórios.
- **Stored procedure:** **bloco de código SQL armazenado**, como uma função; **pode alterar dados**, ter lógica e parâmetros. Serve para automatizar tarefas repetitivas, com segurança e reutilização.

| | View | Stored procedure |
|---|---|---|
| Altera dados? | Não | Pode |
| Lógica/parâmetros | Não | Sim |
| Uso típico | consulta reutilizável | rotina automatizada |

**Exemplo.** `CREATE VIEW livros_por_idioma AS SELECT idioma, COUNT(*) … GROUP BY idioma;` → depois `SELECT * FROM livros_por_idioma;`.

## 5. Arquitetura: monólito × Data Mesh
- **Centralizado (monólito):** uma equipe cuida de toda a base; **simples e bom no começo**.
- **Data Mesh:** **cada time cuida dos dados do seu domínio** e os disponibiliza aos outros.

## Armadilhas e confusões comuns
| Confusão | O correto |
|---|---|
| Engenheiro de dados cria modelos de ML | normalmente **não**; prepara a base para quem cria |
| View altera dados | view só **consulta**; quem altera é a stored procedure |
| String vazia = NULL | são coisas diferentes |
| UPDATE/DELETE sem WHERE é inofensivo | atinge **todas** as linhas |
| Entidade fraca = tabela menos importante | é a que **depende** de outra para existir |
| Todo projeto precisa de cluster/microsserviços | poucos dados dispensam |

## Resumo-relâmpago
- Eng. de dados = coletar, organizar, processar e entregar dados; ETL = extrair, transformar, carregar.
- View = tabela virtual (só leitura); procedure = código armazenado (pode alterar).
- Entidade fraca depende de outra (itens de pedido); associativa = relacionamento com atributos (vendas).
- 3 Vs: Volume, Velocidade, Variedade. Operacional escreve; analítico lê.

## Teste-se
1. Defina engenharia de dados e diga o que o engenheiro normalmente não faz.
<details markdown="1"><summary>Ver resposta</summary>Desenvolve/mantém sistemas que coletam, organizam e processam dados. Normalmente não cria modelos de ML, dashboards, análises, KPIs nem aplicativos.</details>

2. Qual a diferença entre view e stored procedure?
<details markdown="1"><summary>Ver resposta</summary>View é tabela virtual/consulta salva, só leitura e sem lógica. Procedure é bloco de código armazenado que pode alterar dados, ter lógica e parâmetros.</details>

3. Dê um exemplo de entidade fraca.
<details markdown="1"><summary>Ver resposta</summary>Itens de pedido: dependem do pedido e sua chave inclui a chave do pedido.</details>

4. Cite três problemas comuns ao preparar dados.
<details markdown="1"><summary>Ver resposta</summary>Valores ausentes, dados duplicados e formatos despadronizados.</details>

## Pergunta típica
Defina engenharia de dados e diga o que o engenheiro não faz · o que é ETL · diferencie view e stored procedure · o que é entidade fraca e dê exemplo · diferencie sistema operacional e analítico · cite 3 problemas ao preparar dados · quais os 3 Vs
