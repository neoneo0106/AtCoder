n, k = map(int, input().split())

ans = 0

for i in range(k,n+2):
    mini = i*(i-1)//2
    maxa = (i*(n + n-i+1))//2
    ans += maxa - mini + 1
    ans = ans % (10**9 +7)

print(ans)