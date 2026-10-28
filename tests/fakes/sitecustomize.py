"""Offline stand-ins, loaded automatically by every snippet the tests run.

Python imports `sitecustomize` at startup when it is on PYTHONPATH. The tests put
this folder there so Day 20, 22, 27 and 28 run without internet or a database.
Your own runs never load this file.
"""
import json
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / 'data'

SCRAPE_HTML = """<html><head><title>Hockey Teams: Forms, Searching and Pagination</title></head>
<body><table class="table">
<tr><th>Team Name</th><th>Year</th><th>Wins</th></tr>
<tr class="team"><td class="name">
  Boston Bruins
</td><td class="year">1990</td><td class="wins">44</td></tr>
<tr class="team"><td class="name">Buffalo Sabres</td><td class="year">1990</td><td class="wins">31</td></tr>
</table></body></html>"""

COUNTRIES_V3 = [
    {'name': {'common': 'South Africa'}, 'area': 1221037.0, 'languages': {'eng': 'English', 'zul': 'Zulu'}},
    {'name': {'common': 'Türkiye'}, 'area': 783562.0, 'languages': {'tur': 'Turkish'}},
]


class FakeResponse:
    def __init__(self, status_code=200, text='', payload=None, content_type='text/html'):
        self.status_code = status_code
        self._payload = payload
        self.text = text if payload is None else json.dumps(payload)
        self.content = self.text.encode()
        self.headers = {'Content-Type': content_type}

    def json(self):
        return json.loads(self.text)


def fake_request(method, url, **kwargs):
    if 'gutenberg.org' in url:
        return FakeResponse(text=(DATA / 'romeo_and_juliet.txt').read_text(encoding='utf-8'))
    if 'thecatapi.com' in url:
        return FakeResponse(payload=json.loads((DATA / 'cats.json').read_text(encoding='utf-8')),
                            content_type='application/json')
    if 'restcountries.com' in url:
        return FakeResponse(payload=COUNTRIES_V3, content_type='application/json')
    if 'scrapethissite.com' in url:
        return FakeResponse(text=SCRAPE_HTML)
    if 'jsonplaceholder.typicode.com' in url:
        json_type = 'application/json; charset=utf-8'
        if method == 'get':
            return FakeResponse(payload={'id': 1, 'title': 'sunt aut facere'}, content_type=json_type)
        if method == 'post':
            return FakeResponse(201, payload={**kwargs.get('json', {}), 'id': 101}, content_type=json_type)
        return FakeResponse(200, payload={}, content_type=json_type)
    raise RuntimeError(f'Test fake has no response for {method.upper()} {url}')


try:
    import requests

    for _method in ('get', 'post', 'put', 'delete'):
        setattr(requests, _method, lambda url, _m=_method, **kw: fake_request(_m, url, **kw))
except ImportError:
    pass

try:
    import mongomock
    import pymongo

    pymongo.MongoClient = mongomock.MongoClient
except ImportError:
    pass
