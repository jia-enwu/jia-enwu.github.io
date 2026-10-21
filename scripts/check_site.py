"""Check the generated academic site without third-party Python dependencies."""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.references = []
        self.h1_count = 0
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            assert attrs["id"] not in self.ids, f"Duplicate id: {attrs['id']}"
            self.ids.add(attrs["id"])
        self.h1_count += tag == "h1"
        for attribute in ("href", "src", "data"):
            if attribute in attrs:
                self.references.append(attrs[attribute])


root = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
source = Path(__file__).resolve().parent.parent


def resolve_path(path):
    candidate = root / unquote(path).lstrip("/")
    for target in (candidate, candidate / "index.html", candidate.with_suffix(".html")):
        if target.is_file():
            return target
    raise AssertionError(f"Missing local target: {path}")


homepage = root / "index.html"
assert homepage.is_file(), "Build the site before running this check."
pages = [homepage, resolve_path("/publications/"), resolve_path("/teaching/"),
         resolve_path("/cv/"), resolve_path("/404.html"), resolve_path("/terms/")]
for collection in ("_publications", "_teaching"):
    for document in (source / collection).glob("*.md"):
        frontmatter = document.read_text().split("---", 2)[1]
        permalink = re.search(r"^permalink:\s*(.+)$", frontmatter, re.M)
        route = permalink.group(1).strip().strip('"\'') if permalink else (
            f"/{collection[1:]}/{document.stem}/"
        )
        pages.append(resolve_path(route))

checked = 0
for path in pages:
    text = path.read_text()
    assert "{{" not in text and "{%" not in text, f"Unrendered Liquid in {path}"
    parsed = Page(text)
    assert parsed.h1_count == 1, f"Expected one h1 in {path}; got {parsed.h1_count}"
    assert "/assets/css/academic.css" in text, f"Missing shared layout in {path}"
    for ref in parsed.references:
        url = urlsplit(ref)
        if url.scheme or url.netloc:
            continue
        route = url.path
        if route.startswith("/"):
            target = resolve_path(route)
        elif route:
            relative = (path.parent / route).resolve().relative_to(root)
            target = resolve_path(str(relative))
        else:
            target = path
        if url.fragment and target.suffix == ".html":
            assert unquote(url.fragment) in Page(target.read_text()).ids, (
                f"Missing anchor {ref} linked from {path}"
            )
        checked += 1

home_text = homepage.read_text()
home = Page(home_text)
for anchor in ("job-market-paper", "research", "teaching", "grants"):
    assert anchor in home.ids, f"Missing homepage section: {anchor}"
assert home_text.index('id="job-market-paper"') < home_text.index('id="research"')
for pdf in ("/files/Wu_CV.pdf", "/files/job_market_paper_jiaen_wu.pdf"):
    assert pdf in home.references, f"Missing direct homepage PDF link: {pdf}"
    assert resolve_path(pdf).read_bytes().startswith(b"%PDF"), f"Invalid PDF: {pdf}"
expected_papers = len(list((source / "_publications").glob("*.md"))) - 1
expected_courses = len(list((source / "_teaching").glob("*.md")))
assert home_text.count('class="research-paper"') == expected_papers, "Missing or duplicated paper"
assert home_text.count('class="course"') == expected_courses, "Missing or duplicated course"
assert "public management" in home_text, "Research focus is missing"
assert "Journal of Public Administration Research and Theory (2026, early view)" in home_text
for alias in ("/about/", "/about.html", "/research/", "/resume"):
    resolve_path(alias)
print(f"PASS: {len(pages)} pages, {checked} local references, all original paper/course routes,")
print(f"homepage sections, {expected_papers} other papers, {expected_courses} courses, redirects, and both direct PDFs.")
