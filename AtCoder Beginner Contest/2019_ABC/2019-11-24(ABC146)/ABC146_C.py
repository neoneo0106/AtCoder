a, b, x = map(int, input().split())

l, r = 0, 10**9+1

while(l + 1 < r):
    mid = (l + r) // 2
    if a * mid + b * len(str(mid)) <= x:
        l = mid
    else:
        r = mid

print(l)
