a, b, k = map(int, input().split())

p = k
if a < k:
    k = k - a
    a = 0
else:
    k = k - a
    a = a - p

if k < 0:
    k = 0
b = b - k
if b < 0:
    b = 0

print("{}".format(a) + " {}".format(b))
