# Day 1: run Python, do math, check types
# Ex L1.1 (terminal, not Python):  python3 --version

print(7 + 2, 7 - 2, 7 * 2, 7 / 2)      # Ex L1.2: 9 5 14 3.5
print(7 % 2, 7 // 2, 7 ** 2)          # remainder, floor division, power: 1 3 49

print('Cape Town')                     # Ex L1.3: text goes in quotes

print(type(5), type(2.5), type(1 + 2j))                          # Ex L1.4, L3.1
print(type('hi'), type(True), type(None))
print(type([1, 2]), type((1, 2)), type({1, 2}), type({'a': 1}))  # list tuple set dict

# Ex L3.2: distance between (x1, y1) and (x2, y2) = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
print(((4 - 1) ** 2 + (6 - 2) ** 2) ** 0.5)                      # 5.0
