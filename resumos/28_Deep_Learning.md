# 28 · Deep Learning e Inteligência Artificial (Introdução + I, II e III)
**Prof. Luis Augusto Libório O. Fonseca · 4 aulas · Prioridade: alta (conceitos, fórmulas e comparações; nada de código complicado)**

## O fio condutor deste capítulo

No machine learning clássico, **você** desenha as variáveis (features) que o modelo vai usar. No **deep learning**, a rede **aprende sozinha** quais características importam, em camadas: das mais simples (bordas) às mais abstratas (um rosto). Essa ideia sustenta tudo o que se vê hoje, de reconhecimento de imagens aos modelos de linguagem. A tese do capítulo é que, por trás das arquiteturas que mudam a cada ano, existem **poucos princípios estáveis**: função, tensor, neurônio, camada, ativação e treino.

A narrativa segue a ordem em que o conhecimento se constrói: (1) o *porquê* do deep learning e a ideia de **rede como função aproximadora**; (2) a unidade básica, o **perceptron**, e sua composição em **MLP**; (3) **como a rede aprende** (loss, gradiente, otimizadores, overfitting); (4) a arquitetura para **imagens** (CNN); e (5) a arquitetura para **texto** (embeddings, atenção e Transformer).

```mermaid
flowchart LR
  A["Dados em tensores"] --> B["Forward: a rede prediz"]
  B --> C["Loss: mede o erro"]
  C --> D["Backpropagation: gradientes"]
  D --> E["Atualiza os pesos"]
  E --> B
```

## 1. Por que deep learning

**IA** é o campo amplo de simular habilidades inteligentes. **Machine learning** (Samuel, 1959) é dar ao computador a capacidade de aprender **sem ser explicitamente programado**; por isso é chamado de "**Software 2.0**": em vez de escrever regras, você fornece **dados e respostas** e o modelo descobre as regras. A diferença para o ML tradicional está na origem das features:

| | **ML tradicional** | **Deep learning** |
|---|---|---|
| Features | feitas **à mão** (feature engineering): limitadas e pouco escaláveis | **aprendidas** pela rede (*representation learning*) |
| Hierarquia | — | baixo nível (bordas) → médio (olho, boca) → alto (rosto) |
| Ponto fraco | depende do especialista | **interpretabilidade**; em dados tabulares pequenos o ML clássico costuma ser mais eficiente |

Por que agora? Porque se juntaram **Big Data** (volume e variedade), **hardware** (GPUs) e **software** (melhores algoritmos de treino e frameworks). A linha do tempo: 1943 McCulloch–Pitts · 1958 **Perceptron** · 1974–86 **backpropagation** · 2012 **AlexNet** (ImageNet) · 2017 **Transformer** · 2022 ChatGPT. Dois exemplos mostram a **maldição da dimensionalidade**: no xadrez, a força bruta (Deep Blue) bastou; no **Go** (10¹⁷⁰ jogadas), foi preciso o **AlphaGo**, que usou aprendizado por reforço profundo, jogando contra si mesmo.

### A rede como função aproximadora

O fenômeno real é uma função \(f(x)\) desconhecida; a rede \(a(x)\) tenta aproximá-la. O **teorema da aproximação universal** (Hornik et al., 1989) diz que uma rede *feedforward* com **uma camada oculta suficientemente larga** aproxima **qualquer função contínua** com precisão arbitrária. O limite deixa de ser a arquitetura e passa a ser **achar os pesos certos e ter dados que descrevam o fenômeno**: *garbage in, garbage out*. A rede aprende as **amostras**, e onde os dados não olham ela "inventa", produzindo um modelo confiante e errado. As redes são algoritmos **estocásticos**, por isso se fixa a **seed**.

Os dados entram como **tensores**, que se descrevem por **rank** (nº de eixos, `ndim`) e **shape** (tamanho de cada eixo). Não confunda os dois.

