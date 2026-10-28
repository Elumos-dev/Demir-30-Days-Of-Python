# ⚡ Quick Start

The original lessons explain a topic, then set exercises that use tools the page never shows in one place. Every lesson now opens with a **Quick Start**: the smallest working example of each new tool, with `Ex` tags pointing at the exercises each line unlocks. The snippets use different data from the exercises, so they show *how* without solving them.

## Use it

```sh
python3 quickstart/day_05.py      # run any day from the repo root, so data/ paths work
```

`Ex L2.3` = Level 2, exercise 3. Days without levels use `Ex 3`.

| Day | Quick Start covers | | Day | Quick Start covers |
|---|---|---|---|---|
| [01](./day_01.py) | math operators, `type()`, distance formula | | [16](./day_16.py) | `datetime`, `strftime` / `strptime`, `timedelta` |
| [02](./day_02.py) | variables, `len()`, casting, `input()` | | [17](./day_17.py) | `try` / `except` / `else` / `finally`, `*` `**`, `enumerate`, `zip` |
| [03](./day_03.py) | comparisons, `and` / `in` / `not`, casts | | [18](./day_18.py) | `re`: `findall`, `search`, `match`, `sub`, `split`, `Counter` |
| [04](./day_04.py) | string methods, slicing, `find` / `rfind`, f-strings | | [19](./day_19.py) | `open` / `with`, JSON, CSV, `os.remove` |
| [05](./day_05.py) | list methods, slicing, `min` / `max`, unpacking | | [20](./day_20.py) | `pip`, `requests`, `.json()`, `statistics` |
| [06](./day_06.py) | tuples, joining, unpacking, `list()` | | [21](./day_21.py) | classes, `__init__`, methods, inheritance, `super()` |
| [07](./day_07.py) | set methods, `\|` `&` `^`, subset / disjoint | | [22](./day_22.py) | `BeautifulSoup`: table → list of dicts → JSON |
| [08](./day_08.py) | dict keys / values / items, `get`, `pop` | | [23](./day_23.sh) | `venv`, activate, `pip freeze`, `.gitignore` |
| [09](./day_09.py) | `if` / `elif` / `else`, `in`, one-line `if` | | [24](./day_24.py) | NumPy arrays, shape, slicing, stats, dot product |
| [10](./day_10.py) | `for`, `while`, `range`, nested loops, counting | | [25](./day_25.py) | pandas `read_csv`, `head`, filtering, new columns |
| [11](./day_11.py) | `def`, defaults, `*args`, `**kwargs` | | [26](./day_26.py) | Flask routes, forms, templates |
| [12](./day_12.py) | modules, `random`, `string`, hex colors | | [27](./day_27.py) | MongoDB insert / find / update / delete |
| [13](./day_13.py) | list comprehensions, flattening, `lambda` | | [28](./day_28.py) | HTTP methods and status codes with `requests` |
| [14](./day_14.py) | `map` / `filter` / `reduce`, closures, decorators | | [29](./day_29.py) | REST API: Flask + MongoDB CRUD |
| [15](./day_15.py) | the 10 common error types | | [30](./day_30.py) | one-line review of every day |

Dead links in the original exercises are fixed in the notes: `restcountries.eu` (Day 20), the old UCI page (Day 22) and Heroku's free plan (Days 26, 29).

## Install everything once

```sh
python3 -m venv venv && source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements-dev.txt
```

## Tests

```sh
python3 -m pytest              # 96 tests, about 15 seconds
python3 -m pytest -m "not slow"   # skip the Day 23 test that builds a real venv
```

- Every snippet runs in an empty temp folder with fed-in `input()` answers, and must print the values its comments promise.
- Days 20, 22, 27 and 28 use offline fakes (`tests/fakes/sitecustomize.py`), so no internet or database is needed. Your own runs use the real thing.
- Days 26 and 29 run through Flask's test client. Day 29 is checked through a full create, read, update and delete cycle.
- A snippet that leaves stray files behind fails.
- GitHub Actions runs everything on Python 3.10 and 3.13 on each push.

## Edit a Quick Start

The block in each lesson is generated. Change `quickstart/day_NN.py` (or `notes/day_NN.md` for the bullet notes), then:

```sh
python3 quickstart/build.py    # rewrites the blocks; safe to run any number of times
```

The tests fail when a lesson and its snippet drift apart.
