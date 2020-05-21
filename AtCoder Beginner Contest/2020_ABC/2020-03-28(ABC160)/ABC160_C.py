k, n = map(int, input().split())
a = [int(x) for x in input().split()]

dis = [0] * n

for i in range(n-1):
    dis[i] = abs(a[i+1] - a[i])

dis[n-1] = min(abs(a[n-1] - a[0]), abs((a[0]+k)-a[n-1]))

print(sum(dis)-max(dis))