n,k = map(int, input().split())

sum = 0

for i in range(1, n+1):
    cnt = 0
    while(1):
        if i < k:
            cnt += 1
            i = i * 2
        else:
            break
    sum = sum + (1/n) * (1/2)**cnt

print(sum)