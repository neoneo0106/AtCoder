import math
import decimal

a, b = map(str, input().split())

c = decimal.Decimal(a)
d = decimal.Decimal(b)

e = c * d

print(math.floor(e))
