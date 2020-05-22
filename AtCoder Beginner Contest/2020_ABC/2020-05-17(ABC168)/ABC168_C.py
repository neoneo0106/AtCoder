import math
a, b, h, m = map(int, input().split())

minute = h * 60 + m
short = minute * (1/2)
long = m * 6

degree = min(abs(short-long), abs(short-360-long))

c = (a**2 + b**2 - 2 * a * b * math.cos(degree/180 * math.pi)) ** (1/2)

print(c)