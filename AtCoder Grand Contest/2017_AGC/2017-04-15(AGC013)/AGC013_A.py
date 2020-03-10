n = int(input())
a = [int(x) for x in input().split()]

flag = 0
cnt = 1

for i in range(n-1):
    if a[i] < a[i+1] and flag == 0:
        flag = 1
    elif a[i] > a[i+1] and flag == 0:
        flag = 2
    elif flag == 1 and a[i] > a[i+1]:
        cnt += 1
        flag = 0
    elif flag == 2 and a[i] < a[i+1]:
        cnt += 1
        flag = 0

print(cnt)