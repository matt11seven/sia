---
name: fazer
description: >
  Use para construir um sistema a partir de um plano já aprovado, na sessão
  atual, parte por parte. Gatilhos: "pode fazer", "segue a lista", "parte
  por parte", "implementa o plano". Cada parte passa por testar-primeiro e
  para quando a prova passa. Use when executing an approved web
  implementation plan inline.
---

> Adaptado de obra/superpowers, skill `executing-plans`, commit `8ca22dba`, licença MIT, e de juliusbrussee/caveman, skill `lean-build`, commit `2fd153c6`, licença MIT. A escada vem de dietrichgebert/ponytail, skill `ponytail`, commit `e3ba2aa6`, licença MIT. O plano manda, a prova é por parte, o andamento fica em arquivo, e se para quando o aceite passa. Sem os scripts de worktree do original: o andamento é `docs/sia/andamento.md`. Sem a persona, sem os níveis e sem dispensar a prova.

# Fazer

Com a pessoa, siga "Como falar" em `comecar`. Não diga o nome desta skill. Abra com **Etapa: construir, parte N de M (TDD)**, depois uma frase de onde estamos, depois a pergunta ou o que há para olhar. N é a parte em que você está e M o total do plano.

## A lei

O plano já pensou. Execute os passos na ordem, prove cada um, e deixe registro que sobrevive quando a conversa for compactada.

Sem modo, configuração ou peça extra que o aceite não pediu. Sem superfície nova que o combinado não pediu. Entregue o caminho inteiro daquela parte (tela, regra, dado), não um arquivo isolado que não fecha.

Invoque `testar-primeiro` antes da parte 1. Os passos do plano não dispensam essa leitura. A escada escolhe a solução. A prova continua obrigatória, inclusive numa linha só.

Se o repositório já tem código, invoque `mapa` antes da parte que cruza arquivos. No fim da lista, extraia de novo. O mapa não dispensa a prova.

Se `docs/contexto/` tiver o valor, o código usa esse valor. Não invente outro.

Parte com tela: antes de criar componente, procure a seção Peças de `docs/sia/visual.md` e o código. Se a peça existir, use. Diga à pessoa: "Esse botão já existe. Vou usar o mesmo." Se nascer agora, acrescente a linha na lista no mesmo ato, no lugar de `Nenhuma ainda.` Dois jeitos da mesma peça não seguem.

Regra de negócio que já existe é usada, não copiada. Preço, prazo, quem vê o quê e o cálculo moram num lugar. A outra tela chama esse lugar. Diga à pessoa: "Essa conta já existe. Vou usar a mesma." Troque "conta" pela regra.

Ao mostrar uma tela, ela traz só o que a pessoa criou ali ou o que está em `docs/contexto/`. Uma frase diz o que ficou para depois. Sem dado inventado para a tela parecer cheia.

## A escada

Sobe depois de ler o pedido e o código que ele toca, e antes de escrever a prova. Pare no primeiro degrau que segura. Dois degraus servem: fique no de cima.

1. **Isso precisa existir?** Necessidade imaginada não se constrói. Diga numa frase e siga.
2. **Já está neste projeto?** Um helper, um tipo, uma tela, um padrão a poucos arquivos daqui. Olhe antes de reescrever.
3. **A linguagem padrão faz?** Use.
4. **O navegador, o CSS ou o banco já fazem?** `<input type="date">` no lugar de uma biblioteca de calendário. CSS no lugar de JavaScript. Regra no banco no lugar de filtrar só na tela.
5. **Uma dependência que já está instalada resolve?** Use. Não instale outra para o que poucas linhas fazem.
6. **Cabe numa linha?** Uma linha.
7. **Só então:** o mínimo que funciona.

A preguiça é da solução, não da leitura. O menor diff no lugar errado é outro bug.

Não corte, nem para encurtar: validação na borda em que o dado entra, tratamento que evita perder dado, segurança, o básico de acessibilidade, e qualquer coisa que a pessoa pediu com todas as letras. Se ela insistir na versão completa, construa. Sem discutir de novo.

Correção de bug continua em `investigar`. O conserto preguiçoso é o da causa: uma trava no lugar por onde todos passam, não um remendo em cada caminho.

Se a simplificação tem um teto conhecido, deixe um comentário no código, em português, com o teto e quando vale subir. Sem marca de outra skill.

Com a pessoa, uma frase do que ficou de fora e quando valeria a pena: "Usei o calendário do próprio navegador. Uma biblioteca só entra se precisar de um intervalo que ele não faz."

