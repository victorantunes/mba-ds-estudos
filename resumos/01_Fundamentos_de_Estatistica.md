# 01 · Fundamentos de Estatística
**Prof. Wilson Tarantin Jr. · 3 aulas · Prioridade: ALTA — é a base de regressão, logística, contagem, multinível, PCA e séries temporais**

## O fio condutor deste capítulo

Imagine que você recebeu uma planilha com os dados de 500 clientes de um banco: idade, renda, estado civil, se pagaram o empréstimo em dia. Ninguém consegue "ler" 500 linhas e enxergar um padrão. A estatística existe para responder a duas perguntas, nesta ordem.

A primeira é **como resumir o que eu tenho** sem perder o essencial. A segunda é mais ousada: **o que posso concluir sobre os clientes que não estão na planilha**, ou seja, sobre a população inteira, tendo olhado só para uma amostra, e com que grau de segurança.

O capítulo segue exatamente esse caminho. Primeiro aprendemos a distinguir os tipos de coluna da planilha, porque isso decide tudo o que vem depois. Depois aprendemos a resumir uma coluna. Em seguida descobrimos que certos fenômenos seguem "moldes" matemáticos (as distribuições), e é esse molde que nos deixa fazer o passo final: testar hipóteses e decidir.

## 1. Primeiro, que tipo de coluna é essa?

Quem programa já conhece a ideia: uma coluna tem um tipo, e o tipo define quais operações fazem sentido. Em estatística acontece o mesmo, com duas famílias.

**Variáveis qualitativas** (ou categóricas) dizem *a qual grupo* a linha pertence: estado civil, cor do carro, "aprovou ou não o crédito", faixa de renda. Os números que eventualmente as representam são apenas etiquetas. **Variáveis quantitativas** (ou métricas) dizem *quanto*: idade, renda em reais, número de filhos. Dentro delas, as **discretas** vêm de contagem (0, 1, 2 filhos) e as **contínuas** podem assumir qualquer valor num intervalo (altura, salário).

Essa distinção importa porque ela decide quais contas são legítimas. Suponha que você codifique as cores de carro como branco = 1, preto = 2, prata = 3 e calcule a média: 5,68. O que isso significa? Nada. Os números eram só etiquetas, e a média de etiquetas não é uma cor. Esse erro tem nome na disciplina, **ponderação arbitrária**, e reaparece em todo o curso (é o motivo de, mais adiante, usarmos "dummies" em regressões). Para uma variável qualitativa só se contam frequências e se identifica a **moda**, isto é, a categoria mais comum.

## 2. Resumindo uma coluna numérica: centro, espalhamento e forma

Para uma variável quantitativa a pergunta natural é: *se eu tivesse de descrever essa coluna em três frases, o que diria?* A resposta tem três partes.

**Onde está o centro?** A **média** soma tudo e divide por n; usa toda a informação, mas é puxada por valores extremos. Considere cinco salários, em milhares de reais: 3, 3,2, 3,5, 4 e 30. A média é 8,74, um valor que ninguém na amostra ganha, porque o salário de 30 arrastou a conta. A **mediana**, o valor do meio quando ordenamos os dados, vale 3,5 e descreve melhor o "salário típico". Por isso, quando há valores extremos (os *outliers*), a mediana é mais confiável; e quando a média fica **acima** da mediana, sabemos que a distribuição tem cauda longa à **direita**. Os **quartis** (Q1, Q2, Q3) generalizam a mediana: dividem os dados ordenados em quatro partes iguais.

**O quanto os dados se espalham em torno desse centro?** Dizer que a média é 100 não informa se os valores ficam entre 99 e 101 ou entre 0 e 200. A **variância** mede o afastamento médio ao quadrado em relação à média: para os dados 2, 4 e 6 (média 4), os desvios são −2, 0 e 2, os quadrados somam 8, e dividimos por n − 1 = 2, obtendo variância 4. Dividimos por n − 1, e não por n, porque a própria média já foi estimada a partir dos mesmos dados e "consumiu" um grau de liberdade. Como a variância fica em unidade ao quadrado (reais², anos²), tiramos a raiz e obtemos o **desvio padrão**, que tem a mesma unidade dos dados: aqui, 2.

Dois cuidados completam esta parte. Para comparar a dispersão de variáveis em escalas diferentes (altura em metros e peso em quilos) o desvio padrão não serve; usamos o **coeficiente de variação**, que é o desvio dividido pela média. Uma variável com média 100 e desvio 10 tem CV de 10%; outra com média 5 e desvio 2 tem CV de 40%, mais heterogênea, embora seu desvio absoluto seja menor. E, quando o interesse é saber quão precisa é a *média* calculada, usamos o **erro padrão**, o desvio dividido por √n. Com desvio 10, uma amostra de 100 casos dá erro padrão 1; uma de 400 dá 0,5. Quadruplicar a amostra só dobrou a precisão: a raiz explica por que ganhar precisão custa cada vez mais caro.

