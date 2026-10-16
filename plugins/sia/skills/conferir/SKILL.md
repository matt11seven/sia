---
name: conferir
description: >
  Use imediatamente antes de dizer que um sistema ficou pronto, que um bug
  foi corrigido, que os testes passaram ou que pode publicar. Exige o
  comando rodado agora e a saída lida. Se houver tela, inclui abrir. Gatilhos:
  "pronto", "funcionou", "pode subir", "done", "ship it".
---

> Adaptado de obra/superpowers, skill `verification-before-completion`, commit `8ca22dba`, licença MIT, e de juliusbrussee/caveman, skill `verify-and-stop`, commit `2fd153c6`, licença MIT. Sem prova fresca, sem afirmação. Sem enfeite depois que passou.

# Conferir

Com a pessoa, siga "Como falar" em `comecar`. Não diga o nome desta skill. Abra com **Etapa: a conferência**, depois uma frase de onde estamos, depois a pergunta ou o que há para olhar.

## A lei

```
SEM "FICOU PRONTO" SEM A PROVA RODADA AGORA
```

Se você não rodou o comando nesta conversa, você não pode dizer que passou. "Deve passar", "parece", "o agente disse que deu certo" contam como não ter rodado.

## A porta

Antes de qualquer frase de sucesso:

1. Diga qual comando prova essa frase.
2. Rode o comando inteiro, agora.
3. Leia a saída, o código de saída e as falhas.
4. A saída confirma? Se não, diga o estado real com a evidência. Se sim, afirme junto com a evidência.
5. Só então a frase de pronto.

Pular um passo é afirmar no escuro.

Se existir `AGENTS.md` na raiz, os comandos da seção Prova são os que você roda. Não invente outro.

O plano que conta é o da primeira linha de `docs/sia/andamento.md`. Plano antigo, de outra rodada, não bloqueia. Se existir esse plano, cada parte dele precisa da linha `Parte N: pronta (<comando> → <resultado>)` em `docs/sia/andamento.md`. Parte com checkbox aberto, ou sem comando e resultado, bloqueia "ficou pronto". Parte adiada no andamento não entra nessa conta.

Se `docs/sia/combinado.md` está na forma cheia (tem "Quem usa e o que precisa fazer"), precisa existir em `docs/sia/planos/` um plano com a linha `**Combinado:** docs/sia/combinado.md`. Sem esse plano, o trabalho foi tratado como mudança pequena sem ser. Isso bloqueia "ficou pronto". Diga numa frase que a lista ficou faltando, volte para `planejar` e escreva o plano do que já existe e do que falta. Não apague o código que já passou na prova.

## O que cada frase exige

| Frase | Exige | Não basta |
| --- | --- | --- |
| Os testes passaram | saída do comando de teste, zero falhas, nesta conversa | uma corrida antiga |
| O código está no formato | se `Sistema` em `docs/sia/escolhas.md` incluir ESLint: o lint rodado agora, zero erros. Se incluir TypeScript: a checagem de tipo rodada agora, zero erros | o lint no lugar da suíte. Sem esses dois na base, esta linha não se aplica. Sem piso de cobertura |
| O bug sumiu | a prova do sintoma original, verde, depois de ter falhado | o código mudou |
| A tela está certa | a prova de quem usa, na ferramenta da linha Prova, rodada agora, e a tela aberta no fluxo principal, no vazio e no erro, em 375 e em 1280, com teclado, foco visível e console limpo | o Vitest sozinho. Sem tela no combinado, esta linha não se aplica |
| O sistema cruzou a fronteira | a prova de sistema, na ferramenta da linha Prova, rodada agora, no fluxo que entra e chega no dado | mock do caminho inteiro. Sem esse fluxo no combinado, esta linha não se aplica |
| Os dados estão certos | se Dados for Supabase: `get_advisors` de segurança sem aviso de tabela aberta, mais a prova de quem vê o quê. Se for Drizzle: a prova de sistema de quem vê o quê, com a regra no servidor | a tela bonita |
| O segredo ficou fora do Git | `git ls-files` não lista `.env` nem outro `.env.*` com valor. `.env.example`, se existir, não tem valor | o exemplo com senha de verdade |
| Dá para publicar | esta skill verde e `revisar` feito | vontade. O audit de dependência não entra aqui: critical ou high bloqueiam o ar, em `publicar` |

Sem browser na sessão, diga com todas as letras o que ficou sem prova visual. Não transforme isso em "a tela está certa".

Distinga: passou, falhou, ferramenta ausente, bloqueado. Não edite produto nesta skill, a menos que o pedido inclua a correção. Correção volta para `investigar` ou `testar-primeiro`. Não acrescente polimento depois que a prova passou.

## Bandeiras vermelhas

"Deve", "provavelmente", "parece". Satisfação antes da saída. Commit ou publicação sem esta porta. Confiar no relatório de outro agente. Checagem pela metade. "Só desta vez". Cansaço.

## Desculpas

| Desculpa | Resposta |
| --- | --- |
| "Deve funcionar agora" | Rode. |
| "Estou confiante" | Confiança não é saída de comando. |
| "O linter passou" | Linter e tipo entram quando a base os tem. Não substituem a suíte nem o browser. |
| "A parte está pronta na minha cabeça" | Sem comando e resultado no andamento, a parte segue aberta. |
| "Cheque parcial chega" | Parcial não prova o que ficou de fora. |
| "Vou só alinhar um espaçamento" | A prova passou. Espaçamento novo é outro pedido. |
| "Era pequeno, por isso não fiz plano" | Combinado na forma cheia é coisa nova. Sem plano, não fica pronto. |
