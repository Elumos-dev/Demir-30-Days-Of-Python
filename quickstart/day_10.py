# Day 10: loops

for i in range(5):                   # Ex L1.1: 0 1 2 3 4 (stops BEFORE the end)
    print(i, end=' ')                # end=' ' keeps printing on one line
print()

i = 3
while i > 0:                         # Ex L1.2: loop while the condition is True
    print(i, end=' ')
    i -= 1
print()

for i in range(10, -1, -5):          # range(start, stop, step): 10 5 0
    print(i, end=' ')
print()

for n in range(1, 4):                # Ex L1.3: string * number repeats it
    print('*' * n)

for row in range(2):                 # Ex L1.4: loop inside a loop
    for col in range(3):
        print('o', end=' ')
    print()

for n in range(3):                   # Ex L1.5
    print(f'{n} + {n} = {n + n}')

for lang in ['Java', 'Python']:      # Ex L1.6: loop over a list
    print(lang)

total = 0
for n in range(0, 11, 2):            # Ex L1.7-8, L2: step 2, add as you go
    total += n
print('Sum of evens to 10:', total)

for word in ['island', 'lake', 'highland']:   # Ex L3.1: filter while looping
    if 'land' in word:
        print(word)

flipped = []
for item in ['a', 'b', 'c']:         # Ex L3.2: insert(0, x) puts x at the front
    flipped.insert(0, item)
print(flipped)

# Ex L3.3: data/countries-data.py has no variable name, so load the JSON copy (json = Day 19)
import json
with open('data/countries_data.json', encoding='utf-8') as f:
    countries = json.load(f)

counts = {}
for c in countries:                  # count with a dict: start at 0, add 1
    for lang in c['languages']:
        counts[lang] = counts.get(lang, 0) + 1
top = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)   # lambda = Day 13
print(len(counts), top[:2])
