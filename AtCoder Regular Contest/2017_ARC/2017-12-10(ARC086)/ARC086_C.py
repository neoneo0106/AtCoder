import collections

n, k = map(int, input().split())
a = list(map(int, input().split()))

c = collections.Counter(a)
b = list(sorted(c.values(), reverse=True))
sum = 0

if len(c) <= k:
    print("0")
    exit(0)

for i in range(0, k):
    sum = sum + b[i]

print(max(len(a)-sum, 0))