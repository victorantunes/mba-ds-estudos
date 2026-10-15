# 27 · Árvores, Redes e Ensemble Models (I, II, III)
**Profa. Valquíria Alencar · 3 aulas (25/08, 01/09 e 08/09/2026) · Prioridade: ALTA (conceitos de ML supervisionado + métricas caem; você já sabe Python, foque nos conceitos)**

## 1. Árvore de decisão
- **Método de aprendizado supervisionado, não paramétrico:** não impõe fórmula rígida; a própria árvore constrói a estrutura fazendo uma sequência de perguntas "verdadeiro/falso".
- **Estrutura:** **nó raiz** (dados completos, ponto de partida) → **nós internos** (perguntas sobre as características) → **folhas** (resultado final).
- **Vantagens:** pouca preparação dos dados (em geral **não precisa normalizar/padronizar**); aceita variáveis **numéricas e categóricas**; **"caixa branca"** (cada previsão é explicável por regras — oposto das redes neurais); robusta a dados reais fora de distribuições "ideais".
- **Classificação × regressão:** **classificação** → folha retorna a **classe mais frequente**; **regressão** → folha retorna a **média** dos valores que caíram nela.
- **Como aprende (qual o melhor split):** classificação → a divisão que **separa melhor as classes, reduzindo a impureza** dos grupos (ex.: 5 adimplentes + 5 inadimplentes, pergunta "teve atraso?" gera grupos 4×1 e 1×4); regressão → a divisão que **reduz o erro** entre o previsto e o real (critério padrão **squared error**; no sklearn `criterion`).
- **Treino/teste:** separação típica **80% / 20%**; o teste é a "prova final" com dados nunca vistos. Em classificação usar **`stratify=y`** (mantém a proporção das classes). A profundidade da árvore é a mesma para treino e teste.
- **Desvantagens:** **overfitting** (árvore cresce demais e "decora"); **sensível a pequenas mudanças** nos dados (árvore completamente diferente); sensível a **classes desbalanceadas**; **não extrapola** (previsões irreais fora da faixa de treino).
- **Overfitting × underfitting:** overfitting = muito complexo, **acurácia de treino altíssima e queda no teste** (causas: árvore profunda, muitas variáveis irrelevantes, poucos dados); underfitting = modelo simples demais, aprende pouco. Busca-se o equilíbrio (boa generalização).
- **Hiperparâmetros** (definidos **antes** do treino): `max_depth`, `min_samples_split`, `min_samples_leaf`, `criterion`. **Poda** (limitar a árvore) reduz overfitting. Ajuste: definir combinações → treinar versões → avaliar por **validação cruzada** → escolher a melhor.
- **Pré-processamento citado:** não usar **IDs/CPF/RG** como feature; tratar datas (`pd.to_datetime`); variáveis categóricas: **`get_dummies`** (exploração) × **`OneHotEncoder` em pipeline** (produção, lida com categorias novas); cuidado com **vazamento de dados (data leakage)** — variável quase igual ao alvo faz o teste ficar "bom demais".

## 2. Métricas
**Classificação (matriz de confusão: VP, VN, FP, FN — "verdadeiro/falso" diz se o modelo acertou):**
- **Acurácia** = (VP+VN)/(VP+VN+FP+FN) — enganosa em bases **desbalanceadas**.
- **Precisão** = VP/(VP+FP) — "quando diz que é positivo, quanto posso confiar?" (importa quando **falso alarme** é caro).
- **Recall / sensibilidade** = VP/(VP+FN) — capacidade de **encontrar os positivos reais** (crucial quando perder um positivo é grave: doença, fraude).
- **F1** = 2·(Precisão·Recall)/(Precisão+Recall) — **média harmônica** (penaliza desequilíbrio entre os dois).
- **Curva ROC / AUC:** capacidade de distinguir as classes; a diagonal = **classificador aleatório**.
- Exemplos: crédito (FN = concedeu crédito a quem não pagou; FP = negou a bom pagador); doença cardíaca (FN = previu baixo risco para quem tem alto risco → muito ruim).

**Regressão:** **MAE** (erro médio absoluto; mesma unidade, **robusto a outliers**) · **MSE** (erro quadrático médio; **penaliza erros grandes**) · **RMSE** (raiz do MSE; unidade original) · **R²** (proporção da variância explicada) · **MAPE** (distorce quando o valor real é ~0). Exemplo da aula: RMSE ≈ 30,6 e R² ≈ 0,65 no teste (previsão de tempo de entrega).

**Validação cruzada K-fold:** divide em K partes; cada fold é teste uma vez, o resto treino; média dos resultados → avaliação **mais robusta** (não depende da "sorte" de uma divisão). `cross_val_score(modelo, X, y, cv=...)`.

## 3. Viés × variância e a lógica do ensemble
- **Alto viés = modelo simplista** (previsões consistentes mas "fora do alvo"; subajuste). **Alta variância = modelo flexível demais** (previsões espalhadas; overfitting) — é o caso da **árvore de decisão profunda**. Reduzir um tende a aumentar o outro (**trade-off**); busca-se o equilíbrio.
- **Ensemble:** treina **vários modelos e combina as predições numa saída única** ("júri": os erros individuais tendem a se cancelar).

