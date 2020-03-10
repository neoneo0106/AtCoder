n, k = map(int, input().split())
p = list(map(int, input().split()))

temp= sum(p[:k])
ans = temp

for i in range(n-k):
    temp = temp - p[i]
    temp = temp + p[i+k]
    ans = max(temp, ans)

ans = (ans+k) / 2

print(ans)