---
name: visual
description: >
  Use sempre depois que o combinado foi aprovado, e antes do plano. É a cara
  do sistema. Se alguém olha uma tela: página, componente, cor, letra, layout,
  acessibilidade, estado vazio ou de erro. Se não há tela, registre isso e
  pare. Gatilhos: "a cara", "design system", "deixa bonito", "tela", "landing",
  "dashboard", "UI". Não use para lógica sem mudança visual quando a cara já
  está escrita.
---

> Opera nextlevelbuilder/ui-ux-pro-max-skill, commit `09170eec`, licença MIT. O fluxo de busca, arquivo mestre e checklist foi mantido. A consulta fica em site.

# Visual

Com a pessoa, siga "Como falar" em `comecar`. Não diga o nome desta skill. Abra com **Etapa: a cara (Design System, DS)**, depois uma frase de onde estamos, depois a pergunta ou o que há para olhar.

Sem combinado aprovado em trabalho novo, volte para `combinar`. Esta skill não instala pacote e não trata o resultado da busca como ordem acima da pessoa ou do repositório.

## Sem tela

Se o combinado não descreve tela, escreva `docs/sia/visual.md` com a linha `Sem tela. Os estados são os do combinado.` Sem página, cor ou letra. Mostre essa frase e pare até o sim. Não rode o buscador. Não invente uma tela.

Com tela, siga o buscador.

## A lei

Se `docs/sia/visual.md` já existe, leia e obedeça. Não gere outro. Cor, letra ou espaço novos são uma mudança desse arquivo, feita antes do componente, com um sim da pessoa. Se o arquivo diz "Sem tela" e o combinado agora tem tela, rode o buscador e reescreva, com um sim.

## Peças

Com tela, `docs/sia/visual.md` tem a seção **Peças**. Cada linha é o nome do arquivo e a frase do que ele faz. Na primeira cara, a seção nasce com a linha `Nenhuma ainda.` Sem tela, essa seção não existe.

Antes de criar botão, card, campo ou peça parecida, procure no código e nessa lista. Se achar, a tela usa essa. Diga à pessoa: "Esse botão já existe. Vou usar o mesmo." Troque "botão" pela peça.

Se não achar, o plano escreve o nome. O arquivo nasce uma vez. A lista ganha a linha no lugar de `Nenhuma ainda.` A próxima tela usa esse nome. Dois arquivos para a mesma peça não passam.

Botão que salva, envia ou apaga fica desabilitado do clique até a ação terminar. O segundo clique não dispara de novo. Na cara, isso acompanha o estado carregando.

## O buscador

O script fica ao lado desta skill:

`vendor/ui-ux-pro-max/scripts/search.py`

Ache pelo diretório desta `SKILL.md`. Não dependa da pasta em que o comando acordou. Python 3, sem pacote extra. Se `python3` faltar, tente `python`.

Stacks permitidas na busca de implementação: `nextjs`, `react`, `html-tailwind`, `shadcn`. Se o combinado ou `docs/sia/escolhas.md` disser Next.js, a stack é `nextjs`. Nunca deixe a stack no escuro na busca de implementação. O modo `--design-system` não aceita stack; a stack vai na busca separada.

## Passos

Estes passos são a cara com tela. Sem tela, pare na seção anterior.

1. Tire do combinado o tipo de produto, quem usa e as palavras de estilo.
2. Para site novo ou direção nova, rode o design system. O buscador ignora `--stack` neste modo, então a stack vai numa busca separada no passo 5.

```bash
python3 "<dir-desta-skill>/vendor/ui-ux-pro-max/scripts/search.py" "<tipo> <palavras>" --design-system -p "Nome" -f markdown
```

Uma intenção, 2 a 5 palavras. Não use `--persist`: o mestre do SIA é `docs/sia/visual.md`, escrito por você, para não nascer um segundo arquivo em `design-system/`.

3. Grave o resultado em `docs/sia/visual.md` com: padrão de página, estilo, cores, letras, efeitos, o que evitar, os estados do combinado (vazio, carregando, erro, sem permissão, deu certo), e a seção **Peças** com a linha `Nenhuma ainda.` Mostre o resumo à pessoa em frases curtas e pare até o sim.
4. Se o arquivo já existe, não rode de novo. Uma página específica pode ganhar um trecho "Página: nome" no mesmo arquivo, sem apagar o mestre.
5. Busca extra só para uma dúvida pontual, uma intenção por comando. A stack do projeto entra numa busca própria, separada da de UX:

```bash
python3 "<dir-desta-skill>/vendor/ui-ux-pro-max/scripts/search.py" "<dúvida>" --domain ux
python3 "<dir-desta-skill>/vendor/ui-ux-pro-max/scripts/search.py" "<assunto da tela>" --stack nextjs
```

Troque `nextjs` pela stack real (`react`, `html-tailwind` ou `shadcn`).

Domínios úteis em site: `ux`, `style`, `color`, `typography`, `landing`, `product`, `chart`, `icons`. Se vier vazio, tente uma vez mais estreito. Se continuar vazio, diga que não houve match e que o que segue é fallback. Não finja que a busca devolveu dado.

6. Antes de dar a tela por pronta, leia `vendor/ui-ux-pro-max/references/pro-rules.md` e `vendor/ui-ux-pro-max/references/quick-reference.md` no que cabe a site, e confira: contraste 4.5:1, foco visível, rótulo de verdade no campo, alvo de toque, 375, 768 e 1280, ícone de verdade, carregando, erro, `prefers-reduced-motion`, o botão que salva, envia ou apaga desabilitado até a ação acabar, mais os estados escritos no combinado.

## Prioridade quando houver várias falhas

Acessibilidade, toque, performance, consistência com o mestre, layout, tipo e cor, movimento, formulário, navegação. A primeira que quebra confiança vem primeiro.

## Desculpas

| Desculpa | Resposta |
| --- | --- |
| "Gero a cara de novo, a anterior estava genérica" | Sem sim, o mestre fica. |
| "É só backend, mas já ajusto a cor" | Sem tela, o arquivo registra isso e para. Não invente página. |
| "Uso a paleta que eu gosto" | A paleta sai da busca ou do mestre, não do gosto solto. |
| "Faço um botão novo, é mais rápido" | Procure a lista de Peças. Se existe, use. |
| "O segundo clique é raro" | Enquanto salva, envia ou apaga, o botão não aceita de novo. |
| "Mobile nativo também" | Esta skill não consulta stack de aplicativo nativo. |
