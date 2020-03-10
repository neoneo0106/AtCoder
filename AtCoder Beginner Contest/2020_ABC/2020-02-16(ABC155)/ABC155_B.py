n = int(input())
a = list(map(int, input().split()))

flag = 1

for i in range(n):
    if a[i] % 2 == 0:
        if a[i] % 3 == 0 or a[i] % 5 == 0:
            continue
        else:
            flag = 0

if flag == 0:
    print("DENIED")
elif flag == 1:
    print("APPROVED")