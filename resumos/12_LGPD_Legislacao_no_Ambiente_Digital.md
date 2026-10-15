# 12 · Legislação no Ambiente Digital (LGPD)
**Prof. Hélio Ferreira Moraes · 1 aula · Prioridade: ALTA (questões objetivas diretas; o conteúdo abaixo é cobrado)**

> **Em uma frase:** a LGPD diz que dados de pessoas físicas só podem ser tratados com **finalidade clara, base legal e o mínimo necessário**, respeitando os direitos do titular — e quem descumpre pode ser multado e ter a reputação atingida.

**Pré-requisitos:** nenhum. **Vem depois:** aplica-se a BI (03), engenharia (04), cloud (07) e NLP (25).

## Por que isso importa (intuição)
Dados pessoais viraram matéria-prima de negócios (marketing, crédito, IA). A lei existe para equilibrar **o interesse da empresa em usar dados** com **o direito da pessoa à privacidade**. A regra de bolso: *coletei só o necessário? Para uma finalidade informada? Tenho uma base legal? Protegi os dados?*

> Direito digital: *"o direito não é inimigo da tecnologia"*. Características: interdisciplinaridade, dinamismo, alcance global, proteção de direitos fundamentais e normas flexíveis (tecnologicamente neutras).

## 1. Marcos legais
- **GDPR (UE, 2018):** regras estritas; **alcance global** (afeta empresas fora da UE que tratam dados de europeus).
- **CCPA (Califórnia, 2020):** direito de saber o que é coletado e de pedir exclusão.
- **Marco Civil da Internet — Lei 12.965/2014:** neutralidade da rede, privacidade, liberdade de expressão (provedor só responde por conteúdo de terceiros após **ordem judicial**); guarda de registros: **conexão 1 ano; acesso a aplicações 6 meses**.
- **Marco Legal das Criptomoedas — Lei 14.478/2022:** regras para prestadoras de serviços de ativos virtuais.
- **LAI — Lei 12.527/2011:** transparência na administração pública (tensão com a LGPD: transparência × privacidade).
- **LGPD — Lei 13.709/2018:** protege **liberdade, privacidade e livre desenvolvimento da personalidade**; trata de dados de **pessoas naturais**, por qualquer pessoa ou empresa, **em qualquer meio**.

## 2. LGPD — conceitos
- **Dado pessoal:** qualquer informação relacionada a **pessoa natural identificada ou identificável**.
- **Dado pessoal sensível:** origem racial/étnica, convicção religiosa, opinião política, filiação sindical/religiosa/política, **saúde**, vida sexual, **dado genético ou biométrico**. Proteção reforçada, com bases legais diferentes. **CPF e dados financeiros NÃO são sensíveis** pela lei.
- **Agentes:** **Titular** (a pessoa dos dados) · **Controlador** (**decide** sobre o tratamento) · **Operador** (**trata em nome do controlador**) · **Encarregado/DPO** (canal com titulares e ANPD) · **ANPD** (autoridade que fiscaliza).
- **Tratamento:** toda operação com dados (coleta, acesso, armazenamento, compartilhamento, eliminação…).
- **Princípios:** **finalidade, adequação, necessidade** (usar o **mínimo**), livre acesso, qualidade, **transparência**, **segurança**, prevenção, não discriminação e **responsabilização**.
- **Bases legais:** consentimento · obrigação legal/regulatória · políticas públicas · estudos por órgão de pesquisa · **execução de contrato** · exercício regular de direitos · proteção da vida · tutela da saúde · **legítimo interesse** · proteção ao crédito. **Todo tratamento precisa de uma base, mas nem toda base é consentimento.**
- **Direitos do titular:** confirmação, **acesso**, correção, anonimização/bloqueio/eliminação, **portabilidade**, informação sobre compartilhamento, **revogação do consentimento**, oposição e **revisão de decisões automatizadas**.
- **Transferência internacional:** cláusulas-padrão contratuais, normas corporativas globais e cláusulas específicas (Resolução ANPD 19).
- **Sanções:** advertência · **multa simples de até 2% do faturamento, limitada a R$ 50 milhões por infração** · multa diária · publicização da infração · bloqueio/eliminação dos dados · suspensão do banco de dados (até 6 meses) ou da atividade de tratamento · proibição de atividades.

