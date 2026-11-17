# 17 · Supervised ML — Análise de Regressão Simples e Múltipla (OLS)
**Prof. Dr. Luiz Paulo Fávero · 4 aulas · Prioridade: máxima — é o tema com mais destaques de avaliação do curso**

> **Destaques do professor (perguntas de avaliação).** (1) os **nomes do R²**; (2) **interpretar uma saída/tabela**; (3) **calcular o R² da regressão simples a partir da correlação**; (4) **prever Y com dummies, somando betas**; (5) **a diferença entre F, t e R²**; (6) **por que não usar pesos arbitrários em categorias**.

## O fio condutor deste capítulo

Você quer prever o tempo de entrega a partir da distância. Ao desenhar os pontos (distância × tempo), uma reta que passa "no meio da nuvem" resume a relação. A **regressão por mínimos quadrados (OLS)** escolhe a reta que **minimiza a soma dos erros ao quadrado**, isto é, as distâncias verticais de cada ponto à reta. A partir daí surgem as perguntas de qualidade, que organizam o capítulo: *quanto a reta explica?* (R²), *existe modelo?* (teste F), *cada variável pesa?* (teste t) e *os pressupostos valem?* (diagnósticos).

```mermaid
flowchart LR
  A["Estimar o modelo por OLS"] --> B["R²: quanto explica?"]
  B --> C["Teste F: existe modelo?"]
  C --> D["Teste t: cada variável importa?"]
  D --> E["Diagnósticos: normalidade, multicolinearidade, heterocedasticidade"]
  E --> F["Prever dentro da faixa de X"]
```

## 1. Contexto: onde a regressão se encaixa

A regressão é um modelo **supervisionado**, do tipo **GLM**. **A escala de Y define o modelo:** Y contínuo → regressão (OLS); Y binário ou categórico → logística (capítulo 18); contagem → Poisson e afins (19); dados aninhados → multinível (20). O modelo estima \(Y = f(X_1, \ldots, X_k)\), é **confirmatório** e permite **previsão e inferência fora da amostra** (dentro da faixa de X usada no treino). Lembre-se de Box: *"todos os modelos estão errados, mas alguns são úteis"*, e de que **correlação não implica causalidade**.

## 2. Regressão linear simples

O modelo é \(Y_i = \alpha + \beta X_i + u_i\): \(\alpha\) é o intercepto, \(\beta\) a inclinação e \(u\) o **resíduo** (\(Y\) real − \(\hat{Y}\) previsto). O OLS escolhe \(\alpha\) e \(\beta\) de modo que \(\sum u = 0\) e \(\sum u^2\) seja o **mínimo possível**.

![A reta OLS e os resíduos (linhas pontilhadas)](img/17_regressao.png)

### Exemplo completo (da aula): tempo × distância

Um motorista anotou, em 10 trajetos, a **distância** percorrida (km) e o **tempo** gasto (min). A pergunta: quanto o tempo aumenta a cada km?

| Trajeto | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Distância X (km) | 8 | 6 | 15 | 20 | 25 | 11 | 5 | 32 | 28 | 20 |
| Tempo Y (min) | 15 | 20 | 20 | 40 | 50 | 25 | 10 | 55 | 35 | 30 |

**Passo 1: as médias.** \(\bar{X} = 170/10 = 17\) km e \(\bar{Y} = 300/10 = 30\) min.

**Passo 2: as somas de quadrados e produtos.** Somando as 10 observações: \(\sum (x-\bar{x})(y-\bar{y}) = 1155\); \(\sum (x-\bar{x})^2 = 814\); \(\sum (y-\bar{y})^2 = 2000\) (esta última é a **SQT**, a variação total de Y).

**Passo 3: os parâmetros do OLS.**

\[ \beta = \frac{1155}{814} = 1{,}4189 \qquad \alpha = 30 - 1{,}4189\times 17 = 5{,}878 \qquad \hat{Y} = 5{,}878 + 1{,}4189\,X \]

