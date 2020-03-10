n = int(input())
p = list(map(int, input().split()))

count = 0

for i in range(0, n):
    if i + 1 == p[i]:
        count += 1

if count >= n - 2:
    print("YES")
else:
    print("NO")