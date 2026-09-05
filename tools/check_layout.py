from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib, json, re, sys

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / 'SOURCE_MANIFEST.json').read_text(encoding='utf-8'))
site = urlsplit(manifest['website'])

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('href', 'src', 'action') and value:
                self.links.append(value)

def resolve(page, ref):
    parsed = urlsplit(ref)
    if parsed.scheme or parsed.netloc:
        if parsed.netloc != site.netloc or not parsed.path.startswith(site.path):
            return None
        target = root / unquote(parsed.path[len(site.path):])
    elif parsed.path.startswith('/'):
        if not parsed.path.startswith(site.path): return None
        target = root / unquote(parsed.path[len(site.path):])
    elif parsed.path:
        target = page.parent / unquote(parsed.path)
    else: return None
    target = target.resolve()
    target.relative_to(root)
    return target

errors, checked, widths = [], 0, []
for directory in [root, *root.rglob('*')]:
    if not directory.is_dir() or '.git' in directory.relative_to(root).parts: continue
    count = sum(1 for p in directory.iterdir() if p.name != '.git')
    widths.append((str(directory.relative_to(root)), count))
    if count >= 1000: errors.append(f'Directory has {count} entries: {directory}')
for page in root.rglob('*'):
    if '.git' in page.relative_to(root).parts or page.suffix not in ('.html', '.md', '.xml'): continue
    text = page.read_text(encoding='utf-8')
    if page.suffix == '.html':
        parser = Links(); parser.feed(text); refs = parser.links
    elif page.suffix == '.md': refs = re.findall(r'\]\(([^\s)]+)\)', text)
    else: refs = re.findall(r'<loc>(.*?)</loc>', text)
    for ref in refs:
        try:
            target = resolve(page, ref)
            if target is not None:
                checked += 1
                if not target.exists(): errors.append(f'{page.relative_to(root)} -> {ref}')
        except ValueError: errors.append(f'Path escapes repository: {ref}')
lessons = list((root / 'lessons').rglob('*.html'))
if len(lessons) != 1000: errors.append(f'Expected 1000 lessons, found {len(lessons)}')
for entry in manifest['files']:
    p = root / entry['path']
    if not p.is_file(): errors.append(f'Missing original file: {entry["path"]}'); continue
    content = p.read_bytes()
    if len(content) != entry['uploadedBytes'] or hashlib.sha256(content).hexdigest() != entry['uploadedSha256']:
        errors.append(f'Manifest checksum differs: {entry["path"]}')
home = (root / 'index.html').read_text(encoding='utf-8')
match = re.search(r'const ITEMS=(\[[^\r\n]+\]);', home)
if match:
    items = json.loads(match[1]); targets = {resolve(root / 'index.html', item['url']) for item in items}
    if targets != {p.resolve() for p in lessons}: errors.append('Search index does not contain exactly the 1000 lesson paths')
report = {'lessons': len(lessons), 'directories': len(widths), 'maximumEntries': max(n for _, n in widths), 'localReferencesChecked': checked, 'originalFilesRetained': len(manifest['files']), 'errors': errors, 'passed': not errors}
print(json.dumps(report, indent=2))
sys.exit(bool(errors))
