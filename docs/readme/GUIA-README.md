# Guia de comunicação do README do SIA

Este guia diz **como falar** no README. Ele não muda o que o SIA faz. Os fatos (os passos, os comandos, as regras) continuam vindo das skills em `plugins/sia/skills/` e do `README.md` atual. Use este arquivo junto com o Claude para reescrever o README. O prompt pronto para isso está no fim.

O SIA faz parte do **Núcleo Pocket**, o formato de aulas do Núcleo da Sling para pessoas leigas em tecnologia que querem criar um sistema conversando com a IA. O README é a primeira coisa que o aluno abre depois da aula.

---

## 1. Quem lê

| Quem | O que sabe | O que precisa sair sabendo |
|---|---|---|
| Aluno do Núcleo Pocket | Usa computador e celular no trabalho. Nunca programou. Talvez nunca tenha aberto um terminal (a tela preta onde se digitam comandos) | O que é o SIA, se serve para ele, como instalar e o que escrever na primeira conversa |
| Quem recebeu o link de um aluno | Menos ainda. Não viu a aula | Entender em 10 segundos o que é e para quem é |
| Quem desenvolve | Sabe tudo isso | Onde estão as regras técnicas. Isso fica no fim, numa seção própria |

**Regra de ouro.** O README é escrito para o aluno. Tudo o que só interessa a quem desenvolve vai para o fim ou para `docs/harness.md`.

---

## 2. O que o README atual faz bem e o que atrapalha

**Mantenha:**

- A frase de apresentação do SIA ("Oi, eu sou o SIA..."). É a voz do produto.
- A lista "Como a conversa anda". É o coração do README.
- A tabela "O que a pessoa ouve". Ela vira a seção de palavras.
- Os créditos de "De onde veio". As licenças MIT pedem que a origem fique registrada.

**Mude:**

- O segundo e o terceiro parágrafos falam do que acontece por dentro (`AGENTS.md`, `CLAUDE.md`, ESLint, TypeScript, Drizzle, Vitest, Playwright). Para o aluno, isso é ruído antes de ele saber o que é o SIA. Esse conteúdo vai para a seção final "Para quem desenvolve".
- A instalação aparece no meio do texto e mostra três agentes de uma vez. O aluno não sabe qual escolher. Mostre um caminho principal e esconda os outros num bloco que abre com um clique.
- "Kimi e Qwen instalam o mesmo conteúdo" e "O que tem aqui" (a árvore de pastas) são para quem desenvolve. Vão para o fim.
- Falta dizer o que o aluno precisa ter antes de começar, o que digitar na primeira conversa e o que fazer quando algo dá errado.

---

## 3. Ordem das seções

Siga esta ordem. Cada seção diz qual imagem entra e onde.

### 3.1 Capa

- Imagem: `docs/readme/imagens/capa.png` no topo, largura total.
- Logo abaixo, uma frase do que é: um acompanhante que ajuda a criar um sistema conversando com a IA, mesmo sem saber programar.
- Uma segunda frase dizendo para quem é: para quem não programa e quer tirar uma ideia do papel, com a IA fazendo a parte técnica e você aprovando cada passo.

### 3.2 O que o SIA faz por você

Até 4 itens, cada um com um benefício que a pessoa sente. Tire do comportamento real das skills:

- Faz uma pergunta por vez, em português simples.
- Escreve o que ficou combinado antes de construir, para você ler e aprovar.
- Só diz que ficou pronto depois de testar.
- Quando algo quebra, procura a causa antes de mexer.

### 3.3 Antes de começar

Lista curta do que a pessoa precisa ter. Para cada item, uma linha do que é e onde consegue. Confirme os itens com o Matheus antes de publicar (veja a seção 9):

- O agente que a turma usa (o Claude Code, por exemplo), já instalado.
- Uma pasta vazia no computador para o sistema novo.
- Conta no Supabase e na Vercel só quando o SIA pedir. Diga que não precisa criar antes.
- Se tiver planilha, lista de preços, documento da empresa ou regra escrita que o sistema precisa respeitar, separe. Antes de escrever o combinado, o SIA pede para colocar esses arquivos na pasta `docs/contexto/` do projeto e lê tudo antes de escrever. Diga que esses arquivos ficam no computador e não vão para o GitHub.

