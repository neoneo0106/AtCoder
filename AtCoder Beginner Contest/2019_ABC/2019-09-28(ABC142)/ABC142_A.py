n = int(input())

count = 0

for i in range(0, n):
    if i % 2 == 0:
        count += 1

print('{:.10f}'.format(count/n))