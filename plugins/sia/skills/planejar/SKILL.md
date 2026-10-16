---
name: planejar
description: >
  Use quando o combinado de um sistema já foi aprovado e o trabalho tem mais de
  um passo, antes de escrever código. Quebra em partes pequenas, cada uma
  com a prova que falha primeiro. Gatilhos: "lista do que vamos fazer",
  "plano", "por onde começar", implementation plan.
---

> Adaptado de obra/superpowers, skill `writing-plans`, commit `8ca22dba`, licença MIT. Cabeçalho, arquivos, prova que falha, comando esperado e revisão contra o combinado foram mantidos. A pergunta final é em linguagem simples.

# Planejar

Com a pessoa, siga "Como falar" em `comecar`. Não diga o nome desta skill. Abra com **Etapa: a lista**, depois uma frase de onde estamos, depois a pergunta ou o que há para olhar.

## A lei

Sem combinado aprovado, não há plano. Sem a resposta à pergunta do fim ("parte por parte" ou "até o fim"), não há código. Se a pessoa já disse "vai até o fim" ou "entrega pronto", essa frase é a resposta. Grave o ritmo e não pergunte de novo. Cada passo deixa escrever uma coisa só.

Sem combinado aprovado, volte para `combinar`. Sem `docs/sia/visual.md`, volte para `visual`. Se Sistema, Dados ou Prova em `docs/sia/escolhas.md` estiverem em "ainda não" ou faltarem, volte para `escolher` e espere. O plano usa a ferramenta que a pessoa aceitou.

O plano é para quem não viu este repositório. Cada passo deixa uma pessoa escrever uma coisa só: o nome do arquivo, a prova, o comando, a assinatura. O corpo da função fica com quem implementa, salvo algoritmo que a assinatura não determina. DRY. Sem peça que o combinado não pediu. Prova primeiro. Commits frequentes.

## Antes das partes

Se o combinado cobre pedaços independentes, volte e fatie. Um plano produz software que dá para provar sozinho.

Se `docs/contexto/` tiver arquivo além do README, o plano usa esses dados. Não troque um número, um nome ou uma regra que está lá.

Se o repositório já tem código, invoque `mapa` antes de escolher os arquivos. Quem chama a parte entra na lista. O mapa não vira o plano.

Se o combinado pede papéis separados, a parte que escreve o time invoca `criar-agentes`. O plano não inventa outro formato de agente.

Se `Dados` for Supabase, a parte que muda o banco escreve o arquivo e sobe pela ligação de `dados`. O plano não manda colar SQL no painel.

Liste os arquivos que serão criados ou mudados e a responsabilidade de cada um. Arquivo pequeno, uma responsabilidade. No código que já existe, siga o padrão do repositório. Se a parte tem tela, o passo nomeia a peça da seção Peças de `docs/sia/visual.md`. Peça que já está na lista não ganha arquivo novo. A mesma conta, o mesmo preço ou a mesma regra de quem vê o quê mora num lugar. O passo nomeia esse lugar.

Uma parte é a menor unidade com o próprio ciclo de prova. Configuração entra na parte que precisa dela. Separe só onde daria para recusar uma parte e aceitar a vizinha.

Com tela, a parte 1 já abre no navegador o caminho do "deu certo". Parte só de configuração ou só de banco não vem antes dela. Se `Uso` em `docs/sia/escolhas.md` for ativo, a parte que mexe no banco segue a trava de `dados`. Consulta segue. Alteração espera permissão. Delete não entra no plano.

## Onde salvar

`docs/sia/planos/AAAA-MM-DD-<assunto>.md`

## Cabeçalho

```markdown
# Plano: <nome>

**Objetivo:** uma frase.

**Como se encaixa:** duas ou três frases.

**Escolhas:** o que está em docs/sia/escolhas.md.

**Combinado:** docs/sia/combinado.md

**Cara:** docs/sia/visual.md

**Ritmo:** parte por parte, ou até o fim. Grave depois da resposta.

## Vale em todas as partes

<regras do combinado, uma linha cada, com o valor exato>

## O que mais pode morder

<até cinco entradas ou falhas que o combinado implica e nenhuma prova ainda cobre, a mais provável primeiro. Cada linha ganha uma prova na parte dona daquele código.>
```

