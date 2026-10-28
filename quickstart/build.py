"""Inject each quickstart/day_NN snippet into the top of its day's lesson.

Usage (from the repo root):
    python3 quickstart/build.py          write every Quick Start block
    python3 quickstart/build.py --check  exit 1 when a lesson is out of date

Edit quickstart/day_NN.py (or .sh) and quickstart/notes/day_NN.md, never the
generated block inside the lesson markdown.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QS = ROOT / 'quickstart'

START = '<!-- QUICKSTART:START'
END = '<!-- QUICKSTART:END -->'
BLOCK_RE = re.compile(re.escape(START) + r'.*?' + re.escape(END) + r'\n?', re.S)
BANNER_RE = re.compile(r'^!\[30DaysOfPython\]\(.*\)\s*$', re.M)

INDEX_START = '<!-- QUICKSTART-INDEX:START -->'
INDEX_END = '<!-- QUICKSTART-INDEX:END -->'
INDEX_RE = re.compile(re.escape(INDEX_START) + r'.*?' + re.escape(INDEX_END) + r'\n*', re.S)
INDEX_ANCHOR = '<small>🧡🧡🧡 HAPPY CODING 🧡🧡🧡</small>'
INDEX_TEXT = (
    f'{INDEX_START}\n'
    '> ⚡ **Every day opens with a Quick Start**: the smallest working example of each new tool, '
    'tagged with the exercises it unlocks. All 30 are runnable and tested. '
    'See [quickstart/README.md](./quickstart/README.md).\n'
    f'{INDEX_END}\n\n'
)


def lesson_path(day):
    """Day 1 lives in readme.md; every other day has its own folder."""
    if day == 1:
        return ROOT / 'readme.md'
    folder = next(ROOT.glob(f'{day:02d}_Day_*'))
    return next(folder.glob('*.md'))


def snippet_path(day):
    for ext in ('py', 'sh'):
        path = QS / f'day_{day:02d}.{ext}'
        if path.exists():
            return path
    raise FileNotFoundError(f'No quickstart snippet for day {day}')


def render_block(day):
    src = snippet_path(day)
    rel = src.relative_to(ROOT).as_posix()
    code = src.read_text(encoding='utf-8').rstrip('\n')
    if src.suffix == '.sh':
        lang, run = 'sh', 'Type these in a terminal, one line at a time.'
    else:
        lang, run = 'py', f'Run from the repo root: `python3 {rel}` · `Ex L2.3` = the exercise a line helps with.'
    parts = [
        f'{START} generated from {rel} by quickstart/build.py, edit that file instead -->',
        '## ⚡ Quick Start',
        '',
        run,
        '',
        f'```{lang}',
        code,
        '```',
        '',
    ]
    notes = QS / 'notes' / f'day_{day:02d}.md'
    if notes.exists():
        parts += [notes.read_text(encoding='utf-8').rstrip('\n'), '']
    parts += ['---', END, '']
    return '\n'.join(parts)


def inject(text, block):
    """Replace an existing block, or insert one right after the banner image."""
    if START in text:
        return BLOCK_RE.sub(lambda _: block, text, count=1)
    match = BANNER_RE.search(text)
    if match is None:
        raise ValueError('banner image not found')
    cut = match.end()
    return text[:cut] + '\n\n' + block + '\n' + text[cut:].lstrip('\n')


def inject_index(text):
    if INDEX_START in text:
        return INDEX_RE.sub(lambda _: INDEX_TEXT, text, count=1)
    return text.replace(INDEX_ANCHOR, INDEX_TEXT + INDEX_ANCHOR, 1)


def build(check=False):
    stale = []
    for day in range(1, 31):
        path = lesson_path(day)
        old = path.read_text(encoding='utf-8')
        new = inject(old, render_block(day))
        if day == 1:
            new = inject_index(new)
        if new != old:
            stale.append(path.relative_to(ROOT).as_posix())
            if not check:
                path.write_text(new, encoding='utf-8')
    return stale


if __name__ == '__main__':
    check = '--check' in sys.argv
    stale = build(check=check)
    if check and stale:
        print('Out of date, run python3 quickstart/build.py:', *stale, sep='\n  ')
        sys.exit(1)
    print(f'{len(stale)} lesson(s) {"need updating" if check else "updated"}.')
