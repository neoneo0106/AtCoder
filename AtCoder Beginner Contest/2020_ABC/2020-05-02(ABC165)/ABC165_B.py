x = int(input())

ans = 0
cnt = 100
while(1):
    cnt = int(cnt * 1.01)
    ans += 1
    if cnt >= x:
        print(ans)
        exit(0)