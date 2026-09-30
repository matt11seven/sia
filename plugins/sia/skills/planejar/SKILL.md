---
name: planejar
description: >
  Use quando o combinado de um site já foi aprovado e o trabalho tem mais de
  um passo, antes de escrever código. Quebra em partes pequenas, cada uma
  com a prova que falha primeiro. Gatilhos: "lista do que vamos fazer",
  "plano", "por onde começar", implementation plan.
---

> Adaptado de obra/superpowers, skill `writing-plans`, commit `8ca22dba`, licença MIT. Cabeçalho, arquivos, prova que falha, comando esperado e revisão contra o combinado foram mantidos. A pergunta final é em linguagem simples.

# Planejar

Com a pessoa, siga "Como falar" em `comecar`. Não diga o nome desta skill. Uma frase de onde estamos, depois a pergunta ou o que há para olhar.

## A lei

Sem combinado aprovado, não há plano. Sem a resposta à pergunta do fim ("parte por parte" ou "a lista inteira"), não há código. Cada passo deixa escrever uma coisa só.

Sem combinado aprovado, volte para `combinar`. Se houver tela e `docs/sia/visual.md` não existir, volte para `visual`.

O plano é para quem não viu este repositório. Cada passo deixa uma pessoa escrever uma coisa só: o nome do arquivo, a prova, o comando, a assinatura. O corpo da função fica com quem implementa, salvo algoritmo que a assinatura não determina. DRY. Sem peça que o combinado não pediu. Prova primeiro. Commits frequentes.

## Antes das partes

Se o combinado cobre pedaços independentes, volte e fatie. Um plano produz software que dá para provar sozinho.

Liste os arquivos que serão criados ou mudados e a responsabilidade de cada um. Arquivo pequeno, uma responsabilidade. No código que já existe, siga o padrão do repositório.

Uma parte é a menor unidade com o próprio ciclo de prova. Configuração entra na parte que precisa dela. Separe só onde daria para recusar uma parte e aceitar a vizinha.

## Onde salvar

`docs/sia/planos/AAAA-MM-DD-<assunto>.md`

## Cabeçalho

```markdown
# Plano: <nome>

**Objetivo:** uma frase.

**Como se encaixa:** duas ou três frases.

**Escolhas:** o que está em docs/sia/escolhas.md.

**Combinado:** docs/sia/combinado.md

**Cara:** docs/sia/visual.md, ou "sem tela".

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
- Prova: `caminho/do/teste`

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

## Revisão própria

1. Cada prova do combinado aponta para uma parte. Liste o que ficou de fora e cubra.
2. Cada passo decide uma coisa. Corrija buraco e transcrição.
3. O nome que a parte 3 entrega é o nome que a parte 7 usa.
4. Cada linha de "o que mais pode morder" tem prova na parte dona. Seção vazia significa que você olhou e não achou, não que pulou.
5. Se o plano é um transcrito, troque corpo de função por assinatura.

Corrija no arquivo.

## A pergunta

Salve, mostre o caminho e pare.

"O plano está em `<caminho>`. Dá uma lida. Sigo parte por parte e te mostro cada uma, ou ando a lista e te chamo no fim? Eu recomendo <um dos dois> porque <uma frase: quantas partes, se uma depende da outra, o que custa errar>."

"Parte por parte" é o caminho em que você para para a pessoa ver o que dá para olhar (uma tela, um login). "A lista inteira" invoca `fazer` e não pergunta "continuo?" entre partes.

Espere a resposta. Ela libera `fazer`.

## Desculpas

| Desculpa | Resposta |
| --- | --- |
| "O combinado já é o plano" | O combinado diz o quê. O plano diz o arquivo, a prova e o comando. |
| "Escrevo o código no plano para não errar" | Código de mais vira transcrição. Assinatura e prova bastam. |
| "Começo a primeira parte enquanto a pessoa lê" | A pergunta ainda não foi respondida. |
