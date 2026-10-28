# Day 17: try/except, unpacking, spreading, enumerate, zip

try:
    n = int(input('Number: '))
    print(10 / n)
except ValueError:                 # catch one error type
    print('Not a number')
except ZeroDivisionError:
    print('Cannot divide by zero')
else:
    print('No errors')             # runs only when try finished without an error
finally:
    print('Always runs')

a, b, *rest = [1, 2, 3, 4, 5]      # Ex 1: * collects whatever is left over
*start, last = [1, 2, 3, 4, 5]
print(a, b, rest, start, last)


def add3(x, y, z):
    return x + y + z


print(add3(*[1, 2, 3]))                    # * spreads a list into arguments
print(add3(**{'x': 1, 'y': 2, 'z': 3}))    # ** spreads a dict into named arguments
print([0, *[1, 2], 3])                     # spread inside a list

for i, fruit in enumerate(['fig', 'kiwi']):         # index + item
    print(i, fruit)
for name, score in zip(['Ana', 'Ben'], [90, 85]):   # walk two lists side by side
    print(name, score)
