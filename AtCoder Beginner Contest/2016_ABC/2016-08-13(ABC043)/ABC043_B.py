s = input()
n = ""

for i in range(len(s)):
    if s[i] != 'B':
        n = n + s[i]
    else:
        if len(n) != 0:
            n = n[:-1]

print(n)