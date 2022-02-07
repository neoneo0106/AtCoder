n = int(input())

s = input()

cnt = 0

for i in range(n):
    if s[i] == "R":
        cnt += 1

ans = 0

for i in range(cnt):
    if s[i] == "W":
        ans += 1

print(ans)