---
name: mapa
description: >
  Use quando o repositório já tem código, antes de explorar uma mudança que
  cruza arquivos, e de novo depois de construir. Monta um mapa de quem chama
  quem com a CLI graphify, só do código, na máquina. Gatilhos: sistema que
  cresceu, "onde isso é usado", mudança que atravessa partes, projeto
  existente. Não use em pasta vazia. Não use para pular a prova. Use when a
  codebase already has source and the agent needs a code graph before a
  cross-file change.
---

> O jeito vem do [vibe-coding-toolkit](https://github.com/soumatheusgomes/vibe-coding-toolkit), licença MIT, que aponta para [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify). Pacote `graphifyy`, CLI `graphify`. Sem clone. Sem hook de git e sem mandar o mapa para fora.

# Mapa

Com a pessoa, siga "Como falar" em `comecar`. Não diga o nome desta skill nem o da ferramenta. Se precisar falar, diga "um mapa de quem chama quem".

## A lei

O mapa não é prova, não libera código e não substitui o combinado. Relação marcada como inferida ou ambígua se confirma no arquivo antes de virar decisão.

Pasta sem código de produto: pare. Não instale nada.

Não rode `graphify install`, `graphify hook install` nem `--watch`. Isso mexe em instrução, hook e atualização automática. Não envie o mapa para banco externo, wiki publicada ou serviço.

## No projeto

1. Se `.graphifyignore` não existir, escreva o da seção abaixo. Se existir, não apague exclusão de segredo. Acrescente pasta gerada ou de terceiro que o projeto tenha e a lista não cubra.
2. Garanta `graphify-out/` no `.gitignore`. Não commite essa pasta.
3. Se `graphify --version` falhar, instale um método só: `uv tool install graphifyy`. Se `uv` não existir, `pipx install graphifyy`. Confira de novo. Se os dois falharem, escreva `docs/sia/mapa.md` com estado `pendente` e siga lendo o código. Não trave o combinado, a cara nem a prova.
4. Antes de extrair, rode `graphify --help` com `GRAPHIFY_NO_AUTO_REFRESH=1`. Use o modo só de código dessa versão. Na forma que o toolkit usa, e enquanto o help mostrar essas flags:

```bash
GRAPHIFY_NO_AUTO_REFRESH=1 graphify extract . --code-only --no-cluster
```

5. O arquivo esperado é `graphify-out/graph.json`. Ele não lê o combinado nem o sentido dos documentos. Se a flag não existir, não rode extração sem limite: isso pode chamar modelo para ler documento. Registre `pendente` e siga.
6. Escreva `docs/sia/mapa.md` com estado `validado` (comando rodado agora e `graph.json` presente), `configurado sem execução` ou `pendente`. Comando, data e o limite "só código". Sem senha e sem caminho pessoal.

## Consultar

Com `graph.json` presente e desta árvore:

```bash
GRAPHIFY_NO_AUTO_REFRESH=1 graphify query 'O que depende deste módulo?'
GRAPHIFY_NO_AUTO_REFRESH=1 graphify path 'NomeRealA' 'NomeRealB'
GRAPHIFY_NO_AUTO_REFRESH=1 graphify explain 'NomeReal'
```

Troque pelos nomes do grafo. Se o mapa for anterior à mudança que você está fazendo, extraia de novo no modo só de código antes de confiar nele.

Documento, imagem e PDF ficam de fora. A CLI sozinha não herda o login da conversa. Não ligue outro modelo para completar o mapa.

## Exclusões

`.graphifyignore`:

```text
# Não indexe segredo, dependência nem saída gerada.
.git/
.next/
node_modules/
out/
dist/
build/
coverage/
graphify-out/
.agents/
.claude/
.codex/
.vercel/
.env
.env.*
*.pem
*.key
*.p12
*.pfx
auth.json
credentials.json
*.log
*.tsbuildinfo
pnpm-lock.yaml
package-lock.json
yarn.lock
bun.lock
bun.lockb
```

## Desculpas

| Desculpa | Resposta |
| --- | --- |
| "O mapa disse, então está certo" | Mapa não é prova. Confirme no código. |
| "Instalo o hook para não desatualizar" | Sem hook. Extraia de novo quando for usar. |
| "Projeto novo não precisa" | Pasta vazia, pare. Assim que houver código, o mapa entra. |
| "graphify install deixa pronto" | Esse comando mexe na instrução do agente. Use a CLI isolada. |
| "Mando o grafo para um serviço e consulto lá" | O mapa fica na máquina. |
