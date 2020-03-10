n = int(input())
p = list(map(int, input().split()))

min = n
count = 0

for i in range(n):
    if min >= p[i]:
        count += 1
        min = p[i]

print(count)