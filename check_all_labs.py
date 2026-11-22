import subprocess
import sys
from pathlib import Path

ROOT = Path(".")
LAB_FILES = sorted(ROOT.glob("lab/**/ch*.py"))

if not LAB_FILES:
    print("No lab Python files found.")
    sys.exit(1)

failed = []

for lab_file in LAB_FILES:
    print("\n" + "=" * 70)
    print(f"CHECKING: {lab_file}")
    print("=" * 70)

    result = subprocess.run(
        [sys.executable, "auto_grader.py", str(lab_file)]
    )

    if result.returncode != 0:
        failed.append(str(lab_file))

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

if failed:
    print(f"{len(failed)} file(s) failed:")
    for f in failed:
        print(f"- {f}")
    sys.exit(1)
else:
    print("All lab files passed.")
