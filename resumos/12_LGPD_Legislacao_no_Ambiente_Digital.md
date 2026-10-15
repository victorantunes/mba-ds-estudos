# 12 · Legislação no Ambiente Digital (LGPD)
**Prof. Hélio Ferreira Moraes · 1 aula · Prioridade: ALTA (questões de múltipla escolha diretas; tudo abaixo cai)**

> Direito Digital: "o direito não é inimigo da tecnologia; é condição para seu florescimento sustentável". Características: **interdisciplinaridade, dinamismo, globalidade/transnacionalidade, proteção de direitos fundamentais, flexibilidade normativa** (princípios gerais; abordagem "tecnologicamente neutra").

## 1. Marcos legais
| Norma | Pontos-chave |
|---|---|
| **GDPR (UE, 2018)** | regras estritas de tratamento de dados; alcance **global** (afeta empresas fora da UE que tratam dados de cidadãos da UE) |
| **CCPA (Califórnia, 2020)** | direito de saber quais dados são coletados e de pedir exclusão |
| **DMCA (EUA, 1998)** | direitos autorais digitais |
| **Marco Civil da Internet — Lei 12.965/2014** ("Constituição da Internet") | **neutralidade da rede**; privacidade e proteção de dados; **liberdade de expressão** (responsabilidade pelo conteúdo é do usuário; provedor de aplicação só responde após **ordem judicial**, exceto em casos específicos); **guarda de registros: conexão 1 ano; acesso a aplicações 6 meses**; provedores de conexão não respondem por conteúdo de terceiros |
| **Marco Legal das Criptomoedas — Lei 14.478/2022** | regras para prestadoras de serviços de ativos virtuais; **não regula** reais/ativos vinculados a moedas estrangeiras, pontos e fidelidade; CVM Parecer 40 (cripto como valor mobiliário); IN RFB 1888/2019 (declaração de operações) |
| **LAI — Lei de Acesso à Informação 12.527/2011** | transparência na Administração Pública (combate à corrupção); **conflito LAI × LGPD** (ex.: divulgar remuneração de servidores): equilibrar transparência × privacidade |
| **LGPD — Lei 13.709/2018** | protege **direitos fundamentais de liberdade, privacidade e livre desenvolvimento da personalidade**; trata de **dados de pessoas naturais (físicas)**, por pessoa física ou jurídica, pública ou privada, **em qualquer meio (digital inclusive)** |

## 2. LGPD — conceitos
- **Dado pessoal:** **qualquer informação relacionada a pessoa natural identificada ou identificável** (não é só nome/endereço/CPF, nem só intimidade, nem dados da empresa).
- **Dado pessoal sensível:** origem racial/étnica, **convicção religiosa**, opinião política, filiação a sindicato/organização religiosa/filosófica/política, **saúde**, vida sexual/orientação sexual, **dado genético ou biométrico**. Têm **proteção reforçada** (risco de discriminação) e **bases legais diferentes** (não pode usar **legítimo interesse** nem **proteção ao crédito** nem execução de contrato). **Dados financeiros e CPF NÃO são "sensíveis"** pela lei (mas a ANPD os trata com rigor).
- **Titular** (pessoa natural a quem os dados se referem) · **Controlador** (decide sobre o tratamento) · **Operador** (**trata em nome do controlador**) · **Suboperador** (contratado pelo operador, sempre em nome do controlador) · **Encarregado (DPO)** (canal entre controlador, titulares e ANPD) · **ANPD** (zela, implementa e fiscaliza a LGPD; autarquia independente, elevada a "agência").
- **Tratamento:** toda operação (coleta, classificação, acesso, armazenamento, etc.).
- **Princípios:** **finalidade, adequação, necessidade** (usar o **mínimo** para atingir a finalidade), livre acesso, **qualidade dos dados**, **transparência**, **segurança**, **prevenção**, **não discriminação** e **responsabilização/prestação de contas**.
- **Bases legais (10 + as dos dados sensíveis)** — *todo tratamento precisa de uma base, **mas nem toda base é consentimento***: consentimento · cumprimento de obrigação legal/regulatória · execução de políticas públicas · estudos por órgão de pesquisa · **execução de contrato** · exercício regular de direitos · proteção da vida · tutela da saúde · **legítimo interesse** · proteção ao crédito (e prevenção à fraude nos sensíveis). *Afirmação "todo tratamento exige consentimento" = FALSA.*
- **Direitos do titular:** confirmação do tratamento, **acesso**, correção, **anonimização/bloqueio/eliminação**, **portabilidade**, informação sobre compartilhamento, negativa e **revogação do consentimento**, oposição, **revisão de decisões automatizadas** e informações sobre seus critérios (preservado o segredo de negócio).
- **Transferência internacional (Resolução ANPD nº 19):** mecanismos: **cláusulas-padrão contratuais** (anexo II da resolução; já aprovadas, mais rápidas, não alteráveis), **normas corporativas globais** (empresas do mesmo grupo, precisam de aprovação da ANPD) e **cláusulas contratuais específicas** (aprovação da ANPD; processo demorado).
- **Sanções administrativas:** advertência (com prazo p/ correção) · **multa simples** de **até 2% do faturamento** da empresa/grupo no Brasil no último exercício, **limitada a R$ 50 milhões por infração** · multa diária · **publicização da infração** · bloqueio e eliminação dos dados · suspensão parcial do funcionamento do banco de dados (até 6 meses, prorrogável) · suspensão do exercício da atividade de tratamento · proibição parcial/total de atividades. Impactos: financeiros e **reputacionais**.

