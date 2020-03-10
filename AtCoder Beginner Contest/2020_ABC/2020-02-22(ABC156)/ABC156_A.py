n,r = map(int, input().split())

if n >= 10:
    n = 10

print(100*(10-n)+r)