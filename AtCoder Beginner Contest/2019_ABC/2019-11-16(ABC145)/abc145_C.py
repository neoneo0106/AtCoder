import math

def dis(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2) ** (1/2)

def kaijo(n):
    return math.factorial(n)

n = int(input())
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())

sum = 0

for j in range(n):
    for i in range(n):
        if i != j:
            sum = sum + (dis(x[i], y[i], x[j], y[j])) * kaijo(n-1)

print(sum/kaijo(n))