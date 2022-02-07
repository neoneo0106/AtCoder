x, n = map(int, input().split())
if n == 0:
    print(x)
    exit(0)
else:
    p = [int(x) for x in input().split()]

p.sort()


ans1 = 300
ans2 = 300

flag = 1

for i in range(100):
    if x-i not in p:
        ans1 = x-i
        flag = 0
    if x+i not in p:
        ans2 = x+i
        flag = 0
    if flag == 0:
        break
    else:
        continue

print(min(ans1, ans2))