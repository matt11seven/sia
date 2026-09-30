---
name: escolher
description: >
  Use quando um site novo ainda não tem escrito com o que é feito, onde guarda
  os dados e onde fica no ar. Também quando a pessoa perguntar de banco,
  Supabase, Vercel, hospedagem ou stack. Não use para trocar a ferramenta de
  um projeto que já tem uma. Sugere Supabase e Vercel, e espera a resposta.
  Use when choosing web stack, database, or hosting, including Supabase and
  Vercel as suggestions.
---

> A detecção de stack segue nextlevelbuilder/ui-ux-pro-max-skill, skill `ui-ux-pro-max`, commit `09170eec`, licença MIT: nunca assuma a stack. A sugestão de Supabase e de Vercel é regra do SIA.

# Escolher

Com a pessoa, siga "Como falar" em `comecar`. Não diga o nome desta skill. Uma frase de onde estamos, depois a pergunta ou o que há para olhar.

## A lei

Pare na primeira regra que couber. Sem a linha escrita em `docs/sia/escolhas.md`, Supabase e Vercel não existem para as outras skills. Esta skill não cria projeto e não instala nada.

1. O repositório já tem ferramenta (`package.json`, pasta de banco, Prisma, Firebase, API própria, um lugar de publicação já configurado). Siga o que está lá. Não proponha troca. Escreva o que encontrou em `docs/sia/escolhas.md`.
2. A pessoa já disse o nome do banco ou do lugar no ar. Use esse nome.
3. É uma página que não guarda nada de ninguém. Sem banco e sem conta. Escreva isso.
4. Precisa de conta e de dados de mais de uma pessoa, e ninguém escolheu o banco. Sugira Supabase. Na mesma frase, uma alternativa: um banco que a pessoa já tenha, ou uma API feita no projeto. Uma pergunta. Espere.
5. O site ainda não tem endereço no ar, e ninguém escolheu. Sugira Vercel. Na mesma frase, uma alternativa: outro lugar que a pessoa já use. Uma pergunta. Espere. Publicar continua sendo o último passo, depois de `conferir`.

Não instale Supabase, não crie projeto na Vercel e não rode o fluxo de `dados` nem de `publicar` nesta skill. Aqui só se escreve a escolha.

## O arquivo

`docs/sia/escolhas.md`, com três linhas que as outras skills leem ao pé da letra:

```markdown
# Escolhas

- Site: Next.js, TypeScript e Tailwind
- Dados: Supabase
- No ar: Vercel
```

Troque a linha pelo que foi de fato escolhido. "Ainda não" é uma escolha válida para "No ar" enquanto a pessoa não quiser publicar.

Trilha quando as duas sugestões são aceitas: Next.js (App Router), TypeScript, Tailwind, Supabase para pessoas e dados, Vercel para o endereço. A chave secreta do Supabase não vai para o browser. A chave pública pode ir para o lugar no ar.

## Como detectar

Olhe `package.json` (react, next, vue, svelte), `supabase/`, Prisma, `composer.json`, e qualquer arquivo de publicação. Se nada for detectável e a escolha mudar o conselho, pergunte. Não invente um padrão calado.

## Desculpas

| Desculpa | Resposta |
| --- | --- |
| "Site com login é sempre Supabase" | É a sugestão. A regra 1 e a regra 2 ganham. |
| "Já crio o projeto para adiantar" | Criar projeto é outra skill, e só depois do arquivo. |
| "A pessoa não respondeu, sigo a sugestão" | Sem resposta, a sugestão não está escolhida. Espere. |
