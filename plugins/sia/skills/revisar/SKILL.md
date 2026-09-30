---
name: revisar
description: >
  Use quando uma parte ou um site ficou pronto no código e antes de dizer que
  pode ir ao ar ou juntar na branch principal. Confere primeiro o combinado,
  depois a cara do site, depois a qualidade. Gatilhos: "revisa", "tá certo?",
  "code review", "antes de publicar".
---

> Adaptado de obra/superpowers, skill `requesting-code-review`, commit `8ca22dba`, licença MIT. Duas passadas: o combinado, depois a qualidade. A segunda passada do SIA inclui a cara do site.

# Revisar

Com a pessoa, siga "Como falar" em `comecar`. Não diga o nome desta skill. Uma frase de onde estamos, depois a pergunta ou o que há para olhar.

## A lei

Revisar cedo. O revisor olha o trabalho, não o histórico da conversa.

## Quando

Obrigatório ao fim da lista de `fazer`, antes de `publicar`, e antes de juntar na branch principal. Útil quando travou.

## As duas passadas

1. **Combinado.** Cada prova de `docs/sia/combinado.md` tem teste que você viu falhar e passar, ou está escrita como fora desta rodada. O que a pessoa vê (quem vê o quê, estados vazio e erro) está no código, não só no texto.
2. **Cara e qualidade.** Se houve tela, `docs/sia/visual.md` manda em cor, letra e espaço. Depois: nome, responsabilidade do arquivo, segredo fora do browser, dado de uma pessoa invisível para outra.

Se houver ferramenta de subagente, mande um revisor com o caminho do combinado, do plano, do visual e o intervalo de commits. Sem subagente, faça você mesmo numa passada separada, depois da última parte, e diga que foi revisão do mesmo autor, mais fraca.

Grave o intervalo:

```bash
git rev-parse HEAD
git merge-base HEAD main || git rev-list --max-parents=0 HEAD
```

## O que fazer com o achado

- Grave: corrige agora, com `testar-primeiro`.
- Importante: corrige antes de seguir ou de publicar.
- Miúdo: anota em `docs/sia/andamento.md` e na mensagem. Não entra na correção desta passada.
- Revisor errado: discorde com o teste ou o trecho que mostra o contrário.

A nota do revisor não é a nota final. A nota é o que a pessoa que usa o site leva se isso for para o ar.

## Desculpas

| Desculpa | Resposta |
| --- | --- |
| "Eu mesmo olho o diff, já chega" | O autor tem o mesmo ponto cego. Uma passada separada é o mínimo. Sem subagente, diga isso. |
| "É pequeno, pulo" | Pequeno também fura o combinado. |
| "Os testes passaram, a revisão é extra" | Teste verde não relê o combinado linha a linha. |
