# 24 · Coleta de Dados: Crawlers e Web Scraping
**Prof. Guilherme Lima · 1 aula · Prioridade: média-baixa (você é dev: o técnico é fácil; foque nos aspectos legais e éticos e no vocabulário)**

## O fio condutor deste capítulo

Muita informação útil está em sites, e não em APIs ou bancos. Copiar à mão não escala. **Web scraping** é fazer seu programa **agir como um navegador** para extrair dados de páginas automaticamente. Mas, como seu código é "um visitante", ele pode **sobrecarregar o servidor** ou violar termos de uso e privacidade. Saber **como** fazer e **se pode** fazer é parte do trabalho.

O capítulo vai do *conceito* e das *ferramentas* (requests, BeautifulSoup, Selenium) à *prática robusta* (como não quebrar nem incomodar o servidor) e termina nos *limites legais e éticos*.

```mermaid
flowchart LR
  A["requests.get(url)"] --> B{"status_code = 200?"}
  B -->|"Não"| X["Tratar erro, tentar depois"]
  B -->|"Sim"| C["BeautifulSoup lê o HTML"]
  C --> D["Extrair título, preço, links"]
  D --> E["DataFrame / ETL"]
  E --> F["sleep e próxima página"]
```

## 1. Conceitos e ferramentas

Um **scraper** extrai dados de páginas; um **crawler** **percorre páginas seguindo links**. Ambos entram na etapa de **extração** de um ETL. A comunicação é cliente-servidor: a requisição leva a **URL**, o **método HTTP** (GET, POST…) e os **cabeçalhos (headers)**; a resposta traz o **status code**: **200** (ok), **404** (não encontrado), **403** (proibido) ou **500** (erro do servidor).

As **camadas da web** são o **HTML** (estrutura), o **CSS** (estilo) e o **JavaScript** (interatividade e conteúdo dinâmico). O **DevTools** do navegador mostra o HTML e as requisições. As ferramentas Python têm papéis distintos:

| Ferramenta | Papel |
|---|---|
| **requests** | faz a requisição HTTP |
| **BeautifulSoup** | **lê o HTML** e busca por **tags, classes e IDs** |
| **Selenium** | controla um navegador: páginas **dinâmicas** (JavaScript) e login |

Se o site oferece uma **API JSON**, ela é melhor que raspar HTML.

## 2. Prática e robustez

"A web é um quarto bagunçado": páginas são imprevisíveis. Por isso, use **`try/except`**, **timeout**, confira o **`status_code`/`raise_for_status`**, envie um **User-Agent**, faça **pausas (`time.sleep`)** entre requisições e **respeite o `robots.txt`**. Exemplos de código: `requests.get(url, headers=..., timeout=15)`; `BeautifulSoup(res.text, "lxml")`; `soup.find_all("article", class_="product_pod")`; `.get_text(strip=True)`. Os dados extraídos viram dicionários ou DataFrames e entram no ETL.

### Exemplo completo (da aula): os três projetos do notebook

A aula tem **três projetos em sequência**, cada um mostrando um jeito de coletar dados.

**Projeto 1: `requests` + `BeautifulSoup` em uma página de clima.** Primeiro, baixa-se o HTML: `res = requests.get(URL)` devolve `status_code: 200` (**200 = deu certo**) e `res.text` traz um texto com **4.598 caracteres**, com tags, classes e conteúdo **misturados**: para o `requests`, o HTML é só um texto gigante. O **BeautifulSoup** o transforma numa **árvore navegável**:

- `soup.find("h1")` pega o primeiro elemento: o título "Painel de Clima - Capitais do Mundo".
- `soup.find_all("div", class_="bg-white")` pega **todos os cartões de cidade**: **9 cidades**.
- Para cada cartão, extrai-se a cidade (`<h2>`) e os valores dos `<span>`, e monta-se uma lista de dicionários, que vira um **DataFrame** e é salvo em CSV:

| cidade | temperatura | clima | umidade |
|---|---|---|---|
| São Paulo | 26°C | Parcialmente Nublado | 55% |
| Brasília | 29°C | Ensolarado | 40% |
| Rio de Janeiro | 31°C | Muito Quente | 60% |
| Buenos Aires | 22°C | Chuva Leve | 70% |
| Londres | 15°C | Nublado | ... |

**Projeto 2: um site real para praticar (`books.toscrape.com`).** Cada livro está dentro de um `<article class="product_pod">`: o **título** fica no **atributo `title`** do link `<a>` dentro de um `<h3>` (`livro.find("h3").find("a")["title"]`), o **preço** e a **nota** em outros elementos. Na primeira página há **20 livros** (por exemplo, *A Light in the Attic* a £ 51,77, nota Três; *Sapiens* a £ 54,23, nota Cinco). Alternativa ao `find_all`: o `select` com **seletores CSS** (`article.product_pod h3 a`). Para pegar o catálogo todo, faz-se um **crawler simples** com **paginação** (`catalogue/page-N.html`): após percorrer as páginas 1, 2 e 3, o total acumulado é de **20, 40 e 60 livros**, salvos em `livros.csv`. Boas práticas: **pausar entre requisições** (`time.sleep`) e **parar se o `status_code` não for 200**. (Um detalhe real: o preço saiu como `Â£51.77`, um problema de **codificação** do texto; resolve-se ajustando o `encoding` da resposta para UTF-8.)

