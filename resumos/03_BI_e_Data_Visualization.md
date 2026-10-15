# 03 · Business Intelligence e Data Visualization
**Profa. Viviane Martins Ferreira · 3 aulas · Prioridade: média (conceitual + Power BI)**

## O fio condutor deste capítulo

Uma empresa tem dados espalhados em planilhas, sistemas e bancos. Ninguém decide bem olhando para isso. **Business Intelligence (BI)** é o caminho que leva desses dados dispersos até uma informação clara, confiável e visual, na mão de quem decide. O capítulo percorre esse caminho na ordem em que ele acontece: primeiro o *conceito* e as etapas do BI; depois como *mostrar* os dados bem (visualização); em seguida a ferramenta usada no curso (Power BI); e por fim as regras do jogo sobre quem pode usar os dados e como protegê-los (governança e privacidade).

```mermaid
flowchart LR
  A["Fontes: planilhas, bancos, DW"] --> B["Extract"]
  B --> C["Transform"]
  C --> D["Load"]
  D --> E["Modelagem"]
  E --> F["Visualização: relatórios e dashboards"]
  F --> G["Decisão"]
```

## 1. O que é BI e como o trabalho acontece

BI é o conjunto de processos que **transforma dados em informação** para apoiar decisões. É importante fixar que BI é um **conceito**, e não uma ferramenta: Power BI é uma das ferramentas que implementam o conceito.

O trabalho começa por entender o **contexto do negócio**, porque tudo depende do objetivo. Um dos princípios da disciplina é: *se não está no objetivo, não se calcula*. As métricas são definidas a partir do que a empresa quer saber; "achismo" não entra. O fluxo típico é entender o contexto, identificar a fonte dos dados, importá-los e só então desenvolver relatórios e dashboards. Documentar cada decisão é trabalhoso, mas é o que torna o projeto sustentável.

O núcleo técnico é o **ETL**, que mostra a sequência em que o dado é preparado:

| Etapa | O que acontece | Exemplo |
|---|---|---|
| **E**xtract | os dados são extraídos de suas fontes | ler um CSV de vendas e uma tabela do ERP |
| **T**ransform | limpeza, padronização, correção de tipos | datas como data, moedas na mesma unidade |
| **L**oad | carga no destino em que serão consultados | gravar no data warehouse |

As **fases completas** do BI são: identificação, coleta, limpeza e transformação, modelagem, armazenamento, visualização e publicação.

> **Analogia.** O **self-service analytics** é o restaurante self-service: o cliente se serve sozinho, mas só porque existe uma cozinha organizada por trás. Pessoas de negócio criam as próprias análises e dashboards, **sobre uma base estruturada e governada**. Sem isso, vira bagunça. Quando funciona, traz agilidade, menos dependência da TI e menor custo.

## 2. Mostrar bem: a visualização de dados

Ter a informação certa não basta; é preciso que quem a vê **entenda** em segundos. A visualização de dados (dataviz) leva o leitor do incompreensível ao compreensível. O processo tem sete etapas: definir o objetivo, adquirir os dados, formatar, filtrar, analisar, representar e, por último, refinar e interagir.

Antes de desenhar, três perguntas ordenam o trabalho: *o que* quero mostrar, *como* e *para quem*. O tipo de gráfico decorre das respostas:

| Objetivo | Gráfico | Observação |
|---|---|---|
| acompanhar algo **ao longo do tempo** | linha | tempo no eixo horizontal |
| **comparar** categorias | barras ou colunas | ordene para facilitar a leitura |
| **partes de um todo** | pizza ou rosca | só com **poucas** fatias |
| valores **exatos** | tabela | quando o número importa mais que o formato |

O critério final é a **interpretabilidade**: o melhor gráfico é o que o leitor entende, e não o mais bonito. Erros recorrentes: excesso de dados, visual inadequado, informação repetida, ausência de título e de padrão de cores. Um painel profissional segue uma **hierarquia visual** (tamanhos de fonte, posição, grade) e respeita a identidade visual do cliente. Dois termos aparecem com frequência: **drill down** (detalhar do nível agregado para o granular, como ir de "vendas do país" para "vendas da loja") e **UX** (a experiência do usuário ao interpretar o que vê).

> **Exemplo resolvido.** "Vendas mensais dos últimos 24 meses" pede um gráfico de **linha**. "Participação de cada região nas vendas do ano" pede uma **rosca** se houver quatro ou cinco regiões, e **barras ordenadas** se houver quinze.

