n = int(input())
b = list(map(int, input().split()))
c = [0] * n

c[0] = b[0]
c[n-1] = b[n-2]

for i in range(1, n-1):
    c[i] = min(b[i-1], b[i])

print(sum(c))