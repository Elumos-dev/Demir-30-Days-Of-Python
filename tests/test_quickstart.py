"""Every Quick Start snippet runs, prints what its comments promise, and matches its lesson.

Run from the repo root:   python3 -m pytest
Skip the slow venv test:  python3 -m pytest -m "not slow"
"""
import os
import re
import runpy
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
QS = ROOT / 'quickstart'
FAKES = Path(__file__).resolve().parent / 'fakes'
sys.path.insert(0, str(QS))
import build  # noqa: E402

PY_DAYS = [d for d in range(1, 31) if d != 23]
SERVER_DAYS = {26, 29}   # Flask apps: tested through Flask's test client instead

# day: (stdin, [text that must appear in the output])
EXPECTED = {
    1: ('', ['9 5 14 3.5', '1 3 49', "<class 'complex'>", '5.0']),
    2: ('5\n', ['13 5 36 2.25 1 6561 2', '28.26 18.84', 'Area: 78.5']),
    3: ('20\n', ['Double the base is 40.0', '31536000', '2 4 8']),
    4: ('', ['LPF', 'True False', '[padded]', 'Area with radius 5 is 78.5 m2', '7 / 3 = 2.33\n']),
    5: ('', ['5 apple mango plum', '[1, 2, 3, 4] [1, 2, 99, 3, 4]', '195 Lesotho', "A ['B', 'C', 'D']"]),
    6: ('', ["['red', 'green', 'blue'] black white", 'True False']),
    7: ('', ['{1, 2, 3, 4} {1, 2, 3, 4}', '{1} {1, 4}', '5 3']),
    8: ('', ["['name', 'age', 'toys']", "('toys', ['ball', 'string', 'box'])", 'unknown']),
    9: ('15\n', ['Wait 3 more years', 'C or lower', "['cat', 'dog', 'fish']", 'Knows Python', 'Teen']),
    10: ('', ['0 1 2 3 4', '3 2 1', '10 5 0', '***', 'Sum of evens to 10: 30', 'highland',
              "['c', 'b', 'a']", "[('English', 91), ('French', 45)]"]),
    11: ('', ['5 5', '6 Numbers only', 'Hello, Guest! Hello, Demir!', 'level: 3', '4.0 3.14']),
    12: ('6 3\n', ['18', '[1, 2, 3, 4, 5]', '#ff0080', '0123456789abcdefABCDEF']),
    13: ('', ['[1, 2]', '[1, 2, 3, 4]', '[(0, 0, 0), (1, 1, 1), (2, 4, 8)]', "['Kenya', 'Peru']", '25 7']),
    14: ('', ['[10, 20, 30, 40]', "['Chad', 'Peru']", '\n10\n', '\n14\n', 'HELLO', "{'K': 1, 'C': 1, 'P': 1}"]),
    15: ('', ['NameError', 'IndexError', 'KeyError', 'AttributeError', 'TypeError', 'ValueError',
              'ZeroDivisionError', 'ModuleNotFoundError', 'ImportError', 'SyntaxError']),
    16: ('', ['2027-03-14 00:00:00', '2027-01-31']),
    17: ('0\n', ['Cannot divide by zero', 'Always runs', '1 2 [3, 4, 5] [1, 2, 3, 4] 5', '[0, 1, 2, 3]', 'Ben 85']),
    18: ('', ["['555', '1234', '555', '9876']", "['-3', '4']", 'sam@mail.com', 'hello', 'True False',
              "[(3, 'the'), (2, 'and')]"]),
    19: ('', ['2 3', 'Afghanistan 27657145', "'num_points'", 'stephen.marquard@uct.ac.za']),
    20: ('', ['200', 'Abyssinian', '3 6 4.4 4', 'South Africa']),
    21: ('', ['Sam: 3 goals (City FC) [2, 1]', 'Lee: 0 goals (Free agent), 5 saves']),
    22: ('', ['Hockey Teams', "2 {'Team Name': 'Boston Bruins', 'Year': '1990', 'Wins': '44'}"]),
    24: ('', ['[2 4 6 8]', '(2, 3) 6', '6 [1 4] [1 2]', '[3 4]', '\n11\n', '(2, 2)', '[1, 2, 3, 4]']),
    25: ('', ['Ana   17', '(20099, 7)', "'num_points'", '\n160\n', 'From Python to Lua']),
    27: ('', ["{'name': 'Ana', 'age': 17}", "{'name': 'Cy', 'age': 18}", '\n2\n']),
    28: ('', ['200 application/json', 'sunt aut facere', "201 {'title': 'hi', 'id': 101}"]),
    30: ('', ['True 3 49', 'Python nohtyp py', '24 days, 0:00:00', "[('a', 3)]", '\n11\n']),
}
# Files a snippet is supposed to leave behind (anything else is litter)
LEAVES = {22: {'scraped.json'}}


def run_snippet(day, stdin, tmp_path):
    """Run quickstart/day_NN.py in an empty folder that only contains data/."""
    (tmp_path / 'data').symlink_to(ROOT / 'data', target_is_directory=True)
    env = {**os.environ, 'PYTHONPATH': str(FAKES), 'PYTHONIOENCODING': 'utf-8'}
    env.pop('MONGODB_URI', None)
    return subprocess.run(
        [sys.executable, str(QS / f'day_{day:02d}.py')],
        input=stdin, capture_output=True, text=True, cwd=tmp_path, env=env, timeout=120,
    )


