# 16 · Unsupervised ML — Análise de Correspondência (ANACOR e ACM) + Exercícios Aplicados
**Prof. Wilson Tarantin Jr. · 3 aulas · Prioridade: ALTA (fecha o bloco não supervisionado; "qual técnica para qual tipo de variável" cai sempre)**

## 1. Objetivo
- Para **variáveis categóricas (qualitativas)**. Verifica se há **associação estatisticamente significativa** entre variáveis **e entre suas categorias**, e cria o **mapa perceptual** (proximidade das categorias = associação). **Evita a "ponderação arbitrária"** (ex.: escala Likert: cada ponto da escala vira uma categoria). Variável métrica pode entrar se for **categorizada antes** (faixas de idade).
- Técnica **não supervisionada/exploratória** (interdependência, sem Y = f(X)), **não serve para inferência**; se entrarem novas observações, refaz-se a análise.
- **ANACOR (simples)** = 2 variáveis categóricas. **ACM / MCA (múltipla)** = 3 ou mais variáveis.
- Exemplos: faixa de renda × acesso ao crédito; tipo de escola × aprovação no vestibular; severidade dos sintomas × comorbidades; perfil do investidor × tipo de aplicação (ações, CDB, poupança).

## 2. ANACOR — duas etapas
**Etapa 1 — significância da associação (teste qui-quadrado)**
1. **Tabela de contingência** (frequências absolutas observadas; classificação cruzada).
2. **Frequência esperada** de cada célula = (total da linha × total da coluna)/N.
3. **Resíduo = observada − esperada**; **χ² da célula = resíduo²/esperada**; **χ² total = soma** (estatística de teste).
4. **H0: variáveis se associam de forma aleatória (independentes). H1: há dependência.** χ² > valor crítico (**gl = (I−1)·(J−1)**) ⇔ **p < α → rejeita H0 → há associação**. Em Python: `scipy.stats.chi2_contingency`.
- **Teste χ² é global** (entre as variáveis); só se houver associação siga para a etapa 2.

**Etapa 2 — aprofundar nas categorias e mapa perceptual**
- **Resíduo padronizado** = resíduo/√esperada; **resíduo padronizado ajustado** (divide por mais um termo de linha e coluna). **Se o resíduo padronizado ajustado > 1,96 (nível 5%)** → **associação significativa entre aquelas duas categorias** (excesso de ocorrências no cruzamento); abaixo de 1,96, não.
- **Mapa perceptual:** obter **autovalores (λ)** de W = A′A (A = resíduo padronizado/√N…). **Nº de autovalores (dimensões) m = mín(I−1, J−1).** **Autovalores = inércias principais parciais**; **inércia principal total = λ1 + λ2 + … = χ²/N**; **% da inércia por dimensão = λ/inércia total** (quanto da associação cada eixo explica; ex.: dimensão 1 = 73,4%, dimensão 2 = 26,6%). **Quanto maior a inércia total e o χ², mais forte a associação.**
- **Massas** (D_linha e D_coluna): influência (representatividade) de cada categoria dentro da sua variável (totais da tabela). **Autovetores** e **valores singulares σ = √λ**; **coordenadas** das categorias: abscissa X = σ1 · (autovetor ponderado pela massa), ordenada Y = σ2 · …, para as m dimensões.
- **Interpretação:** **categorias próximas no mapa = associadas** (mesmo cluster visual). Se 2 dimensões somam 100% da inércia (tabela pequena), o mapa 2D representa tudo.

## 3. ACM (múltipla)
- **Primeiro passo:** fazer **teste χ² para cada par de variáveis**; **só participam da ACM variáveis que se associem significativamente com pelo menos uma outra** (as demais são retiradas; não faz sentido plotar variável que não se associa com ninguém). Essa etapa é intermediária (nem sempre é reportada).
- **O input é o banco de dados** (não uma única tabela de contingência).
- **1º método — matriz binária (indicadora) Z** (0/1 = ausência/presença de cada categoria por observação) → coordenadas-padrão. **Nº de dimensões = J − Q** (J = total de categorias; Q = nº de variáveis); inércia principal total = (J − Q)/Q.
- **2º método — matriz de Burt: B = Z′·Z** (cruza todos os pares de variáveis e categorias numa única matriz); trata-se como tabela de contingência e aplica-se ANACOR → **coordenadas principais**.
- **Python:** pacote **`prince`** → `prince.MCA(n_components=...)`; no mapa colorir pontos por variável (`hue`); nomes de colunas sem *underline* (a função usa `_` para separar variável/categoria). Plotar dimensões com **autovalor acima do autovalor médio**. Em um exemplo, 3 dimensões retêm 55,4% da inércia.

## 4. Visão integrada das técnicas não supervisionadas (aula de exercícios)
| Técnica | Agrupa | Tipo de variável | Base | Saída |
|---|---|---|---|---|
| **Cluster** | **observações** (homogêneos dentro, heterogêneos entre) | **métricas** | **distâncias (dissimilaridades)** entre observações → **padronizar (Z-score)** | clusters (dendrograma/K-means) |
| **PCA (fatorial)** | **variáveis** em fatores | **métricas** | **correlações de Pearson** (não precisa padronizar) | fatores ortogonais, índices/rankings |
| **Correspondência** | associação entre **categorias** | **categóricas** | **qui-quadrado**/tabela de contingência | **mapa perceptual** |
- **Podem ser combinadas** respeitando o tipo de variável: output de uma vira input da outra (ex.: **cluster → ANACOR** com variáveis categóricas; **cluster usando os fatores da PCA**; **coordenadas das observações do mapa perceptual → cluster ou PCA**). Em bancos com variáveis **quantitativas e qualitativas**, usa-se **mais de uma técnica** (na fatorial as categóricas ficaram de fora e se perde informação).
- Cuidados: remover observações com valores faltantes (`dropna`) se a perda for pequena; **não tirar média de variável categórica**; testar variáveis do cluster com **ANOVA de um fator** (teste F) para ver as que realmente formaram os grupos; ao selecionar fatores sempre há **perda de informação**.
- Cluster com K-means: sem dendrograma; escolher K por **cotovelo (WCSS)** e **silhueta**.

## Pergunta típica
Qual técnica usar para cada tipo de variável/objetivo · hipóteses do χ² e gl · significado do resíduo padronizado ajustado > 1,96 · quantas dimensões tem a ANACOR/ACM · o que mede a inércia · diferença ANACOR × ACM · por que remover variável sem associação na ACM · matriz binária × matriz de Burt · as técnicas não supervisionadas não têm caráter preditivo.