## 3. Segurança da informação
- **Tríade:** **confidencialidade, integridade, disponibilidade**. **Incidente de segurança:** qualquer evento que comprometa essas propriedades (acesso indevido, alteração, destruição).
- **Ataques:** **phishing** (engano por e-mail/sites falsos), **malware** (vírus, **ransomware** = sequestra/criptografa dados e exige resgate, spyware, trojan), **engenharia social**, **DDoS**, **brute force**, exploração de vulnerabilidades, **man-in-the-middle** (risco em Wi-Fi público), **SQL injection**, **XSS**.
- **Ameaças internas (falha humana):** enviar arquivos para e-mail pessoal, compartilhar senhas, usar apps não oficiais, deixar computador desbloqueado, documentos soltos. **Segurança é responsabilidade de todos.** Casos: STJ responsabilizou a **Enel** por vazamento mesmo com ataque de terceiros (não adotou medidas de segurança); funcionário demitido por justa causa por acessar contas indevidamente.

## 4. LGPD na prática (negócio, dados e marketing)
- **Cadastro:** reduzir ao **necessário**; regras de acesso; manter dados corretos e atualizados. **Lead também é titular**: informar finalidade, identificar-se e origem dos dados; ele pode mudar de ideia.
- **Análise de dados:** entender a **origem** (evitar "compra de base"); coletar só o necessário; usar **somente para a finalidade informada** e depois **anonimizar ou excluir**; cuidado com dados públicos (ainda valem finalidade, adequação e necessidade); **segmentação com dados sensíveis** exige justificativa; **clearance** de base antiga; **segregar dados sensíveis**; **"jardim murado"** (rastrear dados sensíveis no pipeline).
- **Marketing digital:** política de privacidade clara; consentimento **livre, informado e inequívoco**; **opt-in** (caixa desmarcada); informar **cookies/pixels/web beacons** (remarketing); cuidado com **preço dinâmico** discriminatório; parceiros também em conformidade; tecnologias de identificação (reconhecimento facial, biometria) elevam a exigência de **RIPD (relatório de impacto)**.
- **Privacy by Design / by Default:** conceber o projeto já com privacidade; **minimização**, pseudonimização/anonimização, criptografia, gestão de acessos, **DPIA/RIPD**.
- **Casos reais:** **Cambridge Analytica / Facebook** (87 mi de usuários; motivou GDPR/LGPD); **Clearview AI** (20 bi de imagens faciais sem consentimento; multada na Europa); **Meta** (ANPD suspendeu uso de dados para treinar IA generativa até haver transparência); **Tools for Humanity/World ID** (compra de biometria da íris, proibida pela ANPD); **TikTok** (dados de menores). Vazamentos: fraude financeira, roubo de identidade, danos morais.

## Quiz da aula (com gabarito)
1. *Qual agente trata dados em nome e sob orientação de outro?* → **Operador**.
2. *Quem decide sobre forma e duração do tratamento?* → **Controlador**.
3. *Princípios da LGPD:* → **finalidade, necessidade, transparência, segurança…** (não "consensualismo", "moralidade administrativa").
4. *Todo tratamento exige consentimento?* → **Falso** (há outras bases).
5. *Dados sensíveis são:* → **dados biométricos, origem racial…** (não CPF/cartão/extrato).
6. *Princípio da necessidade:* → **utilizar o mínimo necessário** para atingir a finalidade.
7. *Dado pessoal é:* → **qualquer informação relativa a pessoa física identificada ou identificável**.
