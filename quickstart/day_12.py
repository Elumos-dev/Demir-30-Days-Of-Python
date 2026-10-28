# Day 12: modules, random, string
# Your own module:  tools.py holds  def hi(): return 'hi'
#                   main.py runs    from tools import hi   (same folder)
import random
import string

print(random.randint(0, 255))            # Ex L1.3: whole number, both ends included
print(random.choice('abc123'))           # one random item from a string or list
print(string.ascii_letters)              # a-z A-Z
print(string.digits, string.hexdigits)   # 0-9 | 0-9 a-f A-F

chars = string.ascii_lowercase + string.digits
code = ''
for _ in range(6):                       # Ex L1.1: build a random string one char at a time
    code += random.choice(chars)         # _ = loop variable you don't use
print(code)

n, count = input('Length and count: ').split()   # Ex L1.2: two values from one input line
print(int(n) * int(count))

nums = [1, 2, 3, 4, 5]
random.shuffle(nums)                     # Ex L3.1: shuffles in place, returns None
print(sorted(nums))
print(len(random.sample(range(10), 7)))  # Ex L3.2: 7 picks, no repeats
print(f'#{255:02x}{0:02x}{128:02x}')     # Ex L2.1: number -> 2-digit hex -> #ff0080
