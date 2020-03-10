n = int(input())
a = [int(x) for x in input().split()]

gray = 0
brown = 0
green = 0
light_blue = 0
blue = 0
yellow = 0
orange = 0
red = 0
ex = 0

for i in range(n):
    if a[i] <= 399:
        gray = 1
    elif a[i] <= 799:
        brown = 1
    elif a[i] <= 1199:
        green = 1
    elif a[i] <= 1599:
        light_blue = 1
    elif a[i] <= 1999:
        blue = 1
    elif a[i] <= 2399:
        yellow = 1
    elif a[i] <= 2799:
        orange = 1
    elif a[i] <= 3199:
        red = 1
    else:
        ex += 1

if ex == n:
    min_color = 1
    max_color = ex
else:
    min_color = gray + brown + green + light_blue + blue + yellow + orange + red
    max_color = min_color + ex

print('{}'.format(min_color) +' {}'.format(max_color))