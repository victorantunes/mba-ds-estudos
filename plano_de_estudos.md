# Plano de estudos
**MBA Data Science e Analytics (USP/Esalq) · 30 disciplinas · 33 dias**

## Premissas (ajuste se não valerem para você)
- **2 h por dia útil, 4 h por dia de fim de semana** (≈ 84 h no total). Se tiver mais tempo, aumente as fases de revisão; se tiver menos, use "Se faltar tempo".
- **Você é desenvolvedor e programa em Python:** por isso Python, SQL, APIs, scraping e cloud básico ficam leves; o peso vai para **estatística, modelos (regressão/GLM, multinível), não supervisionado, séries temporais e conceitos** — o que costuma ser cobrado e onde os professores deram destaques explícitos.
- Assumi que você **não sabe** os assuntos: cada bloco começa pelo resumo, que explica do zero.

## Como estudar cada bloco (método repetível, ~2 h)
1. **Leia o resumo** (`resumos\NN_*.md`) com lápis na mão — 40 min. Se algo não fizer sentido, abra os slides da aula (índice em `MATERIAIS.md`).
2. **Feche o resumo e responda a seção "Pergunta típica"** em voz alta ou por escrito — 30 min. O que você não souber responder volta para o resumo.
3. **Pratique** — 30–40 min: exercícios das listas/planilhas (`MATERIAIS.md`), refaça à mão um cálculo (AHP, centralidade, perda esperada, ACF/PACF, regressão em Excel/Python).
4. **Faça 5–8 flashcards** (fórmula, definição ou "qual técnica para qual caso") — 10 min. Revisite os cartões do dia anterior antes de começar.

## Prioridades (onde está o peso)
| Prioridade | Disciplinas |
|---|---|
| 🔴 **Máxima/Alta** (dica explícita de avaliação ou cálculo) | **17 Regressão** · 18 Logística · 19 Contagem · 20 Multinível · 01 Estatística · 22 Séries Temporais · 14 Clustering · 15 PCA · 16 ANACOR/ACM · 13 AHP · 10 Riscos · 08 SNA · 06 Comp. Evolucionária · 27 Árvores/Ensemble · 28 Deep Learning · 25 Text Mining · 12 LGPD · 05 Ágeis |
| 🟡 **Média** | 26 Pesquisa Operacional · 09 Conjuntura · 23 Data Wrangling · 21 Big Data/MLOps · 03 BI · 04 Eng. de Dados · 07 Cloud · 11 Liderança · 30 Gestão da Mudança |
| 🟢 **Baixa** (você já domina ou é aula extra) | 02 Python (só o "mapa" de ML) · 24 Scraping (só legal/ético) · 29 APIs e LLMs (aula extra) |

## Calendário dia a dia
**Fase 1 — Estatística e modelos supervisionados **
| Dia | Data | Horas | Estudar | Prática |
|---|---|---|---|---|
| 1 | Qui | 2 | **01 Estatística, parte 1:** tipos de variável, tabela de frequências, medidas descritivas, correlação | Exercícios 1–2 da *Lista de Exercícios Complementares* |
| 2 | Sex | 2 | **01 parte 2:** distribuições (binomial, Poisson, normal), IC, testes de hipótese (t, F, qui²) | Exercícios 3–12 (planilha de suporte) |
| 3 | Sáb | 4 | **17 Regressão simples e múltipla** (OLS, R², testes F e t, dummies, interpretação) | Script/planilhas complementares da aula; refaça um modelo no Python |
| 4 | Dom | 4 | **17 (pressupostos e diagnóstico: normalidade, heterocedasticidade, multicolinearidade, stepwise, Box-Cox)** + **18 Logística** (odds, logito, cutoff, ROC) | Refazer à mão: interpretar coeficiente, odds ratio, sensibilidade/especificidade |
| 5 | Seg | 2 | **19 Modelos de contagem** (Poisson, Binomial Negativa, superdispersão, ZIP/ZINB, Vuong) | Perguntas típicas ("o que caracteriza dado de contagem?") |
| 6 | Ter | 2 | **20 Multinível** (ICC, intercepto/inclinação aleatórios, efeito escola × aluno) | Perguntas típicas ("vai cair na avaliação") |
| 7 | Qua | 2 | **22 Séries temporais, parte 1:** componentes, aditivo × multiplicativo, métodos simples, SES/Holt/HW | Planilhas de decomposição e suavização |
| 8 | Qui | 2 | **22 parte 2:** erros (ME, MAE, RMSE, MAPE, Theil), estacionariedade (ADF × KPSS), ARIMA/ACF/PACF, AIC/BIC | Planilha ARIMA (aula 3) + extra de exercícios |
| 9 | Sex | 2 | **02 mapa de ML** (só o mapa) + **autoteste-relâmpago do bloco** (1 pergunta típica de cada disciplina 01, 17–20, 22) | Anote o que errou |

**Fase 2 — Não supervisionado, decisão e ML moderno **
| Dia | Data | Horas | Estudar | Prática |
|---|---|---|---|---|
| 10 | Sáb | 4 | **14 Clustering** (distâncias, hierárquico × k-means, dendrograma, ANOVA) + **15 Análise fatorial e PCA** (KMO, Bartlett, autovalores, cargas fatoriais) | Planilhas "Distâncias e Clusters" e "Fatorial PCA" |
| 11 | Dom | 4 | **16 ANACOR/ACM** (qui², mapa perceptual, inércia) + **13 AHP** (matriz de julgamentos, consistência, AHP-Gaussiano) | **Refazer um AHP completo à mão** |
| 12 | Seg | 2 | **27 Árvores, Random Forest, XGBoost** (métricas, viés × variância, bagging × boosting) | Matriz de confusão: calcular precisão/recall/F1 à mão |
| 13 | Ter | 2 | **28 Deep Learning, parte 1:** perceptron, MLP, ativações, gradient descent, loss, overfitting | Fórmulas: BCE, softmax, W ← W − η∇J |
| 14 | Qua | 2 | **28 parte 2:** CNN (convolução, padding, stride, pooling), embeddings, atenção/Transformer, LSTM × Transformer | Calcular tamanho de saída da convolução |
| 15 | Qui | 2 | **25 Text Mining/NLP** (pipeline, stemming × lematização, granularidade, ABSA) + **24 Scraping** (aspectos legais) | — |
| 16 | Sex | 2 | **23 Data Wrangling** (CRISP-DM, joins, melt/pivot) + **21 Big Data e MLOps** (MLflow, Spark, 5 Vs) | — |

