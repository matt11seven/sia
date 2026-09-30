---
name: fazer
description: >
  Use para construir um site a partir de um plano já aprovado, na sessão
  atual, parte por parte. Gatilhos: "pode fazer", "segue a lista", "parte
  por parte", "implementa o plano". Cada parte passa por testar-primeiro e
  para quando a prova passa. Use when executing an approved web
  implementation plan inline.
---

> Adaptado de obra/superpowers, skill `executing-plans`, commit `8ca22dba`, licença MIT, e de juliusbrussee/caveman, skill `lean-build`, commit `2fd153c6`, licença MIT. O plano manda, a prova é por parte, o andamento fica em arquivo, e se para quando o aceite passa. Sem os scripts de worktree do original: o andamento é `docs/sia/andamento.md`.

# Fazer

Com a pessoa, siga "Como falar" em `comecar`. Não diga o nome desta skill. Uma frase de onde estamos, depois a pergunta ou o que há para olhar.

## A lei

O plano já pensou. Execute os passos na ordem, prove cada um, e deixe registro que sobrevive quando a conversa for compactada.

Sem modo, configuração ou peça extra que o aceite não pediu. Sem superfície nova que o combinado não pediu. Entregue o caminho inteiro daquela parte (tela, regra, dado), não um arquivo isolado que não fecha.

Invoque `testar-primeiro` antes da parte 1. Os passos do plano não dispensam essa leitura.

## Quando parar e perguntar

Só nestes casos: ação irreversível ou destrutiva; segredo ou permissão; efeito fora do repositório (merge, push, publicar); plano tão quebrado que todo caminho é chute. Fora isso, decida, anote e siga.

"Parte por parte", escolhido em `planejar`, acrescenta uma parada: ao fim de cada parte que a pessoa pode olhar, mostre e espere. "A lista inteira" não pergunta "continuo?" entre partes.

## Andamento

`docs/sia/andamento.md`. A primeira linha é o caminho do plano. Parte com a linha `Parte N: pronta` não se refaz. Confie nesse arquivo e no git, não na memória, depois de uma compactação.

Anote também `Decisão: <o que> — <por quê> — <o que custa se estiver errado>` quando o plano e o combinado não fecharem. Desviar do plano sem essa linha é decisão escondida.

Conflito entre partes: o combinado ganha. Anote a decisão e siga.

## O ciclo de cada parte

1. Leia a parte no plano, inclusive se você acha que lembra. Marque em andamento.
2. Siga os passos. Prova primeiro. Rode o comando. Compare com a linha "Esperado".
   - Bateu: próximo passo.
   - O código está errado: `investigar`. Não remende o sintoma para a saída bater.
   - O plano está errado: menor decisão que honra o combinado, anote, siga.
3. Antes da linha `Parte N: pronta`, nesta conversa: a prova da parte rodou, você leu a saída, cada "Esperado" foi comparado, cada desvio tem `Decisão`. Quem governa essa afirmação é `conferir`.
4. Escreva `Parte N: pronta (<comando> → <resultado>)`.

## No fim da lista

Uma passada de `revisar` sobre o conjunto, contra o combinado e contra a cara do site. Achado grave entra numa correção só, cada uma com prova que falhou antes. Achado miúdo vai para o andamento como adiado e para a mensagem final. Não enfeite.

A mensagem final lista as decisões, com o custo se estiver errado, e os miúdos adiados. Sem essa lista, a pessoa não vê o que você decidiu no lugar dela.

## Desculpas

| Desculpa | Resposta |
| --- | --- |
| "Lembro o que a parte pede" | Você lembra um resumo. O plano tem o valor exato. |
| "A prova do plano está certa, não preciso ver falhar" | Prova que não falhou não prova. |
| "Rodo a suíte só no final" | A corrida de cada passo mostra qual passo quebrou. |
| "O plano errou, faço o certo em silêncio" | Faça o certo e anote a decisão. |
| "Pergunto se continuo a cada parte" | Só se a pessoa escolheu parte por parte, e no que ela pode olhar. |
| "Já está bom, paro antes da última prova" | A parte acaba quando a prova passa, não quando o código parece certo. |
