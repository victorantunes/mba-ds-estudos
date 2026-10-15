# 03 · Business Intelligence e Data Visualization
**Profa. Viviane Martins Ferreira · 3 aulas · Prioridade: MÉDIA (conceitual + Power BI)**

> Disciplina muito prática (Power BI). Para avaliação, o que tende a ser cobrado são **conceitos**: o que é BI, ETL, self-service, dataviz, governança, privacidade, e **boas práticas de gráficos/dashboards**.

## 1. Conceitos de Business Intelligence
- **BI** = transformar **dados em informação** para apoiar decisões nas organizações; analisar dados e correlacioná-los para trazer uma informação coerente. **BI é um conceito, não uma ferramenta** ("vou pegar no BI" = vou pegar em uma ferramenta; o conceito não é isso).
- Quanto mais cedo você entende o **contexto do negócio**, melhor o resultado. Fluxo do trabalho de análise: **entender o contexto → identificar a fonte → importar/tentar → desenvolver reports e dashboards**. Fatores importantes: entendimento do cenário, **definição de escopo**, mapeamento de tecnologia, profissionais envolvidos, "qual o destino / como chegar".
- **Premissa:** nunca trabalhar com "achismo" ("eu acho que…"); definir as **métricas de acordo com o objetivo inicial** (se não está no objetivo, não calcula).
- Documentação é trabalhosa mas essencial para o sucesso do projeto.
- **Análise preditiva** dá um norte do que pode acontecer, não certeza.
- **Data mining**: separar o que presta do que não presta nos dados (inclusive colunas aparentemente inúteis podem ser úteis combinadas com outras).

### Fases do processo de BI (ETL → modelagem → visualização → publicação)
**ETL = Extract – Transform – Load.** Etapas: identificação → coleta → limpeza e transformação → modelagem → armazenamento → visualização → publicação.
- Fontes: arquivos (.txt, .csv, .xlsx), bancos (Oracle, SQL Server, MySQL, DB2), data warehouses.

### Self-Service Analytics
Simplifica a análise para usuários que **não são da área de tecnologia**: autonomia para criar análises, relatórios e dashboards **com suporte de uma base tecnológica estruturada** (analogia do restaurante self-service).
- **Pilares técnicos:** DW (Data Warehouse), Analytics (análises avançadas), Data Viz. **Pilares humanos/organizacionais:** skills, recursos. **Entregáveis:** reports, análises, dataviz.
- **Fatores de sucesso:** governança de dados, cultura orientada a dados, capacitação, estrutura robusta.
- **Benefícios:** agilidade na tomada de decisão, **independência dos times de TI**, redução de custos, aumento da produtividade, foco em análises estratégicas.

## 2. Data Visualization (#dataviz)
- Objetivo: ir do **incompreensível para o compreensível**; "contar a história" com objetividade e clareza.
- **Processo de DataViz (7 etapas):** definir o objetivo → adquirir os dados → formatar os dados → filtrar → analisar → representar → refinar e interagir.
- **Pergunte antes de desenhar:** *o que* quero mostrar? *como* quero mostrar? *para quem* (público-alvo)?
- **Erros comuns (o que NÃO fazer):** excesso de dados no gráfico, visuais inadequados, dados repetidos/redundantes, objetivo não claro, sem título, sem cor/padrão, "nem todos os dados são importantes".
- **Escolha do gráfico:** comparação **por data/período → gráfico de linha**; **categorias e quantidades → pizza/rosca** (com cuidado: vários autores desaconselham pizza com muitas fatias); colunas/barras para comparação; tabela quando precisa dos valores exatos; **o melhor gráfico não é o que você gosta e sim o que é interpretável**.
- **Hierarquia visual:** fontes, títulos, subtítulos; padronizar tamanho, posição, cores e fontes; usar **grades (grid)**; respeitar a **identidade visual do cliente** (cores da marca; evitar cores de concorrente). Cores quentes (vermelho/laranja) chamam atenção/alerta, mas nem sempre vermelho = problema; azul = mais sério/fechado.
- **Drill down** = detalhar o dado investigando níveis mais granulares. **UX (User Experience)** = facilidade para o usuário interpretar o que vê.
- Dashboard × infográfico: dashboard é analítico/interativo; infográfico é mais ilustrativo. Ferramentas de design: Figma, Adobe Color, Flaticon (ícones), bancos de imagens.

## 3. Power BI (o que apareceu)
- Lançado em **2015**; líder de mercado segundo o Gartner. Componentes: **Desktop** (desenvolver reports), **Service** (consumo/publicação), **Mobile**, **Embedded** (embarcar em apps de terceiros).
- **Power Query** = editor de transformação de dados (renomear colunas, remover colunas, criar coluna condicional, mudar tipos). Cuidado com o tipo de dado: `AVERAGE` não funciona com texto (string).
- **Medidas (DAX):** cálculos criados por funções DAX (SUM, AVERAGE, COUNT, CALCULATE…). Medida ≠ coluna. Usar **COUNT de uma coluna sempre preenchida** (ex. ID), não de uma com brancos.
- **Modelagem de dados:** relacionar tabelas por **chave primária / chave estrangeira** (ex. ID_localidade, ID_depto). **Nunca remova um relacionamento sem saber** (corrompe visuais). Quando há várias tabelas e joins, filtros nem sempre funcionam como esperado → testar o resultado.
- **Hierarquia de datas** (dia/mês/ano) ao definir coluna como data. **Atualização agendada** exige Power BI Service + **gateway** instalado.
- Importar fonte: pasta/arquivo/banco (precisa nome do servidor e **permissão de acesso**; falar com TI/cibersegurança).

## 4. Gestão, governança e privacidade de dados (aula 3)
- **Governança de dados** = definir **quem** gerencia a informação como **ativo da organização**, **como** (regras, procedimentos, políticas, papéis e responsabilidades sobre o ciclo de vida da informação), e **tecnologia** que suporta. Garante qualidade, consistência, completude, disponibilidade e segurança.
- **Privacidade de dados:** sigilo e confidencialidade — não só dados de clientes, mas também estratégia do negócio, documentos do projeto, e-mails e etapas de negociação.
- **NDA (Non-Disclosure Agreement)** = acordo de sigilo / contrato de confidencialidade assinado entre as partes.
- Boas práticas: senhas seguras, não usar Wi-Fi público, antivírus atualizado, cautela com documentação do cliente.
- **Shadow IT** = qualquer sistema, dispositivo ou serviço usado na organização **sem conhecimento ou aprovação do departamento de TI**.
- **ANPD** (Autoridade Nacional de Proteção de Dados): conscientizar, fiscalizar; regulamentação **LGPD** (ver resumo 12). Riscos citados: ataques cibernéticos, privacidade, fraude, shadow IT.
- **Cultura data-driven**: decisões guiadas por dados; usabilidade de ferramentas de analytics.

## Pergunta típica
- Defina ETL e as fases do BI. · O que é self-service analytics e quais seus benefícios? · Qual gráfico usar para série temporal? · O que é shadow IT? · O que é NDA? · Para que serve uma chave estrangeira no modelo de dados do Power BI? · Diferença entre BI (conceito) e Power BI (ferramenta).
