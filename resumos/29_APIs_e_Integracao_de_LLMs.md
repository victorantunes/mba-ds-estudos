# 29 · Aula Extra: Desenvolvimento de APIs e Integração Prática de LLMs (I–II)
**Prof. Helder Prado Santos · 2 aulas extras · Prioridade: BAIXA para a avaliação (aula extra; você é dev e já sabe quase tudo de API — leia para vocabulário de LLM/RAG)**
*(Confirme com a coordenação se esse conteúdo entra na avaliação final.)*

## 1. Do protótipo ao produto
- **3 fases:** (1) **Prototipação** — notebooks, validação de prompts, sem preocupação com escala; (2) **Abismo de integração** — concorrência, padronização de formatos, latência de rede, gestão de dependências; (3) **Operação** — disponibilização via **API resiliente**, monitoramento de métricas, auditoria e governança.
- **Serviço de IA:** **atualização independente** (troca de modelo/prompt sem alterar quem consome), **poliglotismo** (Python para IA, outros sistemas em TypeScript/Java), **escalabilidade direcionada** (dimensiona só o serviço de inferência).
- **Três pilares:** **API (a ponte)** + **LLM (o cérebro)** + **RAG (a memória)**.

## 2. APIs
- **API = contrato da interface:** isola a complexidade interna, define entrada exigida e formato de saída ("o cardápio"); transforma scripts pontuais em utilitários **reutilizáveis** pela organização.
- **Cliente-servidor:** cliente (navegador, app, dashboard de BI, script) faz **request**; servidor (recursos, regras de negócio, modelos de IA) devolve **response**. **HTTP é stateless** — cada requisição é isolada e traz tudo de que precisa. **Endpoints/rotas** identificam recursos (`/predicao`, `/resumo`).
- **Métodos:** **GET** (consulta/leitura, não altera estado) · **POST** (envio de dados complexos para inferência, criação) · **PUT/PATCH/DELETE** (atualização total/parcial/remoção — REST).
- **Anatomia da request:** **URL + endpoint**, **headers** (Content-Type, tokens de segurança), **query parameters** (filtros na URL, `?formato=resumido`), **body/payload** (dados volumosos).
- **Status codes:** **2xx** sucesso (200 OK) · **4xx erro do cliente** (400 Bad Request) · **5xx erro do servidor** (500 Internal Error — "o pior": falha de código/modelo/infra).
- **JSON:** chave-valor hierárquico, legível por humanos e máquinas; converte fácil para DataFrame/dict/JSONB.
- **FastAPI:** **assíncrono** (async/await, I/O não bloqueante — evita gargalos em chamadas a LLMs), servidor **ASGI (Uvicorn)**, **documentação automática** (OpenAPI/Swagger). **Pydantic:** validação **declarativa** via schemas tipados (`class RequisicaoAnalise(BaseModel): texto: str; max_tokens: int = 500; temperatura: float = 0.1`) — rejeita payloads fora do padrão; modelo nulo/inteiro onde se espera string dá erro.

## 3. LLMs sob a ótica da engenharia
- **Arquitetura Transformer** (self-attention); é uma **função matemática estocástica** que transforma uma sequência de entrada em **distribuições de probabilidade do próximo token** (vê todos os tokens do vocabulário). Mudança de paradigma: de regras determinísticas para **inteligência probabilística**.
- **Provedores:** **proprietários** (Google, OpenAI, Anthropic — conveniência, estado da arte, sem gestão de infra) × **open-weight** (Llama, Mistral — **soberania sobre os dados**, customização avançada, controle de custos em escala) × **aceleração em nuvem** (Groq, Together AI — inferência rápida com LPUs/GPUs).
- **Token:** fragmento de palavra (~4 caracteres em inglês) — base de tarifação e limites. **Janela de contexto:** máximo de tokens (**entrada + saída**) vistos de uma vez (32K → 128K → 1M+).
- **Parâmetros de inferência:** **temperatura baixa (0–0,2)** = determinismo, consistência (extração de dados, JSON, RAG); **alta (0,7–1,0)** = variabilidade/criatividade (ideação, brainstorming); **Top-P (nucleus sampling)** = corte cumulativo de probabilidade (só tokens mais prováveis).
- **Alucinação:** informação incorreta/não sustentada pelos dados, apresentada de forma plausível — risco de conformidade, auditoria e decisões erradas.
- **Segurança e governança:** **API keys nunca no código-fonte** (variáveis de ambiente `.env`); **isolar ambientes** (dev/homologação/produção); **limites financeiros** (teto de gasto); **Rate limits: RPM (requisições/min) e TPM (tokens/min)**; **latência de segundos** → arquiteturas assíncronas e feedback ao usuário; **previsibilidade de custo** por volume de tokens de entrada/saída.
- **Structured Outputs:** **constrained decoding** restringe a geração à gramática do **JSON Schema** → garante 100% dos campos, tipos e sintaxe válidos; converte texto não estruturado (avaliações) em **tabelas** sem erro de parsing.
- **Resiliência:** **exponential backoff** (novas tentativas progressivas), **timeouts explícitos**, **fallback** (modelo secundário/resposta padrão).

