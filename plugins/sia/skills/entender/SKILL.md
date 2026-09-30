---
name: entender
description: >
  Use antes de qualquer trabalho de criação em site ou sistema web: feature,
  tela, comportamento, "quero um site", "vamos fazer", "dá para?". Classifica
  experimento, mudança pequena ou coisa nova, e não deixa código de produto
  começar sem o sim da etapa certa. Use when starting creative web work,
  before writing code.
---

> Adaptado de obra/superpowers, skill `brainstorming`, commit `8ca22dba`, licença MIT. Três caminhos, porta dura e uma pergunta por vez foram mantidos. As perguntas são de site.

# Entender

Com a pessoa, siga "Como falar" em `comecar`. Se esta for a primeira resposta da conversa, a apresentação do SIA vem antes de qualquer classificação. Não diga o nome desta skill.

## A lei

Nenhuma ação de implementação antes da porta do caminho escolhido. Isso inclui invocar skill de construção, escrever código de produto, criar projeto, instalar dependência do produto ou abrir projeto na Supabase ou na Vercel.

Ler o que já existe é permitido.

Um sim aprova só o que foi mostrado. Sim para a ideia não aprova um papel que ainda não existe. Retome na etapa mais cedo que estiver incompleta.

## Três caminhos

Diga o caminho em linguagem de conversa, antes da primeira pergunta, para a pessoa poder corrigir. "Como isso ainda não existe, a gente combina tudo antes de eu construir." "Isso já está no site, então é uma mudança pequena." "Você quer saber se dá, então eu testo e jogo fora." Não diga "caminho", "spike" nem o nome da skill.

- **Experimento.** "Dá para…?", "é possível?", "pode ser jogado fora". A saída é uma resposta, não código para guardar. Mostre a pergunta e o que vai tentar em 2 ou 3 frases, espere um sim, investigue pelo caminho mais barato que ainda seja correto. Sem documento. O que for construído fica marcado como descartável.
- **Mudança pequena.** O fluxo já está neste repositório e dá para ler. Uma flag, um filtro, um conserto de uma tela. Familiaridade com o tipo de site não torna a tarefa pequena. Se não há fluxo para ler, não é mudança pequena. Perguntas que importam, desenho curto no chat (abordagem, arquivos, como provar), e pare. Implementar só depois de um sim explícito. Sem plano longo.
- **Coisa nova.** Projeto vazio, ou um pedaço novo que muda como as partes se encaixam. Perguntas, duas ou três abordagens, combinado escrito, plano. Um site novo é coisa nova.

Na dúvida, o caminho mais pesado. No meio do trabalho, complexidade escondida sobe o caminho. Nada desce.

## Listas

**Experimento**

1. Olhar o contexto o suficiente para formular a prova.
2. Mostrar pergunta e prova em 2 ou 3 frases.
3. Esperar o sim.
4. Investigar.
5. Trazer a recomendação. O que foi construído é descartável.

**Mudança pequena**

1. Olhar arquivos, docs e commits recentes.
2. Uma pergunta por vez, só as que mudam o desenho.
3. Desenho curto no chat: abordagem, arquivos, como provar.
4. Parar até um sim explícito.
5. Aí sim, `testar-primeiro` e construir. Sem documento de plano.

**Coisa nova**

1. Olhar o que já existe.
2. Se o pedido mistura pedaços independentes (chat, pagamento, estoque, aplicativo), dizer isso na hora e fatiar. O combinado desta rodada é só o primeiro pedaço. O resto entra em "não vamos fazer agora".
3. Uma pergunta por vez: quem usa, o que essa pessoa faz, o que é "deu certo".
4. Duas ou três abordagens, com troca e uma recomendação na frente.
5. Mostrar o desenho em pedaços curtos e perguntar se aquele pedaço está certo.
6. Invocar `escolher` se `docs/sia/escolhas.md` ainda não existir.
7. Invocar `combinar` e parar até a pessoa ler o arquivo.

## Perguntas de site

Quando faltar, pergunte nesta ordem, uma por mensagem:

1. Quem abre esse site, e o que essa pessoa precisa conseguir fazer?
2. Como você sabe que deu certo?
3. O que fica para depois, de propósito?

Não pergunte stack, banco ou hospedagem aqui. Isso é `escolher`, e só no caminho de coisa nova, ou quando a mudança pequena não tem como seguir o que já está no repositório.

## Bandeiras vermelhas

| O que você pensou | O que é verdade |
| --- | --- |
| "Simples demais para desenho" | Mudança pequena ganha um desenho curto. Coisa nova ganha combinado. |
| "Chamo de pequena para pular o arquivo" | Essa vontade é o sinal de subir o caminho. |
| "O desenho é óbvio, começo enquanto leem" | A porta é o sim, não o tamanho do texto. |
| "Eu conheço esse tipo de site, então é pequeno" | Pequeno mede o repositório. Projeto vazio é coisa nova. |
| "O experimento funcionou, fico com o código" | Ficar com o código é outro pedido. Classifique de novo. |
| "Cresceu, mas já estou no fim" | Pare e suba o caminho. |

## Desculpas

| Desculpa | Resposta |
| --- | --- |
| "A pessoa já disse que pode fazer" | Pode fazer a etapa mostrada. A próxima ainda não existe. |
| "Vou criando o projeto enquanto conversamos" | Criar projeto é implementação. A porta ainda não abriu. |
