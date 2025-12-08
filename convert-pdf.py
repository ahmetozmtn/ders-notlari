import os
import re
import subprocess
import markdown

BASE = "guz-donemi"


def extract_number(filename):
    m = re.search(r"(\d+)", filename)
    return int(m.group(1)) if m else 999999


for course in os.listdir(BASE):
    cpath = os.path.join(BASE, course)
    if not os.path.isdir(cpath):
        continue

    merged_md = ""

    files = [f for f in os.listdir(cpath) if f.endswith(".md")]
    files = sorted(files, key=extract_number)   # <<< NUMARAYA GÖRE SIRALA

    for fname in files:
        with open(os.path.join(cpath, fname), "r", encoding="utf-8") as f:
            merged_md += "\n\n" + f.read()

    html = markdown.markdown(merged_md, extensions=["fenced_code", "tables"])
    html_path = os.path.join(cpath, "merged.html")

    with open(html_path, "w", encoding="utf-8") as f:
        f.write("<meta charset='utf-8'>\n" + html)

    pdf_name = f"{course}.pdf"
    subprocess.run(["wkhtmltopdf", html_path, pdf_name])

    print(f"{course} → {pdf_name}")
