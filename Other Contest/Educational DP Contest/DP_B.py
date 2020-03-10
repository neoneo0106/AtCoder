n, k = map(int, input().split())
h = [int(x) for x in input().split()]

dp = [0]*n

dp[0] = 0
dp[1] = abs(h[1]-h[0])

for i in range(2,n):
    dp[i] = abs(h[i] - h[i-1]) + dp[i-1]
    for j in range(2,k+1):
        if i-j >= 0:
            dp[i] = min(dp[i], abs(h[i]-h[i-j])+dp[i-j])

print(dp[-1])