## Cada parte

```markdown
### Parte N: <nome>

**Arquivos:**
- Criar: `caminho/exato`
- Mudar: `caminho/exato`
- Prova: `caminho/do/teste` — regra (Vitest), quem usa (Playwright no browser) ou sistema (Playwright no sistema de pé). O corte está em `testar-primeiro`.

**Encaixa:**
- Usa: o que a parte anterior entrega, com o nome exato
- Entrega: o nome que a parte seguinte vai chamar

- [ ] **Passo 1: Escrever a prova que falha**

<o teste, com o valor do combinado>

- [ ] **Passo 2: Rodar e ver falhar**

Rodar: `<comando>`
Esperado: FAIL porque <motivo>

- [ ] **Passo 3: Implementar `nome(args) -> retorno` em `caminho`**

Uma linha de abordagem quando ainda houver escolha. Bloco de código só para algoritmo que a prova não determina.

- [ ] **Passo 4: Rodar e ver passar**

Rodar: `<comando>`
Esperado: PASS, suíte do projeto verde

- [ ] **Passo 5: Commit**
```

Tela cita o token de `docs/sia/visual.md` no passo 3. Não inventa cor.

Um passo está pronto quando dele sai uma coisa só. "Tratar os cantos", "TBD" e "testes adequados" são buraco. Um plano várias vezes maior que o combinado escreveu o programa em vez de decidir.

Os checkboxes nascem abertos. Quem fecha é `fazer`, no mesmo ato em que `docs/sia/andamento.md` ganha `Parte N: pronta (<comando> → <resultado>)`. Este arquivo não é o lugar do que o sistema faz. Isso continua no combinado. O comando que a sessão seguinte roda mora no `AGENTS.md`, escrito quando o código nasce. O `CLAUDE.md` ao lado só aponta para ele.

## Revisão própria

1. Cada prova do combinado aponta para uma parte. Liste o que ficou de fora e cubra.
2. Cada passo decide uma coisa. Corrija buraco e transcrição.
3. O nome que a parte 3 entrega é o nome que a parte 7 usa.
4. Cada linha de "o que mais pode morder" tem prova na parte dona. Seção vazia significa que você olhou e não achou, não que pulou.
5. Se o plano é um transcrito, troque corpo de função por assinatura.
6. Com tela, a parte 1 abre o caminho do "deu certo". Nenhuma parte só de banco ou só de configuração vem antes.

Corrija no arquivo.

## A pergunta

Salve, mostre o caminho e pare.

"O plano está em `<caminho>`. Dá uma lida. Sigo parte por parte e te mostro cada uma, ou vou até o fim e te chamo quando estiver pronto? Eu recomendo <um dos dois> porque <uma frase: quantas partes, se uma depende da outra, o que custa errar>."

Com tela, na primeira lista, recomende parte por parte. Sem tela, recomende até o fim. Se a pessoa já disse "vai até o fim" ou "entrega pronto", não faça esta pergunta.

"Parte por parte" para para a pessoa ver o que dá para olhar (uma tela, um login). "Até o fim" invoca `fazer` e não pergunta "continuo?" entre partes. O loop, o limite de duas falhas iguais e a trava do banco estão em `fazer` e em `dados`.

Grave no cabeçalho do plano `**Ritmo:** parte por parte` ou `**Ritmo:** até o fim`. Espere a resposta, se a pergunta foi feita. Ela libera `fazer`.

## Desculpas

| Desculpa | Resposta |
| --- | --- |
| "O combinado já é o plano" | O combinado diz o quê. O plano diz o arquivo, a prova e o comando. |
| "Escrevo o código no plano para não errar" | Código de mais vira transcrição. Assinatura e prova bastam. |
| "Começo a primeira parte enquanto a pessoa lê" | A pergunta ainda não foi respondida. Sem essa pergunta, só se ela já disse que vai até o fim. |
| "A parte 1 é o banco, a tela vem depois" | Com tela, a parte 1 abre o caminho do "deu certo". |