Interpretação: **cada km a mais aumenta o tempo em média 1,42 min**. O intercepto (5,88 min) é o tempo previsto para distância zero; seu t = 1,30 e p = 0,23 mostram que ele **não é** estatisticamente significante.

**Passo 4: os resíduos.** Para cada trajeto, \(\hat{Y} = 5{,}878 + 1{,}4189 X\) e \(u = Y - \hat{Y}\). Por exemplo, o trajeto 1: \(\hat{Y} = 5{,}878 + 1{,}4189\times 8 = 17{,}23\), então \(u = 15 - 17{,}23 = -2{,}23\).

| Trajeto | X | Y | Ŷ | Resíduo u |
|---|---|---|---|---|
| 1 | 8 | 15 | 17,23 | −2,23 |
| 2 | 6 | 20 | 14,39 | 5,61 |
| 3 | 15 | 20 | 27,16 | −7,16 |
| 4 | 20 | 40 | 34,26 | 5,74 |
| 5 | 25 | 50 | 41,35 | 8,65 |
| 6 | 11 | 25 | 21,49 | 3,51 |
| 7 | 5 | 10 | 12,97 | −2,97 |
| 8 | 32 | 55 | 51,28 | 3,72 |
| 9 | 28 | 35 | 45,61 | −10,61 |
| 10 | 20 | 30 | 34,26 | −4,26 |

Os resíduos somam **zero** (os erros para cima e para baixo se compensam), como o OLS exige.

**Passo 5: o R² (quanto a distância melhora a previsão).** A ideia é comparar **dois jeitos de prever o tempo**:

- **Jeito 1, sem usar a distância:** chutar sempre a **média**, 30 min, para qualquer trajeto. O erro de cada trajeto é "tempo real − 30".
- **Jeito 2, usando a distância:** usar a reta, \(\hat{Y} = 5{,}878 + 1{,}4189 X\). O erro de cada trajeto é o **resíduo** (tempo real − tempo previsto pela reta).

Para medir o tamanho do erro de cada jeito, **eleva-se cada erro ao quadrado** (para não se anularem) e **soma-se**. A tabela faz isso para os 10 trajetos:

| Trajeto | Tempo real | Erro do jeito 1 (real − 30) | **Erro² do jeito 1** | Previsto pela reta | Erro do jeito 2 (resíduo) | **Erro² do jeito 2** |
|---|---|---|---|---|---|---|
| 1 | 15 | −15 | 225 | 17,23 | −2,23 | 4,97 |
| 2 | 20 | −10 | 100 | 14,39 | 5,61 | 31,45 |
| 3 | 20 | −10 | 100 | 27,16 | −7,16 | 51,30 |
| 4 | 40 | +10 | 100 | 34,26 | 5,74 | 32,98 |
| 5 | 50 | +20 | 400 | 41,35 | 8,65 | 74,80 |
| 6 | 25 | −5 | 25 | 21,49 | 3,51 | 12,34 |
| 7 | 10 | −20 | 400 | 12,97 | −2,97 | 8,84 |
| 8 | 55 | +25 | 625 | 51,28 | 3,72 | 13,81 |
| 9 | 35 | +5 | 25 | 45,61 | −10,61 | 112,53 |
| 10 | 30 | 0 | 0 | 34,26 | −4,26 | 18,12 |
| **Soma** | | | **2.000** | | | **361,15** |

Esses dois totais têm nome:

- **SQT = 2.000** (soma dos quadrados **totais**): o erro de **chutar a média**. É toda a variação do tempo que existe para ser explicada.
- **SQE = 361,15** (soma dos quadrados do **erro**): o erro que **sobrou** mesmo usando a reta. É a variação que a distância **não** explica.
- **SQR = 2.000 − 361,15 = 1.638,85** (soma dos quadrados da **regressão**): a parte do erro que a reta **eliminou**. É a variação que a distância **explica**.

