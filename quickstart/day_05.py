# Day 5: lists

empty = []                                          # Ex L1.1
fruits = ['apple', 'kiwi', 'mango', 'pear', 'plum']
print(len(fruits), fruits[0], fruits[len(fruits) // 2], fruits[-1])   # Ex L1.3-4, 8-9

fruits[1] = 'KIWI'                                  # Ex L1.10, 13: change an item
fruits.append('fig')                                # Ex L1.11: add to the end
fruits.insert(2, 'lime')                            # Ex L1.12: insert at an index
print('fig' in fruits)                              # Ex L1.15
print(' + '.join(fruits))                           # Ex L1.14: list -> string

fruits.sort()                                       # Ex L1.16
print(fruits)
fruits.reverse()                                    # Ex L1.17 (or sort(reverse=True))
print(fruits)
print(fruits[:3], fruits[-3:], fruits[3:5])         # Ex L1.18-20: slicing

fruits.pop(0)                                       # Ex L1.21: remove by index
fruits.remove('mango')                              # Ex L1.22: remove by value
fruits.pop()                                        # Ex L1.23: remove the last item
fruits.clear()                                      # Ex L1.24: empty the list
del fruits                                          # Ex L1.25: delete the variable

a, b = [1, 2], [3, 4]
joined = a + b                                      # Ex L1.26
copy = joined.copy()                                # Ex L1.27: copy first, then edit safely
copy.insert(2, 99)
print(joined, copy)

nums = [7, 3, 9, 3]
print(min(nums), max(nums), sum(nums) / len(nums), abs(3 - 9))   # Ex L2.1
print(sorted(nums))                                 # sorted() returns a new list

import sys                                          # Ex L2.2-3: run from the repo root
sys.path.append('data')                             # let import look inside data/
from countries import countries                     # data/countries.py -> its countries list
half = (len(countries) + 1) // 2                    # +1 gives the first half the extra item
print(len(countries), countries[:half][-1])

first, *rest = ['A', 'B', 'C', 'D']                 # Ex L2.4: * collects the rest
print(first, rest)
