import subprocess
from collections import Counter
from pathlib import Path


subprocess.run(["git", "add", "."], check=True)

result = subprocess.run(
    ["git", "diff", "--cached", "--name-only", "--diff-filter=A"],
    capture_output=True,
    text=True,
    check=True
)

tasks = Counter()

for file in result.stdout.splitlines():
    path = Path(file)

    if path.suffix != ".py":
        continue

    for part in path.parts[:-1]:
        if part.isdigit():
            tasks[part] += 1
            break

if not tasks:
    print("No new EGE tasks found.")
    exit()

total = sum(tasks.values())

details = ", ".join(
    f"{number}: +{count}"
    for number, count in sorted(tasks.items(), key=lambda x: int(x[0]))
)

message = f"EGE: +{total} tasks [{details}]"

print(message)

subprocess.run(["git", "commit", "-m", message], check=True)

