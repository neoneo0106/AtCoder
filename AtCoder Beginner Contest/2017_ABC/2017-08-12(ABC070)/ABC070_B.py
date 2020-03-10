a, b, c, d = map(int, input().split())

max_t = max(a, c)
min_t = min(b, d)

print(max(min_t-max_t, 0))