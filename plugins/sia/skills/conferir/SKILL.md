---
name: conferir
description: >
  Use imediatamente antes de dizer que um site ficou pronto, que um bug foi
  corrigido, que os testes passaram ou que pode publicar. Exige o comando
  rodado agora e a saída lida. Em tela, inclui abrir o site. Gatilhos:
  "pronto", "funcionou", "pode subir", "done", "ship it".
---

> Adaptado de obra/superpowers, skill `verification-before-completion`, commit `8ca22dba`, licença MIT, e de juliusbrussee/caveman, skill `verify-and-stop`, commit `2fd153c6`, licença MIT. Sem prova fresca, sem afirmação. Sem enfeite depois que passou.

# Conferir

Com a pessoa, siga "Como falar" em `comecar`. Não diga o nome desta skill. Uma frase de onde estamos, depois a pergunta ou o que há para olhar.

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

## O que cada frase exige

| Frase | Exige | Não basta |
| --- | --- | --- |
| Os testes passaram | saída do comando de teste, zero falhas, nesta conversa | uma corrida antiga |
| O bug sumiu | a prova do sintoma original, verde, depois de ter falhado | o código mudou |
| A tela está certa | o site aberto no fluxo principal, no vazio e no erro, em 375 e em 1280 | o teste de componente sozinho |
| Os dados estão certos | `get_advisors` de segurança sem aviso de tabela aberta, mais a prova de quem vê o quê | a tela bonita |
| Dá para publicar | esta skill verde e `revisar` feito | vontade |

Sem browser na sessão, diga com todas as letras o que ficou sem prova visual. Não transforme isso em "a tela está certa".

Distinga: passou, falhou, ferramenta ausente, bloqueado. Não edite produto nesta skill, a menos que o pedido inclua a correção. Correção volta para `investigar` ou `testar-primeiro`. Não acrescente polimento depois que a prova passou.

## Bandeiras vermelhas

"Deve", "provavelmente", "parece". Satisfação antes da saída. Commit ou publicação sem esta porta. Confiar no relatório de outro agente. Checagem pela metade. "Só desta vez". Cansaço.

## Desculpas

| Desculpa | Resposta |
| --- | --- |
| "Deve funcionar agora" | Rode. |
| "Estou confiante" | Confiança não é saída de comando. |
| "O linter passou" | Linter não é a suíte nem o browser. |
| "Cheque parcial chega" | Parcial não prova o que ficou de fora. |
| "Vou só alinhar um espaçamento" | A prova passou. Espaçamento novo é outro pedido. |
