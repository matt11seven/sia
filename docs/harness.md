# Contrato do harness

Uma biblioteca. Os arquivos de verdade ficam em `plugins/sia/skills/`, porque o Grok copia a pasta do plugin e não leva atalho. `skills/` na raiz é um atalho para esse mesmo lugar, e os caminhos deste documento usam esse atalho. O corpo de cada skill diz a ação: pergunte, leia o arquivo, rode o teste, chame o MCP. Não diz o nome da ferramenta de um produto. O mapa em `skills/comecar/references/<agente>.md` traduz a ação para a ferramenta daquele agente. Se o mapa e a lista real de ferramentas discordarem, vale a lista real.

## Como a abertura entra

| Agente | Mecanismo | Mapa |
| --- | --- | --- |
| Claude | `hooks/session-start` no `SessionStart`. O Claude lê `hookSpecificOutput.additionalContext`. O script entrega `comecar` e o mapa. | `claude.md` |
| Codex | O plugin aponta `skills` para `./skills/`. No Superpowers de referência o bloco de hooks do Codex vem vazio, e é assim que este manifesto fica. A description de `comecar` acorda o loop. | `codex.md` |
| Grok | Plugin. O `SessionStart` do Grok não entrega texto ao modelo. A description de `comecar` carrega a ordem, e as descriptions de `combinar`, `visual` e `testar-primeiro` carregam o gatilho do dia a dia. | `grok.md` |
| Kimi | `.kimi-plugin/plugin.json` com `sessionStart.skill` em `comecar` e o mapa em `skillInstructions`. | `kimi.md` |
| Qwen | Instala o plugin no formato do Claude. Página em `docs/install/qwen.md`. Mapa próprio só se um teste mostrar ferramenta com outro nome. Até lá, usa o mapa do Claude. | `qwen.md` |

Agente fora dessa lista usa a mesma biblioteca no dia em que ganhar mapa e bootstrap. Este arquivo é o contrato desse porte: mesma pasta `skills/`, um mapa, uma forma de colocar `comecar` no contexto no início da sessão, sem a pessoa optar de novo.

## O que a pessoa ouve

| A pessoa ouve | O agente está fazendo |
| --- | --- |
| o combinado | o que o ofício chama de PRD |
| a cara | design system, sempre. Sem tela, o arquivo registra isso |
| a prova antes de construir | TDD |
| cada um só vê o que é seu | RLS |
| a mudança do banco, guardada no projeto | migration |
| colocar no ar | deploy |
| a ligação | MCP |
| o mapa | quem chama quem no código. Só quando o repositório já tem código |
| o time | papéis separados em `squads/<nome>/` |
| a mesma peça | componente já listado em `docs/sia/visual.md`, seção Peças |
| essa conta já existe | a mesma regra de negócio, num lugar só |
| vai até o fim | a lista do combinado aprovado, sem parar entre as partes, até ficar pronto na máquina |

Toda mensagem dentro de uma etapa abre com `**Etapa: <nome>**`. Três etapas levam ao lado o nome que a pessoa aprendeu nas aulas do Núcleo: o combinado (PRD), a cara (Design System, DS) e a prova antes de construir (TDD), que também marca a construção (`construir, parte N de M (TDD)`). Na primeira vez, uma frase explica o termo. A tabela completa está em `skills/comecar/SKILL.md`, na seção "A linha da etapa". RLS, migration, deploy e MCP continuam fora da conversa.

Antes de escrever o combinado na forma cheia, o agente oferece `docs/contexto/` uma vez: a pessoa coloca ali planilha, lista de preços, documento ou regra escrita, e avisa. Se a pasta já tiver arquivo, ele diz o que vai usar e segue.

## Arquivos no projeto da pessoa

| Arquivo | Quem escreve |
| --- | --- |
| `docs/sia/escolhas.md` | `escolher` |
| `docs/sia/combinado.md` | `combinar` |
| `docs/sia/visual.md` | `visual` |
| `docs/sia/planos/` | `planejar` |
| `docs/sia/andamento.md` | `fazer` |
| `docs/sia/mapa.md` | `mapa` |
| `docs/sia/banco/` | `dados`, só quando uma alteração de banco ativo sobe com volta |
| `docs/contexto/` | a pessoa coloca planilha, documento e dado. `comecar` cria o README se faltar. O resto não vai para o Git |
| `.graphifyignore` | `mapa` |
| `AGENTS.md` | `fazer`, quando nasce código de produto |
| `CLAUDE.md` | `fazer`, na mesma hora. Só aponta para o `AGENTS.md`. |
| `squads/<nome>/` | `criar-agentes`, quando há papéis separados |

## Réguas que não amolecem

- Uma aprovação libera só o papel seguinte.
- Sem teste que falhou, sem código de produto.
- Sem causa, sem correção.
- Sem comando rodado nesta conversa, sem “ficou pronto”.
- Advisor de segurança do Supabase com tabela aberta bloqueia o “pronto”, mesmo com a tela boa, quando os dados são Supabase.
- Com Postgres e Drizzle, o “pronto” exige a prova de sistema de quem vê o quê, com a regra no servidor.
- Supabase, Drizzle e Vercel só andam se `docs/sia/escolhas.md` disser isso.
- Supabase aceito instala a ligação na hora. A mudança do banco sobe por ela. Sem colar SQL no painel.
- A base de tela e de prova é sugestão na entrada da prova. Sem sim, não instala.
- O mapa de quem chama quem entra quando já há código. Não é prova. Sem hook e sem envio para fora.
- `AGENTS.md` na raiz leva o comando da prova e o que é pronto. Não repete o combinado. `CLAUDE.md` só aponta para ele.
- Parte sem `pronta (<comando> → <resultado>)` no andamento bloqueia o "pronto".
- ESLint e TypeScript, quando estão na base, entram na conferência. Sem piso de cobertura.
- Time de agentes só nasce em `squads/<nome>/`, pela skill `criar-agentes`, quando a pessoa pediu papéis separados ou o combinado aprovado diz isso. A forma dos arquivos mora nessa skill. Um sistema comum continua numa conversa só.
- A mesma regra de negócio em dois lugares é achado grave.
- Botão que salva, envia ou apaga fica desabilitado enquanto a ação corre. A prova inclui o segundo clique.
- `.env` não entra no Git. `.env.example` lista o nome, sem valor. `.env` acompanhado pelo Git bloqueia o pronto.
- Chamada que cobra por uso leva limite por pessoa no combinado e na prova. Sem essa chamada, a regra não aparece.
- Critical ou high na dependência bloqueia o "no ar". O pronto na máquina segue a prova de sempre.
- Pasta que ainda não é repositório ganha `git init` antes do primeiro arquivo de produto. Sem commit por causa disso.
- O primeiro pedaço é o menor caminho em que o "deu certo" da pessoa acontece inteiro. Entrar, quem vê o quê e a regra que esse caminho precisa entram na rodada.
- Com tela, a parte 1 abre esse caminho no navegador. Parte só de banco ou só de configuração não vem antes.
- "Vai até o fim" percorre a lista do combinado aprovado até a conferência, sem perguntar entre as partes. Não pula o sim do combinado nem o da cara. Não coloca no ar. A mesma falha, pelo mesmo motivo, duas vezes, para o loop.
- `Uso: ativo`: consulta segue, alteração pede sim, delete não segue. Alteração automática só com a linha `Banco ativo: alterações com volta`, arquivo de volta antes, registro em `docs/sia/banco/`. Rodar a volta espera outro sim.
