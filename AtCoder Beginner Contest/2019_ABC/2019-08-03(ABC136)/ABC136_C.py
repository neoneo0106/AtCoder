n = int(input())
h = list(map(int, input().split()))

maxh = h[0]

for i in range(1, n):
    if h[i] < maxh and h[i] < maxh - 1:
        print("No")
        exit(0)
    if h[i] > maxh:
        maxh = h[i]

print("Yes")