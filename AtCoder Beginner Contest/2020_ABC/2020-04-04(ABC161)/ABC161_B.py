n, m = map(int, input().split())
a = [int(x) for x in input().split()]

a.sort(reverse=True)

for i in range(m):
    if a[i] < sum(a) / (4*m):
        print("No")
        exit(0)

print("Yes")