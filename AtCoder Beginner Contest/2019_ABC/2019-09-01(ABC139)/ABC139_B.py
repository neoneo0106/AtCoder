a, b = list(map(int, input().split()))

c = 0

if b == 1:
    c = 0
elif (b-1) % (a-1) == 0:
    c = (b-1) // (a-1)
else:
    c = (b-1) // (a-1) + 1

print(c)