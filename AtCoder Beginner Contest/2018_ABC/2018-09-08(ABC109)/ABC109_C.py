from fractions import gcd

n, k = map(int, input().split())
x = [int(x) for x in input().split()]

min = abs(k-x[0])

for i in range(n-1):
    min = gcd(min, abs(x[i]-x[i+1]))

print(min)
