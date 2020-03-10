n, m, k = map(int , input().split())

friend = [[[],[],[]] for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    friend[a-1][0].append(b)
    friend[b-1][0].append(a)

for k in range(k):
    c, d = map(int, input().split())
    friend[c-1][1].append(d)
    friend[d-1][1].append(c)

print(friend)
