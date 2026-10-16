# Mapa — Grok

O `SessionStart` não entrega texto. Esta description e as outras skills é que acordam o loop. Leia a skill inteira antes de agir. Não confie na lembrança.

| Ação que a skill pede | Ferramenta |
| --- | --- |
| Invocar uma skill | ler o `SKILL.md` dela |
| Ler um arquivo | read_file |
| Escrever um arquivo | write |
| Editar um trecho | search_replace |
| Rodar um comando | run_terminal_command |
| Buscar texto | grep |
| Achar arquivo | list_dir ou grep |
| Lista de partes | todo_write |
| Perguntar com opções | ask_user_question. Uma pergunta. A recomendada primeiro |
| Disparar um subagente | spawn_subagent, só quando a parte for independente. Na v1 o padrão é a própria sessão |
| Abrir uma página | as ferramentas de browser, se existirem. Senão, diga o que ficou sem prova |
| Chamar Supabase ou Vercel | search_tool e depois use_tool, com o schema real. Sem schema, não chute o nome do argumento |
| Postgres com Drizzle | código e SQL no repositório. Sem MCP |
