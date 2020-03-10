n,k,q = map(int,input().split())
a = [0] * q

member = [k] * n

for i in range(q):
    a[i] = int(input())
    member[a[i]-1] = member[a[i]-1] + 1

for j in range(n):
    if member[j] - q <= 0:
        print("No")
    else:
        print("Yes")