Mudança pequena, sem plano, sobe a mesma escada antes de `testar-primeiro`. Sem o sim da forma curta em `docs/sia/combinado.md`, volte para `combinar`.

## Quando parar e perguntar

Só nestes casos: ação irreversível ou destrutiva; segredo ou permissão; efeito fora do repositório (merge, push, publicar); plano tão quebrado que todo caminho é chute. Fora isso, decida, anote e siga. Banco com `Uso: ativo` não entra neste "fora isso". A trava está em `dados`.

"Parte por parte", no `**Ritmo:**` do plano, acrescenta uma parada: ao fim de cada parte que a pessoa pode olhar, mostre e espere. "Até o fim" não pergunta "continuo?" entre partes.

## Até o fim

A pessoa diz "vai até o fim" ou "entrega pronto", ou o plano está com `**Ritmo:** até o fim`. Essa frase é a resposta. Não pergunte de novo. Ela não pula o sim do combinado nem o sim da cara. Não coloca no ar. Isso continua em `publicar`.

O que a frase libera é o combinado já aprovado:

1. O plano desse combinado, se ainda não existir.
2. Cada parte, com a prova falhando antes do código.
3. Prova que falha de verdade vai para `investigar` e volta. A mesma falha, pelo mesmo motivo, duas vezes: pare e conte. Não tente uma terceira sem a pessoa.
4. No fim, `revisar` e `conferir`. "Ficou pronto" só com o comando rodado nesta conversa.

Entre as partes, não pergunte "continuo?". Quando a primeira tela abrir na máquina, uma frase diz isso e o que ficou para depois, e a lista segue. A parte 1 continua sendo o caminho do "deu certo" quando há tela. Este modo não espera nela.

Segredo, efeito fora do repositório e plano que virou chute continuam parando. Banco de sistema ativo segue `dados`.

## Andamento

`docs/sia/andamento.md`. A primeira linha é o caminho do plano. Parte com a linha `Parte N: pronta` não se refaz. Confie nesse arquivo e no git, não na memória, depois de uma compactação.

Anote também `Decisão: <o que> — <por quê> — <o que custa se estiver errado>` quando o plano e o combinado não fecharem. Desviar do plano sem essa linha é decisão escondida.

Conflito entre partes: o combinado ganha. Anote a decisão e siga.

## O ciclo de cada parte

1. Leia a parte no plano, inclusive se você acha que lembra. Marque em andamento. Leia o código que a parte toca.
2. Suba a escada. Se o plano pede uma peça mais pesada do que o degrau de cima, e o combinado continua de pé, fique no degrau e anote a decisão. Aí siga os passos. Prova primeiro. Rode o comando. Compare com a linha "Esperado".
   - Bateu: próximo passo.
   - O código está errado: `investigar`. Não remende o sintoma para a saída bater.
   - O plano está errado: menor decisão que honra o combinado, anote, siga.
3. Antes da linha `Parte N: pronta`, nesta conversa: a prova da parte rodou, você leu a saída, cada "Esperado" foi comparado, cada desvio tem `Decisão`. Quem governa essa afirmação é `conferir`.
4. Escreva `Parte N: pronta (<comando> → <resultado>)` em `docs/sia/andamento.md` e, no mesmo ato, marque os passos dessa parte no plano. Sem o comando e o resultado, o checkbox fica aberto. Atualize o `AGENTS.md` com o comando que passou e mantenha o `CLAUDE.md` apontando para ele.

## Antes do primeiro arquivo de produto

Antes de escrever o primeiro arquivo de produto, confira o git:

```bash
git rev-parse --is-inside-work-tree
```

Se falhar, rode `git init`. Diga numa frase que a pasta virou repositório. Não faça commit dos arquivos da pessoa. Commit só quando o plano já pedir.

No `.gitignore`, garanta estas linhas. A exceção existe para o exemplo entrar no Git:

```text
.env
.env.*
!.env.example
```

Se o projeto precisar de variável de ambiente, escreva `.env.example` com o nome e uma frase do que ela é. Sem valor, sem senha, sem URL com chave. Não crie `.env` com segredo para "deixar pronto". O valor fica na máquina de quem roda.

## AGENTS.md

Escreva na raiz do projeto da pessoa na primeira vez que nascer código de produto. Atualize quando o comando da prova mudar. Não repita o combinado.

