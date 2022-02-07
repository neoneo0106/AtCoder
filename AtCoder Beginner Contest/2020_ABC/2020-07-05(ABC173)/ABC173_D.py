n = int(input())

a = [int(x) for x in input().split()]

a.sort(reverse=True)
ans = a[0]

for i in range(1, n-1):
    j = (i+1) // 2
    ans += a[j]
print(ans)