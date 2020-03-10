a,b = map(int, input().split())

c = []

c.append(a+b)
c.append(a-b)
c.append(a*b)

print(max(c))