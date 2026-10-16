# Instalar no Grok

`grok plugin install` grava o plugin na conta e ele pode acordar em toda pasta. Para o harness ficar só neste projeto, copie o plugin para dentro dele.

Na pasta do projeto que vai ser construído, com o repositório do SIA já clonado ao lado:

```bash
mkdir -p .grok/plugins/sia
cp -R /caminho/do/sia/plugins/sia/. .grok/plugins/sia/
```

A cópia precisa das skills de verdade, em `.grok/plugins/sia/skills`. O Grok ignora atalho. Confie o plugin deste projeto e abra uma sessão nova aqui. Outra pasta não tem `.grok/plugins/sia` e não carrega o harness.

Depois de mudar uma skill no SIA, copie de novo e abra outra sessão. `grok inspect`, nesta pasta, deve listar as 15 skills. O agente que escreve times fica em `.grok/plugins/sia/agents`.

Prova: "Quero um sistema que avisa quando o estoque acaba." A description de `comecar` tem que puxar `entender` antes de código, sem tela e sem Vercel. Esse pedido não cria time de agentes.
