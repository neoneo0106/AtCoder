n, a, b = map(int,input().split())

if a > b:
    print("0")
    exit(0)

min_s = a*(n-1) + b
max_s = b*(n-1) + a

print(max(max_s - min_s + 1, 0))