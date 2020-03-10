import fractions
a,b,c,d = map(int, input().split())

cnt_c = b // c - (a-1) // c
cnt_d = b // d - (a-1) // d
lcm = c * d // fractions.gcd(c, d)
cnt_cd = b // lcm - (a-1) // lcm

mul = cnt_c + cnt_d - cnt_cd

print(b - a + 1 - mul)