# SIA

Um acompanhante para construir um site com quem não programa. A conversa começa com uma apresentação, segue uma pergunta por vez, e só vira código depois que a pessoa viu e concordou.

> Oi, eu sou o SIA. Te acompanho da ideia até o site no ar.

Por baixo dessa conversa o agente não improvisa o processo. Ele escreve o que ficou combinado, define a cara das telas, prova o comportamento antes de construir, acha a causa antes de corrigir, e só diz que acabou com um comando rodado na hora.

Supabase é a sugestão para guardar contas e dados. Vercel é a sugestão para colocar no ar. Nenhuma das duas é obrigatória. Se a pessoa aceitar, o agente usa a ligação daquele serviço e faz o passo com ela, em vez de entregar um tutorial.

Funciona no Claude, no Codex e no Grok. Kimi e Qwen instalam o mesmo conteúdo.

## Como a conversa anda

1. **Oi.** O SIA se apresenta e devolve, numa frase, o que entendeu do pedido.
2. **Quem usa.** Uma pergunta: quem abre o site e o que essa pessoa precisa conseguir fazer.
3. **Escolhas.** Se o projeto já tem ferramenta, segue a que está lá. Se não tem, sugere Supabase para os dados e Vercel para o endereço, sempre com uma alternativa, e espera.
4. **O combinado.** Um texto curto para a pessoa ler. Quem vê o quê, o que fica de fora, como saber que deu certo.
5. **A cara.** Cores, letra e o jeito das telas, gravados para não mudar a cada página.
6. **A lista.** Partes pequenas. A pessoa escolhe ver cada uma ou receber o conjunto no fim.
7. **A prova.** O teste nasce antes do código. Se quebrou, primeiro a causa, depois o conserto.
8. **O link.** Preview para abrir e usar. O endereço definitivo só depois desse sim.

Um pedido quebrado ("apertei salvar e sumiu") não recomeça do zero. O SIA pergunta o que aconteceu e investiga antes de mexer.

## Instalar

Uma vez por agente. Abra uma sessão nova em seguida.

**Grok**

```bash
grok plugin marketplace add https://github.com/matt11seven/sia
grok plugin install sia --trust
```

Depois de atualizar o plugin: `grok plugin update sia`.

**Claude**

```bash
claude plugin marketplace add https://github.com/matt11seven/sia
claude plugin install sia@sia
```

**Codex**

```bash
codex plugin marketplace add https://github.com/matt11seven/sia
```

No Codex, abra `/plugins` e instale o SIA.

Kimi e Qwen estão em [docs/install](docs/install). Para testar nesta pasta, os mesmos comandos aceitam `.` no lugar da URL.

## O que a pessoa ouve

| Na conversa | O que o agente está fazendo |
| --- | --- |
| o combinado | o que o site faz, por escrito |
| a cara do site | cores, letras e telas, num arquivo só |
| a prova antes de construir | um teste que falha antes do código existir |
| cada um só vê o que é seu | a regra de acesso no banco |
| colocar no ar | publicar |
| a ligação | a conexão com Supabase ou Vercel |

Os nomes internos (`comecar`, `entender`, `combinar` e os outros) ficam nas skills. A pessoa não precisa decorá-los.

## O que tem aqui

```text
plugins/sia/skills/     as 13 skills, de verdade
skills/                 atalho para a pasta acima
docs/install/           um arquivo por agente
docs/harness.md         como Claude, Codex, Grok, Kimi e Qwen carregam a mesma biblioteca
references/SOURCES.md   de onde veio cada instrução, com commit e licença
```

O buscador de interface viaja dentro de `visual`, com a licença MIT original.

## De onde veio

As portas do processo vêm do [Superpowers](https://github.com/obra/superpowers) (MIT). A parada no momento certo vem de três skills do [Caveman](https://github.com/juliusbrussee/caveman) (MIT). A cara das telas opera o buscador do [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (MIT), limitado a site. Quando a pessoa escolhe Supabase, o agente lê as skills oficiais da Supabase em vez de reinventar regra de banco.

O motor de compressão do Caveman não entra. A licença dele é outra.

O texto do SIA está na licença MIT deste repositório.
