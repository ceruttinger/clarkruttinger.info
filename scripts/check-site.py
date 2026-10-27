"""Validate generated Quarto pages without changing legacy static content."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

root = Path('docs').resolve()
class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('href', 'src') and value:
                self.links.append(value)

errors = []
# Match the project render inputs, including compatibility pages and blog posts.
for source in [*Path('.').glob('*.qmd'), *Path('posts').rglob('*.qmd')]:
    page = root / source.with_suffix('.html')
    if not page.is_file():
        errors.append(f'Missing rendered page: {page}')
        continue
    parser = Links()
    parser.feed(page.read_text())
    for link in parser.links:
        url = urlsplit(link)
        if url.scheme or url.netloc or not url.path:
            continue
        target = (root / unquote(url.path).lstrip('/')) if url.path.startswith('/') else page.parent / unquote(url.path)
        if not target.exists():
            errors.append(f'{source}: missing local target {link}')
assert (root / 'CNAME').read_text().strip() == 'clarkruttinger.info'
assert (root / '.nojekyll').is_file()
if errors:
    raise SystemExit('\n'.join(sorted(set(errors))))
print('Rendered pages, local links, assets, and custom domain checked.')
