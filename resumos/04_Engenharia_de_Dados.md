# 04 · Engenharia de Dados
**Prof. Guilherme Lima · 3 aulas · Prioridade: MÉDIA (você, como dev, já domina boa parte; foque nos conceitos e vocabulário)**

> Dica do professor (aula 1): *"se cair na avaliação 'O que é engenharia de dados?', provavelmente eu vou errar se só decorar a definição"* → entenda o papel. E na aula 3: *"O que é uma view? Se cair na avaliação, não erre isso."*

## 1. O que é engenharia de dados
- **Definição:** área responsável pelo **desenvolvimento e manutenção de sistemas que coletam, organizam e processam dados**. Trata de **movimentação, manipulação e gerenciamento de dados**: construir a base para a ciência de dados.
- Fluxo: **dados brutos → engenharia (coleta, armazenamento, transformação, entrega) → cientista de dados / BI / ML (análise e modelos)**.
- **Problema que resolve:** cientistas de dados gastam ~**80% do tempo preparando dados** (limpeza, tratamento de nulos, criação de variáveis) e ~20% no modelo. O engenheiro de dados **automatiza coleta, limpeza e transformação** e inverte essa divisão.
- **O engenheiro de dados normalmente NÃO:** cria modelos de ML, faz relatórios/dashboards, faz análises, cria KPIs nem desenvolve aplicativos de software.
- É comum usar **cloud** em projetos maiores. SQL e Python são as linguagens do dia a dia.
- Problemas típicos ao preparar dados: **valores ausentes, dados duplicados, formatos diferentes/despadronizados**.

### ETL
**Extract – Transform – Load:** coletar de diferentes fontes (CSV, API, bancos) → transformar para atender às necessidades (limpar, padronizar, tratar nulos: remover linhas ou preencher com média/mediana/regra de negócio) → carregar no destino (banco/DW) já estruturado. A automação disso = **pipeline de dados**.

### Big Data
- **1998: John Mashey** usa o termo "Big Data" para o crescimento do armazenamento/produção de dados. Em **2001 aparecem os 3 Vs: Volume, Velocidade, Variedade.**
- Previsão citada: ~175 zettabytes de dados em 2025.
- Resposta histórica: dividir dados em **clusters** com hardware comum (commodity) → origem do Hadoop e afins.
- **Maturidade dos dados:** começa simples — **não precisa de microsserviços/Redis/cluster para poucos dados**. Papel do engenheiro: não criar problemas que não existem.

## 2. Bancos relacionais e SQL (revisão rápida)
- **Banco relacional:** dados em **tabelas** (linhas/colunas) que se **relacionam**. **Chave primária (PK)** identifica cada linha; **chave estrangeira (FK)** liga tabelas. *Priorize PK simples* (performance e relacionamentos).
- Comandos: `CREATE DATABASE`, `USE`, `CREATE TABLE … (id INT PRIMARY KEY AUTO_INCREMENT, …)`, `INSERT INTO … VALUES`, `SELECT`, `UPDATE … SET … WHERE`, `DELETE … WHERE`. **Sempre `WHERE` em UPDATE/DELETE.** Strings entre aspas. Erro 1064 do MySQL = erro de sintaxe.
- **String vazia ≠ NULL.** Dados nulos impedem cálculos estatísticos.
- `JOIN` ligando tabelas (livros ↔ autores ↔ gêneros) e `GROUP BY` para agregar (ex.: total de livros por idioma).
- **Vantagem de centralizar dados em um banco:** performance, consistência (um único ID por autor mesmo que o nome venha escrito de formas diferentes), não depender de Excel/CSV/API soltos.
- Convenção: tabelas no plural quando representam coleção; o time de back-end orientado a objetos costuma usar singular.

## 3. Modelagem: MER (aula 2)
- **Entidade** = elemento do mundo real relevante ao sistema (cliente, produto). **Atributo** = característica/propriedade da entidade (nome, preço).
- **Entidade forte:** existe por si só, tem chave primária própria (clientes, produtos).
- **Entidade fraca:** depende de outra para existir, **não tem chave primária completa sem a chave da entidade da qual depende** (ex.: **itens de pedido** dependem de **pedido**).
- **Entidade associativa:** representa um relacionamento que tem atributos próprios (ex.: **vendas** liga clientes e produtos e guarda data e quantidade).
- **Relacionamento** entre duas tabelas por PK/FK.
- **Sistemas operacionais × analíticos:** *operacionais* = backend, regras de negócio, aplicação modifica os dados (muitas escritas); *analíticos* = atendem analistas de negócio e cientistas de dados (leitura/consulta). A base de dados analítica muda com **frequência menor** que a operacional. O desafio da engenharia é servir **pessoas diferentes com necessidades diferentes**.

## 4. View × Stored Procedure (aula 3 — caiu na destaque do professor)
| | **View** | **Stored procedure** |
|---|---|---|
| O que é | **tabela virtual**/consulta SQL salva, baseada em uma ou mais tabelas | **bloco de código SQL armazenado**, como uma função pré-programada |
| Altera dados? | **Não**, só consulta (abstrai dados) | **Pode** alterar dados (insert/update/delete) |
| Lógica/params | sem lógica de programação | pode ter lógica, aceitar parâmetros de entrada e saída |
| Para quê | reutilizar **consultas complexas**, facilitar relatórios, simular uma **tabela personalizada**, otimizar consultas | automatizar tarefas repetitivas (relatórios, cálculos, inserções, atualizações); **segurança e controle, organização do banco, reutilização de código** |
- Exemplo: `CREATE VIEW livros_por_idioma AS SELECT idioma, COUNT(*) … GROUP BY idioma;` depois `SELECT * FROM livros_por_idioma;`.

## 5. Arquitetura: monólito × Data Mesh
- **Centralizado (monólito):** uma equipe coleta e organiza todos os dados; toda a base em um banco só. **Vantajoso no início pela simplicidade**, mas esteja pronto para dividir no futuro.
- **Data Mesh:** **cada time cuida dos dados do seu domínio** e os prepara para uso por outros times (domínios precisam conversar).
- A separação rígida entre **arquitetura e engenharia** de dados está desaparecendo.

## Pergunta típica
- Defina engenharia de dados e diga o que o engenheiro **não** faz. · O que é ETL? · Diferencie view e stored procedure. · O que é entidade fraca? Dê exemplo. · Diferencie sistema operacional e analítico. · Cite 3 problemas ao preparar dados. · Quais os 3 Vs?
