a, b, c, k = map(int, input().split())

sum = 0

if k-a >= 0:
    sum += a
    k = k-a
else:
    sum += k
    print(sum)
    exit(0)

if k-b >= 0:
    k = k-b
else:
    print(sum)
    exit(0)


if k-c >= 0:
    sum -= c
else:
    sum -= k
    print(sum)
    exit(0)

print(sum)