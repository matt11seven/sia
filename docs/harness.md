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
| a cara do site | design system |
| a prova antes de construir | TDD |
| cada um só vê o que é seu | RLS |
| a mudança do banco, guardada no projeto | migration |
| colocar no ar | deploy |
| a ligação | MCP |

## Arquivos no projeto da pessoa

| Arquivo | Quem escreve |
| --- | --- |
| `docs/sia/escolhas.md` | `escolher` |
| `docs/sia/combinado.md` | `combinar` |
| `docs/sia/visual.md` | `visual` |
| `docs/sia/planos/` | `planejar` |
| `docs/sia/andamento.md` | `fazer` |

## Réguas que não amolecem

- Uma aprovação libera só o papel seguinte.
- Sem teste que falhou, sem código de produto.
- Sem causa, sem correção.
- Sem comando rodado nesta conversa, sem “ficou pronto”.
- Advisor de segurança do Supabase com tabela aberta bloqueia o “pronto”, mesmo com a tela boa.
- Supabase e Vercel só andam se `docs/sia/escolhas.md` disser isso.
