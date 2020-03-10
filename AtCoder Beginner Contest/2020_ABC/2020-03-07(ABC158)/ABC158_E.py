n, p = map(int, input().split())
s = input()

cnt = 0

for i in range(n):
    for j in range(i+1,n+1):
        if int(s[i:j]) % p == 0:
            cnt += 1

print(cnt)