### 3.4 Instalar

- Um caminho principal, o do agente que a turma usa. Os outros ficam num bloco recolhido (`<details><summary>Usa o Codex ou o Grok?</summary>`).
- Antes dos comandos, uma frase sobre onde colar: "Abra o terminal (o programa onde se digitam comandos) e cole uma linha de cada vez".
- **Um comando por bloco de código**, para o botão de copiar do GitHub copiar só aquele comando.
- Depois de cada comando, diga o que aparece quando dá certo.
- No fim: "Feche e abra uma sessão nova. Pronto, o SIA já está com você."

### 3.5 Sua primeira conversa

- Imagem: `docs/readme/imagens/conversa.gif`.
- Diga onde abrir a conversa (na pasta do sistema) e dê três pedidos de exemplo para a pessoa copiar e adaptar. Use exemplos de negócio, não de tecnologia: "Quero um sistema para minha clínica marcar consultas", "Quero um controle de estoque da minha loja que avisa quando um produto está acabando", "Quero um formulário para meus clientes pedirem orçamento".
- Diga o que esperar: o SIA se apresenta, repete o pedido numa frase e faz uma pergunta.

### 3.6 Como a conversa anda

- Imagem: `docs/readme/imagens/caminho.gif`.
- Abaixo do GIF, os 8 passos em lista numerada, com o nome do passo em negrito e uma frase cada. O texto precisa funcionar sem a imagem, porque o GIF não lê em voz alta e às vezes não carrega.
- Diga que o SIA abre cada mensagem com a etapa em que está ("Etapa: o combinado (PRD)"), e que três etapas trazem ao lado o nome visto nas aulas: PRD, Design System (DS) e TDD.
- Termine com a frase que segura tudo: só vira código depois que você viu e concordou.

### 3.7 Como o SIA prova que ficou pronto

- Imagem: `docs/readme/imagens/prova.gif`.
- Explique a prova e ligue com a aula (é o TDD): antes de construir cada parte, o SIA escreve um teste que confere se aquela parte funciona. No começo o teste falha, porque a parte ainda não existe. A parte só é dada como pronta quando o teste passa.
- Diga por que isso importa para quem não programa: você não precisa confiar na palavra da IA, porque o teste mostra.

### 3.8 Palavras que você vai ouvir

- Imagem: `docs/readme/imagens/dicionario.png`.
- Logo abaixo, a mesma tabela em texto (Na conversa, O que acontece, Nome técnico). A imagem chama a atenção e o texto pode ser lido, copiado e buscado.

### 3.9 Quando algo der errado

- "Apertei salvar e sumiu": descreva o que aconteceu com as suas palavras. O SIA investiga a causa antes de mexer.
- Conversa fechada no meio: abra de novo na mesma pasta. O SIA lê o que já foi combinado e continua de onde parou, sem repetir as perguntas.
- Erro na instalação: diga o que conferir primeiro e onde pedir ajuda (canal do Núcleo Pocket, a confirmar).

### 3.10 Perguntas comuns

Só responda o que é fato. Pergunta sem resposta confirmada fica fora até o Matheus responder.

- Preciso saber programar? Não. Você aprova os passos e o SIA faz a parte técnica.
- Funciona num sistema que eu já tenho? Sim. O SIA lê o que já existe e segue as ferramentas que estão lá.
- Onde ficam meus dados? Na base que você escolher. O SIA sugere o Supabase e só usa com o seu sim.
- Quanto custa? A confirmar (o custo é do agente e das contas, não do SIA, que é gratuito e de código aberto).

### 3.11 Para quem desenvolve

Aqui entra tudo o que saiu do começo: os arquivos que o SIA escreve (`docs/sia/`, `AGENTS.md`, `CLAUDE.md`), a base sugerida (Next.js, TypeScript, Tailwind, Vitest, Playwright, Supabase ou Postgres com Drizzle), os agentes suportados com Kimi e Qwen, a árvore de pastas, o link para `docs/harness.md` e os créditos de "De onde veio", completos.

---

## 4. Tom e voz

O tom é o do Núcleo da Sling: claro, calmo e honesto, sem euforia. O aluno é leigo em tecnologia, mas é adulto e competente no próprio negócio. Explique sem tratar como criança.

