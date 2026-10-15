# 17 · Supervised ML — Análise de Regressão Simples e Múltipla (OLS)
**Prof. Dr. Luiz Paulo Fávero · 4 aulas (03/02, 10/02, 24/02 e 03/03/2026) · Prioridade: MÁXIMA — é o tema com **mais dicas explícitas de prova** do curso**

> O professor falou "pergunta de prova" várias vezes: (1) **nomes do R²**, (2) **interpretar uma saída/tabela**, (3) **calcular R² de uma regressão simples a partir da correlação**, (4) **prever Y com dummies (somar betas)**, (5) **diferença entre F, t e R²**, (6) **por que não usar pesos arbitrários em categorias**. Treine essas.

## 1. Contexto
- Dentro de *Data Science → Machine Learning → **Supervised ML** → **modelos GLM** (Generalized Linear Models)*. GLMM = modelos multinível/painel (aulas 9–10). **A escala de medida da variável dependente (Y) determina o modelo**: Y quantitativa contínua → regressão (OLS); Y binária/politômica → logística; Y de contagem → Poisson/binomial negativo; dados aninhados → multinível.
- **Modelos supervisionados:** estabelecem **Y = f(X1, X2, …, Xk)**; são **confirmatórios/inferenciais**, estimados para **previsão** (fitted values) com **inferência para fora da amostra** (dentro do range de X usado no treino — ex.: distância entre 5 e 32). "Todos os modelos estão errados, mas alguns são úteis" (Box): o objetivo é o modelo com **maior aderência entre valores reais e previstos** (mais próximo da reta de 45°).
- **Correlação não implica causalidade** (exemplo: chocolate × prêmios Nobel).
- Para diagnosticar um modelo precisa-se de **indicadores de eficiência preditiva**, não só dos betas e do R².

## 2. Regressão linear simples
- **Yi = α + β·Xi + ui** (α = intercepto; β = inclinação; u = **termo de erro/resíduo = Y real − Y previsto (Ŷ, "fitted value")**).
- **Estimação por OLS/MQO (mínimos quadrados ordinários):** os parâmetros garantem **Σui = 0** e **Σui² = mínimo possível**. Em Python: `smf.ols('y ~ x', data=df).fit()` (statsmodels, `OLS from formula`). Resíduos: `modelo.resid`; fitted: `modelo.fittedvalues`.
- **R² (coeficiente de ajuste)** — **também chamado coeficiente de explicação ou coeficiente de determinação** (PERGUNTA DE PROVA): **percentual da variância de Y que é explicado pelo comportamento conjunto da(s) variável(is) explicativa(s)**; varia de 0 a 1; **R² = Σ(Ŷ − Ȳ)² / [Σ(Ŷ − Ȳ)² + Σu²]** (soma dos quadrados do modelo / soma total). **Na regressão simples, R² = (correlação de Pearson entre X e Y)²** (ex.: correlação 0,4428 → R² = 0,196; "se eu rodar retorno contra disclosure, quanto dá o R²? o valor da correlação ao quadrado"). Com erros maiores a nuvem de pontos é mais dispersa e o R² cai.
- **Só α, β e R² não dizem nada sobre eficiência preditiva.**

## 3. Significância estatística — F, t e R² não são a mesma coisa
- **Teste F (significância conjunta do modelo):** **H0: β1 = β2 = … = βk = 0**; **H1: pelo menos um β ≠ 0**. **p-valor do F < 5%** → rejeita H0 → **existe modelo**: pelo menos uma variável X explica Y. **A definição de haver ou não modelo preditivo não é o R², é o F.** Pode haver modelo (F significativo) com R² muito baixo (baixa capacidade preditiva, variáveis omitidas "fazendo as vezes" no termo de erro) — mas isso não autoriza dizer que não há modelo. Gl do F: k (modelo) e n − k − 1 (resíduos). Tabela de **ANOVA** existe na estimação por OLS.
- **Teste t (significância individual de cada parâmetro):** H0: βj = 0; **t = estimativa/erro padrão**; |t| < 1,96 ⇒ p > 0,05 ⇒ não significante (95% de confiança). Em regressão simples, t e F levam à mesma conclusão. Origem da distribuição t: Gosset ("Student", Guinness) para pequenas amostras.
- **Intervalo de confiança** do parâmetro: se contém o zero, o parâmetro não é significante.
- **O alfa (intercepto) NÃO deve ser excluído** mesmo que não significante (frequentemente é problema de tamanho de amostra; triplicando a amostra com os mesmos dados ele passa a ser significante). **Forçar α = 0 gera viés nos betas** para compensar (Σu = 0). O t do alfa "não serve para nada".
- Tabelas de papers: asteriscos indicam significância a 90/95/99%; erros padrão entre parênteses.

## 4. Regressão múltipla
- **Yi = α + β1X1i + β2X2i + … + βkXki + ui** (única diferença: mais variáveis explicativas). Forma matricial: **Y = X·b + u; b = (X′X)⁻¹X′Y**.
- **R² ajustado** = 1 − (1 − R²)·(n − 1)/(n − k − 1) → **para comparar modelos com quantidades diferentes de parâmetros e/ou amostras de tamanhos diferentes**.
- Interpretação do beta (múltipla): efeito de X sobre Y mantendo as demais constantes (ceteris paribus).

