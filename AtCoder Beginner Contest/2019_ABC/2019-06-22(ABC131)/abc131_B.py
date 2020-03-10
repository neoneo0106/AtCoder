n, l = map(int, input().split())

oishisa = [0] * n
min = l

for i in range(0, n):
    oishisa[i] = l + i
    if abs(oishisa[i]) < abs(min):
        min = oishisa[i]

sum = sum(oishisa) - min
print(sum)