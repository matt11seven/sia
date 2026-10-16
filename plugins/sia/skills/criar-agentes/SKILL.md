---
name: criar-agentes
description: >
  Use quando a pessoa pedir um agente, um time ou um squad, ou quando o
  combinado aprovado disser que o trabalho precisa de papéis separados.
  Escreve squads/<nome>/ na forma canônica, em português, e só depois do
  sim. Não use para construir o sistema: isso continua numa conversa só.
  Gatilhos: "cria um agente", "um time de agentes", "um squad", "papéis
  separados".
---

> A pasta segue os squads do aiox-core, licença MIT. O clone local fica em `references/aiox-core`, fora do Git. Ficaram o manifesto, os papéis, as tarefas, o fluxo e a lista. Saíram saudação, signo, ícone e publicação em mercado. A boca é português.

# Criar agentes

Com a pessoa, siga "Como falar" em `comecar`. Não diga o nome desta skill. Abra com **Etapa: o time**. Diga "time". A pasta se chama `squads/`.

Faça nesta sessão. Depois do sim, escreva os arquivos você mesmo e rode o validador. Não chame subagente para isso.

O time é texto. Esta sessão lê e assume um papel por vez. Diga isso à pessoa. Ele não constrói o sistema.

## A lei

Um sistema comum continua nesta conversa. O time nasce em dois casos: a pessoa pediu papéis separados, ou o combinado aprovado diz que o trabalho precisa de mais de um papel.

Até um papel mora em `squads/<id>/`. A forma é a deste arquivo. O `validar.py` ao lado confere. Sem a linha `ok` nesta conversa, o time não existe.

Identificador: letra minúscula, número e hífen, começando em letra, sem acento. O texto que a pessoa lê pode ter acento e fica entre aspas, numa linha.

## Antes de escrever

1. Se o pedido é construir o sistema, pare. Uma frase: isso segue nesta conversa.
2. Se falta o que o time entrega, pergunte isso. Espere.
3. Se faltam os papéis, pergunte quais, ou ofereça o mínimo. Espere.
4. Se já dá para propor, uma mensagem: o nome da pasta, cada papel, o que ele entrega. Espere o sim.
5. Time que já existe: leia a pasta e mude só o que foi pedido.

O mínimo que cobre a entrega. Dois papéis ou mais: um é o chefe e só encaminha. Um papel só não tem chefe.

| Pasta | Entra quando |
| --- | --- |
| `agents/` | sempre, um arquivo por papel |
| `tasks/` | o passo se repete e tem dono |
| `workflows/` | a ordem dos papéis é fixa |
| `checklists/` | existe uma trava antes de entregar |

Pasta vazia não se cria. Lista vazia não se escreve. Na criação, `version` é `"1.0.0"`. Mudança de verdade sobe o último número.

## A forma

Texto de gente entre aspas duplas, numa linha. Identificador e nome de arquivo sem aspas. Sem comentário, sem bloco `|`, sem chave fora da lista abaixo.

`squad.yaml` tem `name`, `version`, `description`, `components`. `components` lista só a pasta que existe: `agents`, `tasks`, `workflows`, `checklists`. O `name` é o nome da pasta.

Cada agente tem `agent` (`name`, `id`, `title`, `whenToUse` e, se houver chefe, `papel`), `persona` (`role`, `style`, `identity`, `focus`), `core_principles` e `commands` (`name`, `description`). O `id` é o nome do arquivo. `papel` é `chefe` ou `especialista`. O chefe não é dono de tarefa e não entra no fluxo.

Cada tarefa tem `task`, `responsavel`, `entrada`, `saida`, `passos`. O arquivo tem o nome do comando desse responsável.

Cada fluxo tem `workflow` com `id`, `name`, `description`, `passos`. Cada passo tem `agente`, `tarefa`, `entrega`. O `id` é o nome do arquivo. A tarefa é daquele agente.

Cada lista tem pelo menos um item `- [ ]`.

O `README.md` começa com o título e, na frase seguinte, a `description`. Cada papel aparece como `` `id` ``.

## Exemplos

Os dois passam no validador. Troque os textos. O estoque não vai para outro pedido. O pequeno é um papel só. O grande mostra as pastas quando elas existem.

### Um papel

#### squads/aviso/squad.yaml

```yaml
name: aviso
version: "1.0.0"
description: "Entra quando um papel só escreve o aviso."
components:
  agents:
    - redator.md
```

#### squads/aviso/README.md

```markdown
# Aviso

Entra quando um papel só escreve o aviso.

## Papéis

- `redator`: Escreve o aviso. Quando já se sabe o que falta.
```

#### squads/aviso/agents/redator.md

````markdown
# Redator

```yaml
agent:
  name: "Redator"
  id: redator
  title: "Escreve o aviso"
  whenToUse: "Quando já se sabe o que falta."
persona:
  role: "Quem escreve o aviso"
  style: "Frase curta. Só o aviso."
  identity: "Entrega o texto e não conta estoque."
  focus: "O aviso que alguém lê e entende."
core_principles:
  - "O aviso diz o que falta e para quem."
commands:
  - name: escrever
    description: "Entrega o aviso em uma frase."
```
````

### Vários papéis

#### squads/estoque/squad.yaml

