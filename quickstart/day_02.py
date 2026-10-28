# Day 2: variables, built-in functions, casting, input   (Ex L1.2: comments start with #)

city = 'Cape Town'                             # Ex L1.3-12: name = value
age = 17
is_student = True
first, last, country = 'Ada', 'Lovelace', 'UK'  # Ex L1.13: many variables on one line

print(type(age), len(city))                    # Ex L2.1-3: type() and len()
print(len(first) > len(last))

a, b = 9, 4                                    # Ex L2.4-11: store results in variables
total = a + b
print(total, a - b, a * b, a / b, a % b, a ** b, a // b)

pi = 3.14
print(pi * 3 ** 2, 2 * pi * 3)                 # Ex L2.12: area pi*r**2, circumference 2*pi*r

radius = float(input('Radius: '))              # Ex L2.12.3, L2.13: input() always returns a str
print('Area:', pi * radius ** 2)               # so cast with int() or float() before doing math

# Ex L2.14: run  help('keywords')  to list words you can't use as variable names
