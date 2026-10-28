# Day 24: NumPy   (pip install numpy)
import numpy as np

a = np.array([1, 2, 3, 4])
m = np.array([[1, 2, 3], [4, 5, 6]])

print(a * 2, a + a, a ** 2)               # math runs on every item at once, no loop
print(m.shape, m.size, m.dtype)           # (rows, cols), item count, type
print(m[1, 2], m[:, 0], m[0, :2])         # [row, col]   : means "all"
print(m.reshape(3, 2))                    # same items, new shape
print(m[::-1])                            # rows reversed
print(a[a > 2])                           # boolean filter
print(np.mean(a), np.median(a), np.std(a), a.min(), a.max())
print(np.arange(0, 10, 3), np.linspace(0, 1, 5))   # step by 3 | 5 evenly spaced values
print(np.random.randint(0, 10, size=3))
print(np.dot([1, 2], [3, 4]))             # dot product: 1*3 + 2*4 = 11
print(np.matmul(m, m.T).shape)            # (2,3) @ (3,2) -> (2,2)
print(a.tolist())                         # back to a normal list
