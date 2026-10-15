# 24 · Coleta de Dados: Crawlers e Web Scraping
**Prof. Guilherme Lima · 1 aula · Prioridade: MÉDIA-BAIXA (você é dev: o técnico é fácil; foque nos aspectos legais/éticos e no vocabulário)**

## 1. Conceito
- **Web scraping** = seu programa faz o papel de um **navegador**: acessa e interpreta sites automaticamente para extrair dados. **Crawler** = rastreia/percorre páginas seguindo links. Automatiza tarefas manuais para sobrar tempo para análise e decisão. Entra no **ETL** (extrair → transformar → carregar); com grande volume, a transformação não cabe no pandas (usar outra ferramenta).
- **Modelo cliente-servidor:** **cliente** = ponto de acesso do usuário (navegador/seu script); **servidor** = fornecedor de conteúdo. A requisição tem: **URL**, **método HTTP** (GET, POST…), cabeçalhos (headers) e retorna **status code** (200 OK, 404, 403, 500…).
- **Camadas da web:** **HTML** (estrutura das páginas), **CSS** (estilo), **JavaScript** (interatividade/conteúdo dinâmico). **DevTools** do navegador: inspecionar/depurar páginas e ver as requisições (URL, método, status).
- **Ferramentas Python:** **requests** (requisições HTTP), **BeautifulSoup** (analisa HTML e o transforma em objetos navegáveis: buscar por **tags, classes, IDs**; extrair títulos, links, tabelas; parser `lxml`/`html.parser`), **Selenium** (conteúdo dinâmico gerado por JavaScript, login/formulários). APIs JSON são alternativa melhor quando existem.

## 2. Prática e robustez
- "A web é um quarto bagunçado": páginas são desorganizadas e imprevisíveis → **tratamento de exceções** (`try/except`), `requests.get(url, headers=..., timeout=15)`, checar **`status_code`/`raise_for_status`**, usar **User-Agent**, **`time.sleep` entre requisições** (não sobrecarregar o servidor), **respeitar o `robots.txt`**.
- Exemplos do código: `BeautifulSoup(res.text, "lxml")`; `soup.find_all("article", class_="product_pod")`; `.find("p", class_="price_color")`; `.select("article.product_pod h3 a")`; `.get_text(strip=True)`.
- Dados extraídos viram dicionários/DataFrames (e depois ETL). Exemplo ilustrativo de validação: **CPF** — 8 primeiros dígitos aleatórios, 9º = região fiscal, 2 últimos = dígitos verificadores (cálculo sobre os 9 anteriores).

## 3. Aspectos legais e éticos
- **Ignorar padrões das organizações (robots.txt, termos de serviço) pode causar problemas** (bloqueios, ações judiciais).
- **LGPD não menciona explicitamente "scraping"**, mas o **art. 7º, §3º** diz que o tratamento de dados pessoais **de acesso público** deve considerar a **finalidade, a boa-fé e o interesse público** que justificaram sua disponibilização (dado público ≠ livre para qualquer uso).
- **Três critérios para avaliar a legalidade/ética (da aula):** **1) Consentimento** — Termos de Serviço (muitos sites proíbem scraping) e consentimento dos titulares; **2) Problemas físicos** — não prejudicar a capacidade do site de atender outros usuários (sobrecarga/DoS); **3) Intencionalidade** — a **real intenção do código/uso**: o que ele faz na prática.
- **Caso histórico (Pete Warden, 2010):** coletou dados públicos de ~**200 milhões de perfis do Facebook** (localizações, interesses) para visualização; os advogados do Facebook exigiram que **parasse e apagasse** os dados — mostra que dados "públicos" ainda têm restrições (consentimento, finalidade).

## Pergunta típica
O que faz um scraper e qual a diferença para crawler · papel de requests × BeautifulSoup × Selenium · o que são status codes e headers · por que usar `robots.txt`, `sleep` e `try/except` · o que a LGPD diz sobre dados públicos · os 3 critérios (consentimento, problemas físicos, intencionalidade).