O **R²** é a fração do erro que a reta eliminou:

\[ R^2 = \frac{SQR}{SQT} = \frac{1638{,}85}{2000} = 0{,}8194 \]

**Leitura:** usar a distância fez o erro cair de **2.000** para **361**, ou seja, a reta **eliminou 82%** do erro. Por isso se diz que "a distância explica 82% da variação do tempo". Os 18% restantes (361 ÷ 2.000) são o que a distância não explica (trânsito, semáforos, saída tarde...). Um R² de 0 significaria que a reta não ajuda em nada (erro igual ao de chutar a média), e um R² de 1 que ela acerta todos os trajetos.

**Passo 6: a reta é de verdade ou foi sorte da amostra?** Temos só 10 trajetos. Com outros 10 trajetos, o β daria um pouco diferente. A pergunta é: **será que, na vida real, a distância não tem efeito nenhum sobre o tempo (β = 0), e o 1,42 que encontramos foi sorte?** Isso é o que o teste responde. H0: **β = 0** (a distância não afeta o tempo).

**6.1 O erro-padrão: o quanto o β "balança".** Mede o quanto o β mudaria de uma amostra de 10 trajetos para outra. Calcula-se com o que já temos:

- **Erro típico da reta (ao quadrado):** SQE ÷ (n − 2) = 361,15 ÷ 8 = **45,14** (o "n − 2" é porque a reta usou 2 números, α e β, e sobram 8 trajetos de "liberdade"). Tirando a raiz, o erro típico é **6,7 minutos**.
- **Erro-padrão do β:** \(EP = \sqrt{\dfrac{45{,}14}{814}} = \sqrt{0{,}0555} = \) **0,2355** (o 814 é a soma dos quadrados das distâncias em relação à média, do Passo 2).

Em palavras: erros maiores em volta da reta aumentam o balanço do β; distâncias mais variadas (X espalhado) diminuem.

**6.2 O teste t: a que distância de zero está o β?**

\[ t = \frac{\beta}{EP} = \frac{1{,}4189}{0{,}2355} = \mathbf{6{,}03} \]

O β está a **6 erros-padrão de distância do zero**. Como regra: **mais de uns 2 erros-padrão já é raro demais para ser sorte**.

**6.3 A decisão.** O t tem **n − 2 = 8** graus de liberdade. O **valor crítico** a 5% (na tabela t, 8 gl) é **2,306**:

- **6,03 > 2,306** → rejeita-se H0: **a distância afeta, sim, o tempo**.
- O **p-valor é 0,0003** (3 chances em 10.000 de ver um β desses por sorte se o efeito fosse zero).

**6.4 O intervalo de confiança do β:** \(\beta \pm \text{crítico}\times EP = 1{,}4189 \pm 2{,}306\times 0{,}2355 = 1{,}4189 \pm 0{,}543\), isto é, de **0,88 a 1,96**. Leitura: com 95% de confiança, **cada km a mais aumenta o tempo entre 0,88 e 1,96 minutos**. O zero **não está** dentro do intervalo, o que dá a mesma resposta do teste t (rejeita β = 0).

**6.5 O teste F: a reta prevê melhor que a média?** Faz a mesma pergunta para o modelo todo (como só há uma variável, o resultado é o mesmo). Compara o que a reta **explica** com o que **sobra**, cada um por "graus de liberdade":

\[ F = \frac{SQR \div 1}{SQE \div 8} = \frac{1638{,}85}{45{,}14} = \mathbf{36{,}30} \]

O crítico F (1 e 8 graus de liberdade, 5%) é **5,32**, e 36,30 > 5,32 → rejeita-se H0 (**p = 0,0003**, o mesmo do t). Na regressão simples, **F = t²**: \(6{,}03^2 = 36{,}3\). (O mesmo vale para o intercepto: seu t é 1,30 e p = 0,23, **não significante**, o que não é problema: o intercepto **nunca é excluído** do modelo.)


