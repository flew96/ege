"""Update EGE statistics while preserving README content outside the markers."""

import re
from collections import Counter
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
START = "<!-- EGE_STATS_START -->"
END = "<!-- EGE_STATS_END -->"
# Task folders and files: "09", "19-21", "3_27269.ods", "18_29350 (1).ods".
TASK = re.compile(r"(\d+)(?:-(\d+))?(?=$|_)", re.ASCII)
SPREADSHEETS = {".ods", ".xls", ".xlsx"}


def task_numbers(name: str) -> range | None:
    """Return the task numbers named by a folder or file name, if any."""
    if not (match := TASK.match(name)):
        return None
    first = int(match[1])
    last = int(match[2]) if match[2] else first
    return range(first, last + 1) if first <= last else None


def solutions(files, base: Path):
    """Yield the tasks of every solution: a .py file, or a spreadsheet without one."""
    found = []
    for file in files:
        if not file.is_file() or file.suffix.lower() not in {".py", *SPREADSHEETS}:
            continue
        # Use the first task folder below the base, or else a filename like 12.py.
        tasks = next(
            (numbers for part in file.relative_to(base).parts[:-1]
             if (numbers := task_numbers(part))),
            None,
        ) or task_numbers(file.stem)
        if tasks:
            found.append((file, tasks))
    scripts = {(file.parent, tasks) for file, tasks in found if file.suffix == ".py"}
    for file, tasks in found:
        if file.suffix == ".py" or (file.parent, tasks) not in scripts:
            yield tasks


def badge(label: str, value: int, color: str) -> str:
    url = f"https://img.shields.io/badge/{quote(label)}-{value}-{color}"
    return f"![{label}: {value}]({url}?style=for-the-badge&labelColor=1e293b)"


def update_stats(root: Path) -> None:
    counts = Counter()
    for path in root.iterdir():
        if path.is_dir() and (numbers := task_numbers(path.name)):
            counts.update({number: 0 for number in numbers})
            for tasks in solutions(path.rglob("*"), root):
                counts.update(tasks)
    practice = root / "practice tests"
    variants = [path for path in practice.iterdir() if path.is_dir()] if practice.is_dir() else []
    for variant in variants:
        for tasks in solutions(variant.rglob("*"), variant):
            counts.update(tasks)
    stats = sorted(counts.items())
    lines = [
        badge("Всего решено задач", sum(counts.values()), "6366f1") + " "
        + badge("Решено вариантов", len(variants), "14b8a6"),
        "",
        "### Решения по заданиям",
        "",
        "| Задание | Решено |",
        "|:-------:|-------:|",
        *(f"| {number} | {count} |" for number, count in stats),
        "",
        "<sub>Учитываются отдельные задачи и задачи из вариантов. "
        "Файл с задачами 19–21 засчитывается за каждую из трёх.</sub>",
    ]
    readme = root / "README.md"
    original = readme.read_bytes() if readme.exists() else b""
    text = original.decode("utf-8")
    newline = "\r\n" if "\r\n" in text else "\n"
    content = newline + newline.join(lines) + newline
    if text.count(START) > 1 or text.count(END) > 1:
        raise ValueError("README.md contains duplicate statistics markers")
    if START in text and END in text:
        start = text.index(START) + len(START)
        end = text.index(END)
        if start > end:
            raise ValueError("README.md statistics markers are in the wrong order")
        updated = text[:start] + content + text[end:]
    elif START in text:
        updated = text.replace(START, START + content + END, 1)
    elif END in text:
        updated = text.replace(END, START + content + END, 1)
    else:
        separator = "" if not text or text.endswith(newline * 2) else (
            newline if text.endswith(newline) else newline * 2
        )
        heading = "" if any(line.strip() == "## 📊 Статистика" for line in text.splitlines()) else (
            "## 📊 Статистика" + newline * 2
        )
        updated = text + separator + heading + START + content + END + newline
    encoded = updated.encode("utf-8")
    if encoded != original:
        readme.write_bytes(encoded)


if __name__ == "__main__":
    update_stats(ROOT)
