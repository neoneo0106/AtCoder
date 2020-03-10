n, m = map(int, input().split())

if 2*n >= m:
    print(m//2)
    exit(0)


c = m - (2*n)
s = c // 4

print(n+s)
