# Day 19: files, JSON, CSV. Run from the repo root so data/ is found.
import csv
import json
import os
import re

with open('notes.txt', 'w') as f:            # 'w' write (wipes the file)  'a' append  'r' read
    f.write('one two\nthree\n')

with open('notes.txt') as f:                 # Ex L1.1: `with` closes the file for you
    text = f.read()                          # whole file as one string (f.readlines() = list)
print(len(text.splitlines()), len(text.split()))   # lines, words

with open('data/countries_data.json', encoding='utf-8') as f:   # Ex L1.2-3
    countries = json.load(f)                 # JSON file -> Python list / dict
print(countries[0]['name'], countries[0]['population'])

print(json.dumps({'a': 1}, indent=2))        # dict -> JSON text
with open('notes.json', 'w') as f:
    json.dump({'a': 1}, f)                   # dict -> JSON file

with open('data/hacker_news.csv', encoding='utf-8') as f:       # Ex L2.6
    rows = list(csv.reader(f))               # each row = list of strings
print(rows[0])

with open('data/email_exchanges_big.txt', encoding='utf-8') as f:   # Ex L2.1
    found = re.findall(r'^From: (\S+)', f.read(), re.M)  # ( ) returns just that part, re.M: ^ = each line
print(found[0])

os.remove('notes.txt')                       # delete a file
os.remove('notes.json')