**Projeto 3: comparar o dólar turismo em várias fontes.** Aqui o dado vem de **três formas diferentes**, e a lição é que **coletar dados nem sempre é raspar HTML**:

| Fonte | Como coletar | Cotação (R$ por US$ 1) |
|---|---|---|
| **Wise** | **API pública** que devolve **JSON**: `requests.get(url).json()["value"]` (mesmo `requests`, só muda o formato) | **5,1731** (comercial) |
| **x-rates** | **tabela HTML**: `pd.read_html(...)` lê **todas** as tabelas da página (2 encontradas) e vira DataFrame em uma linha | **5,1757** (comercial) |
| **DolarHoje** | **BeautifulSoup**: o valor está num campo de formulário, `<input id="nacional" value="...">` | **5,3800** (**turismo**) |

Ordenando pelo preço de venda: Wise (5,1731), x-rates (5,1757) e DolarHoje (5,3800). **Cuidado ao comparar:** as duas primeiras são cotações **comerciais** e a última é de **turismo** (que costuma incluir spread e impostos), então a comparação só faz sentido entre cotações do **mesmo tipo**. Daí as boas práticas: usar um **cabeçalho de navegador** (`User-Agent`), `timeout` e `try/except` (sites mudam e saem do ar), e **respeitar o `robots.txt` e os termos de uso**.

## 3. Aspectos legais e éticos

Ignorar o **robots.txt** e os **termos de serviço** pode causar bloqueio e ações judiciais. A **LGPD** não menciona "scraping", mas o **art. 7º, §3º** diz que dados pessoais de **acesso público** devem ser tratados considerando **finalidade, boa-fé e interesse público**: dado público **não** é livre para qualquer uso. A aula propõe três critérios para avaliar se uma coleta é aceitável:

| Critério | Pergunta |
|---|---|
| **Consentimento** | os termos de serviço permitem? os titulares concordam? |
| **Problemas físicos** | minha coleta sobrecarrega o servidor e prejudica outros usuários? |
| **Intencionalidade** | qual é a **real intenção** do uso dos dados? |

> **Caso Pete Warden (2010).** Coletou dados públicos de cerca de 200 milhões de perfis do Facebook para uma visualização; os advogados da empresa exigiram que **parasse e apagasse** os dados. Mostra que "público" não significa "livre".

## O que levar daqui

Scraper extrai; crawler percorre links. requests faz a requisição, BeautifulSoup lê o HTML, Selenium cobre páginas dinâmicas. Boas práticas: try/except, timeout, User-Agent, sleep e robots.txt. Os critérios éticos são consentimento, problemas físicos e intencionalidade; a LGPD exige finalidade e boa-fé mesmo para dados públicos.

## Erros que todo mundo comete

| Erro | Correção |
|---|---|
| "Dado público pode ser usado livremente" | valem **finalidade e boa-fé** (LGPD art. 7º §3º) |
| "Scraper = crawler" | crawler **percorre links**; scraper **extrai dados** |
| "requests executa JavaScript" | **não**; use Selenium para páginas dinâmicas |
| "Sem robots.txt, tudo liberado" | ainda valem **termos de serviço** e a lei |
| "Rodar sem pausas é inofensivo" | pode **sobrecarregar** o servidor |
| "BeautifulSoup faz a requisição" | quem faz é o **requests**; o BS só **lê o HTML** |

## Teste-se

1. Qual o papel de requests, BeautifulSoup e Selenium?
<details markdown="1"><summary>Ver resposta</summary>requests faz a requisição HTTP; BeautifulSoup analisa o HTML e busca elementos; Selenium controla um navegador para conteúdo dinâmico (JavaScript) e login.</details>

2. Por que usar `sleep` entre requisições?
<details markdown="1"><summary>Ver resposta</summary>Para não sobrecarregar o servidor (critério de problemas físicos) e reduzir o risco de bloqueio.</details>

3. O que a LGPD diz sobre dados de acesso público?
<details markdown="1"><summary>Ver resposta</summary>Devem ser tratados considerando finalidade, boa-fé e interesse público que justificaram sua disponibilização (art. 7º, §3º).</details>

4. Cite os três critérios de legalidade e ética do scraping.
<details markdown="1"><summary>Ver resposta</summary>Consentimento, problemas físicos e intencionalidade.</details>

## Pergunta típica
O que faz um scraper e a diferença para crawler · papel de requests × BeautifulSoup × Selenium · status codes e headers · por que usar robots.txt, sleep e try/except · o que a LGPD diz sobre dados públicos · os 3 critérios (consentimento, problemas físicos, intencionalidade)