| Rank | Nome | Shape de exemplo |
|---|---|---|
| 0 | escalar | `()` |
| 1 | vetor | `(512,)` |
| 2 | matriz | `(128, 256)` |
| 3 | espaço 3D | `(10000, 128, 16)` |
| imagem em cinza / RGB | | `(H, W, 1)` / `(H, W, 3)`; dataset: `(N, H, W, ·)` |

## 2. Perceptron e MLP

O **perceptron** é a "caricatura matemática" de um neurônio: soma as entradas ponderadas e decide.

\[ \hat{y} = g\!\left(\sum_i x_i\,w_i\right) \]

Aqui \(x_i\) são as entradas, \(w_i\) os **pesos** (o que a rede aprende), \(w_0\) o **bias** (entrada fixa em 1) e \(g\) a **função de ativação**. Sem ativação, um perceptron univariado é só uma **regressão linear** (\(w_1\) gira a reta; \(w_0\) a desloca). Empilhando perceptrons em camadas obtém-se o **MLP (Multi-Layer Perceptron)**; com muitas camadas ocultas, uma **rede profunda**. **Sem ativação não linear, a composição de camadas continua linear**: a ativação é o que dá poder à rede.

![Funções de ativação: sigmoid, ReLU e softmax](img/28_ativacoes.png)

| Ativação | Característica | Uso |
|---|---|---|
| **Sigmoid** \(\frac{1}{1+e^{-z}}\) | comprime em (0, 1); **satura nas pontas** (gradiente quase zero) | saída binária |
| **ReLU** \(\max(0, z)\) | barata; não satura para \(z > 0\) | **padrão nas camadas ocultas** |
| **Softmax** | transforma logits em distribuição de probabilidade que **soma 1** | saída **multiclasse** |

O **problema XOR** mostra a necessidade de camada oculta e ativação não linear: nenhuma reta separa as classes do XOR, então um perceptron simples **nunca o resolve** (AND e OR são linearmente separáveis). Esse limite travou o campo por cerca de duas décadas.

## 3. Como a rede aprende

O ciclo é: os dados viram **tensores** → a rede faz o **forward** (\(\hat{y}\)) → a **loss** mede o erro → o **backpropagation** calcula o gradiente da loss em relação aos pesos → os **pesos são atualizados** → repete. O **gradient descent** atualiza assim:

\[ W \leftarrow W - \eta\,\nabla J(W) \]

com \(\eta\) o **learning rate** e \(\nabla J\) o gradiente da loss. A analogia é descer uma duna de olhos vendados: o **gradiente** dá a direção e o **learning rate** dá o tamanho do passo; a superfície pode ter **mínimos locais**.

![Efeito da taxa de aprendizado no gradient descent](img/28_gradient_descent.png)

No **mini-batch SGD**, usam-se subconjuntos dos dados: aproveita a **GPU**, acelera o treino e o ruído de batches pequenos tem efeito regularizador. **Otimizadores:** SGD (simples e lento), SGD + Momentum, **Adam** (**escolha padrão**), AdamW (Transformers) e RMSprop (RNNs).

### As funções de perda

| Loss | Quando | Fórmula/ideia |
|---|---|---|
| **MAE / MSE** | regressão | erro médio absoluto ou quadrático |
| **BCE** (binary cross entropy) | classificação **binária** (1 neurônio + sigmoid) | \(-[y\log\hat{y} + (1-y)\log(1-\hat{y})]\) |
| **CCE** (categorical) | multiclasse com rótulo em **one-hot** + softmax | \(-\sum y_i\log\hat{y}_i\) |
| **SCCE** (sparse) | multiclasse com rótulo como **inteiro** | \(-\log\hat{y}_{[y]}\) (mesmo valor da CCE) |

> **Exemplo resolvido (BCE).** \(y = 1\) e \(\hat{y} = 0{,}75\): \(BCE = -\log 0{,}75 \approx 0{,}288\). Uma predição **confiante e errada** é punida de forma explosiva. Trocar a loss sem trocar o formato do rótulo é um dos erros mais comuns.