```yaml
name: estoque
version: "1.0.0"
description: "Entra quando a contagem e o aviso são papéis separados."
components:
  agents:
    - chefe.md
    - contador.md
    - avisador.md
  tasks:
    - contar.md
    - avisar.md
  workflows:
    - avisar.yaml
  checklists:
    - antes-de-entregar.md
```

#### squads/estoque/README.md

```markdown
# Estoque

Entra quando a contagem e o aviso são papéis separados.

## Papéis

- `chefe`: Encaminha a contagem e o aviso. Quando o pedido ainda não tem um papel só.
- `contador`: Conta a diferença. Quando já se sabe o que deveria existir.
- `avisador`: Avisa quem decide. Quando a diferença já saiu.
```

#### squads/estoque/agents/chefe.md

````markdown
# Chefe

```yaml
agent:
  name: "Chefe do estoque"
  id: chefe
  title: "Encaminha a contagem e o aviso"
  whenToUse: "Quando o pedido ainda não tem um papel só."
  papel: chefe
persona:
  role: "Chefe do time"
  style: "Uma pergunta. Encaminha e não faz o trabalho dos outros."
  identity: "Dono da ordem entre contar e avisar."
  focus: "Escolher o papel e devolver o que saiu."
core_principles:
  - "Um papel, um entregável."
  - "A contagem vem antes do aviso."
commands:
  - name: encaminhar
    description: "Escolhe o papel e devolve o que ele entregou."
```
````

#### squads/estoque/agents/contador.md

````markdown
# Contador

```yaml
agent:
  name: "Contador"
  id: contador
  title: "Conta a diferença"
  whenToUse: "Quando já se sabe o que deveria existir."
  papel: especialista
persona:
  role: "Quem conta"
  style: "Número e item. Sem aviso."
  identity: "Compara o que deveria existir com o que existe."
  focus: "A diferença, só."
core_principles:
  - "Diferença sem item não é contagem."
commands:
  - name: contar
    description: "Devolve a diferença entre o esperado e o que existe."
```
````

#### squads/estoque/agents/avisador.md

````markdown
# Avisador

```yaml
agent:
  name: "Avisador"
  id: avisador
  title: "Avisa quem decide"
  whenToUse: "Quando a diferença já saiu."
  papel: especialista
persona:
  role: "Quem avisa"
  style: "Uma frase. O que falta e para quem."
  identity: "Escreve o aviso a partir da diferença."
  focus: "O aviso que alguém consegue executar."
core_principles:
  - "Aviso sem destinatário não sai."
commands:
  - name: avisar
    description: "Entrega o aviso com o que falta e para quem."
```
````

#### squads/estoque/tasks/contar.md

````markdown
# Contar

```yaml
task: "Contar a diferença"
responsavel: contador
entrada: "A lista do que deveria existir."
saida: "A diferença, com item e quantidade."
passos:
  - "Ler a lista do que deveria existir."
  - "Comparar com o que está no lugar."
  - "Devolver só a diferença."
```
````

#### squads/estoque/tasks/avisar.md

````markdown
# Avisar

```yaml
task: "Avisar quem decide"
responsavel: avisador
entrada: "A diferença já contada."
saida: "O aviso com o que falta e para quem."
passos:
  - "Ler a diferença."
  - "Escrever o aviso numa frase."
  - "Dizer para quem ele vai."
```
````

#### squads/estoque/workflows/avisar.yaml

```yaml
workflow:
  id: avisar
  name: "Avisar o estoque"
  description: "Roda quando a ordem é contar e depois avisar."
  passos:
    - agente: contador
      tarefa: contar
      entrega: "A diferença, com item e quantidade."
    - agente: avisador
      tarefa: avisar
      entrega: "O aviso com o que falta e para quem."
```

#### squads/estoque/checklists/antes-de-entregar.md

```markdown
# Antes de entregar

- [ ] A diferença tem item e quantidade.
- [ ] O aviso diz o que falta e para quem.
```

## Conferir

Na pasta do projeto da pessoa, com o `validar.py` que está ao lado deste arquivo:

```bash
python3 "<pasta desta skill>/validar.py" "squads/<id>"
```

Leia a saída. `ok` fecha a forma. Cada linha `erro` se corrige, e o comando roda de novo.

## O que a pessoa vê

O caminho e os papéis, em frase curta. Ela lê o `README.md` do time.

## Desculpas

| Desculpa | Resposta |
| --- | --- |
| "Um sistema pede um elenco" | Sistema comum continua nesta conversa. |
| "Escrevo e mostro depois" | O sim vem antes do arquivo. |
| "Cada time tem um jeito" | A forma deste arquivo é a única. |
| "Falta ícone, saudação ou signo" | Esses campos não existem. |
| "Crio as pastas vazias" | Pasta sem arquivo não entra. |
| "O validador reclamou, mas está bom" | Reclamar é fora da forma. Ajuste e rode de novo. |
| "Um papel solto na raiz" | Até um papel mora em `squads/<id>/`. |
| "Copio um time que já vi" | O pedido desta pessoa. A forma, não o elenco. |
| "Chamo um subagente para escrever" | Depois do sim, esta conversa escreve e valida. |
| "O time roda sozinho" | O time é texto. Esta sessão assume um papel por vez. |
