# Instalar no Claude

Rode na pasta do projeto que vai ser construído. O SIA fica nesse repositório. Outra pasta não acorda o harness.

```bash
claude plugin marketplace add https://github.com/matt11seven/sia
claude plugin install sia@sia --scope project
```

O mercado fica na conta, só como catálogo. Quem liga o plugin neste repositório é o `--scope project`. Sem esse escopo, o padrão é `user`: o hook entra em toda sessão, em qualquer pasta.

O plugin em si é a pasta `plugins/sia` (skills de verdade e o hook de sessão). Abra uma sessão nova dentro deste projeto. O hook entrega a skill `comecar` no início.

Para experimentar nesta pasta do SIA, os mesmos comandos valem, com `--scope project`. Não use o escopo de usuário.

Prova: diga "Quero um sistema que avisa quando o estoque acaba." A primeira resposta classifica como coisa nova e faz uma pergunta. Não cria projeto, não chama Supabase, não chama Vercel e não abre a cara. Não cria time de agentes. O combinado vem antes da cara. Sem tela, a cara só registra isso. A base, com Supabase na frente e Postgres com Drizzle em seguida, só aparece na entrada da prova. O mapa de quem chama quem não entra nessa primeira resposta. Ele entra quando o repositório já tem código. Um site, como "quero um site para marcar horários", segue o mesmo começo.
