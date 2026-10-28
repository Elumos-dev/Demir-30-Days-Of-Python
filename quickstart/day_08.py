# Day 8: dictionaries (key: value)

cat = {}                                  # Ex 1
cat['name'] = 'Milo'                      # Ex 2-3: add a key by assigning to it
cat['age'] = 3
cat['toys'] = ['ball', 'string']
print(len(cat))                           # Ex 4: number of keys
print(cat['toys'], type(cat['toys']))     # Ex 5
cat['toys'].append('box')                 # Ex 6: edit a list stored inside a dict
print(list(cat.keys()))                   # Ex 7
print(list(cat.values()))                 # Ex 8
print(list(cat.items()))                  # Ex 9: list of (key, value) tuples
print(cat.get('color', 'unknown'))        # safe read: default instead of a crash
cat.pop('age')                            # Ex 10: remove one key
del cat                                   # Ex 11
