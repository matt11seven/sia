---
name: dados
description: >
  Use assim que docs/sia/escolhas.md disser Supabase, para instalar a ligação
  e subir a mudança do banco por ela, e quando disser Postgres com Drizzle.
  Gatilhos: "banco", "login", "cada um só vê o seu", tabela, migration,
  "cola no painel", "copia o SQL", Supabase, Drizzle. Não deixe a pessoa
  colar SQL no painel. Use when the chosen data store is Supabase or
  Postgres with Drizzle.
---

> O caminho Supabase segue as skills oficiais `supabase` e `supabase-postgres-best-practices`. Esta skill não reescreve esse texto. O caminho Drizzle guarda o schema e o SQL no repositório. A boca é a mesma: cada um só vê o que é seu.

# Dados

Com a pessoa, siga "Como falar" em `comecar`. Não diga o nome desta skill. Abra com **Etapa: a base**, depois uma frase de onde estamos, depois a pergunta ou o que há para olhar.

## A lei

Se `docs/sia/escolhas.md` não diz Supabase nem Postgres com Drizzle, pare. Não crie projeto, não sugira de novo, não escreva tabela.

A mudança do banco nasce como arquivo no repositório. SQL só num painel, sem arquivo, não está pronto.

Segredo de banco não entra no browser, nem em variável que o browser lê, nem na mensagem de erro. No Supabase, a chave secreta é a `service_role`. No Drizzle, é a `DATABASE_URL`. Se a chave for parar num arquivo, faça na hora a parte de `.env` da seção "Antes do primeiro arquivo de produto" de `fazer`, mesmo antes do código.

Quem vê o quê mora no servidor, na consulta ou na policy. Filtro só na tela não conta.

## Sistema ativo

Leia `Uso` em `docs/sia/escolhas.md`.

Sem a linha, e o repositório já tem código: uma pergunta, uma vez, antes de qualquer escrita no banco. "Gente já usa este sistema?" Grave `Uso: novo` ou `Uso: ativo`. Consulta pode acontecer antes da resposta. Escrita espera.

`Uso: novo`. O banco de teste que a pessoa já aceitou recebe a mudança do plano. O arquivo nasce no git e sobe pela ligação. Apagar dado que alguém já guardou não entra nem aqui.

`Uso: ativo`. Três classes:

- Consulta. Ler, listar, advisor. Segue.
- Alteração. Mudar linha, coluna ou schema desse banco. Pare. Uma frase com o efeito. Espere o sim daquela mudança.
- Delete. Apagar linha, esvaziar tabela, derrubar tabela com dado. Não faça. Insistir não libera.

Se ela disser com todas as letras que as alterações desse banco ativo podem ir sozinhas, a linha vira `Banco ativo: alterações com volta`. Delete continua de fora.

Antes de aplicar uma alteração nessa linha:

1. O arquivo da mudança já está no projeto.
2. O arquivo da volta está ao lado e desfaz aquela mudança. Sem ele, a mudança não sobe.
3. `docs/sia/banco/AAAA-MM-DD-<assunto>.md` registra o que mudou, o comando e o caminho da volta.

Rodar a volta é outra alteração. Espere um sim novo. Não volte sozinha. Consulta não pede a linha `alterações com volta`.

## Se for Supabase

A ligação vem antes de qualquer SQL. Quem aceitou Supabase não copia migration para o painel.

### Ligar

Faça isto no momento em que `Dados` vira Supabase, e de novo antes da primeira mudança de banco se a ligação ainda não respondeu. Não pergunte se a pessoa quer a ligação. Ela já aceitou o banco.

1. Tente `list_projects`. Se responder, a ligação está pronta. Siga para a mudança.
2. Se a ferramenta não existir, instale sem pedir confirmação:

```bash
npx plugins add supabase-community/supabase-plugin --yes
```

Esse comando detecta o agente da máquina e instala a ligação e as skills oficiais. Não invente outro instalador se este rodar.

3. Se este agente não for detectado, use o jeito dele e pare no primeiro que instalar:
   - Claude: `claude plugin marketplace add anthropics/claude-plugins-official` e `claude plugin install supabase@claude-plugins-official`.
   - Codex, Grok, Kimi e Qwen: o mesmo `npx plugins add`, se o instalador aceitar o agente. Se não aceitar, diga numa frase e use a CLI da Supabase para aplicar o arquivo que está no git. Não mande a pessoa colar SQL no painel.
