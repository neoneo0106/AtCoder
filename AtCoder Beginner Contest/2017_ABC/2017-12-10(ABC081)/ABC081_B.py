n = int(input())
a = list(map(int, input().split()))

cnt = 0

while(1):
    for i in range(n):
        if a[i] % 2 == 1:
            print(cnt)
            exit(0)
        else:
            a[i] = a[i] // 2
    cnt += 1
