n, d = map(int, input().split())
ans = 0
for i in range(n):
    p, q = map(int, input().split())
    if (p ** 2 + q ** 2)**(1/2) <= d:
        ans += 1

print(ans)