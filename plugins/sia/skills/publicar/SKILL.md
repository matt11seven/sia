---
name: publicar
description: >
  Use quando a pessoa quiser que o sistema fique acessível fora da máquina,
  e só depois de conferir ter passado. O passo a passo da Vercel só se
  docs/sia/escolhas.md disser Vercel. Sem essa linha, siga o lugar escrito
  nas escolhas. Gatilhos: "coloca no ar", "publica", "deploy", "quero o
  link", "outras pessoas vão usar". Não use para um sistema que fica na
  máquina de quem constrói.
---

> Não há skill equivalente nas três referências. A régua de "só afirmar com prova" é a de `conferir`.

# Publicar

Com a pessoa, siga "Como falar" em `comecar`. Não diga o nome desta skill. Abra com **Etapa: colocar no ar**, depois uma frase de onde estamos, depois a pergunta ou o que há para olhar.

## A lei

Sem `conferir` verde nesta conversa, não publique. Sem uma linha "Onde roda" que não seja "nesta máquina" nem "ainda não", pergunte uma vez e espere. Não crie projeto no escuro.

Se existir `package.json`, antes de dizer que está no ar rode o audit do gerenciador que o projeto já usa, no nível high. Com npm: `npm audit --audit-level=high`. Com pnpm: `pnpm audit --audit-level high`. Critical ou high bloqueia o "no ar". Corrija ou troque essa dependência e rode de novo. Moderate e low não bloqueiam. Se o comando não existir, diga numa frase e não invente que está limpo. Esta porta não vale para o "ficou pronto" na máquina. Não varra pacote sem uso nem dívida antiga.

## Se não for Vercel

Siga o que o arquivo diz. A régua é a mesma: existe um endereço, a pessoa abre, o fluxo principal do combinado acontece. Sem isso, não diga que está no ar.

## Se for Vercel

1. Se a ligação não existir, pare e ajude com um comando: `npx -y add-mcp https://mcp.vercel.com -g`, ou o plugin `npx plugins add vercel/vercel-plugin` no agente que aceitar. Volte quando a ligação listar os projetos.
2. Ache ou crie o projeto pela ligação.
3. Coloque as variáveis. Se `escolhas.md` disser Supabase: endereço e chave pública. Se disser Postgres com Drizzle: `DATABASE_URL`. Chave secreta só se o servidor precisar, marcada como secreta, nunca em variável que o browser lê.
4. Publique um preview. Leia o resultado. Se falhar, leia o log pela ligação e entre em `investigar`. Não diga que subiu.
5. Traga o link e peça para a pessoa abrir. Produção só depois desse sim.
6. Depois do sim, promova e rode `conferir` de novo no endereço de produção: o fluxo principal abre.

## Com a pessoa

"O ensaio está neste endereço. Faz o fluxo principal. Se estiver certo, eu deixo definitivo."

## Desculpas

| Desculpa | Resposta |
| --- | --- |
| "O build local passou, então está no ar" | No ar é o link aberto. |
| "Já publico em produção para ganhar tempo" | Preview primeiro. Produção é o sim sobre o link. |
| "A pessoa não escolheu, mas Vercel é o padrão" | Sem a linha no arquivo, não há padrão. |
| "Na máquina passou, publico com o aviso high" | Aviso critical ou high segura o ar. O pronto na máquina segue a prova de sempre. |
