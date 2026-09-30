"""Update EGE statistics while preserving README content outside the markers."""

from collections import Counter
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
START = "<!-- EGE_STATS_START -->"
END = "<!-- EGE_STATS_END -->"


def badge(label: str, value: int, color: str) -> str:
    url = f"https://img.shields.io/badge/{quote(label)}-{value}-{color}"
    return f"![{label}: {value}]({url}?style=for-the-badge&labelColor=1e293b)"


def update_stats(root: Path) -> None:
    tasks = sorted(
        (path for path in root.iterdir()
         if path.is_dir() and path.name.isascii() and path.name.isdigit()),
        key=lambda path: (int(path.name), path.name),
    )
    counts = Counter({path.name: sum(file.is_file() for file in path.rglob("*.py"))
                      for path in tasks})
    practice = root / "practice tests"
    variants = [path for path in practice.iterdir() if path.is_dir()] if practice.is_dir() else []
    for variant in variants:
        for file in variant.rglob("*.py"):
            if not file.is_file():
                continue
            # Ignore the variant's own name; use a task folder or a filename like 12.py.
            number = next(
                (part for part in file.relative_to(variant).parts[:-1]
                 if part.isascii() and part.isdigit()),
                file.stem,
            )
            if number.isascii() and number.isdigit():
                counts[str(int(number))] += 1
    stats = sorted(counts.items(), key=lambda item: (int(item[0]), item[0]))
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
        "<sub>Учитываются отдельные задачи и задачи из вариантов.</sub>",
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
