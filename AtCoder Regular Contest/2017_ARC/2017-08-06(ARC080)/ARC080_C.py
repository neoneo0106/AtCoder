n = int(input())
a = [int(x) for x in input().split()]

cnt2 = 0
cnt4 = 0

for i in range(n):
    if a[i] % 2 == 0 and a[i] % 4 != 0:
        cnt2 += 1
    elif a[i] % 4 == 0:
        cnt4 += 1

n = n - cnt2
if cnt2 == 0:
    if n-cnt4 <= cnt4+1:
        print("Yes")
    else:
        print("No")
else:
    if n-cnt4 <= cnt4:
        print("Yes")
    else:
        print("No")
