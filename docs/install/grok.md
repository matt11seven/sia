# Instalar no Grok

```bash
grok plugin marketplace add .
grok plugin install sia --trust
```

Sessão nova. O `SessionStart` do Grok não entrega texto. As skills precisam estar de verdade em `plugins/sia/skills` (o Grok copia a pasta e ignora atalho). Depois de mudar uma skill, rode `grok plugin update sia` e abra outra sessão. `grok inspect` deve listar as 13 skills do plugin.

Prova: "Quero um site para marcar horários da minha clínica." A description de `comecar` tem que puxar `entender` antes de código.
