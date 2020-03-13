n = int(input())
a = [int(input()) for _ in range(n)]

num = 1
cnt = 1

for i in range(n):
    if a[num-1] == 2:
        print(cnt)
        exit(0)
    num = a[num-1]
    cnt += 1

print("-1")