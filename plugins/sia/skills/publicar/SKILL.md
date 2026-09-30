---
name: publicar
description: >
  Use quando a pessoa quiser ver o site no ar, e só depois de conferir ter
  passado. Sugere o passo a passo da Vercel apenas se docs/sia/escolhas.md
  disser Vercel. Gatilhos: "coloca no ar", "publica", "deploy", "quero o
  link", Vercel. Devolve um link de preview e espera a pessoa abrir antes
  de produção.
---

> Não há skill equivalente nas três referências. A régua de "só afirmar com prova" é a de `conferir`.

# Publicar

Com a pessoa, siga "Como falar" em `comecar`. Não diga o nome desta skill. Uma frase de onde estamos, depois a pergunta ou o que há para olhar.

## A lei

Sem `conferir` verde nesta conversa, não publique. Sem linha "No ar" em `docs/sia/escolhas.md`, pergunte uma vez, com a sugestão e uma alternativa, e espere. Não crie projeto no escuro.

## Se não for Vercel

Siga o que o arquivo diz. A régua é a mesma: existe um endereço, a pessoa abre, o fluxo principal do combinado acontece. Sem isso, não diga que está no ar.

## Se for Vercel

1. Se a ligação não existir, pare e ajude com um comando: `npx -y add-mcp https://mcp.vercel.com -g`, ou o plugin `npx plugins add vercel/vercel-plugin` no agente que aceitar. Volte quando a ligação listar os projetos.
2. Ache ou crie o projeto pela ligação.
3. Coloque as variáveis. Endereço do Supabase e chave pública, se `escolhas.md` disser Supabase. Chave secreta só se o servidor precisar, marcada como secreta, nunca em variável que o browser lê.
4. Publique um preview. Leia o resultado. Se falhar, leia o log pela ligação e entre em `investigar`. Não diga que subiu.
5. Traga o link e peça para a pessoa abrir. Produção só depois desse sim.
6. Depois do sim, promova e rode `conferir` de novo no endereço de produção: o fluxo principal abre.

## Com a pessoa

"O ensaio está neste link. Abre e marca um horário. Se estiver certo, eu coloco no endereço definitivo."

## Desculpas

| Desculpa | Resposta |
| --- | --- |
| "O build local passou, então está no ar" | No ar é o link aberto. |
| "Já publico em produção para ganhar tempo" | Preview primeiro. Produção é o sim sobre o link. |
| "A pessoa não escolheu, mas Vercel é o padrão" | Sem a linha no arquivo, não há padrão. |
