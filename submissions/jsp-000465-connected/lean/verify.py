"""Reproduce and audit the vendored JSP-000465 Lean certificate."""

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
THEOREMS = [
    "CompactnessConjecture.quantitativeCompactnessCounterexample",
    "CompactnessConjecture.compactnessCounterexample_bigO",
    "CompactnessConjecture.not_erdos_180",
]
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}

def run(cmd):
    p = subprocess.run(cmd, cwd=ROOT, text=True, encoding="utf-8",
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(p.stdout, end="")
    if p.returncode:
        raise SystemExit(p.returncode)
    return p.stdout

def main():
    source = (ROOT / "CompactnessAndDegeneracy.lean").read_text(encoding="utf-8")
    if re.search(r"(?<![A-Za-z])(sorry|admit)(?![A-Za-z])", source):
        raise SystemExit("Unexpected sorry/admit token in certificate source")

    run(["lake", "build", "CompactnessAndDegeneracy"])
    output = run(["lake", "env", "lean", "JSP465Audit.lean"])

    for name in THEOREMS:
        pattern = rf"'{re.escape(name)}' depends on axioms:\s*\[([^\]]*)\]"
        m = re.search(pattern, output)
        if not m:
            raise SystemExit(f"Missing axiom audit for {name}")
        axioms = {x.strip() for x in m.group(1).split(",") if x.strip()}
        unexpected = axioms - ALLOWED
        if unexpected:
            raise SystemExit(f"Unexpected axioms for {name}: {sorted(unexpected)}")
        if "sorryAx" in axioms:
            raise SystemExit(f"{name} depends on sorryAx")

    print("PASS: complete source builds and all target theorems pass the transitive axiom audit")

if __name__ == "__main__":
    main()
