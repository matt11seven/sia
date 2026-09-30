---
name: combinar
description: >
  Use para escrever o combinado de um site ou sistema web depois que entender
  fechou o desenho, e antes de visual, plano ou código. Cobre coisa nova
  (arquivo inteiro) e mudança pequena (meia página). Gatilhos: "escreve o que
  ficou acertado", "o combinado", "PRD", "requirements", "spec". A pessoa lê
  o arquivo antes de qualquer construção.
---

> Adaptado de obra/superpowers, skill `brainstorming`, commit `8ca22dba`, licença MIT, na parte do documento, da revisão própria e da leitura pela pessoa. O arquivo é o PRD, em linguagem de quem usa o site.

# Combinar

Com a pessoa, siga "Como falar" em `comecar`. Não diga o nome desta skill. Uma frase de onde estamos, depois a pergunta ou o que há para olhar.

## A lei

Sem `docs/sia/combinado.md` aprovado, não existe visual, plano nem código de produto. Aprovação no chat, sem o arquivo, não conta. No caminho de mudança pequena o arquivo pode ser curto, e a porta é a mesma.

## Forma cheia

Para coisa nova. Escreva as seções abaixo, nesta ordem, em frases que a pessoa lê sem traduzir.

1. **Quem usa e o que precisa fazer.**
2. **Deu certo quando.** Uma frase observável.
3. **Não vamos fazer agora.** O que foi fatiado para depois.
4. **Páginas.** O que a pessoa vê em cada uma.
5. **O que fica guardado, e quem vê.** Cada informação, quem cria, quem lê, quem apaga. "Cada um só vê o que é seu" quando for o caso.
6. **Estados.** Vazio, carregando, erro, sem permissão, deu certo.
7. **Provas.** Cada linha vira teste. Exemplo: "A Marina não vê o horário da Ana."
8. **Escolhas.** Aponte `docs/sia/escolhas.md`. Se o arquivo não existir, invoque `escolher` e volte.

Salve em `docs/sia/combinado.md`.

## Forma curta

Para mudança pequena. Uma seção "Mudança" no mesmo arquivo, ou um arquivo novo se o combinado ainda não existir, com: o que muda, as páginas tocadas, uma prova. A pessoa lê mesmo assim.

## Revisão própria

Depois de escrever, olhe de novo:

1. Buraco: "TBD", "depois vemos", seção vazia. Preencha ou corte.
2. Contradição entre seções.
3. Cabe numa rodada só, ou precisa fatiar de novo.
4. Frase com duas leituras. Escolha uma e escreva essa.

Corrija no arquivo. Não peça para a pessoa achar o buraco.

## Porta

Diga o caminho do arquivo e pare. A próxima frase pede que a pessoa leia e diga se quer mudar algo antes da cara das telas e da lista de partes.

Se pedir mudança, edite e repasse a revisão própria. Só um sim sobre este arquivo libera `visual` (se houver tela) ou `planejar` (se não houver).

## Desculpas

| Desculpa | Resposta |
| --- | --- |
| "Já conversamos, o arquivo é formalidade" | O arquivo é o que a próxima skill lê. A conversa não viaja. |
| "Coloco TBD na prova e sigo" | Prova vaga não vira teste. Feche ou corte. |
| "A pessoa aprovou a ideia ontem" | Ontem não leu este arquivo. |
