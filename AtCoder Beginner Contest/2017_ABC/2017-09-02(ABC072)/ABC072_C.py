n = int(input())
a = [int(x) for x in input().split()]

d = [0] * (10**5)

for i in range(n):
    d[a[i]] += 1

ans = 1

for j in range(1, n-1):
    ans = max(ans, d[j-1] + d[j] + d[j+1])

print(ans)