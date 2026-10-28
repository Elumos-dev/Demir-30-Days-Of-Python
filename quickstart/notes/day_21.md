Building the `Statistics` and `PersonAccount` classes:
1. In `__init__`, store the data on `self` (`self.data = data`, or `self.incomes = []`).
2. Write one method per measure. Each method reads `self.data` and **returns** a value.
3. Methods can call each other: `def range(self): return self.max() - self.min()`.
4. `describe()` builds one string from the other methods with an f-string.
