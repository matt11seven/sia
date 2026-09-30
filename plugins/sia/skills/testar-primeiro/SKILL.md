---
name: testar-primeiro
description: >
  Use antes de escrever código de produto em feature, correção ou mudança de
  comportamento de um site. Gatilhos: implementar, corrigir, "faz funcionar",
  "salva", "o botão", bug já com causa achada por investigar. A prova nasce
  primeiro e tem que falhar pelo motivo certo. Use when implementing any web
  feature or bugfix, before writing implementation code. TDD.
---

> Adaptado de obra/superpowers, skill `test-driven-development`, commit `8ca22dba`, licença MIT. A lei, o ciclo e a tabela de desculpas foram mantidos. O exemplo é de site.

# Testar primeiro

Com a pessoa, siga "Como falar" em `comecar`. Não diga o nome desta skill. Uma frase de onde estamos, depois a pergunta ou o que há para olhar. Com a pessoa, chame de "a prova antes de construir".

## A lei

```
SEM CÓDIGO DE PRODUTO ANTES DE UMA PROVA QUE FALHOU
```

Se o código nasceu antes da prova, apague. Não sirva de referência. Não adapte. Escreva de novo a partir da prova.

Violar a letra é violar o espírito. "Já olhei no browser" conta como pular.

## Quando

Sempre: comportamento novo, correção, refatoração que muda comportamento.

Exceções, ditas em voz alta e aceitas pela pessoa: protótipo que será jogado fora, arquivo gerado, configuração sem comportamento.

## O ciclo

Para cada prova do combinado, nesta ordem. Diga o passo.

1. **Vermelho.** Escreva a prova daquele critério. Rode. Ela falha porque o comportamento não existe, não porque o arquivo está quebrado. Se passar agora, a prova está testando o que já existe. Corrija a prova. Se der erro de sintaxe, conserte e rode de novo até falhar pelo motivo certo.
2. **Verde.** O mínimo de código para passar. Rode. Esta prova passa e a suíte do projeto passa. Falhou a prova nova: mexa no código, não na prova, a menos que a prova esteja errada em relação ao combinado. Outra prova ficou vermelha: conserte agora. "A suíte" é o comando de teste do projeto, não só o arquivo que você criou.
3. **Refatorar.** Limpe nome e repetição sem mudar comportamento. A suíte continua verde. Sem comportamento novo neste passo.

Depois, a próxima prova.

## Onde a prova mora

- Regra, transformação de dado, "quem vê o quê": teste automatizado.
- Tela: o roteiro (teste de componente ou os passos que o browser vai cumprir) é escrito antes do componente. A implementação vem depois. Abrir o site de verdade continua obrigatório em `conferir`.
- Bug: a primeira mudança de comportamento é uma prova que reproduz a falha. `investigar` entrega a causa. Esta skill entrega a prova.

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

## Antes de dizer que a parte acabou

- Cada comportamento novo tem prova.
- Você viu cada uma falhar pelo motivo certo.
- O código foi o mínimo para passar.
- A suíte do projeto passou, e você leu a saída nesta conversa.
- Canto e erro estão cobertos quando o combinado fala deles.
