h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

n = [[0] * w for i in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            if i != 0:
                n[i-1][j] += 1
                if j != 0:
                    n[i-1][j-1] += 1
                if j != w-1:
                    n[i-1][j+1] += 1
            if i != h-1:
                n[i+1][j] += 1
                if j != 0:
                    n[i+1][j-1] += 1
                if j != w-1:
                    n[i+1][j+1] += 1
            if j != 0:
                n[i][j-1] += 1
            if j != w-1:
                n[i][j+1] += 1


for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            n[i][j] = "#"
    print(''.join(map(str, n[i])))