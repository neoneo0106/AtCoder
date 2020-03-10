n = int(input())
log = []

for i in range(n):
    s, p = map(str, input().split())
    log.append([s, int(p), i])

b = sorted(log, key=lambda x: x[0])
c = sorted(log, key=lambda x: x[1], reverse=True)

num = []

for i in range(n):
    for j in range(n):
        if b[i][0] == c[j][0]:
            if c[j][2] not in num:
                print(c[j][2]+1)
                num.append(c[j][2])
