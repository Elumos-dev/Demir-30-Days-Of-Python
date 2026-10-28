# Day 6: tuples (lists you cannot change)

empty = ()                                   # Ex L1.1
colors = ('red', 'green')                    # Ex L1.2
more = ('blue',)                             # a one-item tuple needs the comma
all_colors = colors + more                   # Ex L1.3, L2.2: join with +
print(len(all_colors))                       # Ex L1.4

bigger = all_colors + ('black', 'white')     # Ex L1.5: can't edit, so build a new tuple
*primaries, dark, light = bigger             # Ex L2.1: unpack
print(primaries, dark, light)

as_list = list(bigger)                       # Ex L2.3: tuple -> list (tuple() goes back)
mid = len(as_list) // 2
print(as_list[mid], as_list[:3], as_list[-3:])   # Ex L2.4-5
print('red' in bigger, 'pink' in bigger)     # Ex L2.7
del bigger                                   # Ex L2.6
