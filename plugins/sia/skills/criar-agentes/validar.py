#!/usr/bin/env python3
"""Confere a forma de squads/<id> descrita em SKILL.md. Só a biblioteca padrão."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ID = re.compile(r"^[a-z][a-z0-9-]*$")
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
KEY = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
BARE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
FILE_MD = re.compile(r"^[a-z][a-z0-9-]*\.md$")
FILE_YAML = re.compile(r"^[a-z][a-z0-9-]*\.yaml$")
BOX = re.compile(r"^- \[ \] \S")

COMPONENT_SUFFIX = {
    "agents": FILE_MD,
    "tasks": FILE_MD,
    "workflows": FILE_YAML,
    "checklists": FILE_MD,
}


class Text(str):
    quoted: bool

    def __new__(cls, value: str, quoted: bool) -> "Text":
        obj = str.__new__(cls, value)
        obj.quoted = quoted
        return obj


class Forma(Exception):
    pass


def parse(text: str, origin: str) -> dict:
    lines = _tokenize(text, origin)
    if not lines:
        raise Forma(f"{origin}: vazio")
    if lines[0][1] != 0:
        raise Forma(f"{origin}:{lines[0][0]}: começa na coluna 0")
    value, idx = _node(lines, 0, 0, origin)
    if idx != len(lines):
        raise Forma(f"{origin}:{lines[idx][0]}: sobrou texto")
    if not isinstance(value, dict):
        raise Forma(f"{origin}: começa com campo, não com lista")
    return value


def _tokenize(text: str, origin: str) -> list[tuple[int, int, str]]:
    rows: list[tuple[int, int, str]] = []
    for number, line in enumerate(text.replace("\r\n", "\n").splitlines(), 1):
        if not line.strip():
            continue
        if line.lstrip(" ").startswith("#"):
            raise Forma(f"{origin}:{number}: comentário não entra na forma")
        if "\t" in line:
            raise Forma(f"{origin}:{number}: use espaços")
        indent = len(line) - len(line.lstrip(" "))
        if indent % 2:
            raise Forma(f"{origin}:{number}: recuo de 2 espaços")
        rows.append((number, indent, line.strip()))
    return rows


def _node(lines, idx, indent, origin):
    number, found, content = lines[idx]
    if found != indent:
        raise Forma(f"{origin}:{number}: recuo de {indent} espaços")
    if content.startswith("- "):
        return _list(lines, idx, origin, indent)
    return _map(lines, idx, origin, indent)


def _map(lines, idx, origin, indent):
    result: dict = {}
    while idx < len(lines):
        number, found, content = lines[idx]
        if found < indent:
            break
        if found != indent:
            raise Forma(f"{origin}:{number}: recuo inesperado")
        if content.startswith("- "):
            raise Forma(f"{origin}:{number}: lista no lugar de campo")
        key, sep, raw = content.partition(":")
        if not sep:
            raise Forma(f"{origin}:{number}: falta :")
        key = key.strip()
        raw = raw.strip()
        if not KEY.fullmatch(key):
            raise Forma(f"{origin}:{number}: chave fora da forma")
        if key in result:
            raise Forma(f"{origin}:{number}: chave repetida")
        if raw == "":
            if idx + 1 >= len(lines) or lines[idx + 1][1] != indent + 2:
                raise Forma(f"{origin}:{number}: campo vazio")
            child, idx = _node(lines, idx + 1, indent + 2, origin)
            result[key] = child
            continue
        if raw[0] in "|>" or raw in ("[]", "{}"):
            raise Forma(f"{origin}:{number}: texto numa linha, entre aspas")
        result[key] = _scalar(raw, origin, number)
        idx += 1
    if not result:
        raise Forma(f"{origin}: campo vazio")
    return result, idx


def _list(lines, idx, origin, indent):
    items = []
    while idx < len(lines):
        number, found, content = lines[idx]
        if found < indent:
            break
        if found != indent or not content.startswith("- "):
            raise Forma(f"{origin}:{number}: item de lista fora do lugar")
        rest = content[2:].strip()
        if rest == "":
            raise Forma(f"{origin}:{number}: item vazio")
        if _map_item(rest):
            key, _, raw = rest.partition(":")
            key = key.strip()
            raw = raw.strip()
            if raw == "" or raw[0] in "|>":
                raise Forma(f"{origin}:{number}: texto numa linha, entre aspas")
            item = {key: _scalar(raw, origin, number)}
            idx += 1
            while idx < len(lines) and lines[idx][1] == indent + 2:
                child_number, _, child = lines[idx]
                if child.startswith("- ") or ":" not in child:
                    raise Forma(f"{origin}:{child_number}: item fora da forma")
                child_key, _, child_raw = child.partition(":")
                child_key = child_key.strip()
                child_raw = child_raw.strip()
                if not KEY.fullmatch(child_key):
                    raise Forma(f"{origin}:{child_number}: chave fora da forma")
                if child_key in item:
                    raise Forma(f"{origin}:{child_number}: chave repetida")
                if child_raw == "" or child_raw[0] in "|>":
                    raise Forma(f"{origin}:{child_number}: texto numa linha, entre aspas")
                item[child_key] = _scalar(child_raw, origin, child_number)
                idx += 1
            items.append(item)
            continue
        items.append(_scalar(rest, origin, number))
        idx += 1
    if not items:
        raise Forma(f"{origin}: lista vazia")
    return items, idx


def _map_item(rest: str) -> bool:
    if rest.startswith('"'):
        return False
    key, sep, _raw = rest.partition(":")
    return bool(sep) and KEY.fullmatch(key.strip()) is not None


def _scalar(raw: str, origin: str, number: int) -> Text:
    if raw.startswith('"'):
        if len(raw) < 2 or not raw.endswith('"'):
            raise Forma(f"{origin}:{number}: aspas não fecham")
        inner = raw[1:-1]
        out: list[str] = []
        i = 0
        while i < len(inner):
            if inner[i] == "\\":
                if i + 1 < len(inner) and inner[i + 1] in '"\\':
                    out.append(inner[i + 1])
                    i += 2
                    continue
                raise Forma(f"{origin}:{number}: escape fora da forma")
            if inner[i] == '"':
                raise Forma(f"{origin}:{number}: aspas não fecham")
            out.append(inner[i])
            i += 1
        value = "".join(out)
        if not value.strip():
            raise Forma(f"{origin}:{number}: texto vazio")
        return Text(value, True)
    if raw.startswith("'"):
        raise Forma(f"{origin}:{number}: use aspas duplas")
    if raw in ("true", "false", "null"):
        raise Forma(f"{origin}:{number}: texto numa linha, entre aspas")
    if BARE.fullmatch(raw):
        return Text(raw, False)
    raise Forma(f"{origin}:{number}: texto com espaço ou pontuação vai entre aspas")


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _text(path: Path, origin: str, errors: list[str]) -> str | None:
    if not path.is_file():
        errors.append(f"{origin}: arquivo ausente")
        return None
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        errors.append(f"{origin}: não deu para ler")
        return None


def _yaml_block(text: str, origin: str, errors: list[str], prose: bool) -> str | None:
    text = text.replace("\r\n", "\n")
    if not text.endswith("\n"):
        text += "\n"
    if not re.match(r"# .+\n", text):
        errors.append(f"{origin}: a primeira linha é um título #")
        return None
    blocks = re.findall(r"```yaml\n(.*?)```", text, re.S)
    if len(blocks) != 1 or text.count("```") != 2:
        errors.append(f"{origin}: um bloco yaml")
        return None
    if not prose:
        rest = re.sub(r"\A# .+\n", "", text, count=1)
        rest = re.sub(r"```yaml\n.*?```", "", rest, count=1, flags=re.S)
        if rest.strip():
            errors.append(f"{origin}: só o título e o bloco yaml")
            return None
    return blocks[0]


def _quoted(value, label: str, errors: list[str]) -> str | None:
    if not isinstance(value, Text) or not value.quoted:
        errors.append(f"{label}: entre aspas")
        return None
    return str(value)


def _ident(value, label: str, errors: list[str]) -> str | None:
    if not isinstance(value, Text) or value.quoted or not ID.fullmatch(str(value)):
        errors.append(f"{label}: letra minúscula, número e hífen, sem aspas")
        return None
    return str(value)


def _keys(obj, allowed: set[str], required: set[str], label: str, errors: list[str]) -> bool:
    if not isinstance(obj, dict):
        errors.append(f"{label}: campo com subcampos")
        return False
    ok = True
    for key in sorted(set(obj) - allowed):
        errors.append(f"{label}: campo fora da forma ({key})")
        ok = False
    for key in sorted(required - set(obj)):
        errors.append(f"{label}: falta {key}")
        ok = False
    return ok


def _strings(value, label: str, errors: list[str]) -> list[str] | None:
    if not isinstance(value, list) or not value:
        errors.append(f"{label}: lista com pelo menos um item")
        return None
    found = []
    for item in value:
        text = _quoted(item, label, errors)
        if text is None:
            return None
        found.append(text)
    return found


def _files_of(directory: Path) -> list[str]:
    if not directory.exists():
        return []
    return sorted(p.name for p in directory.iterdir() if not p.name.startswith("."))


def validate(directory: Path) -> tuple[list[str], str]:
    errors: list[str] = []
    directory = directory.resolve()
    if not directory.is_dir():
        return [f"{directory}: pasta inexistente"], ""

    extras = sorted(
        p.name
        for p in directory.iterdir()
        if not p.name.startswith(".") and p.name not in {"squad.yaml", "README.md", "agents", "tasks", "workflows", "checklists"}
    )
    for name in extras:
        errors.append(f"{name}: fora da forma")

    squad_path = directory / "squad.yaml"
    readme_path = directory / "README.md"
    if not squad_path.is_file():
        errors.append("falta squad.yaml")
    if not readme_path.is_file():
        errors.append("falta README.md")
    if errors and (not squad_path.is_file() or not readme_path.is_file()):
        return errors, ""

    try:
        squad = parse(_read(squad_path), "squad.yaml")
    except Forma as exc:
        return errors + [str(exc)], ""
    except (OSError, UnicodeDecodeError):
        return errors + ["squad.yaml: não deu para ler"], ""

    if not _keys(squad, {"name", "version", "description", "components"}, {"name", "version", "description", "components"}, "squad.yaml", errors):
        return errors, ""

    name = _ident(squad["name"], "squad.yaml name", errors)
    version = _quoted(squad["version"], "squad.yaml version", errors)
    description = _quoted(squad["description"], "squad.yaml description", errors)
    if name and name != directory.name:
        errors.append("squad.yaml name: igual ao nome da pasta")
    if version and not SEMVER.fullmatch(version):
        errors.append("squad.yaml version: número.número.número")
    components = squad["components"]
    if not _keys(components, set(COMPONENT_SUFFIX), {"agents"}, "components", errors):
        return errors, ""

    listed: dict[str, list[str]] = {}
    for key, pattern in COMPONENT_SUFFIX.items():
        if key not in components:
            continue
        rows = components[key]
        if not isinstance(rows, list) or not rows:
            errors.append(f"components.{key}: lista com pelo menos um arquivo")
            continue
        names = []
        for item in rows:
            if not isinstance(item, Text) or item.quoted or not pattern.fullmatch(str(item)):
                errors.append(f"components.{key}: arquivo em letra minúscula, sem aspas")
                continue
            names.append(str(item))
        if len(names) != len(set(names)):
            errors.append(f"components.{key}: arquivo repetido")
        listed[key] = names
        on_disk = _files_of(directory / key)
        if sorted(names) != on_disk:
            errors.append(f"{key}: a lista e a pasta divergem")
    for key in COMPONENT_SUFFIX:
        if key in listed:
            continue
        if _files_of(directory / key):
            errors.append(f"{key}: pasta sem entrada em components")

    readme = _text(readme_path, "README.md", errors) or ""
    if description and description not in readme:
        errors.append("README.md: a primeira frase é a description do squad.yaml")

    agents: dict[str, dict] = {}
    for filename in listed.get("agents", []):
        path = directory / "agents" / filename
        text = _text(path, f"agents/{filename}", errors)
        if text is None:
            continue
        block = _yaml_block(text, f"agents/{filename}", errors, prose=False)
        if block is None:
            continue
        try:
            body = parse(block, f"agents/{filename}")
        except Forma as exc:
            errors.append(str(exc))
            continue
        if not _keys(body, {"agent", "persona", "core_principles", "commands"}, {"agent", "persona", "core_principles", "commands"}, f"agents/{filename}", errors):
            continue
        agent = body["agent"]
        many = len(listed.get("agents", [])) > 1
        allowed_agent = {"name", "id", "title", "whenToUse", "papel"} if many else {"name", "id", "title", "whenToUse"}
        required_agent = allowed_agent if many else {"name", "id", "title", "whenToUse"}
        if not _keys(agent, allowed_agent, required_agent, f"agents/{filename} agent", errors):
            continue
        agent_name = _quoted(agent["name"], f"agents/{filename} agent.name", errors)
        agent_id = _ident(agent["id"], f"agents/{filename} agent.id", errors)
        _quoted(agent["title"], f"agents/{filename} agent.title", errors)
        when = _quoted(agent["whenToUse"], f"agents/{filename} agent.whenToUse", errors)
        if agent_id and f"{agent_id}.md" != filename:
            errors.append(f"agents/{filename}: o id é o nome do arquivo")
        if agent_id and f"`{agent_id}`" not in readme:
            errors.append(f"README.md: falta o papel `{agent_id}`")
        papel = None
        if many:
            papel_value = agent["papel"]
            if not isinstance(papel_value, Text) or papel_value.quoted or str(papel_value) not in ("chefe", "especialista"):
                errors.append(f"agents/{filename} agent.papel: chefe ou especialista, sem aspas")
            else:
                papel = str(papel_value)
        persona = body["persona"]
        if _keys(persona, {"role", "style", "identity", "focus"}, {"role", "style", "identity", "focus"}, f"agents/{filename} persona", errors):
            for field in ("role", "style", "identity", "focus"):
                _quoted(persona[field], f"agents/{filename} persona.{field}", errors)
        if _strings(body["core_principles"], f"agents/{filename} core_principles", errors) is None:
            pass
        commands = body["commands"]
        command_names = []
        if isinstance(commands, list):
            for index, command in enumerate(commands, 1):
                label = f"agents/{filename} commands[{index}]"
                if not _keys(command, {"name", "description"}, {"name", "description"}, label, errors):
                    continue
                command_name = _ident(command["name"], f"{label} name", errors)
                _quoted(command["description"], f"{label} description", errors)
                if command_name:
                    command_names.append(command_name)
            if len(command_names) != len(set(command_names)):
                errors.append(f"agents/{filename}: comando repetido")
        else:
            errors.append(f"agents/{filename} commands: lista")
        if agent_id and agent_name and when:
            agents[agent_id] = {"papel": papel, "commands": command_names, "file": filename}

    chefes = [agent_id for agent_id, agent in agents.items() if agent["papel"] == "chefe"]
    if len(listed.get("agents", [])) > 1 and len(chefes) != 1:
        errors.append("um time com mais de um papel tem um chefe")
    chefe = chefes[0] if len(chefes) == 1 else None

    tasks: dict[str, str] = {}
    for filename in listed.get("tasks", []):
        stem = filename[:-3]
        path = directory / "tasks" / filename
        text = _text(path, f"tasks/{filename}", errors)
        if text is None:
            continue
        block = _yaml_block(text, f"tasks/{filename}", errors, prose=True)
        if block is None:
            continue
        try:
            body = parse(block, f"tasks/{filename}")
        except Forma as exc:
            errors.append(str(exc))
            continue
        if not _keys(body, {"task", "responsavel", "entrada", "saida", "passos"}, {"task", "responsavel", "entrada", "saida", "passos"}, f"tasks/{filename}", errors):
            continue
        _quoted(body["task"], f"tasks/{filename} task", errors)
        owner = _ident(body["responsavel"], f"tasks/{filename} responsavel", errors)
        _quoted(body["entrada"], f"tasks/{filename} entrada", errors)
        _quoted(body["saida"], f"tasks/{filename} saida", errors)
        if _strings(body["passos"], f"tasks/{filename} passos", errors) is None:
            pass
        if owner and owner not in agents:
            errors.append(f"tasks/{filename}: responsavel inexistente")
        elif owner and owner == chefe:
            errors.append(f"tasks/{filename}: o chefe não é dono de tarefa")
        elif owner and stem not in agents[owner]["commands"]:
            errors.append(f"tasks/{filename}: o comando {stem} não existe em {owner}")
        tasks[stem] = owner or ""

    for filename in listed.get("workflows", []):
        stem = filename[:-5]
        path = directory / "workflows" / filename
        text = _text(path, f"workflows/{filename}", errors)
        if text is None:
            continue
        try:
            body = parse(text, f"workflows/{filename}")
        except Forma as exc:
            errors.append(str(exc))
            continue
        if not _keys(body, {"workflow"}, {"workflow"}, f"workflows/{filename}", errors):
            continue
        flow = body["workflow"]
        if not _keys(flow, {"id", "name", "description", "passos"}, {"id", "name", "description", "passos"}, f"workflows/{filename} workflow", errors):
            continue
        flow_id = _ident(flow["id"], f"workflows/{filename} workflow.id", errors)
        _quoted(flow["name"], f"workflows/{filename} workflow.name", errors)
        _quoted(flow["description"], f"workflows/{filename} workflow.description", errors)
        if flow_id and flow_id != stem:
            errors.append(f"workflows/{filename}: o id é o nome do arquivo")
        passos = flow["passos"]
        if not isinstance(passos, list):
            errors.append(f"workflows/{filename} workflow.passos: lista")
            continue
        for index, step in enumerate(passos, 1):
            label = f"workflows/{filename} passos[{index}]"
            if not _keys(step, {"agente", "tarefa", "entrega"}, {"agente", "tarefa", "entrega"}, label, errors):
                continue
            worker = _ident(step["agente"], f"{label} agente", errors)
            task_name = _ident(step["tarefa"], f"{label} tarefa", errors)
            _quoted(step["entrega"], f"{label} entrega", errors)
            if worker and worker == chefe:
                errors.append(f"{label}: o chefe não entra no fluxo")
            elif worker and worker not in agents:
                errors.append(f"{label}: agente inexistente")
            if task_name and task_name not in tasks:
                errors.append(f"{label}: tarefa inexistente")
            elif task_name and worker and tasks.get(task_name) not in (None, "", worker):
                errors.append(f"{label}: a tarefa {task_name} é de {tasks[task_name]}")

    for filename in listed.get("checklists", []):
        text = _text(directory / "checklists" / filename, f"checklists/{filename}", errors)
        if text is None:
            continue
        if not any(BOX.match(line.strip()) for line in text.splitlines()):
            errors.append(f"checklists/{filename}: pelo menos um item - [ ]")

    bits = [f"{len(listed.get('agents', []))} {'papel' if len(listed.get('agents', [])) == 1 else 'papéis'}"]
    for key, one, many in (("tasks", "tarefa", "tarefas"), ("workflows", "fluxo", "fluxos"), ("checklists", "lista", "listas")):
        count = len(listed.get(key, []))
        if count:
            bits.append(f"{count} {one if count == 1 else many}")
    return errors, f"ok: {directory.name} ({', '.join(bits)})"


def main() -> int:
    if len(sys.argv) != 2:
        print("erro: use validar.py squads/<id>", file=sys.stderr)
        return 2
    errors, summary = validate(Path(sys.argv[1]))
    if errors:
        for error in errors:
            print(f"erro: {error}")
        return 1
    print(summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
