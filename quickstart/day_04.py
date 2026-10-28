# Day 4: strings

s = 'Learn Python Fast'
print('Learn' + ' ' + 'Python')                   # Ex 1-2: concatenate with +
print(s, len(s), s.upper(), s.lower())            # Ex 3-7
print(s.capitalize(), s.title(), s.swapcase())    # Ex 8
print(s[0], s[6], s[-1], len(s) - 1)              # Ex 15-17: index from 0, last index = len - 1
print(s[:5], s[6:12])                             # Ex 9, 25, 27: s[start:end], end not included
print('Python' in s, s.find('Python'), s.index('P'))  # Ex 10, 20-21, 23, 26
print(s.rfind('a'), s.rindex('a'))                # Ex 22, 24: search from the right
print(s.replace('Fast', 'Slowly'))                # Ex 11-12
print(s.split(), 'a, b, c'.split(', '))           # Ex 13-14: string -> list

words = s.split()
print(words[0][0] + words[1][0] + words[2][0])    # Ex 18-19: first letter of each word -> LPF

print(s.startswith('Learn'), s.endswith('fast'))  # Ex 28-29: case matters -> True False
print('[' + '   padded   '.strip() + ']')         # Ex 30
print('my_var'.isidentifier(), '2var'.isidentifier())  # Ex 31
print(' # '.join(['a', 'b', 'c']))                # Ex 32: list -> string

print('Line one\nLine two')                       # Ex 33: \n new line
print('Name\tAge\nSam\t17')                       # Ex 34: \t tab

r = 5
print(f'Area with radius {r} is {3.14 * r ** 2} m2')  # Ex 35: f-string, {} runs code
print(f'{7} / {3} = {7 / 3:.2f}')                 # Ex 36: :.2f = 2 decimal places