**Fase 3 — Negócio, cálculo e gestão **
| Dia | Data | Horas | Estudar | Prática |
|---|---|---|---|---|
| 17 | Sáb | 4 | **26 Pesquisa Operacional** (modelar variáveis/objetivo/restrições, Branch-and-Bound, binárias) + **06 Computação Evolucionária** (seleção, crossover, mutação, elitismo) | Monte o modelo de "Nova ala hospitalar" sem olhar |
| 18 | Dom | 4 | **10 Analytics e Riscos** (Markowitz, Basileia, perda esperada, VaR) + **09 Conjuntura** (PIB, inflação, juros, câmbio, BP) | Planilhas de risco (resolvidas) |
| 19 | Seg | 2 | **08 Social Network Analysis** (centralidades à mão, densidade, comunidades) | Calcule grau, proximidade e intermediação em um grafo pequeno |
| 20 | Ter | 2 | **12 LGPD** (princípios, bases legais, direitos, ANPD, sanções) | Perguntas típicas |
| 21 | Qua | 2 | **05 Metodologias Ágeis** (Scrum, Kanban, DICE, Cynefin, PMRL) + **11 Liderança em Data Science** | Estudo de caso PMRL |
| 22 | Qui | 2 | **03 BI e Data Visualization** + **04 Engenharia de Dados** (ETL, SQL, MER, view × procedure) | — |
| 23 | Sex | 2 | **07 Cloud Computing** + **30 Gestão da Mudança** (Bridges, Kotter, 10 chaves) + **29 APIs e LLMs** (RAG) | — |

**Fase 4 — Revisão ativa e autotestes **
| Dia | Data | Horas | O que fazer |
|---|---|---|---|
| 24 | Sáb | 4 | **Revisão 1 — Estatística e modelos supervisionados** (01, 17–20): refaça os exercícios que errou e releia as "destaques do professor" de cada resumo |
| 25 | Dom | 4 | **Revisão 2 — ML** (14–16, 22, 27, 28, 25): responda todas as "Pergunta típica" sem consultar; cartões de "qual técnica para qual caso" |
| 26 | Seg | 2 | **Revisão 3 — Cálculos** (AHP, risco, SNA, PO, conjuntura, métricas): refaça um cálculo de cada |
| 27 | Ter | 2 | **Revisão 4 — Conceitual** (LGPD, ágil, liderança, mudança, cloud, BI, eng. dados, big data): releia resumos de 1 página |
| 28 | Qua | 2 | **Autoteste 1:** 40 perguntas "Pergunta típica" sorteadas de todas as disciplinas (sem consulta, 2 h) |
| 29 | Qui | 2 | Corrigir o Autoteste 1 e reestudar as 3 áreas mais fracas |
| 30 | Sex | 2 | **Autoteste 2** (novas perguntas) + correção |

**Fase 5 — Reta final **
| Dia | Data | Horas | O que fazer |
|---|---|---|---|
| 31 | Sáb | 4 | Leitura rápida de todos os 30 resumos priorizando 🔴; monte uma **folha de fórmulas/definições** (1–2 páginas) |
| 32 | Dom | 3 | Revisão leve só do que ainda erra; durma cedo |
| 33 | Seg | 1 | Leia só a folha de fórmulas e as "Pergunta típica" 🔴. **Descanse.** |

## Se faltar tempo (ordem de corte)
1. Corte primeiro: **29 APIs/LLMs, 24 Scraping, 02 Python, 07 Cloud, 03 BI, 04 Eng. de Dados** (leia só a "Pergunta típica" de cada: ~15 min cada).
2. Reduza 11 Liderança, 30 Gestão da Mudança, 09 Conjuntura e 26 Pesquisa Operacional a uma leitura + perguntas típicas.
3. **Nunca corte:** 17 Regressão, 18–20 (GLM/multinível), 01 Estatística, 22 Séries, 14–16 (não supervisionado), 13 AHP, 10 Riscos, 12 LGPD.

## O que não foi analisado / limites
- **Vídeos** (.mp4): não incluídos, como você pediu — as **transcrições** (legendas) foram usadas, mas **condensadas** (extraí as passagens com definições, destaques do professor e exemplos; não li cada hora de fala).
- **Lousas** (imagens .jpg/.png em zips de Regressão, Logística, Contagem, Multinível, Clustering, Fatorial) e **podcast** de Algoritmos Genéticos (.mp3): não analisados.
- **Planilhas de solução (.xlsx), scripts e `.pbix`:** listados e usados como fonte de exercício; não reescrevi todos os cálculos.
- **Caderno do aluno:** é um **caderno em branco** de anotações (páginas "ANOTAÇÕES" + instruções) — não tem conteúdo de estudo.
- A aula extra 29 (APIs e LLMs) é complementar ao currículo principal.
- Esses resumos são um **guia de estudo**, não substituem os slides: em caso de dúvida, o slide do professor manda.
