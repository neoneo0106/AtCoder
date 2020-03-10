n, m = map(int, input().split())

if n == m == 1:
    print("1")
elif n == 1:
    print(max(0,m-2))
elif m == 1:
    print(max(0,n-2))
else:
    print((max(0,n-2)) * (max(0,m-2)))