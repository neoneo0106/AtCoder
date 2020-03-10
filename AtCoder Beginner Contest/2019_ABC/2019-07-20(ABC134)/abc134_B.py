n, d = map(int, input().split())

visible = d * 2 + 1

if n % visible == 0:
    print(n // visible)
else:
    print(n// visible + 1)