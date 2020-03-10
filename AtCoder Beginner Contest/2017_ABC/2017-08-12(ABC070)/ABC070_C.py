from fractions import gcd

def lcm(x, y):
    return x * y // gcd(x, y)

n = int(input())
t = [int(input()) for _ in range(n)]

a = 1
for i in range(n):
    b = t[i]
    a = lcm(a, b)

print(a)