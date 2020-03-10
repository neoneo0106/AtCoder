n, a, b = map(int, input().split())
cnt = 0

for i in range(1, n+1):
    s = str(i)
    sum = 0
    for j in range(len(s)):
        sum += int(s[j])
    if sum >= a and sum <= b:
        cnt += i

print(cnt)
