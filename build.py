"""Χτίζει το index.html από το src/template.html και τα δεδομένα στο data/."""
from pathlib import Path

root = Path(__file__).parent
html = (root / "src/template.html").read_text(encoding="utf-8")
html = html.replace("__DATA__", (root / "data/sports.json").read_text(encoding="utf-8"))
html = html.replace("__DK__", (root / "data/koinotites.json").read_text(encoding="utf-8"))
(root / "index.html").write_text(html, encoding="utf-8")
print("index.html", len(html), "bytes")
