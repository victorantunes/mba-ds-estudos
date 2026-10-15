# 07 · Cloud Computing (I e II)
**Prof. Rodrigo Vale · 2 aulas (19 e 26/08/2025) · Prioridade: MÉDIA — conceitual; você, como dev, já conhece boa parte**

## 1. O que é nuvem e que problemas resolve
**Definição:** entrega de serviços de computação (servidores, armazenamento, software) **pela internet, com pagamento sob demanda** (analogia: energia elétrica).
| On-premises (modelo antigo) | Cloud (modelo novo) |
|---|---|
| **CAPEX** (comprar hardware caro) | **OPEX** (paga pelo uso) |
| manutenção e espaço físico | sem manutenção de hardware |
| lento para escalar | **elasticidade** em minutos |
| você é responsável por tudo | **responsabilidade compartilhada** |
Problemas resolvidos: alto custo inicial/ociosidade; dificuldade de escalar (Black Friday); lentidão (provisionar em minutos); manutenção de data center; baixa confiabilidade/DR (**múltiplos data centers**, replicar entre regiões); acesso global/colaboração.

**Desvantagens:** dependência da internet; **segurança e privacidade** (a principal causa de vazamento é **erro de configuração**, não hacker; soberania de dados; ameaça interna); **vendor lock-in**; **custos fora de controle** (*cloud sprawl*, egress, recursos ociosos); menos controle de hardware; **latência**; complexidade de gestão (FinOps, segurança cloud). *Muitas empresas "voltam do cloud" porque não implantaram controle de custo.*
**Gigantes:** **AWS** (pioneira/líder), **Azure** (mundo corporativo/Microsoft), **GCP** (dados, ML, contêineres).

## 2. Modelos de serviço (pirâmide) — CAI SEMPRE
| | O que é | Você gerencia | Analogia | Exemplos |
|---|---|---|---|---|
| **IaaS** | VMs, redes, storage | SO, apps, dados | alugar o terreno e as ferramentas | EC2, Azure VMs, Compute Engine |
| **PaaS** | plataforma para desenvolver/implantar sem cuidar da infra | só apps e dados | casa pré-fabricada | Heroku, App Engine, Elastic Beanstalk |
| **SaaS** | software pronto | nada | apartamento mobiliado | Gmail, Office 365, Salesforce, Netflix |
**Topo = mais conveniência/menos controle; base = mais controle/menos conveniência.** **Soluções totalmente gerenciadas** (ex.: **Cloud SQL**): o provedor cuida de provisionamento, patches, escala, backup/DR e HA.

## 3. Modelos de implantação
- **Pública:** infra do provedor, **multi-tenant**; menor custo, escala quase infinita; startups/sites.
- **Privada:** uso exclusivo de uma organização (própria ou hospedada); máximo controle/segurança; bancos, governos. (Na prática, "nuvem privada" de provedor público = **VPC**; privada de verdade = rede **e host** só da sua empresa.)
- **Híbrida:** conecta on-prem (privada) + pública; dados sensíveis locais e nuvem para escalar/DR (ex.: varejista usa nuvem na Black Friday).

## 4. Pilares da infraestrutura
- **Computação:** **VMs** (computador completo) e **contêineres** (virtualização mais leve; empacotam código+dependências).
- **Armazenamento:** **objetos** (quase infinito, S3), **blocos** (discos das VMs, EBS, rápido), **arquivos** (compartilhado por várias VMs, EFS).
- **Rede:** **VPC** (fatia privada isolada), **sub-redes** (pública para web, privada para BD), **grupos de segurança** (firewall da VM: portas liberadas, ex. porta 80). Acesso a VM por SSH exige configuração de segurança.

## 5. Serverless e bancos
- **Serverless/FaaS:** "execute código, não gerencie servidores" (servidores existem, o provedor cuida). Você escreve a função, define um **gatilho (trigger)** (upload em bucket, requisição HTTP POST, cron) e a nuvem aloca/libera recursos. **Vantagens:** paga só pelos **milissegundos** de execução (ocioso = custo zero), escala automática de 0 a milhares, menos carga operacional. **Desvantagens:** **cold start** (latência na primeira execução, 1–3 s), **limite de tempo de execução** (5–15 min) e de memória, monitoramento/debug difícil, **vendor lock-in** (Lambda, Cloud Functions não portam sem reescrever).
- **DBaaS:** banco totalmente gerenciado (instalação, patches, backup, HA).
  - **SQL (relacional):** tabelas, **schema fixo**, SQL, **ACID** (Atomicidade, Consistência, Isolamento, Durabilidade); ideal para transações financeiras/ERP; difícil escalar **horizontalmente**; rígido. (MySQL, PostgreSQL, SQL Server, Oracle, Cloud SQL, RDS.)
  - **NoSQL:** **schema flexível**, escalabilidade horizontal, prioriza disponibilidade e velocidade (modelo **BASE**: Basically Available, Soft state, Eventually consistent); **consistência eventual**, sem linguagem padrão, JOIN ruim. Tipos: **documentos** (MongoDB, Firestore), **chave-valor** (Redis, DynamoDB; cache/sessão), **colunar** (Cassandra, Bigtable; IoT/telemetria), **grafo** (Neo4j, Neptune; redes sociais/recomendação).
