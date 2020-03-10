n = int(input())
a = list(map(int, input().split()))

mother = 0

for i in range(n):
    mother = mother + 1 / a[i]

print(1/mother)