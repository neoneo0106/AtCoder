def dijkstra(s, n, w, cost):
    d = [float("inf")] * n
    used = [False] * n
    d[s] = 0

    while True:
        v = -1
        for i in range(n):
            if (not used[i]) and (v == -1):
                v = i
            elif (not used[i]) and d[i] < d[v]:
                v = i
        if v == -1:
            break
        used[v] = True

        for j in range(n):
            d[j] = min(d[j], d[v] + cost[v][j])

    return d


n, x, y = map(int, input().split())

cost = [[float("inf") for _ in range(n)] for _ in range(n)]

ans = [0] * n
for i in range(n-1):
    cost[i][i+1] = 1
    cost[i+1][i] = 1

cost[x-1][y-1] = 1
cost[y-1][x-1] = 1

for i in range(n):
    cost[i][i] = 0

for i in range(n):
    a = dijkstra(i, n, n, cost)
    for j in range(n):
        ans[a[j]] += 1

for i in range(1, n):
    print(ans[i]//2)
