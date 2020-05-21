n = int(input())
s = list(input())

r = 0
g = 0
b = 0

for i in range(n):
    if s[i] == "R":
        r += 1
        s[i] = 1
    elif s[i] == "G":
        g += 1
        s[i] = 2
    else:
        b += 1
        s[i] = 4

cnt = r*g*b

for i in range(n):
    for j in range(i+1, n):
        k = 2 * j - i
        if k < n:
            if s[i] + s[j] + s[k] == 7:
                cnt -= 1

print(cnt)