- **Kubernetes** (orquestração de contêineres em cluster: painel de controle + nós) e **service mesh**. **CI/CD:** *CI* = mesclar o trabalho dos devs numa linha principal várias vezes ao dia; *CD* = produzir entregável em ciclos curtos, pronto para release a qualquer momento (build → teste → deploy; multi-cloud).
- **Balanceamento de carga** e **autoscaling** de VM/BD.

## 6. Segurança, IAM e custos
- **Modelo de responsabilidade compartilhada:** o provedor é responsável pela segurança **DA** nuvem (hardware, data centers); você pela segurança **NA** nuvem (dados, firewall/rede, senhas, permissões). *A configuração errada é sua.*
- **IAM** (Identity and Access Management): **Identidade** (quem; usuário, grupo ou serviço) · **Permissão** (o que pode fazer) · **Recurso** (em quê). **Princípio do menor privilégio (PoLP).** 3 pilares: **autenticação** ("você é quem diz?": algo que sabe/tem/é; **MFA essencial**), **autorização** (políticas e **roles**) e **auditoria** (quem fez o quê, onde e quando; LGPD). Boas práticas: MFA, nunca `*.*`, usar grupos/roles em vez de usuário direto, revisar permissões, **SSO**. Ex.: app em VM acessando bucket → **role** com política de leitura, **nunca chaves no código**.
- **FinOps:** responsabilidade financeira no modelo variável (**gastar melhor, não só menos**); cultura Engenharia + Finanças + Negócio. **Tags** (chave-valor) para alocar custos; dashboards (Cost Explorer) e **alertas de orçamento**. Otimização: **rightsizing**, caça a **recursos zumbis** (discos soltos, IPs, snapshots), **agendamento** (desligar ambiente de teste fora do expediente, ~70% de economia). Ciclo contínuo: **Informar → Otimizar → Operar**.

## 7. Multi-cloud
Usar vários provedores numa arquitetura. **Por quê:** best-of-breed, **evitar lock-in**, exigência de clientes (ex. Walmart não quer SaaS na AWS), ROI, segurança, baixa latência, menos sujeito a desastres. **Contra:** **custo de egress**, governança/conformidade, ferramentas em ilhas, falta de gerenciamento unificado, escassez de pessoal. **Padrões:** **cloud bursting** (data center local + nuvem para picos, com réplica de leitura do BD na nuvem e escrita no mestre), edge/IoT, soberania de dados, DR.

## 8. Cloud II — Dados na nuvem (ciclo de vida da análise)
- **Dados → informação → insight** ("dados são o novo petróleo": precisam ser refinados).
- **4 tipos de análise:** **descritiva** (o que aconteceu?), **diagnóstica** (por que?), **preditiva** (o que vai acontecer?), **prescritiva** (o que devemos fazer? otimização/simulação/IA).
- **Dados como produto (DaaP):** descobrível, endereçável, confiável (SLOs), compreensível (metadados), seguro, valioso por si só; equipes de produto descentralizadas e duráveis.
- **Ciclo de vida:** **Coletar → Processar → Armazenar → Analisar → Ativar → Empoderar.**
- **Fila de mensagens (MQ)** × **streaming de eventos:** fila entrega uma mensagem a **um** consumidor e a remove; streaming (Kafka) mantém **eventos imutáveis e reproduzíveis**, vários consumidores (publish-subscribe). MQ dá desacoplamento, tolerância a falhas, balanceamento e absorve picos.
- **CDC (Change Data Capture):** captura INSERT/UPDATE/DELETE e envia só as mudanças. Métodos: **baseado em log** (mais popular, baixo impacto), por **gatilhos** (sobrecarga) e por **consulta** (pode perder alterações e DELETEs).
- **Apache Kafka:** plataforma de streaming distribuída (LinkedIn → Apache): escalável, durável, alto rendimento, desacopla produtores/consumidores.
- **Batch × tempo real:** batch = grande volume, alta latência, agendado, mais barato (folha, ETL); tempo real = pequenos eventos, latência mínima, mais caro (fraude, monitoramento de paciente).
- **Hadoop** (HDFS + MapReduce, em disco) × **Apache Spark** (**processamento em memória**, até 100× mais rápido; RDDs imutáveis e tolerantes a falhas; DAG; ETL, SQL, ML, streaming).
- **Windowing** em streaming: **fixed/tumbling**, **hopping**, **session**; **dados atrasados e marca d'água (watermark)** (tempo do evento × tempo de processamento).
- **Formatos:** **Parquet** (colunar, compressão eficiente, bom para análise; binário, escrita mais lenta) × **Avro** (baseado em linha, menor latência de escrita, bom para streaming). **Apache Iceberg:** *formato de tabela* sobre Parquet em data lake: transações **ACID**, evolução de esquema, particionamento oculto, **time travel**, arquitetura **lakehouse**; 3 camadas: catálogo, metadados, dados.
- **Spark SQL:** SQL + DataFrame API sobre dados distribuídos; otimizador **Catalyst**; plano **lógico** ("o quê") × **físico** ("como").

## Pergunta típica
IaaS/PaaS/SaaS (exemplos); CAPEX × OPEX; responsabilidade compartilhada; menor privilégio e MFA; cold start; SQL × NoSQL (ACID × BASE); multi-cloud (prós e contras, egress, cloud bursting); batch × streaming; Hadoop × Spark; Parquet × Avro; 4 tipos de análise.
