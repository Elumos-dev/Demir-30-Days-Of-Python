# Day 15: error types. Read the LAST line of a traceback first:  ErrorType: message
# Each string below is broken code. exec() runs a string as code, so one loop can show them all.

broken = [
    'print(undefined_name)',     # NameError: the variable doesn't exist
    '[1, 2][5]',                 # IndexError: position out of range
    "{'a': 1}['b']",             # KeyError: missing dict key
    "'abc'.push('d')",           # AttributeError: that method doesn't exist
    "1 + '1'",                   # TypeError: types that don't mix
    "int('abc')",                # ValueError: right type, impossible value
    '10 / 0',                    # ZeroDivisionError
    'import mathh',              # ModuleNotFoundError: typo in a module name
    'from math import pie',      # ImportError: module exists, name doesn't
    "print 'hi'",                # SyntaxError: in a real file this stops everything before it runs
]

for code in broken:
    try:                         # try/except = Day 17
        exec(code)
    except Exception as e:
        print(f'{type(e).__name__:<20} {code}')