```markdown
# Para o agente

O que o sistema faz está em docs/sia/combinado.md. Este arquivo não repete isso.

## Prova

- Regra: `<comando que passou>`
- Quem usa: `<comando, ou "sem tela">`
- Sistema: `<comando, ou "sem esse fluxo">`
- Lint: `<comando, ou "não faz parte da base">`
- Tipos: `<comando, ou "não faz parte da base">`

## Pronto

Pronto só com esses comandos rodados nesta conversa, saída lida, e cada parte do plano com `Parte N: pronta (<comando> → <resultado>)` em docs/sia/andamento.md.

## Banco e segredo

Segredo não entra no browser nem no log. `.env` não entra no Git. `.env.example`, se existir, tem o nome e uma frase, sem valor. Se docs/sia/escolhas.md disser Supabase, a mudança do banco sobe pela ligação. Não cole SQL no painel. Se disser Postgres com Drizzle, o SQL do repositório é a mudança. Se disser Uso: ativo, consulta segue, alteração pede sim, delete não segue. Alteração automática só com a linha Banco ativo: alterações com volta, e a trava está em `dados`.
```

Se `Sistema` incluir ESLint e o projeto ainda não tiver script de lint, o script é `eslint .`. Se incluir TypeScript e não houver checagem de tipo, o script é `tsc --noEmit`. Grave os dois em `package.json` e nesta lista. Sem piso de cobertura.

Mudança pequena, sem plano, também escreve ou atualiza este arquivo quando o código de produto nasce.

## CLAUDE.md

Na mesma hora em que o `AGENTS.md` nasce, escreva na raiz um `CLAUDE.md` que só aponta para ele. O Claude Code lê esse nome. Codex e Grok leem o `AGENTS.md`.

```markdown
# SIA

Leia `AGENTS.md` nesta raiz e siga a seção Prova. O que o sistema faz está em `docs/sia/combinado.md`. Este arquivo não repete isso.
```

Se já existir `CLAUDE.md` e ele não citar `AGENTS.md`, acrescente esse ponteiro no fim. Não apague o que a pessoa já escreveu. Se o ponteiro já estiver lá, não escreva de novo.

## No fim da lista

Uma passada de `revisar` sobre o conjunto, contra o combinado e contra a cara. Achado grave entra numa correção só, cada uma com prova que falhou antes. Achado miúdo vai para o andamento como adiado e para a mensagem final. Não enfeite.

A mensagem final lista as decisões, com o custo se estiver errado, e os miúdos adiados. Sem essa lista, a pessoa não vê o que você decidiu no lugar dela.

## Desculpas

| Desculpa | Resposta |
| --- | --- |
| "Lembro o que a parte pede" | Você lembra um resumo. O plano tem o valor exato. |
| "A prova do plano está certa, não preciso ver falhar" | Prova que não falhou não prova. |
| "Rodo a suíte só no final" | A corrida de cada passo mostra qual passo quebrou. |
| "O plano errou, faço o certo em silêncio" | Faça o certo e anote a decisão. |
| "Pergunto se continuo a cada parte" | Só se a pessoa escolheu parte por parte, e no que ela pode olhar. |
| "Já está bom, paro antes da última prova" | A parte acaba quando a prova passa, não quando o código parece certo. |
| "Uma linha não precisa de prova" | A escada encurta a solução. A prova continua. |
| "Instalo a biblioteca, fica mais completo" | Suba a escada. Biblioteca nova só quando o degrau de cima não segura. |
| "Filtro na tela chega" | Quem chama o banco direto não passa pela tela. A regra mora no banco. |
| "Fecho a parte e anoto a prova depois" | A linha `pronta` e o checkbox nascem juntos, com o comando e o resultado. |
| "Copio a conta na outra tela, é igual" | A conta mora num lugar. A outra tela chama esse lugar. |
| "A pasta ainda não é repositório, deixo assim" | Antes do primeiro arquivo de produto, `git init`. Sem commit por causa disso. |
| "Coloco a senha no exemplo para ficar fácil" | O exemplo leva o nome. O valor fica na máquina. |
| "Vai até o fim, então pulo o combinado" | Até o fim libera a lista do combinado já aprovado. O sim desse arquivo continua. |
| "A mesma prova falhou de novo, tento outra vez" | Duas vezes pelo mesmo motivo: pare e conte. |
| "Encho a tela com nomes para ela ver" | A tela mostra o que ela criou ou o que está em `docs/contexto/`. |
