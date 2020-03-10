a, b, c = map(int, input().split())

d = a % b
for i in range(b):
    if (d * i + c) % b == 0:
        print("YES")
        exit(0)

print("NO")