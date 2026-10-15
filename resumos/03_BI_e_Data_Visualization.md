# 03 · Business Intelligence e Data Visualization
**Profa. Viviane Martins Ferreira · 3 aulas · Prioridade: MÉDIA (conceitual + Power BI)**

> **Em uma frase:** BI é o processo de transformar dados dispersos em informação confiável e visual para decidir melhor — e a visualização é a ponte entre o número e a decisão.

**Pré-requisitos:** noção de tabelas e bancos de dados. **Vem depois:** 04 (engenharia de dados) e 12 (LGPD).

## Por que isso importa (intuição)
Dados brutos em planilhas e bancos ninguém lê. BI cria um **caminho organizado** (extrair → limpar → modelar → mostrar) para que a pessoa de negócio enxergue a resposta. Um bom gráfico responde uma pergunta; um gráfico ruim esconde a resposta mesmo com dados certos.

## 1. Conceitos de BI
- **BI:** conjunto de processos para **transformar dados em informação** de apoio à decisão. **É um conceito, não uma ferramenta** (Power BI é uma ferramenta de BI).
- **Premissas:** entender o contexto do negócio primeiro; **definir escopo e métricas a partir do objetivo** (se não está no objetivo, não se calcula); nunca decidir por "achismo"; **documentar**.
- **Fluxo do trabalho:** entender o contexto → identificar a fonte → importar → desenvolver reports e dashboards.
- **Data mining:** separar o que presta do que não presta nos dados (colunas aparentemente inúteis podem ajudar combinadas). **Análise preditiva** dá um norte do que pode acontecer, não certeza.

### ETL e fases do BI
- **ETL = Extract – Transform – Load:** **extrair** das fontes (arquivos, bancos, data warehouses) → **transformar** (limpar, padronizar, tipar) → **carregar** no destino.
- **Fases:** identificação → coleta → limpeza e transformação → modelagem → armazenamento → visualização → publicação.

### Self-service analytics
Permite que **usuários de negócio** (não de TI) criem análises e dashboards sozinhos, **sobre uma base técnica estruturada** (analogia do restaurante self-service: o cliente se serve, mas a cozinha está organizada).
- **Pilares:** técnicos (DW, analytics, dataviz) e humanos (skills, recursos). **Sucesso depende de:** governança, cultura de dados, capacitação, estrutura robusta.
- **Benefícios:** agilidade na decisão, **independência da TI**, redução de custos, mais produtividade.

## 2. Visualização de dados (dataviz)
- **Objetivo:** do incompreensível ao compreensível; contar a história com clareza.
- **Processo (7 etapas):** definir o objetivo → adquirir → formatar → filtrar → analisar → representar → refinar e interagir.
- **Antes de desenhar, pergunte:** *o que* mostrar? *como*? *para quem*?
- **Escolha do gráfico:** **série no tempo → linha**; comparar categorias → barras/colunas; **partes de um todo → pizza/rosca (poucas fatias)**; valores exatos → tabela. O melhor gráfico é **o mais interpretável**, não o mais bonito.
- **Erros comuns:** excesso de dados, visual inadequado, informação repetida, objetivo confuso, falta de título, ausência de padrão de cores.
- **Hierarquia visual e identidade:** padronize fontes, tamanhos, posições e cores; use **grid**; respeite a identidade visual do cliente. Cor quente chama atenção.
- **Drill down:** detalhar do nível agregado ao granular. **UX:** facilidade de interpretação para o usuário. Dashboard = analítico e interativo; infográfico = ilustrativo.

**Exemplo.** "Vendas por mês nos últimos 24 meses" → gráfico de **linha** (tempo no eixo X). "Participação de cada região nas vendas do ano" → **rosca/pizza** com 4–5 regiões; com 15 regiões, prefira barras ordenadas.

## 3. Power BI (o que apareceu)
- **Componentes:** Desktop (desenvolver), Service (publicar/consumir), Mobile, Embedded.
- **Power Query:** editor de transformação (renomear, remover colunas, coluna condicional, mudar tipos). **Tipo de dado errado** quebra cálculos (média de texto não funciona).
- **Medidas DAX:** cálculos como SUM, AVERAGE, COUNT, CALCULATE; **medida ≠ coluna**. Use COUNT em coluna sempre preenchida (ID).
- **Modelo de dados:** tabelas relacionadas por **chave primária/estrangeira**; **não remova relacionamentos sem saber**.
- **Atualização agendada:** exige Service + **gateway**. Acesso a bancos exige servidor e permissão (alinhar com TI/segurança).

## 4. Governança, privacidade e riscos
- **Governança de dados:** define **quem** gerencia a informação como ativo, **como** (regras, políticas, papéis) e com que **tecnologia**; garante qualidade, consistência, disponibilidade e segurança.
- **Privacidade:** vale para dados de clientes **e** para estratégia, documentos e negociações. **NDA** = acordo de confidencialidade assinado entre as partes.
- **Shadow IT:** sistema, dispositivo ou serviço usado **sem conhecimento/aprovação da TI**.
- **ANPD** fiscaliza a LGPD (resumo 12). **Cultura data-driven:** decisões guiadas por dados.
- Boas práticas: senhas fortes, não usar Wi-Fi público, antivírus atualizado, cuidado com documentos do cliente.

## Armadilhas e confusões comuns
| Confusão | O correto |
|---|---|
| BI = Power BI | BI é o **conceito**; Power BI é uma **ferramenta** |
| Quanto mais dados no gráfico, melhor | excesso de dados atrapalha; mostre o que responde ao objetivo |
| Pizza serve para tudo | só para **poucas** partes de um todo |
| Shadow IT = ataque hacker | é uso de TI **não autorizada/desconhecida** pela TI |
| Self-service dispensa TI | exige **base estruturada e governança** da TI |
| Medida = coluna calculada | medida é calculada na consulta (DAX); coluna é armazenada na tabela |

## Resumo-relâmpago
- BI: dados → informação para decidir. ETL: extrair, transformar, carregar.
- Self-service: autonomia do negócio sobre base governada.
- Linha para tempo; barras para comparar; pizza para poucas partes.
- Governança = quem, como e com qual tecnologia; NDA = sigilo; Shadow IT = TI sem aprovação.

## Teste-se
1. Defina ETL e cite as fases do BI.
<details markdown="1"><summary>Ver resposta</summary>ETL = Extract, Transform, Load. Fases: identificação, coleta, limpeza/transformação, modelagem, armazenamento, visualização, publicação.</details>

2. Qual gráfico usar para uma série temporal?
<details markdown="1"><summary>Ver resposta</summary>Gráfico de linha, com o tempo no eixo X.</details>

3. O que é shadow IT e por que é um risco?
<details markdown="1"><summary>Ver resposta</summary>Uso de sistemas/serviços sem conhecimento ou aprovação da TI; escapa de controles de segurança, governança e LGPD.</details>

4. Para que serve uma chave estrangeira no modelo do Power BI?
<details markdown="1"><summary>Ver resposta</summary>Para relacionar duas tabelas (liga a coluna de uma tabela à chave primária da outra), permitindo que filtros e medidas funcionem entre elas.</details>

## Pergunta típica
Defina ETL e as fases do BI · o que é self-service analytics e quais seus benefícios · qual gráfico usar para série temporal · o que é shadow IT · o que é NDA · para que serve uma chave estrangeira no Power BI · diferença entre BI (conceito) e Power BI (ferramenta)
