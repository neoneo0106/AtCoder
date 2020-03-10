n, m = map(int, input().split())
x = [int(x) for x in input().split()]

x.sort()

dis = []

if n >= m:
    print("0")
    exit(0)

for i in range(m-1):
    dis.append(x[i+1]-x[i])

dis.sort(reverse=True)

print(sum(dis[n-1:]))