## 4. Embeddings e busca semântica
- **Por que LLMs falham com dados privados:** **knowledge cutoff** (conhecimento congelado), **ponto cego corporativo** (nunca viram os seus documentos), **retreinar do zero é inviável**.
- **Embedding:** lista de centenas/milhares de números reais gerada por modelo neural; cada dimensão captura traços latentes (assunto, tom, intenção); textos similares ficam **próximos** no hiperespaço ("dor de cabeça intensa" ≈ "paciente com cefaleia").
- **Busca léxica** (BM25, SQL `LIKE` — correspondência exata; falha com sinônimos/erros de digitação) × **busca semântica/vetorial** (significado contextual).
- **Métricas de similaridade:** **cosseno** (ângulo; ignora o comprimento do texto; **a mais usada**), **distância euclidiana (L2)**, **produto escalar** (direção + magnitude; vetores normalizados).
- **Vector DBs:** respondem "quais os **K vetores mais parecidos**?" em milissegundos; guardam vetor + texto original + metadados. **k-NN exato** (comparar com 100% dos vetores) é inviável em bases grandes → **ANN (Approximate Nearest Neighbors)**: sacrifica um pouco de precisão por ganho de até ~100× em velocidade; índice **HNSW** (grafos navegáveis). Tecnologias: **ChromaDB, DuckDB** (locais/protótipo), **Pinecone, Qdrant, Milvus** (nuvem distribuída, bilhões), **pgvector** (extensão do PostgreSQL).

## 5. RAG (Retrieval-Augmented Generation)
- **Ideia:** "especialista com uma biblioteca" — a LLM recebe, **no momento da pergunta**, os trechos relevantes dos documentos corporativos antes de responder. **Duas etapas:** **Retrieval** (busca os trechos no banco vetorial) + **Generation** (LLM redige a resposta **ancorada** na fonte). Referência: Lewis et al., 2020.
- **Fluxo em duas fases:**
  - **Offline (ingestão e indexação):** extrair texto (PDFs, web, planilhas) → **limpeza** (cabeçalhos, rodapés, ruído) → **enriquecimento** (metadados: data, setor, autor, para filtros) → **chunking** → **embeddings** → salvar no Vector DB. (Ordem pedida em aula: processar o PDF → chunking → coletar embeddings → **por último** salvar.)
  - **Online (inferência + augmentation):** pergunta → **embedding da pergunta** → busca no Vector DB → **Top-K trechos** → monta o **prompt aumentado** → LLM gera a resposta.
- **Chunking:** chunks **grandes demais diluem a busca**, **pequenos demais perdem contexto**; **overlap** (sobreposição) evita quebrar frases/conceitos; **divisão semântica** (parágrafos, títulos, seções Markdown).
- **Grounding (ancoragem):** prompt com [INSTRUÇÃO] "responda **apenas** com o contexto; se não estiver, diga que não encontrou" + [CONTEXTO RECUPERADO] + [PERGUNTA] → **reduz alucinação**.
- **RAG × Fine-Tuning:** **RAG** = **conhecimento factual**, dados **dinâmicos**, necessidade de **auditoria da fonte**, menor custo; **Fine-Tuning** = **estilo e comportamento** (tom de voz, jargões, formatos complexos de saída), não para atualizar fatos.
- **API como hub de analytics:** pipelines ETL/ELT enriquecendo/classificando registros, dashboards/BI, sistemas corporativos (CRM, ERP, RH) consumindo via HTTP.
- **Arquitetura do laboratório:** **FastAPI** (rotas, validação, docs) + **Pydantic** (contrato JSON) + **Gemini API** (embeddings e geração) + **ChromaDB** (banco vetorial local).

## Pergunta típica
O que é uma API/contrato e o que significa stateless · métodos HTTP e famílias de status (2xx/4xx/5xx) · papel de FastAPI/Pydantic · tokens, janela de contexto, temperatura e Top-P · o que é alucinação e como RAG/grounding reduzem · embedding, busca semântica × léxica, similaridade de cosseno · ANN/HNSW × k-NN exato · etapas do RAG (ingestão: chunking + embeddings + vector DB; consulta: Top-K + prompt) · RAG × fine-tuning · boas práticas (API keys em .env, rate limits RPM/TPM, backoff, structured outputs).
