def up(x):
    return x-1

n = int(input())
h = [int(x) for x in input().split()]

sum = 0

for j in range(max(h)):
    if h[0] <= 0:
        cnt = 0
    else:
        cnt = 1
    flag = 1
    for i in range(n):
        if flag == 1 and h[i] <= 0:
            flag = 0
        elif flag == 0 and h[i] > 0:
            flag = 1
            cnt += 1
    h = list(map(up, h))
    sum = sum + cnt

print(sum)