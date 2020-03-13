n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sumb = sum(b)

for i in range(0, n):
    b[i] = b[i] - a[i]
    if b[i] > 0:
        a[i+1] = a[i+1] - b[i]
        if a[i+1] < 0:
            b[i] = abs(a[i+1])
            a[i+1] = 0
        elif a[i+1] >= 0:
            b[i] = 0
    elif b[i] <= 0:
        b[i] = 0

print(sumb - sum(b))