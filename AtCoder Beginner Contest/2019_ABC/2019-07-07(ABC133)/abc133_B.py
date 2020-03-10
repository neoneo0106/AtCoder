n, d = map(int, input().split())

x = [list(map(int, input().split())) for i in range(n)]
count = 0

for j in range(0, n-1):
    for k in range(j+1, n):
        sum = 0
        for i in range(0, d):
            sum = sum + (abs(x[j][i] - x[k][i]) ** 2)
        if sum**(1/2) % 1 == 0:
            count += 1

print(count)