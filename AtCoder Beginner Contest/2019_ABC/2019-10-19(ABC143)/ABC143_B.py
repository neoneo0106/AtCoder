N = int(input())
d = list(map(int, input().split()))

sum = 0

for i in range(0, N):
    for j in range(i, N):
        if i != j:
            sum = sum + d[i] * d[j]

print(sum)