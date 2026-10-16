# Mapa — Codex

O plugin entrega as skills. Multi-agente, se um dia uma skill pedir subagente, depende de `multi_agent` em `~/.codex/config.toml`. Sem essa ferramenta, o trabalho fica na sessão. Não invente o nome de um spawn.

| Ação que a skill pede | Ferramenta |
| --- | --- |
| Invocar uma skill | a ferramenta de skill da sessão |
| Ler, escrever, editar | as ferramentas de arquivo da sessão |
| Rodar um comando | a ferramenta de shell da sessão |
| Buscar texto ou arquivo | as ferramentas de busca da sessão |
| Lista de partes | a lista de tarefas da sessão, ou o arquivo do plano se não houver |
| Perguntar com opções | uma pergunta no chat, com a recomendada primeiro |
| Disparar um subagente | só se a sessão tiver spawn. Senão, na sessão |
| Chamar Supabase ou Vercel | o MCP ligado, pelo nome real |
| Postgres com Drizzle | código e SQL no repositório. Sem MCP |

Confie na lista de ferramentas desta sessão quando ela divergir desta tabela.