**Qual a forma?** Por fim, olhamos para o desenho da distribuição: se é simétrica ou tem uma cauda (**assimetria**) e se é mais "pontuda" ou mais achatada que o padrão (**curtose**). A regra de Tukey usa os quartis para apontar outliers: qualquer valor abaixo de Q1 − 1,5·AIQ ou acima de Q3 + 1,5·AIQ, em que AIQ = Q3 − Q1.

## 3. De resumo a molde: as distribuições de probabilidade

Até aqui descrevemos dados que já tínhamos. Para dar o salto à população precisamos de uma ideia nova: muitos fenômenos se comportam como **moldes conhecidos**, as distribuições de probabilidade. Se sabemos qual é o molde, conseguimos calcular a chance de qualquer resultado sem observar tudo.

O molde depende de *o que estamos contando*. Se há **um único experimento com dois desfechos** (compra ou não compra), a distribuição é a **Bernoulli**, e é ela que está por trás da regressão logística. Se repetimos esse experimento n vezes de forma independente e contamos os sucessos, temos a **Binomial**. Por exemplo, lançando uma moeda 3 vezes, a chance de exatamente 2 caras é C(3,2) · 0,5² · 0,5 = 0,375. Se, em vez de n tentativas fixas, contamos **eventos que ocorrem ao longo de uma janela** (pacientes por ano, chamadas por hora), usamos a **Poisson**, cuja taxa média λ é o único parâmetro: com λ = 2 pacientes por ano, a chance de ver exatamente um é e⁻² · 2 ≈ 27%. Poisson e uma variante chamada binomial negativa são a base dos modelos de contagem do curso.

Para variáveis contínuas o molde central é a **normal**, a curva em sino definida por média μ e desvio σ. Sua propriedade prática é a regra empírica: cerca de 68% dos valores ficam a até 1 desvio da média, 95% a até 2 e 99,7% a até 3. Para trabalhar com qualquer normal usamos o **escore Z**, Z = (X − μ) / σ, que responde "a quantos desvios padrão do centro está este valor?". Se o retorno médio de um ativo é 2,8% e o desvio é 1,2%, a chance de o retorno passar de 4% é a chance de Z passar de 1, aproximadamente 16%.

Três outras distribuições entram porque aparecem em testes que veremos já. A **t de Student** parece a normal, mas com caudas mais pesadas: ela corrige a incerteza extra de quem tem poucos dados e não conhece o desvio padrão da população. A **qui-quadrado (χ²)** serve para comparar frequências de categorias. A **F** compara variâncias. Todas dependem dos **graus de liberdade**, que pode-se entender como "quantos valores ainda são livres para variar": se cinco números devem somar 18, escolhemos quatro livremente e o quinto fica determinado.

## 4. A lógica de um teste de hipóteses

Agora podemos responder à segunda pergunta. Um fabricante afirma que seus potes têm 100 g. Você pesa 25 potes e encontra média 104 g. A diferença é real ou foi sorte da amostra?

O raciocínio estatístico funciona como um tribunal. Parte-se de uma afirmação que se presume verdadeira até haver evidência forte contra ela: a **hipótese nula, H0** (aqui, "a média é 100"). A **hipótese alternativa, H1**, é o que se quer demonstrar ("a média é diferente de 100"). Você nunca *prova* H0; apenas verifica se os dados são tão improváveis, **supondo H0 verdadeira**, que ela deve ser rejeitada.

Para medir "improvável" usamos o **p-valor**: a probabilidade de observar um resultado tão extremo quanto o seu (ou mais) *se H0 fosse verdadeira*. Um p-valor pequeno significa que o seu resultado seria raro num mundo em que H0 é verdadeira; então você desconfia de H0. Quão pequeno? Você decide antes, escolhendo um **nível de significância α** (usualmente 5%). A regra fica simples: **se p < α, rejeita-se H0**; caso contrário, não se rejeita, o que quer dizer apenas "evidência insuficiente", e não "H0 é verdadeira".

Há duas maneiras de errar. Rejeitar H0 quando ela é verdadeira é o **erro tipo I**, e sua probabilidade é exatamente α: é o "alarme falso". Não rejeitar H0 quando ela é falsa é o **erro tipo II**: o culpado que passou.

No exemplo dos potes, calcula-se a estatística t = (X̄ − μ₀) / (S/√n). Com média 104, desvio 10 e n = 25: t = 4 / (10/5) = 2,0, com 24 graus de liberdade. O valor crítico a 5% é cerca de 2,064. Como 2,0 < 2,064, **não rejeitamos H0**: apesar de 4 g parecer muito, com essa variabilidade e esse tamanho de amostra a diferença poderia ser acaso. Repare como a decisão combina três coisas: o tamanho da diferença, a variabilidade dos dados e o tamanho da amostra.

