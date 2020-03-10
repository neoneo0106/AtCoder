n, a, b = map(int, input().split())

cnt = (n // (a+b)) * a
ex = n % (a+b)
if a > ex:
    cnt = cnt + ex
else:
    cnt = cnt + a

print(cnt)