## 5. Variáveis explicativas qualitativas → dummies (CAI SEMPRE)
- **Erro clássico: "ponderação arbitrária"** (codificar categorias como 1, 2, 3…) → pressupõe que a mudança em Y entre categorias é **linear**, o que quase nunca é verdade.
- Solução: **dummização / one-hot encoding**: variável binária (0/1) por categoria; **para n categorias usa-se n − 1 dummies** (a categoria omitida é a **referência/baseline**; evita **multicolinearidade perfeita**). O beta de cada dummy = diferença média de Y em relação à categoria de referência. Dummizar cria "modelos não lineares" que capturam idiossincrasias contextuais.
- **Previsão com dummies (pergunta de prova):** soma-se α + betas das dummies que valem 1 (ex.: Y médio da América do Sul = α da categoria de referência, se ela é a omitida; Europa = α + β_Europa…). Leia o output e só some o que a observação ativa.

## 6. Pressupostos e diagnósticos
**a) Normalidade dos termos de erro (principal pressuposto do OLS para inferência/IC):**
- Se os erros **não aderem à normalidade** → **forma funcional inadequada** (a especificação linear não se ajusta aos dados) e os intervalos de confiança não são fidedignos.
- **Teste de normalidade: Shapiro-Francia (sf)**; **H0: os resíduos seguem distribuição normal**; queremos **p > 0,05 (não rejeitar H0)**. (Em Python: `shapiro_francia` / `sfrancia` + gráficos histograma/QQ.) *Atenção: aqui o desejo é NÃO rejeitar H0 — oposto do teste F/t.*
- **Normalização × padronização:** **padronização (Z-score)** muda média/desvio mas **não** a forma da distribuição; **normalização (Box-Cox)** transforma Y para aproximar da normal.

**b) Transformação de Box-Cox (modelos não lineares):** Y* = (Y^λ − 1)/λ; escolhe-se o **λ (de −∞ a +∞) que maximiza a aderência da nova variável à normalidade** (e o R²). **Casos de λ:** 1 = linear; 2 = quadrática; 3 = cúbica; 0,5 = raiz; −1 = inversa; **0 = ln(Y) (semilogarítmica)**. Estimar o modelo com Y* e depois testar a normalidade dos novos resíduos. **Parâmetros do modelo com Y transformado NÃO são diretamente comparáveis** com os do linear (a métrica de Y mudou). Variáveis podem aparecer/sumir ao transformar.

**c) Procedimento Stepwise:** retira, passo a passo, **variáveis cujos betas não são estatisticamente significantes** (limite p, ex. 0,05 → 95% de confiança) **e também resolve problemas de multicolinearidade** (uma variável pode cair por estar correlacionada com outra, mesmo sozinha sendo boa preditora). Em Python: `stepwise(modelo, pvalue_limit=0.05)`. O stepwise **não** conserta heterocedasticidade nem forma funcional.

**d) Multicolinearidade:** alta correlação entre **duas ou mais variáveis explicativas**. **Consequências:** distorção de **sinais e significâncias** (risco de inversão de sinal), **estatísticas t baixas com F significante e R² alto**, **erros na predição**. **Causas:** variáveis com mesma tendência, **amostras pequenas**, **valores defasados** como novas explicativas. Matematicamente, det(X′X) → 0 e **(X′X)⁻¹ com valores muito altos na diagonal → ↓ estatística t sem alterar o F**. **Detecção:** sinais inesperados, t não significante e F significante, **VIF e Tolerance**: regressão auxiliar de cada X nas demais; **Tolerance = 1 − R²p; VIF = 1 / Tolerance**. VIF alto (> 10 como regra) / Tolerance baixa → problema. Solução: stepwise/remover variável, reduzir com **PCA (fatores ortogonais)**.

**e) Heterocedasticidade:** **variância não constante dos termos de erro** (gráfico em "cone": resíduos crescem com Ŷ; correlação resíduos × Ŷ). **Causas:** **omissão de variável X relevante** e/ou forma funcional errada. **Teste de Breusch-Pagan:** H0 = homocedasticidade (variância constante); **p < 0,05 → heterocedasticidade**. Mitigação: **incluir variáveis preditoras significantes** (conhecer o fenômeno) ou **modelos multinível**.

## 7. Roteiro de estimação OLS (script da aula)
1) correlações/gráficos exploratórios → 2) estimar OLS com variáveis (dummies) → 3) **Stepwise** (95%) → 4) **Shapiro-Francia dos resíduos** → 5) se não normal, **Box-Cox** em Y e repetir stepwise e teste → 6) checar **VIF** e **Breusch-Pagan** → 7) **previsão** (`.predict()`) apenas dentro do range de X do treino.
Exemplos: tempo × distância/semáforos (modelo simples/múltiplo); **CPI (índice de corrupção) por região (dummies)** — ponderação arbitrária 1–5 × dummies; **retorno de ações × disclosure × endividamento** (endividamento cai no stepwise; disclosure só no modelo com Box-Cox); comprimento de bebês × idade (não linear); notas SAEB (heterocedasticidade); econometria × RH1 × RH2 (multicolinearidade).

## Pergunta típica
Nomes do R² e o que mede · diferença entre F, t e R² (há modelo ≠ R² alto) · hipóteses do F e do t · por que usar R² ajustado · n−1 dummies e por que não usar pesos 1,2,3 · calcular valor previsto com dummies · R² na simples = r² · o que testa o Shapiro-Francia e qual resultado se espera · o que é Box-Cox (λ=0 → ln) · stepwise · multicolinearidade (VIF/Tolerance, consequências) · heterocedasticidade (causas, Breusch-Pagan) · por que não excluir o intercepto.