@pytest.mark.parametrize('day', [d for d in PY_DAYS if d not in SERVER_DAYS])
def test_snippet_runs_and_prints_expected(day, tmp_path):
    stdin, expected = EXPECTED[day]
    result = run_snippet(day, stdin, tmp_path)
    assert result.returncode == 0, result.stderr
    for text in expected:
        assert text in result.stdout, f'day {day}: missing {text!r}\n{result.stdout}'
    left = {p.name for p in tmp_path.iterdir()} - {'data'}
    assert left == LEAVES.get(day, set()), f'day {day} left files behind: {left}'


@pytest.mark.parametrize('stdin, expected', [
    ('4\n', ['2.5', 'No errors', 'Always runs']),
    ('abc\n', ['Not a number', 'Always runs']),
])
def test_day_17_every_branch(stdin, expected, tmp_path):
    result = run_snippet(17, stdin, tmp_path)
    assert result.returncode == 0, result.stderr
    for text in expected:
        assert text in result.stdout


def test_day_09_adult_branch(tmp_path):
    result = run_snippet(9, '30\n', tmp_path)
    assert 'Adult' in result.stdout and 'Not a teen' in result.stdout


def load_app(day, monkeypatch):
    import mongomock
    import pymongo
    monkeypatch.setattr(pymongo, 'MongoClient', mongomock.MongoClient)
    monkeypatch.delenv('MONGODB_URI', raising=False)
    return runpy.run_path(str(QS / f'day_{day:02d}.py'), run_name=f'quickstart_day_{day}')['app']


def test_day_26_flask_text_analyzer(monkeypatch):
    client = load_app(26, monkeypatch).test_client()
    assert client.get('/').data == b'Home page'
    page = client.get('/analyze')
    assert page.status_code == 200 and b'<form method="post">' in page.data and b'words</p>' not in page.data
    assert b'<p>4 words</p>' in client.post('/analyze', data={'content': 'one two  three\nfour'}).data
    assert b'<p>0 words</p>' in client.post('/analyze', data={'content': ''}).data


def test_day_29_rest_api_full_crud(monkeypatch):
    client = load_app(29, monkeypatch).test_client()
    url = '/api/v1/students'
    assert client.get(url).get_json() == []

    created = client.post(url, json={'name': 'Ana', 'age': 17})
    assert created.status_code == 201
    sid = created.get_json()['_id']

    assert client.get(url).get_json() == [{'_id': sid, 'name': 'Ana', 'age': 17}]
    assert client.get(f'{url}/{sid}').get_json()['name'] == 'Ana'

    updated = client.put(f'{url}/{sid}', json={'age': 18})
    assert updated.get_json() == {'_id': sid, 'name': 'Ana', 'age': 18}

    assert client.delete(f'{url}/{sid}').status_code == 204
    missing = client.get(f'{url}/{sid}')
    assert missing.status_code == 404 and missing.get_json() == {'error': 'not found'}


@pytest.mark.slow
@pytest.mark.skipif(shutil.which('bash') is None, reason='needs bash')
def test_day_23_virtual_environment(tmp_path):
    script = (QS / 'day_23.sh').read_text(encoding='utf-8')
    result = subprocess.run(['bash', '-e', '-c', script], capture_output=True, text=True,
                            cwd=tmp_path, timeout=600)
    assert result.returncode == 0, result.stderr
    project = tmp_path / 'my_project'
    assert (project / 'venv').is_dir()
    assert re.search(r'^requests==', (project / 'requirements.txt').read_text(), re.M)
    assert (project / '.gitignore').read_text().strip() == 'venv/'


def test_every_day_has_a_snippet():
    for day in range(1, 31):
        assert build.snippet_path(day).exists()


@pytest.mark.parametrize('day', range(1, 31))
def test_snippet_is_short(day):
    lines = build.snippet_path(day).read_text(encoding='utf-8').splitlines()
    assert len(lines) <= 55, f'day {day} has {len(lines)} lines'
    assert lines[0].startswith(f'# Day {day}:'), 'first line names the day'


@pytest.mark.parametrize('day', range(1, 31))
def test_lesson_has_exactly_one_block_at_the_top(day):
    text = build.lesson_path(day).read_text(encoding='utf-8')
    assert text.count(build.START) == 1 and text.count(build.END) == 1
    banner = build.BANNER_RE.search(text)
    between = text[banner.end():text.index(build.START)]
    assert between.strip() == '', 'Quick Start must sit directly under the day banner'
    assert build.snippet_path(day).read_text(encoding='utf-8').strip() in text


def test_lessons_are_in_sync_with_snippets():
    assert build.build(check=True) == [], 'run: python3 quickstart/build.py'


def test_build_is_idempotent():
    original = '# Title\n\n![30DaysOfPython](../images/banner.png)\n\n- [Day 6](#day-6)\n'
    once = build.inject(original, build.render_block(6))
    assert build.inject(once, build.render_block(6)) == once
    assert once.index('![30DaysOfPython]') < once.index(build.START) < once.index('- [Day 6]')
