def moji(x):
    return chr(x + 96)

n = int(input())
s = ""

cnt = 0
a = 26
i = 1

while(1):
    if n <= a:
        cnt = i
        break
    i += 1
    a = 26 ** i + a



for i in range(1, cnt+1):
    if i != 1:
        n = n - (26**(i-1))
    if i == 1:
        k = n % 26
        if k == 0:
            k = 26
        s += moji(k)
    else:
        if n %  (26 ** (i-1)) == 0:
            k = (n // (26 ** (i-1))) % 26
        else:
            k = (n // (26 ** (i-1))) % 26 + 1
        if k == 0:
            k = 26
        s += moji(k)

print(s[::-1])