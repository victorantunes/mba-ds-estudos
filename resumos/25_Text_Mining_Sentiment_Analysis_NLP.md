# 25 · Text Mining, Sentiment Analysis e NLP
**Prof. Guilherme Bezerra de Lima · 3 aulas · Prioridade: ALTA (pipeline de pré-processamento e granularidades caem em avaliação)**

## 1. Definições (as 4 áreas)
- **NLP / PLN (Processamento de Linguagem Natural):** processa e entende a linguagem humana por meio de algoritmos.
- **Análise de Sentimento (AS):** **detecta emoções e opiniões** em textos, classificando como **positivas, negativas ou neutras**. "Computadores não sentem; identificam padrões na linguagem."
- **LLMs:** modelos de IA treinados em grandes volumes de texto para **gerar e compreender linguagem** (redes neurais que representam texto como números/matrizes e **preveem as próximas palavras**).
- **Text Mining:** **extrai padrões, insights e informações úteis de grandes quantidades de texto** (processo de descobrir padrões e conhecimento a partir de grandes volumes textuais). A maior parte dos dados gerados está em formato textual (redes sociais, documentos, artigos).
- **Aplicações:** análise de sentimentos, **extração de informação**, **sumarização**, **classificação**, **modelagem de tópicos**, **detecção de fraudes e spam**.

## 2. Pipeline de Text Mining
**Coleta de dados** (APIs, web, JSON/CSV/Excel) → **Pré-processamento** (limpeza e normalização) → **Modelagem e análise** (algoritmos) → **Interpretação dos resultados** → **Insights e conhecimento**. **O pré-processamento impacta diretamente a acurácia final**; "qualidade do dado > qualquer algoritmo de ponta".

## 3. Pré-processamento de texto (CAI — exemplo com "Eu amo DS!")
| Etapa | O que faz | Exemplo |
|---|---|---|
| **Lowercasing** | padroniza caixa | "Eu amo DS!" → "eu amo ds!" |
| **Remoção de pontuação** (e acentos, se for o caso) | elimina sinais | → "eu amo ds" |
| **Tokenização** | divide o texto em **unidades menores (tokens)** | ["eu","amo","ds"] |
| **Stopwords** | remove palavras muito comuns que **não agregam significado** ("a, o, e, de, que, em") | "eu estou aprendendo processamento de linguagem natural" → "aprendendo processamento linguagem natural" |
| **Stemming** | reduz a palavra à **raiz (radical) por corte de sufixos, pode não ser palavra real** | aprendendo → "aprend"; algoritmo → "algoritm"; rapidamente → "rapid" |
| **Lemmatization (lematização)** | reduz à **forma canônica/lema (palavra real do dicionário)**, usa a classe gramatical | "amasse" → "amar"; "balançando" → "balançar"; "incríveis" → "incrível" |
- **Stemming × Lemmatization:** stemming é **mais rápido e grosseiro** (radical); lematização **mais precisa** (lema real). Bibliotecas: **NLTK** (RSLP stemmer, stopwords, punkt), **spaCy** (`pt_core_news_sm`). Inglês tem mais recursos/precisão que português.
- Depois do pré-processamento, **vetorização/extração**: transformar texto em vetores numéricos — **Bag of Words/CountVectorizer, TF-IDF, Word Embeddings**.

## 4. Análise de Sentimento
- **Polaridade e espectro:** escala ex.: **+2 muito positivo, +1 positivo, 0 neutro, −1 negativo, −2 muito negativo** (ou apenas pos/neg/neutro).
- **AS como pipeline de decisões técnicas:** **granularidade → algoritmo → métrica**.
- **Granularidade (escolher ANTES da arquitetura do modelo):**
  - **Nível de documento:** classifica o texto inteiro como uma única opinião (reviews globais; pouco detalhado).
  - **Nível de frase:** classifica cada sentença; primeiro identifica se é **subjetiva ou objetiva**, depois a polaridade.
  - **Nível de aspecto — ABSA (Aspect-Based Sentiment Analysis):** o mais refinado; identifica **aspectos/características** e dá um sentimento a cada um. Ex.: "O atendimento foi excelente, **mas** a comida demorou muito" → atendimento (+), comida/tempo (−); "O quarto do hotel era confortável, mas o Wi-Fi era lento".
- **Algoritmos:**
  - **Baseados em léxico** (dicionário de palavras com polaridade): **VADER** (inglês), **LeIA** (adaptação do VADER ao português), **TextBlob**. Limite: gírias/expressões que não estão no dicionário (ex.: Twitter).
  - **Machine Learning clássico:** vetorização (**CountVectorizer/TF-IDF**) + classificador (**Naive Bayes — MultinomialNB**, regressão logística…) com **divisão treino/teste** e métricas de acerto (o modelo precisa de **dados rotulados**: "não passo nenhuma informação e quero que ele classifique do nada" não funciona).
  - **Deep Learning / Transformers / LLMs:** modelos pré-treinados via `transformers.pipeline("sentiment-analysis")` (retorna **predição e probabilidade**); modelos **open source** (podem rodar na empresa) × LLMs pagos. Com recurso financeiro e confiabilidade, um LLM pode substituir as etapas clássicas.
- **Métrica:** validação técnica (acurácia, precisão, recall, F1, matriz de confusão — compare com o rótulo real).
- **Passos no mundo real (da aula):** coleta → pré-processamento → extração (vetores) → classificação; **validar** o resultado; um modelo de sentimento **não é "para sempre"** (a linguagem muda).
- **Desafios atuais:** **sarcasmo, ironia e emojis**; dependência de dados do Twitter/X; **polaridade intermediária e ambiguidade**; **viés linguístico**; erros ortográficos e linguagem informal. "Essas lacunas é onde o cientista de dados agrega valor." Futuro: **multimodal** (texto + imagem + áudio).

## Pergunta típica
Diferença entre NLP, text mining, AS e LLM · ordem das etapas de pré-processamento · o que é stopword · stemming × lematização (exemplos) · granularidade documento/frase/aspecto e o que é ABSA · abordagens (léxico × ML × deep learning/LLM) · por que a qualidade dos dados importa mais que o algoritmo · desafios (sarcasmo, ambiguidade, viés).
