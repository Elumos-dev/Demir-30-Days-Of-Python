# Day 14: higher-order functions, closures, decorators, map / filter / reduce
from functools import reduce

nums = [1, 2, 3, 4]
words = ['Kenya', 'Chad', 'Peru']

for w in words:                                      # Ex L1.4-6
    print(w)

print(list(map(lambda n: n * 10, nums)))             # map: same count out, each item changed
print(list(map(str.upper, words)))                   # any function works, not only lambdas
print(list(filter(lambda w: len(w) == 4, words)))    # filter: keeps items where the test is True
print(reduce(lambda a, b: a + b, nums))              # reduce: folds the list into ONE value
print(reduce(lambda a, b: a + b, map(lambda n: n * 2, filter(lambda n: n > 2, nums))))  # chain


def make_multiplier(k):        # closure: the inner function remembers k after the outer one ends
    def multiply(x):
        return x * k
    return multiply


triple = make_multiplier(3)
print(triple(5))


def shout(func):               # decorator: takes a function, returns an upgraded one
    def wrapper():
        return func().upper()
    return wrapper


@shout                         # same as: hello = shout(hello)
def hello():
    return 'hello'


print(hello())

print(sorted(words, key=len))                        # Ex L3: sort by a rule
print(sorted(words, key=lambda w: w[-1], reverse=True))

starts = {}
for w in words:                                      # Ex L2: count by first letter
    starts[w[0]] = starts.get(w[0], 0) + 1
print(starts)
