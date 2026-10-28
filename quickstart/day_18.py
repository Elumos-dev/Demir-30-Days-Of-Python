# Day 18: regular expressions
#  \d digit  \w letter/digit/_  \s space  .  any char   [abc] one of   [^abc] none of
#  +  1 or more   *  0 or more   ?  0 or 1   {2,4}  2 to 4 times   ^ start   $ end
import re
from collections import Counter

text = 'Call 555-1234 or 555-9876. Email sam@mail.com now. Python python PYTHON'

print(re.findall(r'\d+', text))                  # Ex L1.2: every match as a list
print(re.findall(r'-?\d+', 'at -3 and 4'))       # -? = optional minus sign
print(re.findall(r'python', text, re.I))         # re.I ignores case
print(re.search(r'\S+@\S+', text).group())       # first match anywhere
print(re.match(r'Call', text) is not None)       # match() only checks the START
print(re.sub(r'[^\w\s]', '', 'he@l%lo!'))        # Ex L3: replace junk chars with ''
print(re.split(r'\s+', 'a  b   c'))

pattern = r'^[A-Za-z_]\w*$'                      # Ex L2: whole string, start to end
print(bool(re.match(pattern, 'ok_name')), bool(re.match(pattern, '9lives')))

words = re.findall(r'\w+', 'the cat and the hat and the bat')
top = Counter(words).most_common(2)              # Ex L1.1: [(word, count), ...] biggest first
print(top, [(count, word) for word, count in top])
