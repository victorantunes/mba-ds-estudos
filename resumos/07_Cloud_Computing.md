# 07 · Cloud Computing (I e II)
**Prof. Rodrigo Vale · 2 aulas · Prioridade: MÉDIA — conceitual; você, como dev, já conhece boa parte**

> **Em uma frase:** nuvem é alugar computação **pela internet, pagando pelo uso**, em vez de comprar e manter servidores — com ganho de elasticidade e custo variável, mas novos riscos de segurança e de custos descontrolados.

**Pré-requisitos:** noção de servidores e redes. **Vem depois:** 21 (Big Data/MLOps).

## Por que isso importa (intuição)
Analogia da **energia elétrica**: você não constrói uma usina; liga e paga pelo consumo. Uma loja que vende 10× na Black Friday não precisa comprar servidores para o ano todo — **escala por alguns dias e paga só por isso**.

## 1. Nuvem × on-premises
| On-premises | Nuvem |
|---|---|
| **CAPEX** (compra de hardware caro) | **OPEX** (paga pelo uso) |
| manutenção e espaço físico | sem manutenção de hardware |
| escala lenta | **elasticidade** em minutos |
| você responde por tudo | **responsabilidade compartilhada** |
- **Desvantagens:** dependência da internet; **segurança** (a principal causa de vazamento é **erro de configuração**); **vendor lock-in**; **custos fora de controle** (*cloud sprawl*, egress); latência; complexidade de gestão (FinOps). **Gigantes:** AWS, Azure, GCP.

## 2. Modelos de serviço (cai sempre)
- **IaaS:** VMs, redes, storage; **você gerencia SO, apps e dados** (EC2, Azure VMs). Analogia: alugar o terreno e as ferramentas.
- **PaaS:** plataforma para desenvolver e implantar **sem cuidar da infra**; você gerencia **apps e dados** (App Engine, Elastic Beanstalk). Analogia: casa pré-fabricada.
- **SaaS:** **software pronto**; você gerencia nada (Gmail, Office 365, Salesforce). Analogia: apartamento mobiliado.
- **Quanto mais alto, mais conveniência e menos controle.** Soluções **totalmente gerenciadas** (Cloud SQL): o provedor cuida de patches, backup e alta disponibilidade.

## 3. Modelos de implantação
- **Pública:** infra do provedor compartilhada (*multi-tenant*); menor custo, grande escala.
- **Privada:** uso exclusivo de uma organização; máximo controle (bancos, governos). Na prática, "privada" de provedor público = **VPC**.
- **Híbrida:** on-premises + nuvem pública (dados sensíveis locais, nuvem para picos e DR).

## 4. Pilares da infraestrutura
- **Computação:** **VMs** (computador completo) e **contêineres** (virtualização leve; empacotam código e dependências).
- **Armazenamento:** **objetos** (quase infinito, S3), **blocos** (disco rápido de VM, EBS), **arquivos** (compartilhado, EFS).
- **Rede:** **VPC** (fatia privada isolada), **sub-redes** (pública para web, privada para banco), **grupos de segurança** (firewall da VM).

## 5. Serverless e bancos
- **Serverless/FaaS:** você escreve a função e define um **gatilho** (upload, HTTP, cron); o provedor aloca recursos. **Vantagens:** paga só pelos **milissegundos** de execução, escala automática, menos operação. **Desvantagens:** **cold start**, limite de tempo/memória, difícil depurar, **lock-in**.
- **SQL (relacional):** tabelas, esquema fixo, **ACID**; ideal para transações; difícil escalar horizontalmente.
- **NoSQL:** esquema flexível, escala horizontal, modelo **BASE** (consistência eventual). Tipos: **documentos** (MongoDB), **chave-valor** (Redis, DynamoDB), **colunar** (Cassandra), **grafo** (Neo4j).
- **Kubernetes:** orquestra contêineres em cluster. **CI/CD:** *CI* = integrar o trabalho dos devs várias vezes ao dia; *CD* = entregar em ciclos curtos. Balanceamento de carga e **autoscaling**.

**Exemplo.** Um app de ingressos: front em **SaaS/PaaS**, banco **SQL** gerenciado (transações precisam de ACID), cache em **Redis** (chave-valor), geração de PDFs por **serverless** disparado pela compra.

