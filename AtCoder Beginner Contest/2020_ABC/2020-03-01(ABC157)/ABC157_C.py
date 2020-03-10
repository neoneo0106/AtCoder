n, m = map(int, input().split())

if n == 1 and m == 0:
    print("0")
    exit(0)

num = [-1]*n
s = [0]*m
c = [0]*m

flag = 1

for i in range(m):
    s[i], c[i] = map(int, input().split())
    if n != 1:
        if s[i] == 1 and c[i] == 0:
            flag = 0

if flag == 0:
    print("-1")
    exit(0)

if flag == 1:
    for i in range(m):
        if num[s[i]-1] == -1:
            num[s[i]-1] = c[i]
        elif num[s[i]-1] != c[i]:
            print("-1")
            exit(0)


for i in range(n):
    if num[0] != -1:
        if num[i] == -1:
            num[i] = 0
    else:
        num[0] = 1

if n != 1 and set(num) == {0}:
    print("-1")
else:
    print(''.join(map(str, num)))
