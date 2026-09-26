"""Update EGE statistics while preserving README content outside the markers."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
START = "<!-- EGE_STATS_START -->"
END = "<!-- EGE_STATS_END -->"


def update_stats(root: Path) -> None:
    tasks = sorted(
        (path for path in root.iterdir()
         if path.is_dir() and path.name.isascii() and path.name.isdigit()),
        key=lambda path: (int(path.name), path.name),
    )
    stats = [(path.name, sum(file.is_file() for file in path.rglob("*.py")))
             for path in tasks]
    practice = root / "practice tests"
    variants = sum(path.is_dir() for path in practice.iterdir()) if practice.is_dir() else 0
    lines = [
        f"**Всего решено задач: {sum(count for _, count in stats)}**",
        "",
        f"**Решено вариантов: {variants}**",
        "",
        "| Задание | Решено |",
        "|---------|--------|",
        *(f"| {number} | {count} |" for number, count in stats),
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