## 6. Segurança, IAM e custos
- **Responsabilidade compartilhada:** o provedor cuida da segurança **DA** nuvem (hardware, data centers); você, da segurança **NA** nuvem (dados, permissões, rede, senhas).
- **IAM:** **identidade** (quem) + **permissão** (o que) + **recurso** (em quê). **Menor privilégio (PoLP).** Pilares: **autenticação** (MFA essencial), **autorização** (políticas e roles) e **auditoria**. Boas práticas: nunca `*.*`, usar roles/grupos, **nunca chaves no código**.
- **FinOps:** **gastar melhor, não só menos.** **Tags** para alocar custo; alertas de orçamento; **rightsizing**; caçar **recursos zumbis**; agendar desligamento de ambientes de teste. Ciclo: **Informar → Otimizar → Operar**.

## 7. Multi-cloud
Vários provedores na mesma arquitetura. **A favor:** evitar lock-in, melhor ferramenta para cada caso, exigência de clientes. **Contra:** **custo de egress**, governança, ferramentas dispersas. **Cloud bursting:** data center local + nuvem para picos.

## 8. Cloud II — dados na nuvem
- **4 tipos de análise:** **descritiva** (o que aconteceu?), **diagnóstica** (por quê?), **preditiva** (o que vai acontecer?), **prescritiva** (o que fazer?).
- **Ciclo de vida do dado:** Coletar → Processar → Armazenar → Analisar → Ativar → Empoderar. **Dados como produto (DaaP):** descobrível, confiável, seguro.
- **Fila de mensagens (MQ):** entrega a **um** consumidor e remove. **Streaming (Kafka):** eventos **imutáveis e reproduzíveis**, vários consumidores.
- **CDC (Change Data Capture):** captura só as mudanças (INSERT/UPDATE/DELETE); **baseado em log** é o mais usado.
- **Batch × tempo real:** batch = grande volume, agendado, mais barato; tempo real = baixa latência, mais caro (fraude).
- **Hadoop** (HDFS + MapReduce, em **disco**) × **Spark** (**em memória**, até ~100× mais rápido; RDDs, DAG).
- **Parquet** (colunar, bom para análise) × **Avro** (por linha, bom para escrita/streaming). **Iceberg:** formato de tabela sobre Parquet com **ACID, evolução de esquema, time travel** (lakehouse).

## Armadilhas e confusões comuns
| Confusão | O correto |
|---|---|
| Nuvem é sempre mais barata | pode sair **mais cara** sem governança (FinOps) |
| O provedor cuida de toda a segurança | cuida **DA** nuvem; você cuida **NA** nuvem |
| Serverless não tem servidor | tem; **você não os gerencia** |
| SaaS e PaaS são iguais | SaaS = software pronto; PaaS = plataforma para **você** desenvolver |
| NoSQL é sempre melhor/mais rápido | troca **consistência** por escala; cada tipo serve um uso |
| Fila (MQ) = streaming | fila **remove** a mensagem ao consumir; streaming **guarda e reproduz** |

## Resumo-relâmpago
- CAPEX × OPEX; elasticidade; responsabilidade compartilhada.
- IaaS (você gerencia SO), PaaS (só app/dados), SaaS (nada).
- Pública, privada, híbrida; VPC. Serverless: pago por execução, cold start.
- SQL = ACID; NoSQL = BASE. IAM: menor privilégio + MFA. FinOps: informar, otimizar, operar.
- 4 análises: descritiva, diagnóstica, preditiva, prescritiva. Spark em memória; Parquet colunar.

## Teste-se
1. Diferencie IaaS, PaaS e SaaS e dê um exemplo de cada.
<details markdown="1"><summary>Ver resposta</summary>IaaS: infraestrutura (EC2); PaaS: plataforma para desenvolver sem gerir infra (App Engine); SaaS: software pronto (Gmail).</details>

2. O que é cold start?
<details markdown="1"><summary>Ver resposta</summary>Latência extra na primeira execução de uma função serverless, quando o ambiente ainda precisa ser iniciado.</details>

3. Quem é responsável pela configuração errada de um bucket?
<details markdown="1"><summary>Ver resposta</summary>O cliente (segurança NA nuvem, pelo modelo de responsabilidade compartilhada).</details>

4. Qual a diferença entre ACID e BASE?
<details markdown="1"><summary>Ver resposta</summary>ACID (SQL) garante transações consistentes; BASE (NoSQL) prioriza disponibilidade e velocidade com consistência eventual.</details>

## Pergunta típica
IaaS/PaaS/SaaS (exemplos) · CAPEX × OPEX · responsabilidade compartilhada · menor privilégio e MFA · cold start · SQL × NoSQL (ACID × BASE) · multi-cloud (prós e contras, egress, cloud bursting) · batch × streaming · Hadoop × Spark · Parquet × Avro · 4 tipos de análise
