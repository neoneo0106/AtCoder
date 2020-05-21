import math

def gcd(a,b,c):
    d = math.gcd(a, b)

    return math.gcd(c,d)

k = int(input())
sum = 0
for a in range(1, k+1):
    for b in range(1, k+1):
        for c in range(1, k+1):
            sum += gcd(a,b,c)

print(sum)