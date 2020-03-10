n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())

maxa = max(a)
index_max = a.index(maxa)

for i in range(0, n):
    if i == index_max:
        print(sorted(a)[-2])
    else:
        print(maxa)