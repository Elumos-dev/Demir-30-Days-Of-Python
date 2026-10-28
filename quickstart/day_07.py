# Day 7: sets (no duplicates, no order)

langs = {'Python', 'Java', 'C'}
print(len(langs))                        # Ex L1.1
langs.add('Go')                          # Ex L1.2
langs.update(['Rust', 'Swift'])          # Ex L1.3: add many at once
langs.remove('C')                        # Ex L1.4-5: remove() crashes if the item is missing
langs.discard('Ruby')                    #            discard() does nothing if it is missing

X, Y = {1, 2, 3}, {2, 3, 4}
print(X | Y, X.union(Y))                 # Ex L2.1, L2.5: join
print(X & Y, X.intersection(Y))          # Ex L2.2: in both
print(X.issubset(Y), X.isdisjoint(Y))    # Ex L2.3-4
print(X - Y, X ^ Y)                      # Ex L2.6: only in X | in one but not both
del X                                    # Ex L2.7

nums = [1, 1, 2, 3, 3]
print(len(nums), len(set(nums)))         # Ex L3.1: set() removes duplicates
print(len(set('to be or not to be'.split())))   # Ex L3.3: unique words -> 4