**Passo 7: usando a reta para prever.** Para um trajeto de **25 km**:

\[ \hat{Y} = 5{,}878 + 1{,}4189\times 25 = \mathbf{41{,}35 \text{ minutos}} \]

Esse é o tempo **esperado**; um trajeto real de 25 km pode variar em torno disso (o erro típico é de 6,7 min). Repare que o trajeto 5 do banco tinha exatamente 25 km e levou 50 min: o resíduo de +8,65 que vimos na tabela.

**Cuidado com a extrapolação.** A reta foi estimada com distâncias de **5 a 32 km**. Prever para 25 km é seguro (está dentro da faixa). Prever para **100 km** daria \(5{,}878 + 1{,}4189\times 100 = 147{,}8\) min, mas **não se pode confiar**: nada nos dados mostra que a relação continua linear tão longe (em 100 km entram rodovia, parada, trânsito diferente...).


O **R²** (também chamado **coeficiente de ajuste, de explicação ou de determinação**) é o **percentual da variância de Y explicado pelas variáveis explicativas**. Varia de 0 a 1 e, **na regressão simples, \(R^2 = r^2\)** (o quadrado da correlação de Pearson).

## 3. F, t e R² não são a mesma coisa

| Medida | Responde | Hipótese | Decisão |
|---|---|---|---|
| **R²** | quanto da variância de Y é explicada? | — | descritivo, não decide se há modelo |
| **Teste F** | o modelo **como um todo** existe? | H0: \(\beta_1 = \ldots = \beta_k = 0\) | **p < 5% → existe modelo** |
| **Teste t** | **cada** parâmetro é significante? | H0: \(\beta_j = 0\); \(t = \hat\beta / EP\) | \(\lvert t\rvert > 1{,}96\) (p < 0,05) → significante |

> **Atenção.** **Quem decide se há modelo é o F, não o R².** Pode haver modelo com R² baixo (baixo poder preditivo). Se o intervalo de confiança de um parâmetro contém o zero, ele não é significante. **Nunca exclua o intercepto \(\alpha\)** só porque não é significante: forçar \(\alpha = 0\) vicia os betas.

## 4. Regressão múltipla

