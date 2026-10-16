---
name: escolher
description: >
  Use quando um sistema ainda não tem escrito com o que é feito, onde guarda
  os dados, como se prova e onde roda. Também na entrada da prova, se essas
  linhas estiverem em "ainda não". Não use para trocar a ferramenta de um
  projeto que já tem uma. Supabase é a sugestão de dados. Postgres com Drizzle
  é a segunda. A base de tela e de prova é sugestão, não trava. Espera a resposta.
---

> A detecção de stack segue nextlevelbuilder/ui-ux-pro-max-skill, skill `ui-ux-pro-max`, commit `09170eec`, licença MIT: nunca assuma a stack. A base sugerida na prova (Next.js, TypeScript, Tailwind, ESLint, Zod, Pino, Vitest, Playwright) segue o núcleo do soumatheusgomes/vibe-coding-toolkit, licença MIT. Supabase continua a primeira sugestão de dados. Postgres com Drizzle é a segunda.

# Escolher

Com a pessoa, siga "Como falar" em `comecar`. Não diga o nome desta skill. Abra com **Etapa: a base**, depois uma frase de onde estamos, depois a pergunta ou o que há para olhar.

## A lei

Escreva `docs/sia/escolhas.md`. Sem a linha, as outras skills não inventam ferramenta. Esta skill não cria projeto, não instala pacote e não sobe banco.

Para cada linha, pare na primeira regra que couber.

1. O repositório já tem ferramenta (`package.json`, pasta de banco, Prisma, Drizzle, Supabase, Firebase, API própria, Vitest, Playwright, um lugar de publicação já configurado). Siga o que está lá. Não proponha troca. Escreva o que encontrou.
2. A pessoa já disse o nome do banco, da prova ou do lugar. Use esse nome.
3. Não guarda dado de ninguém e não precisa de conta. Dados: não guarda.
4. Precisa guardar dado e ninguém escolheu. Se a cara ainda não teve o sim, escreva "ainda não" e não pergunte. Na entrada da prova, sugira Supabase. Na mesma frase, a segunda opção: Postgres com Drizzle no projeto. Uma pergunta. Espere.
5. Há tela web, o sistema é novo e ninguém escolheu com o que ele é feito. Se a cara ainda não teve o sim, escreva "ainda não" e não pergunte. Na entrada da prova, sugira a base abaixo, com Supabase na frente. Uma pergunta. Espere. Sem tela, não proponha Next.js, Tailwind nem Vercel.
6. Não há tela, o sistema é novo (uma API, uma rotina, uma integração) e ninguém escolheu com o que ele é feito. Se a cara ainda não teve o sim, escreva "ainda não" e não pergunte. Na entrada da prova, sugira TypeScript em Node.js, porque a prova da regra já é Vitest. Se a pessoa já trabalha com outra linguagem, ofereça essa na mesma frase. Uma pergunta, junto com a de dados se ela também couber. Espere. Com a resposta, nenhuma linha fica em "ainda não", e `planejar` segue.
7. Precisa ficar acessível fora da máquina de quem constrói, e ninguém escolheu onde. Se há tela web, sugira Vercel e, na mesma frase, outro lugar que a pessoa já use. Se não há tela, pergunte onde deve rodar: a máquina dela ou um servidor que ela já tenha. Essa pergunta espera a pessoa querer que outros acessem.

Não crie tabela nem rode `publicar` nesta skill. Se a linha `Dados` ficou Supabase, invoque `dados` só para ligar, na hora. A pessoa não escolhe a ligação à parte.

## O arquivo

`docs/sia/escolhas.md`:

```markdown
# Escolhas

- Sistema: ainda não
- Dados: ainda não
- Prova: ainda não
- Onde roda: ainda não
- Uso: novo
```

Troque cada linha pelo que foi de fato escolhido. "Não guarda" e "nesta máquina" são escolhas válidas. "Ainda não" vale enquanto a pergunta daquela linha não chegou.

Quando a pessoa aceita a base de tela web, as linhas ficam:

```markdown
- Sistema: Next.js, TypeScript, Tailwind e ESLint
- Dados: Supabase
- Prova: Vitest na regra, Playwright em quem usa e no sistema
- Entrada e registro: Zod e Pino
- Onde roda: ainda não
- Uso: novo
```

Se ela escolhe a segunda opção de dados, `Dados` fica `Postgres com Drizzle`. A chave do Supabase e a `DATABASE_URL` não vão para o browser.

Com Supabase, `dados` acrescenta `Projeto Supabase: <nome> (<id>)` depois que a pessoa escolhe o projeto. Esta skill não escolhe projeto.

Quando é um sistema novo sem tela, as linhas ficam:

```markdown
- Sistema: TypeScript em Node.js
- Dados: Supabase
- Prova: Vitest na regra, Playwright no sistema se outro sistema chama uma entrada
- Onde roda: ainda não
- Uso: novo
```

## Uso

A linha `Uso` nasce com o arquivo.

A linha `Uso: novo` do modelo vale para pasta nova. Se o repositório já tem código de produto, não copie essa linha. `dados` pergunta antes de escrever no banco.

- Pasta nova, ou sistema que ainda não tem gente usando: `Uso: novo`. Sem pergunta.
- A pessoa diz que gente já usa, ou `Onde roda` já é um endereço de verdade: `Uso: ativo`.
- Pasta nova não decide sozinha quando o banco já existe. Se o projeto Supabase escolhido tem tabela com dado, `dados` troca para `Uso: ativo`.
- Repositório com código e sem essa linha: não invente. `dados` pergunta uma vez, antes de escrever no banco.

## Base sugerida

Fale uma vez, quando a regra 4, a 5 ou a 6 mandar perguntar. Não instale na mesma mensagem.

Com tela web:

> Para provar, eu sugiro esta base: Next.js com TypeScript e Tailwind, validação na entrada, registro no servidor, um teste rápido para a regra e um teste que faz o fluxo de verdade para quem usa e para o sistema inteiro. Os dados ficam no Supabase. Se preferir o banco no próprio projeto, Postgres com Drizzle. Serve esta base, com Supabase?

Sem tela, e com dado para guardar:

> Eu faço em TypeScript, rodando em Node.js. Os dados ficam no Supabase. A outra opção é Postgres com Drizzle no projeto. A regra se prova num teste rápido. Se algo de fora chama o sistema, o teste do sistema faz essa chamada de verdade. Serve assim?

Sem tela e sem dado:

> Eu faço em TypeScript, rodando em Node.js, e a regra se prova num teste rápido. Serve assim?

Sem tela e sem dado, a prova é Vitest. Não ofereça Playwright de browser nem Next.js. Playwright de sistema só se existir uma entrada que outro sistema chama.

## Como detectar

Olhe `package.json` (react, next, vue, svelte, vitest, playwright, drizzle, zod), `supabase/`, `drizzle/`, Prisma, e qualquer arquivo de publicação. Se nada for detectável e a escolha mudar o conselho, pergunte. Não invente um padrão calado.

## Desculpas

| Desculpa | Resposta |
| --- | --- |
| "Sistema com dados é sempre Supabase" | É a primeira sugestão. Postgres com Drizzle é a segunda. A regra 1 e a regra 2 ganham. |
| "Todo sistema vai para a Vercel" | Vercel é sugestão de tela web que precisa ser acessível. Sem tela, pergunte onde roda. |
| "Todo sistema novo é Next.js" | Next.js entra na base quando há tela web e a pessoa aceita. Sem tela, não. |
| "Já crio o projeto para adiantar" | Criar projeto é depois do sim, na prova. |
| "A pessoa não respondeu, sigo o Supabase" | Sem resposta, a sugestão não está escolhida. Espere. |
| "Tem código, então gente já usa" | Sem a frase dela ou um endereço de verdade, `Uso` não vira ativo. `dados` pergunta. |
| "Ofereço os dois e deixo ela pesquisar" | Uma frase. Supabase na frente, Drizzle na mesma frase. Espere. |