## 3. A ferramenta: Power BI

| Peça | Função |
|---|---|
| **Desktop** | onde se desenvolve o relatório |
| **Service** | publicar e consumir |
| **Mobile** | acesso no celular |
| **Embedded** | incorporar em outros sistemas |

O trabalho segue o fluxo do BI. No **Power Query** fazem-se as transformações: renomear e remover colunas, criar colunas condicionais e, principalmente, **ajustar os tipos de dado**, porque um número lido como texto quebra os cálculos. Depois, no **modelo de dados**, as tabelas são ligadas por **chaves**: uma **chave primária** identifica uma linha em uma tabela e a **chave estrangeira** a referencia em outra. É esse relacionamento que faz um filtro em uma tabela afetar a outra; por isso não se remove um relacionamento sem saber o que ele sustenta. Os cálculos são feitos por **medidas** escritas em **DAX** (SUM, AVERAGE, COUNT, CALCULATE): uma medida é calculada no momento da consulta, ao contrário de uma coluna, que fica armazenada na tabela. A atualização agendada dos dados exige o Service mais um **gateway**.

## 4. Governança, privacidade e segurança

À medida que os dados viram ativo, surge a pergunta: *quem pode fazer o quê com eles?* A **governança de dados** responde a isso: define **quem** gerencia a informação como ativo da organização, **como** (regras, políticas, papéis e responsabilidades ao longo do ciclo de vida do dado) e com que **tecnologia**. O objetivo é garantir qualidade, consistência, disponibilidade e segurança.

A **privacidade** vai além dos dados de clientes: estratégia, documentos de projeto e negociações também são sigilosos. Daí o **NDA** (*Non-Disclosure Agreement*), o acordo de confidencialidade assinado entre as partes. Um risco típico é o **shadow IT**: qualquer sistema, dispositivo ou serviço usado **sem conhecimento ou aprovação da TI**. A fiscalização da lei de proteção de dados cabe à **ANPD** (capítulo 12). Rotinas básicas: senhas fortes, evitar Wi-Fi público, antivírus atualizado.

## O que levar daqui

BI é o processo que leva dados a decisões, e o ETL (extrair, transformar, carregar) é o seu núcleo. O self-service dá autonomia ao negócio sobre uma base governada. A escolha do gráfico depende do objetivo (linha para tempo, barras para comparação, pizza para poucas partes). No Power BI, tipos de dado e relacionamentos por chaves são o que mais quebra os relatórios. Governança diz quem faz o quê com os dados; NDA protege o sigilo; shadow IT é o risco de TI sem aprovação.

## Erros que todo mundo comete

| Erro | Correção |
|---|---|
| Confundir BI com Power BI | BI é o **conceito**; Power BI é uma **ferramenta** |
| "Mais dados no gráfico é melhor" | excesso atrapalha; mostre o que responde ao objetivo |
| Usar pizza para muitas categorias | pizza é para **poucas** partes |
| "Self-service dispensa a TI" | exige **base estruturada e governança** |
| Tratar medida como coluna | medida é calculada na consulta (DAX); coluna é armazenada |

## Teste-se

1. Defina ETL e cite as fases do BI.
<details markdown="1"><summary>Ver resposta</summary>ETL = Extract, Transform, Load. Fases: identificação, coleta, limpeza/transformação, modelagem, armazenamento, visualização e publicação.</details>

2. Qual gráfico usar para uma série temporal?
<details markdown="1"><summary>Ver resposta</summary>Gráfico de linha, com o tempo no eixo horizontal.</details>

3. O que é shadow IT e por que é um risco?
<details markdown="1"><summary>Ver resposta</summary>É o uso de sistemas ou serviços sem conhecimento ou aprovação da TI; escapa dos controles de segurança, governança e proteção de dados.</details>

4. Para que serve uma chave estrangeira no modelo do Power BI?
<details markdown="1"><summary>Ver resposta</summary>Relaciona duas tabelas (liga a coluna de uma à chave primária da outra), permitindo que filtros e medidas funcionem entre elas.</details>

## Pergunta típica
Defina ETL e as fases do BI · o que é self-service analytics e quais seus benefícios · qual gráfico usar para série temporal · o que é shadow IT · o que é NDA · para que serve uma chave estrangeira no Power BI · diferença entre BI (conceito) e Power BI (ferramenta)
