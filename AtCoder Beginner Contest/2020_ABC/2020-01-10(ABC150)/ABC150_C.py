import itertools
import numpy as np
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

num = np.arange(1, n+1)

zyun = list(itertools.permutations(list(num), n))

for i in range(0, len(zyun)):
    if zyun[i] == p:
        a = i+1
    if zyun[i] == q:
        b = i+1

print(abs(a-b))