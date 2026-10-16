# Instalar no Qwen

Instale no projeto que vai ser construído. Outro repositório fica sem o SIA.

O Qwen instala plugin no formato do Claude. O manifesto é o `.claude-plugin/` do repositório do SIA.

```bash
qwen extensions install <caminho-do-sia>
```

Rode na pasta do projeto. Se o comando pedir o nome, escolha `sia`. Se aceitar escopo, use o do projeto, como o `--scope project` do Claude. Sem esse escopo, a instalação vale para a conta inteira e o harness acorda em toda pasta. Sessão nova, aberta neste projeto.

Enquanto os nomes de ferramenta baterem com os do Claude, vale `skills/comecar/references/claude.md`. Se uma ferramenta não existir, anote o nome real em `skills/comecar/references/qwen.md`. Não reescreva o corpo das skills.

Prova: "Quero um sistema que avisa quando o estoque acaba." Sem arquivo de produto antes de `entender`, e sem tela.
