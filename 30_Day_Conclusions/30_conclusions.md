<div align="center">

  <h1> 30 Days Of Python: Day 30- Conclusions</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>


<sub>Author:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small>Second Edition: July, 2021</small>
</sub>

</div>

[<< Day 29](../29_Day_Building_API/29_building_API.md)
![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)


<!-- QUICKSTART:START generated from quickstart/day_30.py by quickstart/build.py, edit that file instead -->
## ⚡ Quick Start

Run from the repo root: `python3 quickstart/day_30.py` · `Ex L2.3` = the exercise a line helps with.

```py
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
```

---
<!-- QUICKSTART:END -->

- [Day 30](#day-30)
  - [Conclusions](#conclusions)
  - [Testimony](#testimony)

# Day 30


## Conclusions

In the process of preparing this material I  have learned quite a lot and you have inspired me to do more. Congratulations for making it to this level. If you have done all the exercise and the projects, now you are capable to go to  a data analysis, data science, machine learning or web development paths. [Support the author for more educational materials](https://www.paypal.com/paypalme/asabeneh).

## Testimony
Now it is time to express your thoughts about the Author and 30DaysOfPython. You can leave your testimonial on this [link](https://www.asabeneh.com/testimonials)

GIVE FEEDBACK:
http://thirtydayofpython-api.herokuapp.com/feedback

🎉 CONGRATULATIONS ! 🎉

[<< Day 29](../29_Day_Building_API/29_building_API.md)
