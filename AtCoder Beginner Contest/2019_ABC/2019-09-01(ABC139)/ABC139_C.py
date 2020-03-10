n = int(input())
h = list(map(int, input().split()))

count = 0
go = []

for i in range(0, n-1):
    if h[i] >= h[i+1]:
        count += 1
    else:
        go.append(count)
        count = 0

go.append(count)

print(max(go))