### Overfitting e regularização

No **underfitting**, o modelo vai mal no treino e no teste. No **overfitting**, o erro de treino cai a quase zero e o **erro de teste dispara**. Nas curvas, a loss de validação cai e depois **sobe**: usa-se **early stopping** (parar no melhor ponto) e **dropout** (desligar aleatoriamente uma fração dos neurônios a cada passo). A **prática guiada** usou o dataset **Abalone** (prever a idade do molusco a partir de medidas baratas): fixar a seed, **analisar os dados antes de modelar**, e preparar com *encoding* e *scaling*:

| Encoding | Quando |
|---|---|
| **One-hot** | categorias **sem ordem** |
| **Ordinal** | ordem genuína (Likert, escolaridade) |
| **Embedding** | alta cardinalidade |

| Scaler | Característica |
|---|---|
| **MinMax** | [0, 1]; sensível a outliers |
| **Standard** | média 0 e desvio 1 (dados ~normais) |
| **Robust** | mediana e IQR; **resistente a outliers** |

## 4. Visão computacional e CNN

Uma MLP que **achata** a imagem perde a vizinhança entre pixels. A **CNN** preserva a estrutura espacial, com **features locais**, **hierarquia espacial** e **invariância à translação**. As tarefas clássicas são **classificação, localização, detecção e segmentação** (arquiteturas famosas: YOLO para detecção em tempo real, U-Net para segmentação). O núcleo é a **convolução**: um **kernel** (ex.: 3×3) **desliza sobre a imagem**; em cada posição faz produto elemento a elemento e soma, gerando o **feature map**. Os pesos do kernel são **aprendidos** por gradient descent.

| Conceito | O que faz | Exemplo |
|---|---|---|
| **Padding 'valid'** | não preenche as bordas; a saída **diminui** | entrada 5×5, kernel 3×3 → 3×3 |
| **Padding 'same'** | preenche; a saída **mantém** a resolução | 5×5 → 5×5 |
| **Stride (2,2)** | passo maior; **reduz a resolução** | 5×5, same → 3×3 |
| **MaxPooling2D** | maior valor de cada janela; sem parâmetros treináveis | (4,4,1) com janela 2×2 → (2,2,1) |

Em imagens RGB, o kernel tem **profundidade igual ao nº de canais**.

## 5. Texto: embeddings, atenção e Transformer

O computador "não lê, ele conta". O texto passa por **padronização**, **tokenização** e **indexação** (0 = padding; 1 = fora do vocabulário), e depois escolhe-se uma **representação**:

| Encoding | Preserva ordem? | Frequência? | Semântica? |
|---|---|---|---|
| **N-gram multi-hot** (bag of words) | não | não | não |
| **N-gram TF-IDF** | não | sim | não |
| **Sequence one-hot** | **sim** | sim | não |
| **Embedding** | sim | sim | **sim** |

O **TF-IDF** pesa cada termo por \(tf \cdot \log(N/df)\): frequente no documento e raro no corpus é informativo. O **embedding** é um vetor **denso e treinável** (poucas dimensões, em vez de milhares do one-hot), em que palavras de uso parecido ficam próximas. O limite é que o embedding é **fixo**: "banco" tem o mesmo vetor em "banco da praça" e "banco da esquina".

A **self-attention** reescreve cada vetor como uma **mistura dos vetores da própria frase**, dependendo do contexto. Cada token gera **Query** (o que procura), **Key** (o que oferece) e **Value** (o conteúdo). Em três operações:

\[ \text{score}(i,j) = k_j\cdot q_i \qquad s(i,j) = \text{softmax}_j\!\left(\frac{\text{score}}{\sqrt{d}}\right) \qquad y_i = \sum_j s(i,j)\,v_j \]

