# Instalar no Claude

Nesta pasta do SIA:

```bash
claude plugin marketplace add .
claude plugin install sia@sia
```

O plugin em si é a pasta `plugins/sia` (skills de verdade e o hook de sessão). Abra uma sessão nova. O hook entrega a skill `comecar` no início.

Prova: diga "Quero um site para marcar horários da minha clínica." A primeira resposta classifica como coisa nova e faz uma pergunta. Não cria projeto, não chama Supabase, não chama Vercel.
