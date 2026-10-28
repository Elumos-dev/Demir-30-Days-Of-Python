# Day 11: functions
import math


def add(a, b):                       # Ex L1.1: parameters in, return value out
    return a + b


def total(*nums):                    # Ex L1.3: *args packs any number of arguments into a tuple
    for n in nums:
        if not isinstance(n, (int, float)):   # type check
            return 'Numbers only'
    return sum(nums)


def greet(name='Guest'):             # Ex L2.5: default value when nothing is passed
    return f'Hello, {name}!'


def show(**info):                    # Ex L2.6: **kwargs packs named arguments into a dict
    for key, value in info.items():
        print(f'{key}: {value}')


def apply(func, value):              # a function can be passed in like any other value
    return func(value)


print(add(2, 3), add(b=3, a=2))      # positional or by name
print(total(1, 2, 3), total(1, 'x'))
print(greet(), greet('Demir'))
show(sport='football', level=3)
print(apply(len, 'hello'))
print(math.sqrt(16), math.pi)        # Ex L1.2, L1.7: sqrt for the quadratic formula