Com várias variáveis: \(Y = \alpha + \beta_1 X_1 + \cdots + \beta_k X_k + u\), ou, em forma matricial, \(b = (X'X)^{-1}X'Y\). Cada beta é o efeito da variável **mantendo as demais constantes** (*ceteris paribus*). Para **comparar modelos com números diferentes de variáveis**, usa-se o **R² ajustado**, que penaliza variáveis inúteis:

\[ R^2_{aj} = 1 - (1 - R^2)\,\frac{n-1}{n-k-1} \]

### Exemplo completo (da aula): percepção de corrupção em 50 países

Variável dependente: **CPI** (*Corruption Perception Index*, índice da Transparência Internacional: **quanto maior, menor a corrupção percebida**). Explicativas: a **idade média dos bilionários** do país e as **horas semanais de trabalho**. Dados de 50 países (CPI médio de 4,89; idade média de 60,5 anos; 32,7 horas).

**Correlações com o CPI:** idade = **+0,44** e horas = **−0,44** (e entre idade e horas, só −0,19, então não há colinearidade).

O modelo \(\widehat{CPI} = \alpha + \beta_1\,\text{idade} + \beta_2\,\text{horas}\) estimado por OLS:

| Termo | Coeficiente | Erro-padrão | t | p-valor | IC 95% |
|---|---|---|---|---|---|
| Intercepto | 11,972 | 5,165 | 2,32 | 0,025 | 1,58 a 22,36 |
| **idade** | **0,0997** | 0,033 | 3,05 | 0,004 | 0,03 a 0,17 |
| **horas** | **−0,4013** | 0,135 | −2,98 | 0,005 | −0,67 a −0,13 |

**Interpretação (ceteris paribus).** Com as horas de trabalho constantes, **cada ano a mais na idade média dos bilionários eleva o CPI em 0,10** (bilionários mais velhos despertam menos desconfiança). Com a idade constante, **cada hora a mais de trabalho semanal reduz o CPI em 0,40**. Os dois sinais batem com a intuição, e os dois betas são significantes (p < 0,05).

**Ajuste global.** \(R^2 = 0{,}3239\) (as duas variáveis explicam 32% da variância do CPI). O **R² ajustado** penaliza o número de variáveis, com n = 50 e k = 2:

\[ R^2_{aj} = 1 - (1 - 0{,}3239)\times\frac{50-1}{50-2-1} = 1 - 0{,}6761\times\frac{49}{47} = 1 - 0{,}7049 = 0{,}2951 \]

O **F** testa se **ao menos um** beta é diferente de zero:

\[ F = \frac{R^2/k}{(1-R^2)/(n-k-1)} = \frac{0{,}3239/2}{0{,}6761/47} = \frac{0{,}1620}{0{,}01439} = 11{,}26 \quad (p = 0{,}0001) \]

**Pressupostos.** Resíduos normais? **Shapiro-Francia: W = 0,980, p = 0,455 > 0,05, então não rejeita a normalidade.** Heterocedasticidade? **Breusch-Pagan: p = 0,891 > 0,05, então não há evidência de problema.** O modelo é adequado para inferência.


## 5. Variáveis qualitativas: as dummies (cai sempre)

O erro clássico é a **ponderação arbitrária**: codificar categorias como 1, 2, 3. Isso supõe que o efeito entre categorias é **linear**, o que quase nunca é verdade. A solução é a **dummização**: para n categorias criam-se **n − 1 dummies** (0/1); a categoria omitida é a **referência** (evita multicolinearidade perfeita), e o beta de cada dummy é a diferença média de Y **em relação à referência**. Para **prever**, soma-se \(\alpha\) mais os betas das dummies que valem 1.

### Exemplo completo (da aula): CPI por região do planeta

Os mesmos 50 países, agora explicados pela **região** (variável qualitativa): Europa (24 países), Ásia (17), América do Sul (5), Oceania (2) e EUA e Canadá (2). O CPI médio de cada uma é:

| Região | Países | CPI médio |
|---|---|---|
| Ásia | 17 | 2,329 |
| América do Sul | 5 | 4,180 |
| Europa | 24 | 6,258 |
| EUA e Canadá | 2 | 8,000 |
| Oceania | 2 | 9,000 |

**A forma errada (ponderação arbitrária).** Se codificarmos as regiões em ordem alfabética como 1 = América do Sul, 2 = Ásia, 3 = EUA e Canadá, 4 = Europa, 5 = Oceania e regredirmos o CPI nesse número, obtemos \(\widehat{CPI} = 0{,}52 + 1{,}448\times\text{código}\), com R² = 0,41. Os valores previstos para cada região ficam:

| Região | Média real | Previsão do modelo errado |
|---|---|---|
| América do Sul | 4,18 | **1,97** |
| Ásia | 2,33 | 3,42 |
| EUA e Canadá | 8,00 | **4,87** |
| Europa | 6,26 | 6,31 |
| Oceania | 9,00 | 7,76 |

O modelo errado tira conclusões absurdas (por exemplo, que a América do Sul tem **menos** CPI que a Ásia) porque supõe que passar de "América do Sul" para "Ásia" tem o **mesmo efeito** que passar de "Ásia" para "EUA e Canadá". A ordem alfabética não tem significado.

**A forma certa: dummies.** Com 5 regiões criam-se **4 dummies**; a omitida é a **referência** (aqui, a **Ásia**, a de menor CPI):

| Termo | Coeficiente | p-valor |
|---|---|---|
| Intercepto (Ásia) | **2,329** | < 0,001 |
| América do Sul | +1,851 | 0,045 |
| EUA e Canadá | +5,671 | < 0,001 |
| Europa | +3,929 | < 0,001 |
| Oceania | +6,671 | < 0,001 |

O intercepto é exatamente a **média da referência** (Ásia = 2,329), e cada beta é a **diferença** entre aquela região e a Ásia. Para **prever**, soma-se \(\alpha\) mais o beta da dummy que vale 1:

- **Europa:** 2,329 + 3,929 = **6,258** (a média real da Europa)
- **Oceania:** 2,329 + 6,671 = **9,000**
- **América do Sul:** 2,329 + 1,851 = **4,180**

O ajuste global é \(R^2 = 0{,}603\) e \(F = 17{,}09\) (p ≈ 10⁻⁸). Num modelo só com dummies, as previsões são **as médias de cada grupo**: nada de ponderação arbitrária.


## 6. Pressupostos e diagnósticos

| Diagnóstico | O que verifica | Teste e decisão |
|---|---|---|
| **Normalidade dos resíduos** | base da inferência e dos IC | **Shapiro-Francia**; H0: normais; queremos **p > 0,05** (não rejeitar) |
| **Multicolinearidade** | alta correlação entre as explicativas | **VIF = 1/Tolerance**, com Tolerance = \(1 - R^2_{aux}\); **VIF > 10** é alerta |
| **Heterocedasticidade** | variância dos erros **não constante** (cone no gráfico) | **Breusch-Pagan**; H0: homocedasticidade; **p < 0,05 → problema** |

**Se os resíduos não são normais**, a forma funcional é inadequada. Uma saída é a **transformação de Box-Cox**, \(Y^* = (Y^\lambda - 1)/\lambda\), em que se escolhe o \(\lambda\) que melhor aproxima a normalidade: \(\lambda = 1\) é linear, 2 quadrática, 0,5 raiz, −1 inversa e **\(\lambda = 0\) equivale a \(\ln Y\)**. Os betas do modelo transformado **não são comparáveis** com os do linear, porque a métrica de Y mudou.

**O procedimento stepwise** remove passo a passo as variáveis **não significantes** e ajuda na multicolinearidade, mas **não corrige** heterocedasticidade nem forma funcional. A **multicolinearidade** causa sinais invertidos e **t baixo com F significante e R² alto**; as saídas são o stepwise, remover a variável ou usar **PCA** (capítulo 15). A **heterocedasticidade** costuma vir de **variável relevante omitida** e se mitiga incluindo preditores ou usando modelos multinível.

> **Exemplo completo (da aula): Box-Cox com o comprimento de bebês.** Dados de 74 bebês: **comprimento** (cm) em função da **idade** (semanas de vida). O modelo linear dá \(\widehat{comp} = 43{,}10 + 0{,}941\times\text{idade}\), com \(R^2 = 0{,}9027\), mas o **Shapiro-Francia dos resíduos tem p = 0,00014 < 0,05: os resíduos NÃO são normais** (o crescimento não é linear). Aplicando a transformação de Box-Cox ao comprimento, o λ ótimo é **2,66**; o modelo com \(Y^*\) transformado sobe para \(R^2 = 0{,}9620\), e o Shapiro-Francia passa para **p = 0,103 > 0,05**: agora **não se rejeita** a normalidade. Os betas do modelo transformado (4.995 e 947) **não são comparáveis** com os do linear, porque a métrica de Y mudou.

> **Exemplo completo (da aula): multicolinearidade com salários.** Dados de 15 pessoas: **salário** explicado pelas notas em duas disciplinas. Compare dois modelos:
>
> | | Modelo 1: rh1 e econometria1 | Modelo 2: rh2 e econometria2 |
> |---|---|---|
> | Correlação entre as duas explicativas | −0,27 | **0,994** |
> | **VIF** de cada explicativa | **1,08** | **82,06** (tolerance = 1/82,06 = 0,012) |
> | R² e F | 0,827 e 28,8 (F significante) | 0,829 e 29,1 (F significante) |
> | p de rh | 0,79 | 0,23 |
> | p de econometria | **< 0,001** | 0,67 |
>
> No modelo 2 há **R² alto e F significante, mas nenhum beta significante** (e o beta da econometria até muda de sinal, para −139): é o **sintoma clássico de multicolinearidade**. A econometria2 e a rh2 são praticamente a mesma informação (correlação de 0,994), então o modelo não consegue separar o efeito de cada uma. Já no modelo 1 o VIF é 1,08 (longe de 10) e a econometria é muito significante.


**Roteiro da aula:** explorar correlações → estimar OLS (com dummies) → stepwise a 95% → Shapiro-Francia dos resíduos → se não normal, Box-Cox em Y e repetir → VIF e Breusch-Pagan → prever dentro da faixa de X.

## O que levar daqui

O OLS minimiza a soma dos resíduos ao quadrado. R² mede a variância explicada (na simples, \(R^2 = r^2\)); o F decide se há modelo; o t avalia cada variável; o R² ajustado compara modelos. Categorias viram n − 1 dummies, e o beta é a diferença à referência. Diagnósticos: Shapiro-Francia (p > 0,05), VIF < 10, Breusch-Pagan (p > 0,05).

## Erros que todo mundo comete

| Erro | Correção |
|---|---|
| "R² baixo = não há modelo" | quem decide é o **F** |
| "No Shapiro-Francia queremos p < 0,05" | queremos **p > 0,05** (normalidade) |
| "Breusch-Pagan com p > 0,05 indica problema" | p **< 0,05** = heterocedasticidade |
| "Para n categorias, n dummies" | **n − 1** (uma é a referência) |
| Codificar categorias como 1, 2, 3 | ponderação arbitrária: use dummies |
| "Excluir o intercepto se não for significante" | **não exclua** |
| "Os betas do Box-Cox são comparáveis" | a métrica de Y mudou: **não comparáveis** |
| "O stepwise resolve a heterocedasticidade" | só variáveis não significantes e multicolinearidade |

## Teste-se

1. A correlação entre X e Y é 0,5. Qual o R² da regressão simples?
<details markdown="1"><summary>Ver resposta</summary>R² = 0,5² = 0,25 (25%).</details>

2. O F é significativo e o R² é 0,08. Existe modelo?
<details markdown="1"><summary>Ver resposta</summary>Sim, existe modelo (ao menos uma variável explica Y), mas com baixa capacidade preditiva.</details>

3. Uma variável qualitativa tem 5 categorias. Quantas dummies?
<details markdown="1"><summary>Ver resposta</summary>4; a quinta é a referência.</details>

4. O que se espera do Shapiro-Francia dos resíduos?
<details markdown="1"><summary>Ver resposta</summary>Não rejeitar H0 (p > 0,05): resíduos normais.</details>

5. Cite duas consequências da multicolinearidade.
<details markdown="1"><summary>Ver resposta</summary>Sinais invertidos ou instáveis nos betas, e t baixo com F significante e R² alto (erros de predição).</details>

## Pergunta típica
Nomes do R² e o que mede · diferença entre F, t e R² (há modelo ≠ R² alto) · hipóteses do F e do t · por que usar o R² ajustado · n−1 dummies e por que não usar pesos 1, 2, 3 · calcular valor previsto com dummies · R² na simples = r² · o que testa o Shapiro-Francia e qual resultado se espera · Box-Cox (λ = 0 → ln) · stepwise · multicolinearidade (VIF/Tolerance) · heterocedasticidade (causas, Breusch-Pagan) · por que não excluir o intercepto
