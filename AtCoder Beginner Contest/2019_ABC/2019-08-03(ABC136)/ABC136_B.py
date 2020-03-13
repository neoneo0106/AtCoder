n = int(input())
count = 0

for i in reversed(range(1, n+1)):
    if i // 10 == 0:
        count += 1
    elif i // (10 ** 2) >= 1 and i // (10 ** 2) <= 9:
        count += 1
    elif i // (10 ** 4) >= 1 and i // (10 ** 4) <= 9:
        count += 1

print(count)