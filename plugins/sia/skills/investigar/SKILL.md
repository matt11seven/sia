---
name: investigar
description: >
  Use em qualquer bug, teste vermelho ou comportamento inesperado de um site,
  antes de propor correção. Gatilhos: "não guarda", "sumiu", "quebrou",
  "não funciona", "o botão", erro, falha intermitente. Quatro fases, nesta
  ordem. Sem causa, sem correção. Use when debugging any web bug before
  proposing a fix.
---

> Adaptado de obra/superpowers, skill `systematic-debugging`, commit `8ca22dba`, licença MIT, e de juliusbrussee/caveman, skill `investigate-first`, commit `2fd153c6`, licença MIT. Quatro fases na ordem. Sintoma separado da causa. Sem edição até a causa. A fase 4 entrega para testar-primeiro.

# Investigar

Com a pessoa, siga "Como falar" em `comecar`. Não diga o nome desta skill. Uma frase de onde estamos, depois a pergunta ou o que há para olhar.

## A lei

```
SEM CORREÇÃO ANTES DE SABER A CAUSA
```

Sem a fase 1 completa, você não propõe correção. Conserto de sintoma é falha. Separe o que você observou do que você inferiu.

## Quando

Teste vermelho, bug, comportamento estranho, lentidão, build quebrado, integração. Ainda mais sob pressa, quando "é só uma linha", quando a correção anterior não segurou, quando você não entendeu.

## Fase 1 — Causa

1. Leia a mensagem de erro inteira. Linha, arquivo, código.
2. Reproduza. Quais passos, toda vez? Se não reproduz, junte dado. Não chute.
3. Olhe o que mudou: diff, commit, dependência, ambiente.
4. Se atravessa mais de uma camada (tela → servidor → banco), registre o que entra e o que sai de cada camada. Rode uma vez. Aí diga onde quebra.
5. Se o valor ruim está fundo, suba a pilha até a origem. Corrija na origem.

Pare de explorar quando der para nomear a causa ou o bloqueio exato.

## Fase 2 — Padrão

Ache um exemplo que funciona no mesmo repositório. Liste cada diferença, inclusive a pequena. Leia a referência inteira se estiver copiando um padrão. Não adapte pela metade.

## Fase 3 — Hipótese

Uma hipótese: "acho que X porque Y". O menor teste que mexe numa variável só. Funcionou: fase 4. Não funcionou: hipótese nova, sem empilhar correção. Se não souber, diga que não sabe.

## Fase 4 — Correção

1. Invoque `testar-primeiro`. A prova reproduz a falha e falha antes do conserto.
2. Uma mudança, a da causa. Sem "já que estou aqui".
3. `conferir` antes de dizer que o bug sumiu.
4. Se não segurou: volte à fase 1. Menos de três tentativas. Na terceira que falha, pare e converse sobre a estrutura. Não tente a quarta no escuro. Três falhas em lugares diferentes são estrutura errada, não hipótese azarada.

## Bandeiras vermelhas

"Corrijo agora e investigo depois". "Vou mudando para ver". "Várias mudanças de uma vez". "Pulo o teste". "Provavelmente é X". "Mais uma tentativa" depois de duas. Cada correção revela um problema novo.

## Desculpas

| Desculpa | Resposta |
| --- | --- |
| "É simples, não precisa de fase" | O simples também tem causa. A fase 1 nele é curta. |
| "É urgente" | Chute urgente demora mais. |
| "Deixa eu tentar isto primeiro" | A primeira correção vira o hábito. Comece pela causa. |
| "Escrevo o teste depois que confirmar" | Sem a prova que falhou, o conserto não cola. |
| "Não tem causa, é o ambiente" | 95% desses casos são fase 1 incompleta. Se for de verdade ambiente, escreva o que você olhou e trate com mensagem clara, sem fingir correção. |

Com a pessoa, o relato é a causa e a prova. "O horário sumia porque a lista pedia os dados de todo mundo e a tela filtrava errado. A prova agora falha se a Marina vir o horário da Ana, e passa com o filtro certo."
