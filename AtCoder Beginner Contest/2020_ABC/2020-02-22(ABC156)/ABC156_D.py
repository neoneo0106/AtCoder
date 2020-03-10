def extgcd(a, b):
    r = [1, 0, a]
    w = [0, 1, b]
    while w[2] != 1:
        q = r[2] // w[2]
        r2 = w
        w2 = [r[0] - q * w[0], r[1] - q * w[1], r[2] - q * w[2]]
        r = r2
        w = w2
    return [w[0], w[1]]

def mod_inv(a, m):
    x = extgcd(a, m)[0]
    return (m + x % m) % m

def mod_e(n, p):
    res = 0
    while n >= p:
        res += n // p
        n = n // p
    return res

def mod_fact(n, p):
    if n == 0:
        return 1

    res = mod_fact(n // p, p)

    if n // p % 2 != 0:
        return res * (p - fact[n % p]) % p
    return res * fact[n % p] % p

def cmb(n, k, p):
    if n < 0 or k < 0 or n < k:
        return 0
    e1 = mod_e(n, p)
    e2 = mod_e(k, p)
    e3 = mod_e(n - k, p)
    if e1 > e2 + e3:
        return 0
    a1 = mod_fact(n, p)
    a2 = mod_fact(k, p)
    a3 = mod_fact(n - k, p)
    return a1 * mod_inv(a2 * a3 % p, p) % p

p =10**9+7

fact = [1]
k = 1
for i in range(1,10**9+1):
    k = k*i%p
    fact.append(k)

n,a,b = map(int, input().split())

sum = 0
for i in range(n // 2):
    sum = sum + 2 * cmb(n, i, p)
    sum = sum % p

if n % 2 == 0:
    sum = sum + cmb(n, n // 2, p)

sum = sum - cmb(n, a, p) - cmb(n, b, p)

sum = sum % p

print(sum - 1)

