a = []
for i in range(3):
    c = list(map(int, input().split()))
    a.append(c)
n = int(input())

for k in range(n):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if b == a[i][j]:
                a[i][j] = '#'

flag = 0

if a[0][0] == a[0][1] and a[0][1] == a[0][2]:
    flag = 1
if a[1][0] == a[1][1] and a[1][1] == a[1][2]:
    flag = 1
if a[2][0] == a[2][1] and a[2][1] == a[2][2]:
    flag = 1
if a[0][0] == a[1][0] and a[1][0] == a[2][0]:
    flag = 1
if a[0][1] == a[1][1] and a[1][1] == a[2][1]:
    flag = 1
if a[0][2] == a[1][2] and a[1][2] == a[2][2]:
    flag = 1
if a[0][0] == a[1][1] and a[1][1] == a[2][2]:
    flag = 1
if a[0][2] == a[1][1] and a[1][1] == a[2][0]:
    flag = 1

if flag == 0:
    print("No")
else:
    print("Yes")




