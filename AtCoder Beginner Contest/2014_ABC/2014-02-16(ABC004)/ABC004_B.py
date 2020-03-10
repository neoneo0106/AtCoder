import numpy as np

a = [list(input()) for _ in range(4)]
a = np.array(a)
a = a[::-1,::-1]

for i in range(4):
    print(''.join(map(str, a[i])))
