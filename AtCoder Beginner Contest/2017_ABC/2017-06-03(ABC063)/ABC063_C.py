n = int(input())
s = []
cnt = 0
for i in range(n):
    s.append(int(input()))
    if s[i] % 10 == 0:
        cnt += 1

if cnt == n:
    print("0")
    exit(0)

if sum(s) % 10 != 0:
    print(sum(s))
else:
    s.sort()
    for i in range(n):
        if s[i] % 10 != 0:
            print(sum(s)-s[i])
            exit(0)
