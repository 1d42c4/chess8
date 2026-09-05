#!/usr/bin/env python3
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib, sys, re

root=Path(__file__).resolve().parents[1]
lesson_dir=root/"lessons"
lessons=list(lesson_dir.rglob("[0-9]*.html"))

class P(HTMLParser):
    def __init__(self):
        super().__init__(); self.refs=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        for k in ("href","src"):
            if d.get(k): self.refs.append(d[k])

broken=[]
for page in root.rglob("*.html"):
    parser=P()
    try:
        parser.feed(page.read_text(encoding="utf-8"))
    except Exception as e:
        broken.append((page.relative_to(root),f"parse error: {e}"))
        continue
    for ref in parser.refs:
        if not ref or ref.startswith(("#","http://","https://","mailto:","javascript:","data:")): continue
        path=unquote(urlsplit(ref).path)
        if not path: continue
        target=(page.parent/path).resolve()
        try: target.relative_to(root)
        except ValueError:
            broken.append((page.relative_to(root),ref)); continue
        if not target.exists(): broken.append((page.relative_to(root),ref))

too_short=[]
for p in lessons:
    if p.stat().st_size < 6500:
        too_short.append((p.name,p.stat().st_size))

# Detect exact duplicate lesson files (should not happen).
hashes={}
dupes=[]
for p in lessons:
    h=hashlib.sha256(p.read_bytes()).hexdigest()
    if h in hashes: dupes.append((hashes[h],p.name))
    hashes[h]=p.name

print("Lesson pages:",len(lessons))
print("All HTML pages:",sum(1 for _ in root.rglob("*.html")))
print("Broken local links:",len(broken))
print("Lesson pages under 6500 bytes:",len(too_short))
print("Exact duplicate lessons:",len(dupes))

if broken:
    for x in broken[:50]: print("BROKEN",x)
if too_short:
    for x in too_short[:20]: print("SHORT",x)
if dupes:
    for x in dupes[:20]: print("DUPLICATE",x)

if len(lessons)!=1000 or broken or too_short or dupes:
    sys.exit(1)
print("SITE AUDIT PASSED")
