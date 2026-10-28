# Day 30: no new syntax. One line per day to check you still know it all.
import math
import re
from collections import Counter
from datetime import date
from functools import reduce

import numpy as np

name, n = 'python', 7                                    # 2  variables
print(n % 2 == 1, n // 2, n ** 2)                        # 3  operators
print(f'{name.title()} {name[::-1]} {name[:2]}')         # 4  strings
nums = [5, 1, 4]
nums.append(2)
print(sorted(nums), nums[-1])                            # 5  lists
print(('a', 'b') + ('c',))                               # 6  tuples
print({1, 2} & {2, 3})                                   # 7  sets
print({'k': 1}.get('x', 0))                              # 8  dicts
print('big' if n > 5 else 'small')                       # 9  conditionals
print(sum(i for i in range(5)))                          # 10 loops
print((lambda *a, **k: (a, k))(1, x=2))                  # 11 functions
print(math.floor(2.7), math.ceil(2.1))                   # 12 modules
print([x * x for x in range(4) if x])                    # 13 comprehensions
print(reduce(lambda a, b: a * b, map(int, '1234')))      # 14 map / reduce
print(type(ValueError()).__name__)                       # 15 error types
print(date(2026, 12, 25) - date(2026, 12, 1))            # 16 datetime
first, *rest = 'abc'
print(first, rest, list(enumerate('xy')))                # 17 unpacking, enumerate
print(re.findall(r'\d+', 'a1b22c333'))                   # 18 regex
print(Counter('banana').most_common(1))                  # 19 counting words in files
print(np.array([1, 2]) @ np.array([3, 4]))               # 24 numpy
# 20 pip + requests | 21 classes | 22 scraping | 23 venv | 25 pandas | 26 flask | 27 mongo | 28-29 APIs
