# Fontes

Os clones abaixo ficam na máquina, fora do git. O que o SIA adapta leva a linha de atribuição no topo da skill. O buscador de visual vai inteiro para `skills/visual/vendor/ui-ux-pro-max/`, com o `LICENSE` original.

| Pasta | URL | Commit | Licença que usamos |
| --- | --- | --- | --- |
| `references/superpowers` | https://github.com/obra/superpowers | `8ca22dba9a94f28898bbce59f2537ff4d87c747d` (v6.4.2, 2026-09-25) | MIT. Estrutura das skills de processo |
| `references/caveman` | https://github.com/juliusbrussee/caveman | `2fd153c67988e980fb0b2455c90832159a6a5a25` (2026-09-22) | MIT só em `investigate-first`, `lean-build` e `verify-and-stop`. Motor, proxy e binários são BSL-1.1 e não entram |
| `references/ui-ux-pro-max-skill` | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | `09170eec67eefd46a7ae85de61b40c194020f997` (2026-09-27) | MIT. Busca, dados e checklist de interface para site |
| `references/vibe-coding-toolkit` | https://github.com/soumatheusgomes/vibe-coding-toolkit | `f13bb354363dafef8ce8d8f605856cc9e1cc52cc` (2026-10-15) | MIT. O arquivo `LICENSE` do clone é MIT, copyright 2026 Matheus Gomes |
| `references/aiox-core` | https://github.com/SynkraAI/aiox-core | `4ef6530ff03b83aea953e4a426f95e012b8b70c5` (5.4.1, 2026-08-15) | MIT. O arquivo `LICENSE` do clone é MIT, copyright 2025 BMad Code, LLC e SynkraAI Inc. |
| ponytail, só a skill | https://github.com/dietrichgebert/ponytail | `e3ba2aa6f1e6f0bc4d69eb09c9f0d0a93af56156` | MIT. A escada de `fazer`. Sem clone: não entram a persona, os níveis nem o hook |

Quando a pessoa escolhe Supabase, o agente instala a ligação com `npx plugins add supabase-community/supabase-plugin --yes` e lê as skills oficiais `supabase` e `supabase-postgres-best-practices`. Esse texto não é copiado para cá. A mudança do banco sobe pela ligação. A pessoa não cola SQL no painel.

A base sugerida na prova (Next.js, TypeScript, Tailwind, ESLint, Zod, Pino, Vitest, Playwright) e o corte entre prova da regra, de quem usa e de sistema vêm do núcleo do [vibe-coding-toolkit](https://github.com/soumatheusgomes/vibe-coding-toolkit), licença MIT. O clone local está na tabela acima. Supabase continua a primeira sugestão de dados. Postgres com Drizzle é a segunda, e nesse caminho o SQL fica no projeto.

O mapa de quem chama quem segue o mesmo toolkit: CLI `graphify`, pacote `graphifyy`, de [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify). Extração só de código, `.graphifyignore`, saída `graphify-out/` fora do git. Sem hook e sem o código do Graphify neste repositório.

A parte que só fecha com o comando e o resultado no andamento vem da validação de história do [aiox-core](https://github.com/SynkraAI/aiox-core), licença MIT. O clone local está na tabela acima. O arquivo que a sessão seguinte lê é um `AGENTS.md` curto, no formato que Codex e Grok carregam, e não a história hiperdetalhada. Ao lado, um `CLAUDE.md` só aponta para ele, porque o Claude lê esse nome. Lint e checagem de tipo entram na conferência quando a base os tem. Sem o piso de 80% de cobertura.

A pasta `squads/<nome>/`, com `squad.yaml`, `agents/`, `tasks/`, `workflows/` e `checklists/`, segue a lógica dos squads do mesmo aiox-core. O clone local está na tabela acima. A forma canônica fica na skill `criar-agentes`: os campos obrigatórios, em português, sem saudação, sem signo e sem publicação em mercado.

Linha padrão no topo de cada skill adaptada:

> Adaptado de `<repo>`, skill `<nome>`, commit `<curto>`, licença MIT. A porta, a ordem e a tabela de desculpas foram mantidas. A boca foi trocada para português simples, estreita a sistemas. Tela e publicação só quando o sistema tiver.
