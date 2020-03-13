n = int(input())
v = list(map(int, input().split()))


for i in range(0, n-1):
    min1 = min(v)
    v.remove(min1)
    min2 = min(v)
    v.remove(min2)
    fusion = (min1 + min2) / 2
    v.append(fusion)


print(v[0])