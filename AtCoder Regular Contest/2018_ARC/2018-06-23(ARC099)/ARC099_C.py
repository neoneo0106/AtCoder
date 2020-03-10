n, k = map(int, input().split())
a = [int(x) for x in input().split()]

if (n-1) % (k-1) == 0:
    print((n-1)//(k-1))
else:
    print((n-1)//(k-1)+1)
