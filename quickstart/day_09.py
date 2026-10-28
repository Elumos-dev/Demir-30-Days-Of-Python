# Day 9: if / elif / else

age = int(input('Enter your age: '))         # Ex L1.1-3: cast input before comparing
if age >= 18:
    print('Adult')
else:
    print(f'Wait {18 - age} more years')

score = 73                                    # Ex L2.1: check ranges top-down with elif
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
else:
    grade = 'C or lower'
print(grade)

month = 'july'                                # Ex L2.2: match against a group
if month in ['june', 'july', 'august']:
    print('Mid-year month')

pets = ['cat', 'dog']                         # Ex L2.3
if 'fish' not in pets:
    pets.append('fish')
print(pets)

user = {'name': 'Sam', 'skills': ['Python', 'SQL']}
if 'skills' in user and 'Python' in user['skills']:   # Ex L3: check the key, then the value
    print('Knows Python')

print('Teen' if 13 <= age <= 19 else 'Not a teen')    # one-line if
