---
name: testar-primeiro
description: >
  Use antes de escrever código de produto em feature, correção ou mudança de
  comportamento de um sistema. Gatilhos: implementar, corrigir, "faz funcionar",
  "salva", "o botão", bug já com causa achada por investigar. A prova nasce
  primeiro e tem que falhar pelo motivo certo. A ferramenta é a da linha Prova
  em escolhas. Em projeto novo, a regra vai para o Vitest e quem usa e o
  sistema vão para o Playwright. Se a base ainda não foi escolhida,
  sugira a de escolher e espere. Use when implementing any system feature or
  bugfix, before writing implementation code. TDD.
---

> Adaptado de obra/superpowers, skill `test-driven-development`, commit `8ca22dba`, licença MIT. A lei, o ciclo e a tabela de desculpas foram mantidos. O exemplo é de sistema.

# Testar primeiro

Com a pessoa, siga "Como falar" em `comecar`. Não diga o nome desta skill. Numa mudança pequena, abra com **Etapa: a prova antes de construir (TDD)**. Chamada de dentro de `fazer`, a linha continua a de `fazer`. Depois, uma frase de onde estamos, depois a pergunta ou o que há para olhar. Com a pessoa, chame de "a prova antes de construir".

## A lei

```
SEM CÓDIGO DE PRODUTO ANTES DE UMA PROVA QUE FALHOU
```

Se o código nasceu antes da prova, apague. Não sirva de referência. Não adapte. Escreva de novo a partir da prova.

Violar a letra é violar o espírito. "Já olhei no browser" conta como pular.

## Quando

Sempre: comportamento novo, correção, refatoração que muda comportamento.

Exceções, ditas em voz alta e aceitas pela pessoa: protótipo que será jogado fora, arquivo gerado, configuração sem comportamento.

Antes da primeira prova, olhe o caminho. Coisa nova só entra aqui por dentro de `fazer`, com plano em `docs/sia/planos/`. Chamada direto, sem plano, só vale para mudança pequena com a forma curta aprovada. Se o combinado está na forma cheia e não há plano que aponte para ele, pare e volte para `planejar`.

## Três provas

A lei vale para as três. Nenhuma nasce depois do código.

A ferramenta de cada prova é a da linha Prova em `docs/sia/escolhas.md`. Vitest e Playwright, nomeados abaixo, são a base de projeto novo. Se o projeto já prova com outra (Jest na regra, Cypress no fluxo), use essa. Não instale Playwright num projeto que já tem ferramenta de fluxo.

1. **Regra.** Vitest, ou o teste rápido que o projeto já usa. Sem browser. Uma afirmação. É a primeira prova quando o comportamento é uma regra.
2. **Quem usa.** A ferramenta de fluxo no browser (Playwright em projeto novo). A pessoa abre, preenche, envia e vê o resultado, o erro e o vazio. Escrita antes da tela. Só se o combinado tiver tela. O gesto é o mesmo que `conferir` abre.
3. **Sistema.** A ferramenta de fluxo com o sistema de pé (Playwright em projeto novo). O fluxo cruza entrada, regra e dado, no banco de teste, sem mock do caminho inteiro. Serviço de fora pode ser trocado na borda. Sem tela, e com uma entrada que outro sistema chama, a prova chama essa entrada de verdade (no Playwright, pelo `request`). Uma prova por fluxo crítico do combinado.

Num fluxo com tela, a parte da regra começa vermelha no teste rápido. A parte do fluxo começa vermelha na ferramenta de fluxo, a de quem usa e a de sistema quando cruza dado de verdade. Função pura não ganha prova de fluxo. Fluxo que uma pessoa faz não termina só no teste rápido.

Se `docs/sia/escolhas.md` não tiver a linha Prova, ou ela disser "ainda não", volte para a base sugerida de `escolher` e espere. Não instale no escuro. Não escreva a prova numa ferramenta que a pessoa não aceitou.

## O ciclo

Para cada prova do combinado, nesta ordem. Diga o passo.

1. **Vermelho.** Escreva a prova daquele critério. Rode. Ela falha porque o comportamento não existe, não porque o arquivo está quebrado. Se passar agora, a prova está testando o que já existe. Corrija a prova. Se der erro de sintaxe, conserte e rode de novo até falhar pelo motivo certo.
2. **Verde.** O mínimo de código para passar. Se este for o primeiro arquivo de produto, faça antes a seção "Antes do primeiro arquivo de produto" de `fazer`. Rode. Esta prova passa e a suíte do projeto passa. Falhou a prova nova: mexa no código, não na prova, a menos que a prova esteja errada em relação ao combinado. Outra prova ficou vermelha: conserte agora. "A suíte" é o comando de teste do projeto, não só o arquivo que você criou.
3. **Refatorar.** Limpe nome e repetição sem mudar comportamento. A suíte continua verde. Sem comportamento novo neste passo.