**Exemplo resolvido.** Uma loja coleta CPF, endereço e data de nascimento para emitir nota fiscal (**base: obrigação legal**) e, separadamente, pede o e-mail para enviar promoções (**base: consentimento**). Usar o endereço para criar um perfil de crédito sem avisar viola a **finalidade**. Pedir a religião do cliente "por curiosidade" viola a **necessidade** (e é dado sensível).

## 3. Segurança da informação
- **Tríade:** **confidencialidade, integridade, disponibilidade.** Incidente = evento que compromete uma delas.
- **Ataques:** **phishing**, **malware/ransomware** (sequestra dados e pede resgate), engenharia social, DDoS, força bruta, man-in-the-middle, SQL injection, XSS.
- **Ameaças internas:** enviar arquivos ao e-mail pessoal, compartilhar senhas, deixar o computador desbloqueado. **Segurança é responsabilidade de todos.**

## 4. LGPD na prática
- **Cadastro:** só o necessário; o **lead também é titular**. **Análise de dados:** conhecer a **origem** (evite "comprar base"), usar **só para a finalidade informada** e depois **anonimizar ou excluir**.
- **Marketing:** política de privacidade clara; consentimento **livre, informado e inequívoco** (**opt-in**, caixa desmarcada); informar cookies e pixels; cuidado com preço dinâmico discriminatório.
- **Privacy by Design/Default:** privacidade desde a concepção; minimização, anonimização, criptografia e **RIPD** (relatório de impacto).
- **Casos:** **Cambridge Analytica/Facebook** (87 milhões de usuários), **Clearview AI** (imagens faciais sem consentimento), ANPD × **Meta** (treino de IA), **World ID** (biometria da íris).

## Armadilhas e confusões comuns
| Confusão | O correto |
|---|---|
| Todo tratamento exige consentimento | **Falso**: há outras bases legais |
| CPF e dado bancário são sensíveis | **não** são sensíveis pela LGPD |
| Operador decide como tratar | quem decide é o **controlador**; o operador trata em nome dele |
| Dado público pode ser usado como quiser | continuam valendo finalidade, adequação e necessidade |
| Anonimizado = sempre fora da LGPD | só se for **irreversível**; senão ainda é dado pessoal |
| LGPD vale só para dados digitais | vale em **qualquer meio** |
| Multa de 2% do faturamento sem teto | limitada a **R$ 50 milhões por infração** |

## Resumo-relâmpago
- Dado pessoal = pessoa natural identificável; sensível = raça, religião, política, saúde, sexo, genético/biométrico.
- Controlador decide; operador executa; DPO é o canal; ANPD fiscaliza.
- Princípio da necessidade = mínimo. Bases legais ≠ só consentimento. Multa até 2% do faturamento (teto R$ 50 mi).

## Teste-se
1. Qual agente trata dados em nome de outro?
<details markdown="1"><summary>Ver resposta</summary>O operador (em nome do controlador).</details>

2. Todo tratamento de dados exige consentimento?
<details markdown="1"><summary>Ver resposta</summary>Falso. Exige uma base legal, e há dez além do consentimento (contrato, obrigação legal, legítimo interesse etc.).</details>

3. O que diz o princípio da necessidade?
<details markdown="1"><summary>Ver resposta</summary>Usar o mínimo de dados necessário para atingir a finalidade.</details>

4. Biometria e CPF são dados sensíveis?
<details markdown="1"><summary>Ver resposta</summary>Biometria sim; CPF não.</details>

5. Qual o limite da multa simples?
<details markdown="1"><summary>Ver resposta</summary>Até 2% do faturamento do último exercício, limitada a R$ 50 milhões por infração.</details>

## Pergunta típica
Qual agente trata dados em nome de outro · quem decide a forma e a duração do tratamento · princípios da LGPD · todo tratamento exige consentimento · quais são dados sensíveis · princípio da necessidade · o que é dado pessoal · sanções e limite da multa · direitos do titular
