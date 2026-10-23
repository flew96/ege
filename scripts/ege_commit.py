"""Stage repository changes and commit with a summary of new EGE solutions."""

import subprocess
from collections import Counter
from pathlib import Path, PurePosixPath

from update_stats import solutions, task_numbers

ROOT = Path(__file__).resolve().parent.parent


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True,
        text=True, encoding="utf-8", errors="surrogateescape",
    ).stdout


def variants(paths: str) -> set:
    return {
        parts[1]
        for name in paths.split("\0")
        if len(parts := PurePosixPath(name).parts) >= 3
        and parts[0] == "practice tests"
    }


def main() -> None:
    git("add", ".")
    if not git("diff", "--cached", "--name-only", "-z"):
        print("No changes to commit.")
        return

    tasks = Counter()
    added = [
        ROOT / name
        for name in git("diff", "--cached", "--name-only", "--diff-filter=A", "-z").split("\0")
        if len(parts := PurePosixPath(name).parts) >= 2 and task_numbers(parts[0])
    ]
    for numbers in solutions(added, ROOT):
        tasks.update(numbers)

    has_head = subprocess.run(
        ["git", "rev-parse", "--verify", "HEAD"], cwd=ROOT,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    ).returncode == 0
    previous = git("ls-tree", "-r", "--name-only", "-z", "HEAD", "--", "practice tests/") if has_head else ""
    added_variants = variants(git("ls-files", "-z", "--", "practice tests/")) - variants(previous)

    summary = []
    if tasks:
        details = ", ".join(
            f"{number}: +{count}"
            for number, count in sorted(tasks.items())
        )
        summary.append(f"+{sum(tasks.values())} tasks [{details}]")
    if added_variants:
        summary.append(f"practice tests: +{len(added_variants)}")
    message = "EGE: " + ("; ".join(summary) or "update files")
    subprocess.run(["git", "commit", "-m", message], cwd=ROOT, check=True)


if __name__ == "__main__":
    main()
