n = int(input())
p = list(map(int, input().split()))

count = 0

for i in range(0, n-2):
    if p[i] < p[i+1] and p[i+1] < p[i+2]:
        count += 1
    elif p[i] > p[i+1] and p[i+1] > p[i+2]:
        count += 1

print(count)