- **Fale com "você".** O SIA fala em primeira pessoa só dentro de citações.
- **Frases curtas.** Uma ideia por frase. Parágrafo de até 3 linhas.
- **Verbo de ação no começo das instruções:** "Abra", "Cole", "Escreva".
- **Termo técnico explicado na primeira vez.** Formato: termo (o que é, numa linha). Exemplo: "terminal (o programa onde se digitam comandos)". Depois, use só o termo.
- **Use o vocabulário do SIA:** o combinado, a cara, a prova, a ligação, colocar no ar, cada um só vê o que é seu.
- **Os nomes das aulas andam junto.** PRD, Design System (DS) e TDD aparecem entre parênteses ao lado do nome da etapa, igual ao que o SIA faz na conversa: o combinado (PRD), a cara (DS), a prova (TDD). Os outros nomes técnicos (RLS, deploy, MCP) ficam só na tabela de palavras e na seção para quem desenvolve.
- **Honestidade sobre esforço.** Não prometa "em minutos" nem "sem esforço". Diga o que a pessoa vai fazer: ler, responder e aprovar.
- **Educação primeiro.** O README ensina e acompanha. Não vende consultoria nem serviço. No máximo, uma linha no fim dizendo que o SIA faz parte do Núcleo Pocket da Sling.

### Proibido no texto

- Travessão e ponto e vírgula. Use ponto ou vírgula com conectivo.
- Emoji decorativo em título, lista ou tabela.
- Antítese no molde "X, não Y". Escreva a frase direta.
- Pergunta retórica ("Cansado de...?"). Pergunta só em perguntas comuns, que são de verdade.
- Clichê de IA e de marketing: "revolucionário", "mágica", "o futuro chegou", "potencialize", "desbloqueie", "jornada", "game changer", "simples assim".
- Promessa que o SIA não cumpre sozinho: sistema "pronto para vender", "sem bugs", "seguro" sem explicar como.
- Nome de skill (`comecar`, `entender`, `combinar`...) fora da seção para quem desenvolve.

### Antes e depois

| Antes (atual) | Depois (para o aluno) |
|---|---|
| "Por baixo dessa conversa o agente não improvisa o processo." | "O SIA segue sempre a mesma ordem, então você sabe o que vem a seguir." |
| "Se a base tiver ESLint e TypeScript, a conferência também roda o lint e a checagem de tipo." | (vai para "Para quem desenvolve") |
| "Supabase é a sugestão para guardar contas e dados. Postgres com Drizzle é a segunda, na mesma frase." | "Para guardar os dados do sistema, o SIA sugere o Supabase (um serviço que guarda as informações e os logins). Ele só usa com o seu sim." |
| "Publicação entra quando o sistema precisa ficar acessível." | "Se você quiser que outras pessoas usem o sistema, o SIA coloca no ar e te manda o link para testar antes." |

---

## 5. Imagens e GIFs

Todas seguem a identidade nova da Sling: fundo branco, verde `#01CB8B`, letra Urbanist e ondas só na capa.

| Arquivo | Onde entra | Texto alternativo (alt) |
|---|---|---|
| `imagens/capa.png` | 3.1 Capa | SIA, do pedido ao sistema pronto. Crie um sistema conversando com a IA, mesmo sem saber programar |
| `imagens/conversa.gif` | 3.5 Primeira conversa | Exemplo de conversa: a pessoa pede um sistema para a clínica, o SIA se apresenta, repete o pedido e faz uma pergunta, depois escreve o combinado |
| `imagens/caminho.gif` | 3.6 Como a conversa anda | Os oito passos da conversa acendendo um por vez, do Oi até colocar no ar, com PRD no combinado, DS na cara e TDD na prova |
| `imagens/caminho.png` | Versão parada do caminho, para slide ou PDF da aula | Os oito passos da conversa com o SIA |
| `imagens/prova.gif` | 3.7 A prova | Três partes de um sistema de exemplo. Cada teste falha primeiro, a parte é construída e o teste passa |
| `imagens/dicionario.png` | 3.8 Palavras | Tabela com as palavras da conversa, o que cada uma quer dizer e o nome técnico |

**Regras:**

