# 13 · Modelagem Matemática e Estruturação de Problemas Complexos
**Prof. Dr. Marcos dos Santos (Marinha, IME/ITA/UFF) · 2 aulas (28/10 e 04/11/2025) · Prioridade: ALTA (cálculo passo a passo de AHP e AHP-Gaussiano; dica de prova do professor sobre a matriz de julgamentos)**

> Dica dita em aula: *"Vai que um dia cai na prova… na matriz de ponderações, a diagonal principal tem valores sempre: **1**."* e *"se estou comparando custo com custo, o grau tem que ser um."*

## 1. Contexto
- **Pesquisa Operacional (OR):** abordagem científica para resolver problemas na gestão de sistemas complexos e **ajudar quem decide a decidir melhor**; usa analytics, modelagem, estruturação de problemas, simulação, otimização e ciência de dados. Áreas: apoio multicritério à decisão, análise envoltória (DEA), ciência de dados, teoria dos grafos, simulação de eventos, estatística, matemática.
- **Tomada de decisão:** decide-se sempre que há problema com **mais de uma alternativa** (mesmo "fazer ou não fazer"). Cada decisão tem **ganho e perda**; difícil porque queremos sempre ganhar, nunca perder.
- **Decisão multicritério (MCDM):** problema caracterizado por uma **matriz de decisão** (alternativas × critérios, com pesos dos critérios dados pelo decisor). Matriz 10×20 = 200 dados. Métodos: **AHP, ANP, PROMETHEE, ELECTRE, TOPSIS, SAPEVO-M, THOR, PrOPPAGA**.
- É preciso informar para cada critério se é **monotônico de lucro (quanto maior, melhor)** ou **de custo (quanto menor, melhor)**.

## 2. AHP (Analytic Hierarchy Process — Saaty, década de 1970, Wharton)
- Método de decisão multicritério **simples e flexível**, baseado em **matemática e psicologia (escala psicométrica)**; aceita julgamentos **subjetivos/verbais**, critérios conflitantes; ganhos: **transparência, lisura, rastreabilidade e replicabilidade**. Ajuda a **escolher e justificar** a decisão.
- **Estruturação (hierarquia):** objetivo estratégico → critérios → alternativas. Ex.: comprar um celular; critérios Custo, Câmera, Armazenamento, Bateria; alternativas Xiaomi, Samsung, iPhone.
- **Escala Fundamental de Saaty:** 1 = igualdade; 3 = importância moderada; 5 = mais importante; 7 = muito mais importante; 9 = extremamente mais importante; 2, 4, 6, 8 = valores intermediários; **recíprocos 1/3, 1/5, 1/7, 1/9**.
- **Matriz de julgamentos (ponderações) par a par:** quadrada; **diagonal principal = 1**; **axioma da reciprocidade: se aij = 3, então aji = 1/3**; nº de comparações = **n(n−1)/2** (para 4 critérios, 6). **Transitividade:** se A > B e B > C, então A > C.
- **Passo a passo:**
  1. **Normalizar** a matriz: dividir cada elemento pela **soma da sua coluna**.
  2. **Vetor prioridade (pesos)** = **média das linhas** da matriz normalizada. Exemplo da aula: **Custo 0,548; Câmera 0,283; Armazenamento 0,117; Bateria 0,052**.
  3. **Consistência:** calcular **λmax** (multiplicar a matriz original pelo vetor prioridade, dividir cada resultado pelo respectivo peso e tirar a média = **4,14**) → **CI = (λmax − n)/(n − 1) = 0,046** → **CR = CI / RI = 0,046/0,9 = 0,052**. **RI (índice aleatório de Saaty):** n=3 → 0,58; n=4 → 0,90; n=5 → 1,12; n=6 → 1,24; n=7 → 1,32; n=8 → 1,41. **CR < 10% = consistente/aceitável.**
  4. Repetir o julgamento par a par das **alternativas em cada critério** (ou normalizar dados quantitativos) → **prioridades locais**.
  5. **Agregação:** nota global = Σ (peso do critério × prioridade da alternativa no critério). Ranking final do exemplo: **1º Xiaomi, 2º Samsung, 3º iPhone**.
- **Com dados quantitativos** (preço, GB, horas de bateria) **não precisa comparar par a par**: **normaliza-se** a coluna dividindo cada valor pela soma. Para critérios de **custo** (quanto menor, melhor) usa-se o **inverso** (1/x) e depois normaliza (preço 1500, 1800, 5000 → 0,469, 0,391, 0,141). Para **lucro**, normaliza direto. *Por que normalizar a matriz de decisão?* Para torná-la **adimensional** e permitir somar critérios com unidades diferentes.
- **Limitações do AHP:** nenhum método resolve tudo; **só funciona bem até ~7 critérios (teoricamente 15)**; número de comparações cresce rápido; **desgaste cognitivo** do decisor; **difícil obter CR < 10%**; demanda tempo do decisor.
- Ferramenta: **3 Decision Methods (www.3decisionmethods.com)** (IME).

## 3. AHP-Gaussiano (Santos et al., 2020/2021)
- Origem: problema real da **Marinha do Brasil** (escolha de navio de guerra, ~2005); publicado no **International Journal of the AHP (2021)**.
- **Ideia:** os **pesos dos critérios saem dos próprios dados** da matriz de decisão por uma análise de **dispersão (fator gaussiano)**, **sem comparação par a par** entre critérios → **menos esforço cognitivo e menos viés/subjetividade, mais transparência**; funciona com **muitas alternativas e critérios**; ferramentas grátis em R, Python, Excel, Julia.
- **8 passos:**
  1. **Matriz de decisão** (alternativas × critérios).
  2. **Normalização** (custo: inverso e normaliza; lucro: normaliza pela soma).
  3. **Matriz transposta** e **média** das alternativas em cada critério (sempre **1/n**).
  4. **Desvio padrão** das alternativas dentro de cada critério.
  5. **Fator gaussiano = desvio padrão / média = coeficiente de variação (CV)** de cada critério.
  6. **Fator gaussiano normalizado** (cada fator ÷ soma dos fatores) = **peso do critério**. *Quanto mais dispersos os valores num critério, mais ele discrimina as alternativas e maior seu peso.* Exemplo: Custo 0,325; Câmera 0,198; Armazenamento 0,219; Bateria 0,257.
  7–8. **Agregação:** nota = Σ (peso gaussiano × valor normalizado) → **ranking**: Xiaomi 0,369 (1º), Samsung 0,358 (2º), iPhone 0,273 (3º).
- **Pontos fortes:** método novo; conceito fácil (dispersão em torno da média); fácil de usar (só preenche a matriz); grande volume de dados; menor esforço do decisor.
- Aplicações citadas: viaturas policiais (PMERJ), perfuração de poços e **transição energética (Petrobras)**, ranking de estados para investimento em educação, TCCs do MBA.

## Pergunta típica
Calcular o vetor prioridade (normalizar pela soma da coluna e tirar a média das linhas) · calcular CI/CR com RI dado e decidir se é consistente · aplicar reciprocidade e identificar a diagonal (=1) · diferenciar critério de custo × lucro · o que muda no AHP-Gaussiano (peso vem do CV, sem comparação par a par) · limitações do AHP.
