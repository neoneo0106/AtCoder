n = int(input())
a = [int(x) for x in input().split()]

cnt = 0

div = [1] * n
for i in range(n):
    lst = list(map(lambda x: x % a[i], a))
    lst[i] = 1
    div = [x * y for (x, y) in zip(div, lst)]

print(n-div.count(0))
