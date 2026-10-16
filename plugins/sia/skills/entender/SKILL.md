---
name: entender
description: >
  Use antes de qualquer trabalho de criação de sistema: feature, comportamento,
  "quero um sistema", "vamos fazer", "planejar", "dá para?". Classifica
  experimento, mudança pequena ou coisa nova, e não deixa código de produto
  começar sem o sim da etapa certa. Use when starting new system work,
  before writing code.
---

> Adaptado de obra/superpowers, skill `brainstorming`, commit `8ca22dba`, licença MIT. Três caminhos, porta dura e uma pergunta por vez foram mantidos. As perguntas são de sistema.

# Entender

Com a pessoa, siga "Como falar" em `comecar`. Se esta for a primeira resposta da conversa, a apresentação do SIA vem antes de qualquer classificação, sem linha de etapa. Da segunda mensagem em diante, abra com **Etapa: quem usa**. Não diga o nome desta skill.

## A lei

Nenhuma ação de implementação antes da porta do caminho escolhido. Isso inclui invocar skill de construção, escrever código de produto, criar projeto, instalar dependência do produto ou abrir projeto na Supabase ou na Vercel.

Ler o que já existe é permitido. Se o repositório já tem código, invoque `mapa` antes de vasculhar quem chama quem. Pasta vazia não leva mapa.

Um sim aprova só o que foi mostrado. Sim para a ideia não aprova um papel que ainda não existe. Conversa nova com arquivo em `docs/sia/` retoma pela abertura de `comecar`.

## Três caminhos

Diga o caminho em linguagem de conversa, antes da primeira pergunta, para a pessoa poder corrigir. "Como isso ainda não existe, a gente combina tudo antes de eu construir." "Isso já está no sistema, então é uma mudança pequena." "Você quer saber se dá, então eu testo e jogo fora." Não diga "caminho", "spike" nem o nome da skill.

- **Experimento.** "Dá para…?", "é possível?", "pode ser jogado fora". A saída é uma resposta, não código para guardar. Mostre a pergunta e o que vai tentar em 2 ou 3 frases, espere um sim, investigue pelo caminho mais barato que ainda seja correto. Sem documento. O que for construído fica marcado como descartável.
- **Mudança pequena.** O fluxo já está neste repositório e dá para ler. Uma flag, um filtro, um conserto pontual. Familiaridade com o tipo de sistema não torna a tarefa pequena. Se não há fluxo para ler, não é mudança pequena. Perguntas que importam, depois a forma curta de `combinar`. A pessoa lê o arquivo. Implementar só depois do sim desse arquivo. Sem plano longo. Aprovação no chat, sem o arquivo, não conta.
- **Coisa nova.** Projeto vazio, ou um pedaço novo que muda como as partes se encaixam. Perguntas, duas ou três abordagens, combinado escrito, plano. Um sistema novo é coisa nova, com ou sem tela.

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
3. Invocar `combinar` na forma curta: o que muda, o que isso toca, uma prova.
4. Parar até um sim sobre `docs/sia/combinado.md`.
5. Se a mudança mexe no que alguém vê, ou `docs/sia/visual.md` não existe, `visual` vem antes do código. Se a cara já está escrita e a mudança não mexe nela, siga.
6. Aí sim, suba a escada de `fazer` e invoque `testar-primeiro`. Sem documento de plano. A escada não dispensa a prova.

**Coisa nova**

1. Olhar o que já existe.
2. Se o pedido mistura pedaços independentes (chat, pagamento, estoque, aplicativo), dizer isso na hora e fatiar. O combinado desta rodada é só o primeiro pedaço. O resto entra em "não vamos fazer agora".
3. Uma pergunta por vez: quem usa, o que essa pessoa faz, o que é "deu certo". Dos pedaços, o primeiro é o menor que já entrega esse "deu certo", inteiro e verdadeiro. Entrar, quem vê o quê e a regra que ele precisa entram nesta rodada. O resto fica em "não vamos fazer agora".
4. Duas ou três abordagens, com troca e uma recomendação na frente.
5. Mostrar o desenho em pedaços curtos e perguntar se aquele pedaço está certo.
6. Invocar `escolher` se `docs/sia/escolhas.md` ainda não existir.
7. Invocar `combinar` e parar até a pessoa ler o arquivo.

## Perguntas

Quando faltar, pergunte nesta ordem, uma por mensagem:

1. Quem vai usar, e o que essa pessoa, ou esse outro sistema, precisa conseguir fazer?
2. Como você sabe que deu certo?
3. O que fica para depois, de propósito?

Não pergunte de tela, banco ou onde vai rodar enquanto essas três não estiverem respondidas. Tela só entra se alguém for olhar. Banco e endereço são `escolher`.



## Bandeiras vermelhas

| O que você pensou | O que é verdade |
| --- | --- |
| "Simples demais para desenho" | Mudança pequena ganha a forma curta do combinado. Coisa nova ganha o arquivo inteiro. |
| "Chamo de pequena para pular o arquivo" | A forma curta também é arquivo. Pular esse arquivo sobe o caminho. |
| "O desenho é óbvio, começo enquanto leem" | A porta é o sim, não o tamanho do texto. |
| "Eu conheço esse tipo de sistema, então é pequeno" | Pequeno mede o repositório. Projeto vazio é coisa nova. |
| "O experimento funcionou, fico com o código" | Ficar com o código é outro pedido. Classifique de novo. |
| "Cresceu, mas já estou no fim" | Pare e suba o caminho. |

## Desculpas

| Desculpa | Resposta |
| --- | --- |
| "A pessoa já disse que pode fazer" | Pode fazer a etapa mostrada. A próxima ainda não existe. |
| "Vou criando o projeto enquanto conversamos" | Criar projeto é implementação. A porta ainda não abriu. |
