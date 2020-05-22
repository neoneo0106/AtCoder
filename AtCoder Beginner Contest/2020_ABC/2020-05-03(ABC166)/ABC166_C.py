n,m = map(int,input().split())
h = [int(x) for x in input().split()]

mem = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int,input().split())
    mem[a-1].append(b-1)
    mem[b-1].append(a-1)

ans = 0



for j in range(n):
    flag = 1
    for k in range(len(mem[j])):
        if h[j] <= h[mem[j][k]]:
            flag = 0
    if flag ==  1:
        ans += 1

print(ans)