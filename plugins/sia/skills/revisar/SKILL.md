---
name: revisar
description: >
  Use quando uma parte ou um sistema ficou pronto no código e antes de dizer
  que pode ir para outras pessoas ou juntar na branch principal. Confere
  primeiro o combinado, depois a cara, depois a qualidade. Sem tela, a cara
  não cobre cor.
  Gatilhos: "revisa", "tá certo?",
  "code review", "antes de publicar".
---

> Adaptado de obra/superpowers, skill `requesting-code-review`, commit `8ca22dba`, licença MIT. Duas passadas: o combinado, depois a qualidade. A segunda passada lê a cara. Sem tela, não cobre cor.

# Revisar

Com a pessoa, siga "Como falar" em `comecar`. Não diga o nome desta skill. Abra com **Etapa: a conferência**, depois uma frase de onde estamos, depois a pergunta ou o que há para olhar.

## A lei

Revisar cedo. O revisor olha o trabalho, não o histórico da conversa.

## Quando

Obrigatório ao fim da lista de `fazer`, antes de `publicar`, e antes de juntar na branch principal. Útil quando travou.

## As duas passadas

1. **Combinado.** Cada prova de `docs/sia/combinado.md` tem teste que você viu falhar e passar, ou está escrita como fora desta rodada. O que a pessoa vê (quem vê o quê, estados vazio e erro) está no código, não só no texto.
2. **Cara e qualidade.** `docs/sia/visual.md` manda. Se disser sem tela, não cobre cor. Se houver tela, cor, letra e espaço. Dois arquivos para a mesma peça são achado grave. A mesma regra de negócio em dois lugares é achado grave: preço, prazo, quem vê o quê ou o cálculo copiados. `.env` acompanhado pelo Git é achado grave. `.env.example` com valor também. Depois: nome, responsabilidade do arquivo, segredo fora do browser, dado de uma pessoa invisível para outra na consulta do servidor, entrada validada antes de gravar. Botão que salva, envia ou apaga precisa ficar desabilitado enquanto a ação corre.

Se este agente consegue chamar subagente, chame o `revisor` em `plugins/sia/agents/revisor.md`. Entregue o caminho do combinado, do plano, do visual e o intervalo de commits. Ele só lê e não edita. Você aplica o achado grave e o importante. Sem subagente, faça você mesmo numa passada separada, depois da última parte, e diga que foi revisão do mesmo autor, mais fraca.

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

A nota do revisor não é a nota final. A nota é o que quem usa o sistema leva se isso passar a valer.

## Desculpas

| Desculpa | Resposta |
| --- | --- |
| "Eu mesmo olho o diff, já chega" | O autor tem o mesmo ponto cego. Uma passada separada é o mínimo. Sem subagente, diga isso. |
| "É pequeno, pulo" | Pequeno também fura o combinado. |
| "Os testes passaram, a revisão é extra" | Teste verde não relê o combinado linha a linha. |
