n = int(input())
max_t = [0] * n
min_t = [0] * n
for i in range(n):
    max_t[i], min_t[i] = map(float, input().split())

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

for i in range(n):
    if max_t[i] >= 35:
        a += 1
    elif max_t[i] >= 30:
        b += 1
    elif max_t[i] >= 25:
        c += 1
    elif max_t[i] < 0:
        f += 1

    if min_t[i] >= 25:
        d += 1
    elif min_t[i] < 0 and max_t[i] >= 0:
        e += 1

print(str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(d) + ' ' + str(e) + ' ' + str(f))