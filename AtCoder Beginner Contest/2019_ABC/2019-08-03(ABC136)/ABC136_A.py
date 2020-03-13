a,b,c = map(int, input().split())

d = 0

d = c - (a - b)

if d < 0:
    d = 0

print(d)