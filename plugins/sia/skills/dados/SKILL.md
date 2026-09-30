---
name: dados
description: >
  Use só quando docs/sia/escolhas.md disser Supabase, para guardar dados,
  conta, arquivo ou a regra de quem vê o quê. Gatilhos: "banco", "login",
  "cada um só vê o seu", tabela, migration, Supabase. Usa a ligação MCP e
  lê as skills oficiais da Supabase antes de escrever regra. Use when the
  chosen backend is Supabase.
---

> O jeito de modelar banco, Auth e RLS vem das skills oficiais `supabase` e `supabase-postgres-best-practices`. Esta skill não reescreve esse texto. Acrescenta a ordem da ligação e a boca simples.

# Dados

Com a pessoa, siga "Como falar" em `comecar`. Não diga o nome desta skill. Uma frase de onde estamos, depois a pergunta ou o que há para olhar.

## A lei

Se `docs/sia/escolhas.md` não diz Supabase, pare. Não crie projeto, não sugira de novo, não escreva policy.

A mudança do banco nasce como arquivo no repositório e sobe pela ligação. SQL só no painel, sem arquivo, não está pronto.

A chave secreta (`service_role`) não entra no browser nem em variável pública. A chave pública pode.

## Ordem

1. Leia as skills oficiais `supabase` e `supabase-postgres-best-practices` para o pedaço desta tarefa (tabela, conta, arquivo, quem vê o quê) e siga o que elas mandam. Se não estiverem instaladas, diga isso numa frase e use a documentação que o MCP devolver, sem inventar um padrão paralelo.
2. Use a ligação como a mão. Ferramentas da v1, pelos nomes reais do schema, sem chute: `list_projects`, `list_tables`, `list_migrations`, `apply_migration`, `execute_sql`, `get_advisors`, `generate_typescript_types`, `get_project_url`, `get_publishable_keys`.
3. Se a ligação não existir, pare e ajude a ligar com um comando, no agente da sessão:
   - Claude, Codex, Grok, Kimi: o plugin oficial da Supabase (`npx plugins add supabase-community/supabase-plugin`) ou o MCP documentado por eles para esse agente.
   - Qwen: o mesmo comando se o instalador aceitar. Se não aceitar, diga numa frase e use a CLI da Supabase. Não largue a pessoa num passeio pelo painel.
   Volte ao passo 2 quando a ligação responder `list_projects`.
4. Escreva a migration no projeto. Suba com `apply_migration`. O arquivo continua no git.
5. Antes de dizer que os dados estão certos: `get_advisors` com tipo security. Aviso de tabela aberta para qualquer um é correção, não nota. Rode de novo e veja o aviso sumir. Aviso de performance fica registrado. O que quebra confiança bloqueia `conferir`.
6. Gere os tipos com `generate_typescript_types` quando o projeto for TypeScript, e guarde no lugar que o repositório já usa.

## Com a pessoa

Conte o efeito. "A Marina entra e vê só os horários dela." A policy fica no arquivo.

Não ofereça três desenhos de regra. Escolha o que as skills oficiais mandam para "cada linha tem um dono" e diga a consequência numa frase.

## Desculpas

| Desculpa | Resposta |
| --- | --- |
| "Todo site merece Supabase" | Só com a linha no arquivo de escolhas. |
| "Aplico no painel e depois copio" | O arquivo vem primeiro. A ligação aplica o arquivo. |
| "O advisor é exagero, a tela já filtra" | Filtro na tela não impede quem chama o banco direto. O aviso alto bloqueia. |
| "Coloco a chave secreta só para testar no front" | Não. Nem para testar. |
