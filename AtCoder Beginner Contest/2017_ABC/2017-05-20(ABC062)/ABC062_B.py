h, w = map(int, input().split())

s = []*(h+2)
for i in range(h+2):
    s.append(['#']*(w+2))

for i in range(h):
    c = input()
    s[i+1][1:w+1] = c

for j in range(h+2):
    print(''.join(s[j]))