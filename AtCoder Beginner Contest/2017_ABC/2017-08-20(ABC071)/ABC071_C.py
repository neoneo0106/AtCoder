from collections import Counter

n = int(input())
s = [int(x) for x in input().split()]

c = Counter(s)

c = sorted(c.items())

max1 = 0
max2 = 0
max3 = 0

for i in range(len(c)):
    if c[i][1] >= 2:
        if c[i][0] >= max2:
            if c[i][0] >= max1:
                max2 = max1
                max1 = c[i][0]
            else:
                max2 = c[i][0]

    if c[i][1] >= 4:
        max3 = c[i][0]

if max2 == 0:
    print("0")
else:
    print(max(max1*max2, max3**2))