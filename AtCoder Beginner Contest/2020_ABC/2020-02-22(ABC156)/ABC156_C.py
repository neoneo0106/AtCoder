n = int(input())
x = [int(x) for x in input().split()]


for i in range(min(x), max(x)):
    sum = 0
    for j in range(len(x)):
        sum = sum + (x[j]-i)**2

    if i == min(x):
        max_n = sum

    if sum <= max_n:
        max_n = sum

if len(set(x)) == 1:
    max_n = 0

print(max_n)