n, s, t = map(int, input().split())
w = int(input())
if w >= s and w <= t:
    cnt = 1
else:
    cnt = 0

for i in range(n-1):
    a = int(input())
    w = w + a
    if w >= s and w <= t:
        cnt += 1

print(cnt)