| Técnica | Como funciona | Efeito |
|---|---|---|
| **Voting / Averaging** | modelos diferentes votam; **hard voting** = classe mais votada; **soft voting** = média das **probabilidades**; regressão = **média** | simples |
| **Bagging** (Bootstrap Aggregating) | modelos do **mesmo tipo**, **independentes e em paralelo**, cada um em uma amostra **bootstrap** (com reposição); agrega por votação/média | **reduz variância**, mantém o viés |
| **Boosting** | modelos **sequenciais**; cada novo modelo foca nos **erros (resíduos)** do anterior; previsão final = soma ponderada | **reduz viés** (principalmente); risco de overfitting |
| **Stacking** | **meta-modelo (nível 1)** aprende a combinar as previsões dos **modelos base (nível 0)**; para evitar **vazamento** usam-se previsões **out-of-fold** | combina modelos diferentes |

- **Bootstrap:** amostra do mesmo tamanho dos dados, **com reposição** → ~**63% dos registros únicos**, ~**37% ficam de fora = OOB (out-of-bag)** → servem como **validação "grátis"**.
- **Boosting em detalhe:** weak learners (árvores rasas); freios: **nº de estimadores**, **learning rate** (tamanho do passo; alto demais oscila, baixo demais é lento), **early stopping**. **Gradient Descent:** gradiente dá a direção, learning rate o tamanho do passo. **Três gerações:** **AdaBoost** (repondera as observações), **Gradient Boosting** (ajusta o resíduo/gradiente da função de perda), **XGBoost** (boosting otimizado: regularização + engenharia de alto desempenho).

## 4. Random Forest
- **Bagging + aleatoriedade na seleção de variáveis:** (1) **bootstrap das linhas** para cada árvore e (2) **subconjunto aleatório de colunas em cada split** → **árvores descorrelacionadas** → maior redução de variância. Árvores **profundas/completas**, agregação por votação (classificação) ou média (regressão). (Bagging tradicional considera todas as variáveis em cada split → variáveis fortes dominam e as árvores ficam correlacionadas.)
- **Hiperparâmetros:** `n_estimators` (nº de árvores; padrão 100 — mais árvores = mais estável, mais custo), `max_features` (variáveis candidatas por split), `max_depth` (`None` = cresce livremente), `min_samples_split`, `min_samples_leaf`, `bootstrap`.
- Exemplo da aula: RF alcançou **recall 83% e acurácia 96%** (comparado à árvore única).

## 5. XGBoost (eXtreme Gradient Boosting)
- Gradient boosting com **árvores como base** + **regularização L1 (`reg_alpha`) e L2 (`reg_lambda`)** + paralelização/cache/sparsity. **Trata valores faltantes nativamente**; aceita categóricas nas features (**não no target** y); escala para grandes volumes (distribuído).
- **Objetivo = erro nos dados + penalidade pela complexidade.** **L1** pode zerar contribuições (seleção/simplificação); **L2** suaviza os pesos das folhas (mais estável, normalmente não zera).
- **Hiperparâmetros:** `n_estimators`, **`learning_rate`**, `max_depth`, `min_child_weight` (maior = mais conservador), `colsample_bytree` (fração de variáveis por árvore), `reg_alpha/reg_lambda`. **`objective`** define o problema (ex.: `binary:logistic` → probabilidade 0–1; também multiclasse, regressão, ranking). **`DMatrix`** = estrutura otimizada para validação cruzada nativa (`xgb.cv`); `label` = target. **Early stopping** para quando a validação para de melhorar.
- Mesma interface `fit/predict` do scikit-learn; mesmas métricas.

## 6. Comparativo
| | Decision Tree | Random Forest | XGBoost |
|---|---|---|---|
| Tipo | modelo único | ensemble **bagging** (paralelo) | ensemble **boosting** (sequencial) |
| Viés/variância | baixo viés, **alta variância** | **reduz variância** | reduz viés; regularização controla variância |
| Overfitting | alto risco | menor | controlável com regularização/tuning |
| Interpretabilidade | **alta** | média/baixa (feature importance) | média/baixa (feature importance) |
| Quando usar | baseline, explicabilidade | robustez sem muito tuning | alta performance (sensível a tuning) |
**Estratégia:** comece simples (Decision Tree → Random Forest → XGBoost).

## 7. Redes neurais (fechamento da aula III)
A última parte da aula introduz uma **rede neural (TensorFlow/Keras)** treinada para prever o status do cliente (ativo/inativo): erro cai por rodadas (ex.: 0,10 → 0,05 → … 0,033) e avalia-se em **dados nunca vistos**; **pequena diferença treino × teste = bom sinal; diferença grande = problema (overfitting)**. Aprofundamento em **28 · Deep Learning**.

## Pergunta típica
Estrutura da árvore (raiz, nós, folhas) e por que é "caixa branca" · classificação × regressão (classe mais frequente × média) · overfitting (sinais, causas, hiperparâmetros que controlam) · definições e fórmulas de acurácia/precisão/recall/F1, e qual priorizar em cada caso (FN × FP) · MAE × MSE × RMSE × R² · K-fold · viés × variância · bagging × boosting × stacking × voting (hard/soft) · bootstrap e OOB (63%/37%) · o que a "dupla aleatoriedade" do Random Forest faz · o que o XGBoost acrescenta (regularização L1/L2, faltantes, paralelização) · learning rate e early stopping.
