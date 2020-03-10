def calc(n, x):
    return n // x

n = int(input())

if n % 2 == 1 or n == 0:
    print(0)

else:
    ans = 0
    m = 10
    while m <= n:
        ans += calc(n, m)
        m *= 5
    print(ans)

