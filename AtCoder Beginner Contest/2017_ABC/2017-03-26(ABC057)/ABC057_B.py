n, m = map(int, input().split())
a = [0]*n
b = [0]*n
for i in range(n):
    a[i], b[i] = map(int, input().split())

c = [0]*m
d = [0]*m
for i in range(m):
    c[i], d[i] = map(int, input().split())

index = 0

for i in range(n):
    ans = 2 * 10 ** 16 + 1
    for j in range(m):
        cnt = abs(a[i]-c[j]) + abs(b[i]-d[j])
        if cnt < ans:
            ans = cnt
            index = j+1
    print(index)