4. Se as ferramentas só aparecem numa sessão nova, diga isso numa frase e pare até ela voltar. Não improvise o banco enquanto isso.
5. Se a ferramenta existe e pede login, uma frase: "Abre o login do banco. É uma vez." Espere. Não peça chave no chat.
6. Volte ao passo 1. Sem `list_projects`, a mudança espera. A única saída, se o instalador não aceitar o agente, é a CLI aplicando o arquivo que já está no git. O painel não é saída.

Escreva em `docs/sia/escolhas.md` a linha `Ligação: ligada`, `Ligação: falta login` ou `Ligação: pendente`.

### Mudar o banco

1. Leia as skills oficiais `supabase` e `supabase-postgres-best-practices` para o pedaço desta tarefa (tabela, conta, arquivo, quem vê o quê) e siga o que elas mandam. Se não estiverem instaladas, diga isso numa frase e use a documentação que a ligação devolver, sem inventar um padrão paralelo.
2. Use a ligação como a mão. Ferramentas da v1, pelos nomes reais do schema, sem chute: `list_projects`, `list_tables`, `list_migrations`, `apply_migration`, `execute_sql`, `get_advisors`, `generate_typescript_types`, `get_project_url`, `get_publishable_keys`.
3. Escreva a migration no projeto. Antes de subir, passe por Sistema ativo. Suba com `apply_migration`. O arquivo continua no git. O SQL não vai para o chat como algo para a pessoa colar.
4. Antes de dizer que os dados estão certos: `get_advisors` com tipo security. Aviso de tabela aberta para qualquer um é correção, não nota. Rode de novo e veja o aviso sumir. Aviso de performance fica registrado. O que quebra confiança bloqueia `conferir`.
5. Gere os tipos com `generate_typescript_types` quando o projeto for TypeScript, e guarde no lugar que o repositório já usa.

## Se for Postgres com Drizzle

Não há ligação. O schema e o SQL ficam no projeto.

1. O schema é a fonte. A migration é o SQL gerado a partir dele, revisado, commitado. Não use `db push` como caminho padrão. Não rode migration no import, no build nem a cada request.
2. Aplique o SQL só num banco conhecido, de teste ou de desenvolvimento, que a pessoa autorizou. Banco de produção espera o mesmo sim de `publicar`. Se `Uso` for ativo, a seção Sistema ativo ganha desta frase.
3. Dado que entra de fora passa pela validação da linha "Entrada e registro" antes de gravar. Se a linha disser Zod, use Zod. Se o projeto já tiver outra, use a que está.
4. A consulta de "quem vê o quê" filtra no servidor, com o dono da sessão. A prova disso é a de sistema, em `testar-primeiro`.
5. Os tipos saem do schema (`$inferSelect` e `$inferInsert`). Não escreva um tipo paralelo na mão.
6. Registro do que aconteceu, se a linha disser Pino, não leva senha, `DATABASE_URL` nem dado pessoal.

## Com a pessoa

Conte o efeito. "A Marina entra e vê só os horários dela." A regra fica no arquivo.

Não ofereça três desenhos de banco. A linha de escolhas já decidiu. Diga a consequência numa frase.

## Desculpas

| Desculpa | Resposta |
| --- | --- |
| "Supabase é o padrão, uso mesmo com Drizzle escrito" | A linha do arquivo manda. |
| "Aplico no painel e depois copio" | O arquivo nasce no projeto. A ligação aplica. A pessoa não cola SQL. |
| "Ela não sabe que existe ligação, mando o SQL" | Instala a ligação e aplica o arquivo. O chat não é o lugar do SQL. |
| "A ligação falhou, uso o painel desta vez" | Sem `list_projects`, a mudança espera. Não abre exceção. |
| "db push é mais rápido" | O SQL revisado é a mudança guardada no projeto. |
| "O filtro da tela chega" | Quem chama o banco direto não passa pela tela. A regra mora no servidor. |
| "Coloco a chave secreta só para testar no front" | Não. Nem para testar. |
| "O sistema já está em uso, aplico a mudança e aviso depois" | Alteração em banco ativo espera o sim. Delete não segue. |
| "Ela insistiu, então apago" | Delete não segue. Insistir não libera. |
| "Alteração automática dispensa a volta" | Sem o arquivo que desfaz, a mudança não sobe. |
