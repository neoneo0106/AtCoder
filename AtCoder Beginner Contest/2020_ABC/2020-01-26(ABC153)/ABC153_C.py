n, k = map(int, input().split())
h = list(map(int, input().split()))

if k >= len(h):
    print("0")
    exit(0)

h.sort()
# print(h[:n-k])
print(sum(h[:n-k]))