- O caminho no README é relativo à raiz: `![alt](docs/readme/imagens/capa.png)`.
- Imagem complementa, não substitui. Todo conteúdo de imagem também existe em texto logo abaixo dela.
- No máximo uma imagem por seção. O README não vira galeria.
- Para trocar um texto de imagem, edite o HTML em `docs/readme/fontes/` e gere de novo:

```bash
NODE_PATH=<pasta node_modules com o playwright> node docs/readme/fontes/render.js
```

O script precisa do Playwright e do ffmpeg. Sem nome, ele gera tudo. Com nome (`render.js conversa`), gera só aquela peça.

---

## 6. Comandos e blocos de código

- Um comando por bloco. Nada de dois comandos no mesmo bloco.
- Nada de `$` ou `>` no começo do comando. O aluno copia e o símbolo quebra o comando.
- Antes do bloco, onde colar. Depois do bloco, o que aparece quando dá certo.
- Caminho e nome de arquivo sempre em `código`. Nome de passo da conversa sempre em **negrito**.

---

## 7. Formatação

- Títulos de seção curtos e em frase direta ("Sua primeira conversa", "Quando algo der errado").
- Lista numerada só para o que tem ordem (instalar, os 8 passos). O resto é lista com marcador.
- Tabela só para comparar (palavras e o que querem dizer). Nada de tabela com uma coluna.
- Bloco recolhido (`<details>`) para o que só parte do público precisa: outros agentes, detalhes de erro.
- Comprimento: quem lê até "Sua primeira conversa" tem de conseguir começar. Essa parte cabe em duas rolagens de tela.

---

## 8. Conferência antes de publicar

- [ ] Quem nunca programou entende, em 10 segundos, o que é o SIA e para quem é
- [ ] A instalação tem um caminho principal e um comando por bloco
- [ ] Todo termo técnico tem a explicação na primeira vez
- [ ] Nenhum nome de skill e nenhuma ferramenta técnica antes de "Para quem desenvolve"
- [ ] Toda imagem tem alt descritivo e o mesmo conteúdo em texto
- [ ] Zero travessão, zero ponto e vírgula, zero emoji decorativo
- [ ] Nenhuma promessa que as skills não sustentam
- [ ] Os créditos de "De onde veio" estão completos, com as licenças
- [ ] Os comandos de instalação são os mesmos do README atual e de `docs/install/`
- [ ] Os links e as imagens abrem no GitHub (confira no preview do GitHub, não só no editor)

---

## 9. Pendências para confirmar antes de publicar

Estas respostas não estão no repositório. Não invente: pergunte ao Matheus.

1. Qual agente a turma do Núcleo Pocket usa (Claude Code, Codex ou Grok)? Ele vira o caminho principal da instalação.
2. O que o aluno precisa ter antes (conta paga do agente, qual plano)?
3. Onde o aluno pede ajuda quando trava (grupo, plantão, e-mail)?
4. A logo da Sling fica nas imagens? O repositório é `matt11seven/sia`, conta pessoal.
5. Existe link da aula ou da página do Núcleo Pocket para colocar no fim?

---

## 10. Prompt para gerar o README com o Claude

Abra o Claude na pasta do SIA e cole:

```text
Reescreva o README.md do SIA seguindo docs/readme/GUIA-README.md.

Regras:
1. Leia o guia inteiro, o README.md atual, docs/install/ e a skill plugins/sia/skills/comecar/SKILL.md antes de escrever.
2. Mude só a comunicação. Os fatos, os comandos e os passos vêm do README atual e das skills. Não invente recurso, preço nem prazo.
3. Siga a ordem das seções do guia (seção 3) e use as imagens de docs/readme/imagens/ nos lugares indicados, com o alt da seção 5.
4. Respostas da seção 9 que eu não der ficam como "a confirmar" num comentário HTML (<!-- -->), fora do texto visível.
5. Antes de me entregar, rode a conferência da seção 8 e me diga o resultado item por item.

Respostas da seção 9:
- Agente da turma: <preencher>
- O que precisa ter antes: <preencher>
- Onde pedir ajuda: <preencher>
- Logo da Sling nas imagens: <sim ou não>
- Link do Núcleo Pocket: <preencher ou "sem link">
```