comparar, **normalizar** (cada linha soma 1; \(\sqrt{d}\) mantém a escala estável) e **misturar**. Como a atenção compara todos os tokens ao mesmo tempo e **não sabe a ordem**, soma-se o **positional encoding** (\(\sin\) e \(\cos\) em frequências diferentes).

| | **LSTM** | **Transformer** |
|---|---|---|
| Complexidade | linear, \(O(N)\) | quadrática, \(O(N^2)\) |
| Treino | **sequencial** (não paraleliza) | **paralelo** |
| Relações de longo prazo | limitadas (esquece) | todos os pares conectados |
| Dados exigidos | poucos/médios | muitos |
| Usos | séries temporais, IoT, áudio de baixa latência | LLMs, tradução |

## O que levar daqui

O deep learning aprende features em camadas e funciona como aproximador universal, dependendo de bons dados. O neurônio soma entradas ponderadas e aplica uma ativação não linear (ReLU nas ocultas, softmax na saída multiclasse). A rede aprende minimizando a loss por gradient descent (W ← W − η∇J). A CNN usa convolução, padding, stride e pooling; para texto, embeddings e atenção (Q, K, V) levam ao Transformer.

## Erros que todo mundo comete

| Erro | Correção |
|---|---|
| "Rank = shape" | rank é o **nº de eixos**; shape é o **tamanho de cada eixo** |
| "Sem ativação a rede ainda aprende curvas" | sem ativação não linear, a composição é **linear** |
| "Sigmoid é a melhor ativação nas ocultas" | **ReLU** é o padrão (a sigmoid satura) |
| "Learning rate maior é sempre melhor" | alto demais **oscila**; baixo demais é lento |
| "CCE e SCCE são diferentes na perda" | mesmo valor; muda o **formato do rótulo** |
| "Overfitting = erro alto no treino" | erro **baixo no treino e alto no teste** |
| "Embedding resolve a ambiguidade de 'banco'" | o embedding é **fixo**; a atenção traz o contexto |

## Teste-se

1. Por que a rede neural é chamada de "função aproximadora"?
<details markdown="1"><summary>Ver resposta</summary>Porque aproxima uma função desconhecida do fenômeno real; o teorema da aproximação universal garante que uma rede suficientemente larga aproxima qualquer função contínua.</details>

2. Qual a fórmula do gradient descent e o papel do learning rate?
<details markdown="1"><summary>Ver resposta</summary>W ← W − η∇J(W). O learning rate (η) define o tamanho do passo: grande demais oscila; pequeno demais é lento.</details>

3. Qual loss usar para classificação binária e qual para multiclasse com rótulo inteiro?
<details markdown="1"><summary>Ver resposta</summary>Binária: BCE (com sigmoid). Multiclasse com rótulo inteiro: SCCE (com softmax).</details>

4. Entrada 5×5, kernel 3×3, padding 'same', stride (2,2). Qual a saída?
<details markdown="1"><summary>Ver resposta</summary>3×3.</details>

5. Diferença entre LSTM e Transformer?
<details markdown="1"><summary>Ver resposta</summary>LSTM é sequencial, linear em N e esquece o longo prazo; o Transformer paraleliza no treino e conecta todos os pares, ao custo quadrático em N.</details>

## Pergunta típica
ML tradicional × DL (feature engineering × representation learning) · por que rede neural é função aproximadora e o que diz o teorema da aproximação universal · rank × shape de tensor · fórmula do perceptron, papel do bias e da ativação não linear · sigmoid × ReLU × softmax · gradient descent (fórmula, learning rate, mini-batch, mínimo local) · BCE, CCE e SCCE · overfitting × underfitting e como combatê-los · scalers (MinMax, Standard, Robust) · FCN × CNN, convolução, padding, stride, pooling · bag-of-words × TF-IDF × embedding · Query/Key/Value e softmax(QKᵀ/√d)V · positional encoding · LSTM × Transformer
