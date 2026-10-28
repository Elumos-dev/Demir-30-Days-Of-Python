# Day 13: list comprehension and lambda
# [expression  for item in iterable  if condition]

nums = [-2, -1, 0, 1, 2]
print([n for n in nums if n > 0])                # Ex 1: filter
print([n * n for n in range(4)])                 # transform

grid = [[1, 2], [3, 4]]
print([x for row in grid for x in row])          # Ex 2: flatten, outer loop written first

print([(n, n ** 2, n ** 3) for n in range(3)])   # Ex 3: build tuples

pairs = [[('Kenya', 'Nairobi')], [('Peru', 'Lima')]]
print([country for [(country, city)] in pairs])  # Ex 4-6: unpack the nested tuple in the for
print([{'name': c} for [(c, _)] in pairs])       # build dicts

square = lambda x: x * x                         # Ex 7: lambda args: result (one line, no return)
line = lambda m, x, b: m * x + b                 # y = mx + b
print(square(5), line(2, 3, 1))