## 5. Qual teste usar?

O procedimento é sempre o mesmo; o que muda é a estatística, e a escolha depende do tipo de variável e da pergunta.

Se queremos saber se **duas variáveis qualitativas** estão associadas (sexo e compra, por exemplo), usamos o **qui-quadrado de associação**. Montamos a tabela de contingência, calculamos para cada célula quantos casos *esperaríamos* se não houvesse associação ((total da linha × total da coluna) / N) e comparamos com o observado. Exemplo: 100 casos, com 30 e 20 compras entre os dois sexos de uma linha e 10 e 40 na outra. Os esperados são 20, 30, 20 e 30; χ² = Σ (observado − esperado)² / esperado = 5 + 3,33 + 5 + 3,33 ≈ 16,7, com (2−1)(2−1) = 1 grau de liberdade. Como o crítico a 5% é 3,84, rejeita-se H0: **há associação**.

Se queremos saber se **duas variáveis quantitativas** caminham juntas, usamos o **coeficiente de correlação de Pearson**, que vai de −1 a 1, e testamos H0: correlação = 0 com um teste t.

Se a pergunta é sobre a **média de um grupo**, usamos o teste **Z** quando o desvio padrão populacional é conhecido (ou a amostra é grande) e o teste **t** quando é desconhecido, como no exemplo dos potes. Para **comparar as médias de dois grupos**, antes fazemos o **teste F** para ver se as variâncias dos grupos são iguais, porque isso define a versão do teste t. E se queremos comparar **observado e esperado** de uma só variável categórica, usamos o χ² de aderência.

Por fim, um **intervalo de confiança** diz o mesmo de outra forma: em vez de responder "sim/não", entrega a faixa de valores plausíveis para a média (X̄ ± t · erro padrão). Se o valor de H0 estiver fora do intervalo de 95%, o teste a 5% rejeita H0.

## O que levar daqui

A estatística começa em classificar cada variável, porque isso delimita as contas permitidas. Resumimos uma coluna com centro, espalhamento e forma, escolhendo medidas robustas (mediana) quando há outliers. As distribuições são moldes que permitem calcular probabilidades: Bernoulli e Binomial para sucessos, Poisson para eventos numa janela, normal para variáveis contínuas. E um teste de hipóteses é um tribunal: presume-se H0, calcula-se quão raros seriam os dados sob H0 (p-valor) e rejeita-se H0 apenas quando p < α.

## Erros que todo mundo comete

Dizer que "p = 0,03 significa 3% de chance de H0 ser verdadeira" está errado: o p-valor é a probabilidade dos *dados* sob H0, não de H0. Concluir que H0 é verdadeira só porque não foi rejeitada também está errado. Confundir α (escolhido antes) com o p-valor (calculado dos dados) é frequente. E calcular média ou mediana de uma variável qualitativa produz números sem sentido.

## Teste-se

1. Por que a "média" das cores dos carros não faz sentido, e o que se pode calcular?
<details markdown="1"><summary>Ver resposta</summary>Porque os números são apenas etiquetas de categorias (ponderação arbitrária). Para uma variável qualitativa só se calculam frequências e a moda.</details>

2. Cinco salários: 3; 3,2; 3,5; 4; 30. Qual medida descreve melhor o salário típico e por quê?
<details markdown="1"><summary>Ver resposta</summary>A mediana (3,5): o valor extremo de 30 puxa a média (8,74) para um valor que ninguém recebe.</details>

3. Em um teste com α = 5% e p = 0,03, qual a decisão? E com α = 1%?
<details markdown="1"><summary>Ver resposta</summary>Com 5%, p < α: rejeita H0. Com 1%, p > α: não rejeita H0.</details>

4. Quantos graus de liberdade tem um qui-quadrado de associação de uma tabela 3×4?
<details markdown="1"><summary>Ver resposta</summary>(3 − 1)(4 − 1) = 6.</details>

5. Qual teste fazer antes de comparar as médias de dois grupos, e para quê?
<details markdown="1"><summary>Ver resposta</summary>O teste F das variâncias, para decidir entre o t com variâncias iguais ou diferentes.</details>

## Pergunta típica
Para variável qualitativa, qual medida de posição posso usar · o que significa p < α · α é a probabilidade de qual erro · média > mediana indica qual assimetria · por que mais amostra reduz o erro padrão · quando usar o CV · qual teste para associação entre categóricas e qual para duas métricas · qual distribuição está na base de cada modelo (Bernoulli, Binomial, Poisson, Binomial negativa) · diferença entre Z e t

*Fonte: slides do Prof. Tarantin (baseados em Fávero e Belfiore, "Manual de análise de dados") e transcrições das 3 aulas.*
