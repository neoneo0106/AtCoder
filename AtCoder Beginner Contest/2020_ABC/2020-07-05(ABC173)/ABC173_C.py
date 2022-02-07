import numpy as np

h, w, k = map(int, input().split())

gyo = [0] * (h+1)
retsu = [0] * (w+1)

c = []

black = 0

for i in range(h):
    a = list(input())
    black += a.count("#")
    c.append(a)

d = np.array(c).T
d = d.tolist()


for i in range(h):
    gyo[i] = c[i].count("#")
for j in range(w):
    retsu[j] = d[j].count("#")

ans = 0


for i in range(1<<len(gyo[:h])):
    l = []
    for j in range(len(gyo[:h])):
        if (i>>j & 1) == 1:
            l.append(gyo[:h][j])
    if len(l) != 0:
        if sum(l) == black-k:
            ans += 1


for i in range(1<<len(retsu[:w])):
    l = []
    for j in range(len(retsu[:w])):
        if (i>>j & 1) == 1:
            l.append(retsu[:w][j])
    if len(l) != 0:
        if sum(l) == black-k:
            ans += 1

print(ans)



