import numpy as np
k, x = map(int, input().split())

min = x - (k - 1)
max = x + (k - 1)
a = np.arange(min, max+1, 1)
print(' '.join(map(str, a)))
