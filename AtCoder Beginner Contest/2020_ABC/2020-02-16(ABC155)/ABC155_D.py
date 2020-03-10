def cross(L):
    ans = 1
    for x in L:
        ans = ans * x
    return ans

import sys
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())
a = [int(x) for x in input().split()]

st = []
for combi in combinations(a, r=2):
    s = cross(combi)
    st.append(s)

lis = sorted(st)

print(lis[k-1])