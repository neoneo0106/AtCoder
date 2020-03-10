n = int(input())
s = input()

ans = 0

for i in range(1,n):
    x = list(set(s[:i]))
    y = list(set(s[i:]))
    cnt = 0
    for j in range(len(x)):
        for k in range(len(y)):
            if x[j] ==  y[k]:
                cnt += 1

    ans = max(cnt ,ans)

print(ans)
