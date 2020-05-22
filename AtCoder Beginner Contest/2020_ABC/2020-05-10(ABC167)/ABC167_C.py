n, m, x = map(int, input().split())

c = []
for i in range(n):
    c.append([int(x) for x in input().split()])

min_cost = float('inf')

for i in range(2**n):
    cost = []
    ex = [0]*m
    for j in range(n):
        if (i>>j) & 1 == 1:
            cost.append(c[j][0])
            for k in range(1, m+1):
                ex[k-1] += c[j][k]
    flag = 1
    for l in range(len(ex)):
        if ex[l] < x:
            flag = 0
    if flag == 1:
        min_cost = min(min_cost, sum(cost))

if min_cost == float('inf'):
    print("-1")
else:
    print(min_cost)
