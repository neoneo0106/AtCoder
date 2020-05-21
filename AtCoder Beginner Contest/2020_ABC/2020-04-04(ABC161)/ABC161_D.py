k = int(input())
queue = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(k):
    a = queue.pop(0)
    if a % 10 != 0:
        queue.append(10*a + (a % 10) - 1)
    queue.append(10 * a + (a % 10))
    if a % 10 != 9:
        queue.append(10 * a + (a % 10) + 1)

print(a)