import argparse
import ast
import json
import os

IGNORE = {".git", "__pycache__", "node_modules", ".venv", ".rag"}


def parse_python(path: str) -> list[str]:
    with open(path, encoding="utf-8") as f:
        tree = ast.parse(f.read())
    symbols = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            symbols.append(f"def {node.name}(...):")
        elif isinstance(node, ast.AsyncFunctionDef):
            symbols.append(f"async def {node.name}(...):")
        elif isinstance(node, ast.ClassDef):
            symbols.append(f"class {node.name}:")
    return symbols


def walk(root: str) -> dict[str, list[str] | str]:
    out: dict[str, list[str] | str] = {}
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in IGNORE]
        for fn in fns:
            p = os.path.join(dp, fn)
            rp = os.path.relpath(p, root)
            if fn.endswith(".py"):
                out[rp] = parse_python(p)
            else:
                out[rp] = "non-python"
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--out", default="repo_map.json")
    a = ap.parse_args()
    data = walk(a.root)
    with open(a.out, "w") as f:
        json.dump(data, f, indent=2)
    print(f"wrote {a.out}")
