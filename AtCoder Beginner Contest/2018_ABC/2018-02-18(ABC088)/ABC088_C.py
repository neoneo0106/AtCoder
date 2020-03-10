a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

for i in range(0, 3):
    for j in range(i, 3):
        if a[i] + b[j] != a[j] + b[i] or a[i] + c[j] != a[j] + c[i] or b[i] + c[j] != b[j] + c[i]:
            print("No")
            quit(0)

print("Yes")

