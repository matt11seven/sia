# Instalar no Codex

O Codex não tem escopo `project` no `codex plugin add`. Instalação por esse comando vale para a conta. Para o harness ficar só neste projeto, o repositório carrega o próprio mercado e liga o plugin nele.

Na pasta do projeto que vai ser construído, crie `.agents/plugins/marketplace.json`:

```json
{
  "name": "sia",
  "interface": {
    "displayName": "SIA"
  },
  "plugins": [
    {
      "name": "sia",
      "source": {
        "source": "git-subdir",
        "url": "https://github.com/matt11seven/sia.git",
        "path": "./plugins/sia",
        "ref": "main"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Developer Tools"
    }
  ]
}
```

E `.codex/config.toml`:

```toml
[plugins."sia@sia"]
enabled = true
```

Abra uma sessão nova dentro deste projeto. Outro repositório, sem esses arquivos, não carrega o SIA.

O bloco de hooks fica vazio, como no Superpowers para Codex. Quem acorda o loop é a description de `comecar`.

Nesta pasta do SIA o mercado local já existe, em `.agents/plugins/marketplace.json`, apontando para `./plugins/sia`. Não copie esse arquivo para outro projeto: o caminho local quebraria. Use o `git-subdir` acima.

Prova: "Quero um sistema que avisa quando o estoque acaba." A resposta entra em `entender` antes de qualquer arquivo de produto, sem tela e sem Vercel.
