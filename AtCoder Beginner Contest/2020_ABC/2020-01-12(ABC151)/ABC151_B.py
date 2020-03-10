n, k, m = map(int, input().split())
a = list(map(int, input().split()))

score = 0

for i in range(n-1):
    score += a[i]

iru = n * m

b = iru - score

if b <= k:
    if b < 0:
        print("0")
    else:
        print(b)
else:
    print("-1")