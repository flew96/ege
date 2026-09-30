"""Run with: python -m unittest discover -s tests -v."""

import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("update_stats", ROOT / "scripts/update_stats.py")
stats = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stats)


class RepositoryTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def write(self, name, content="pass\n"):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content.encode("utf-8"))
        return path


class StatisticsTests(RepositoryTest):
    def test_counts_and_preserves_surrounding_bytes(self):
        self.write("16/3200-158.py")
        self.write("16/nested/решение.py")
        (self.root / "2").mkdir()
        (self.root / "16/not-a-file.py").mkdir()
        self.write("16/data.txt")
        self.write("practice tests/123/17/nested/solution.py")
        (self.root / "practice tests/empty").mkdir()
        self.write("practice tests/link.txt")
        for folder in (".git", ".github", "scripts", "tests"):
            self.write(f"{folder}/18/ignored.py")
        before = "# Подготовка\r\n\r\n" + stats.START
        after = stats.END + "\r\nСсылки\r\n"
        readme = self.write("README.md", before + "\r\nold\r\n" + after)
        stats.update_stats(self.root)
        result = readme.read_bytes()
        self.assertTrue(result.startswith(before.encode()))
        self.assertTrue(result.endswith(after.encode()))
        self.assertIn("**Всего решено задач: 3**".encode(), result)
        self.assertIn("**Решено вариантов: 2**".encode(), result)
        self.assertIn(b"| 2 | 0 |\r\n| 16 | 2 |", result)
        self.assertIn(b"| 17 | 1 |", result)
        stats.update_stats(self.root)
        self.assertEqual(readme.read_bytes(), result)

    def test_practice_solutions_join_task_totals(self):
        self.write("13/any-name.py")
        self.write("practice tests/123/12.py")
        self.write("practice tests/123/13/13.py")
        self.write("practice tests/123/17/nested/any-name.py")
        self.write("practice tests/second/13.py")
        self.write("practice tests/123/helper.py")
        self.write("practice tests/123/12.txt")
        self.write("practice tests/12.py")
        stats.update_stats(self.root)
        text = (self.root / "README.md").read_text()
        self.assertIn("**Всего решено задач: 5**", text)
        self.assertIn("**Решено вариантов: 2**", text)
        self.assertIn("| 12 | 1 |\n| 13 | 3 |\n| 17 | 1 |", text)
        self.assertNotIn("| 123 |", text)

    def test_missing_readme_and_markers(self):
        readme = self.root / "README.md"
        for original in (None, "", "# Intro\n", "## 📊 Статистика\n", stats.START, stats.END):
            with self.subTest(original=original):
                if original is not None:
                    self.write("README.md", original)
                stats.update_stats(self.root)
                result = readme.read_bytes()
                text = result.decode()
                self.assertEqual(text.count(stats.START), 1)
                self.assertEqual(text.count(stats.END), 1)
                self.assertLess(text.index(stats.START), text.index(stats.END))
                self.assertIn("**Решено вариантов: 0**", text)
                if original and stats.START not in original and stats.END not in original:
                    self.assertTrue(text.startswith(original))
                stats.update_stats(self.root)
                self.assertEqual(readme.read_bytes(), result)

    def test_invalid_markers_do_not_change_file(self):
        for original in (stats.END + stats.START, stats.START * 2 + stats.END, stats.START + stats.END * 2):
            readme = self.write("README.md", original)
            with self.assertRaises(ValueError):
                stats.update_stats(self.root)
            self.assertEqual(readme.read_bytes(), original.encode())


class CommitTests(RepositoryTest):
    def setUp(self):
        super().setUp()
        self.git("init", "-q")
        self.git("config", "user.name", "Test")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "commit.gpgsign", "false")
        self.git("config", "core.hooksPath", str(self.root / "no-hooks"))
        (self.root / "scripts").mkdir()
        shutil.copyfile(ROOT / "scripts/ege_commit.py", self.root / "scripts/ege_commit.py")

    def git(self, *args):
        return subprocess.run(
            ["git", *args], cwd=self.root, check=True, capture_output=True,
            text=True, encoding="utf-8",
        ).stdout.strip()

    def commit(self):
        subprocess.run(
            [sys.executable, str(self.root / "scripts/ege_commit.py")],
            cwd=self.root / "scripts", check=True, capture_output=True,
        )
        self.assertEqual(self.git("status", "--porcelain"), "")
        return self.git("log", "-1", "--format=%s")

    def test_new_tasks_and_variants_are_separate(self):
        self.write("16/nested/решение с пробелом.py")
        self.write("16/other.py")
        self.write("practice tests/123/17/solution.py")
        self.write("practice tests/123/16.py")
        self.write("practice tests/Вариант 2/2.py")
        self.write("scripts/99/ignored.py")
        self.assertEqual(self.commit(), "EGE: +2 tasks [16: +2]; practice tests: +2")
        self.write("practice tests/123/18.py")
        self.assertEqual(self.commit(), "EGE: update files")
        self.write("practice tests/456/18.py")
        self.assertEqual(self.commit(), "EGE: practice tests: +1")

    def test_edits_deletions_and_no_changes(self):
        path = self.write("16/solution.py")
        self.assertEqual(self.commit(), "EGE: +1 tasks [16: +1]")
        path.write_text("print(42)\n")
        self.assertEqual(self.commit(), "EGE: update files")
        path.unlink()
        self.assertEqual(self.commit(), "EGE: update files")
        head = self.git("rev-parse", "HEAD")
        self.commit()
        self.assertEqual(self.git("rev-parse", "HEAD"), head)


if __name__ == "__main__":
    unittest.main()
