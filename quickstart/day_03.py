# Day 3: operators

height = 1.82                               # Ex 1-3: int, float, complex
z = 3 + 4j

base = float(input('Enter base: '))         # Ex 4-7, 21-22: prompt, cast, calculate, print
print('Double the base is', base * 2)

print(5 > 3, 5 == 5.0, 5 != 4)              # comparison -> True True True
print(len('cat') > len('dog'))              # Ex 12: compare lengths -> False
print('at' in 'cat' and 'at' in 'hat')      # Ex 13-15: in, and, not in
print('x' not in 'cat')
print(10 % 2 == 0)                          # Ex 17: even means remainder 0
print(7 // 2 == int(3.9))                   # Ex 18: int() chops decimals, no rounding
print(type('5') == type(5))                 # Ex 19
print(int(float('9.8')))                    # Ex 20: int('9.8') crashes, go through float()
print(str(float(len('code'))))              # Ex 16: chain casts

m = (8 - 2) / (5 - 2)                       # Ex 8-10: slope = (y2 - y1) / (x2 - x1)
print(m)

x = -2                                      # Ex 11: plug x in, try values until y == 0
print(x ** 2 + 4 * x + 4)

print(60 * 60 * 24 * 365)                   # Ex 22: seconds in a year
print(f'{2} {2 ** 2} {2 ** 3}')             # Ex 23: one table row per print