Depois, a próxima prova.

## Onde a prova mora

- Regra e "quem vê o quê" na lógica: o teste rápido da linha Prova (Vitest em projeto novo).
- Quem usa, se houver tela: a ferramenta de fluxo no browser, antes do componente. Abrir de verdade continua obrigatório em `conferir`.
- Sistema: a ferramenta de fluxo no caminho que cruza a fronteira. Sem tela, a chamada de verdade na entrada, se houver.
- Bug: a primeira mudança de comportamento é uma prova que reproduz a falha. `investigar` entrega a causa. Esta skill entrega a prova.
- Botão que salva, envia ou apaga: a prova de quem usa inclui o segundo clique no meio da ação. O efeito acontece uma vez.
- Limite por pessoa: se o combinado tiver essa prova numa chamada que cobra por uso, ela nasce primeiro, no Vitest. Sem essa linha no combinado, não invente a prova.

## Exemplo

Prova do combinado: a Marina não vê o horário da Ana.

Vermelho:

```typescript
test("Marina não vê o horário da Ana", async () => {
  const visiveis = await horariosDe("marina");
  expect(visiveis.map((h) => h.dono)).not.toContain("ana");
});
```

Rode. A falha esperada é a lista ainda trazer o horário da Ana, ou a função ainda não existir.

Verde: o mínimo para a lista da Marina só ter horários dela.

Quem usa, no Playwright, antes da tela:

```typescript
test("Marina não vê o horário da Ana", async ({ page }) => {
  await page.goto("/entrar");
  await page.getByLabel("E-mail").fill("marina@example.com");
  await page.getByRole("button", { name: "Entrar" }).click();
  await expect(page.getByText("Ana")).toHaveCount(0);
});
```

Sistema, no Playwright, contra a entrada real:

```typescript
test("a lista da Marina não traz a Ana", async ({ request }) => {
  const resposta = await request.get("/api/horarios", {
    headers: { cookie: cookieDaMarina },
  });
  expect(await resposta.json()).not.toEqual(
    expect.arrayContaining([expect.objectContaining({ dono: "ana" })]),
  );
});
```

Refatorar só se o mínimo ficou repetido.

## Boa prova

Uma coisa só. O nome diz o comportamento. O valor esperado é o do combinado. Sem mock que só confere se o mock foi chamado, salvo quando não houver outro jeito.

## Bandeiras vermelhas

Pare e recomece se aparecer: código antes da prova, prova depois, prova que passa de primeira, não saber dizer por que falhou, "testo depois", "só desta vez", "já olhei", "é o espírito, não o ritual", "deixo o código como referência", "já gastei horas, apagar é desperdício".

## Desculpas

| Desculpa | Resposta |
| --- | --- |
| "Simples demais para testar" | O simples quebra. A prova é curta. |
| "Testo depois e dá no mesmo" | Prova depois responde o que o código faz. Prova antes responde o que ele deve fazer. |
| "Já testei na mão" | Mão não repete igual amanhã. |
| "Apagar o que já escrevi é desperdício" | O tempo já foi. Código que ninguém viu falhar não merece confiança. |
| "Preciso explorar antes" | Explore e jogue fora. A implementação começa na prova. |
| "A prova está difícil" | A interface está difícil. Simplifique. |
| "O bug é óbvio, corrijo e testo" | Primeiro a prova que mostra o bug. |
| "O teste da regra chega para a tela" | Quem usa faz o gesto. A regra sozinha não abre a tela. |
| "Mock do caminho inteiro chega" | A prova de sistema cruza a entrada real. Serviço de fora pode ser trocado na borda. |

## Antes de dizer que a parte acabou

- Cada comportamento novo tem prova.
- Você viu cada uma falhar pelo motivo certo.
- O código foi o mínimo para passar.
- A suíte do projeto passou, e você leu a saída nesta conversa.
- Canto e erro estão cobertos quando o combinado fala deles.
- Se nasceu código de produto e não existe `AGENTS.md`, escreva o `AGENTS.md` e o `CLAUDE.md` das seções de `fazer`.
- A pasta é um repositório e `.env` não está no Git. O passo está na seção "Antes do primeiro arquivo de produto" de `fazer`.
