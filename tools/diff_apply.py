import pathlib
import subprocess
import sys
import tempfile

ALLOWED = ("src/", "tests/")


def allowed_patch(p: str) -> bool:
    return any(p.startswith(a) for a in ALLOWED)


def main() -> None:
    diff = sys.stdin.read()
    # Quick path guard: only allow changes under ALLOWED
    for line in diff.splitlines():
        if line.startswith("+++ b/"):
            path = line.split("b/", 1)[1]
            if not allowed_patch(path):
                raise SystemExit(f"blocked path: {path}")
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(diff.encode("utf-8"))
        patch = f.name
    subprocess.check_call(["git", "apply", "--whitespace=nowarn", patch])
    pathlib.Path(patch).unlink(missing_ok=True)


if __name__ == "__main__":
    main()
