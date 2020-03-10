h, w = map(int, input().split())

s = []
for i in range(h):
    s.append([x for x in input().split()])


for i in range(h):
    for j in range(w):
        cnt = 0
        shape = 0

        if s[i][0][j] == "#":
            if i != 0 :
                cnt += 1
                if s[i-1][0][j] == "#":
                    shape += 1
            if i != h-1:
                cnt += 1
                if s[i+1][0][j] == "#":
                    shape += 1
            if j != 0:
                cnt += 1
                if s[i][0][j-1] == "#":
                    shape += 1
            if j != w-1:
                cnt += 1
                if s[i][0][j+1] == "#":
                    shape += 1

            if shape == 0:
                print("No")
                exit(0)

print("Yes")
