m = int(input())

v = m / 1000
vv = 0

if v < 0.1:
    vv = 0
elif v >= 0.1 and v <= 5:
    vv = v * 10
elif v >= 6 and v <= 30:
    vv = v + 50
elif v >= 35 and v <= 70:
    vv = (v - 30)/5 + 80
else:
    vv = 89

vv = int(vv)
print('{0:02d}'.format(vv))