s = input()

a = 0
b = 0
c = 0

for i in range(3):
    if s[i] == 'a':
        a += 1
    elif s[i] == 'b':
        b += 1
    elif s[i] == 'c':
        c += 1

if a == b and b == c:
    print('Yes')
else:
    print('No')