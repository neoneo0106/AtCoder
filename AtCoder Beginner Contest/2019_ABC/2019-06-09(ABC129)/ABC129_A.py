p, q, r = map(int, input().split())
time = []
time.append(p+q)
time.append(r+q)
time.append(p+r)

print(min(time))
