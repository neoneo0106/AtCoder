n, y = map(int, input().split())

for i in range(n, -1, -1):
    for j in range(n-i, -1, -1):
        if i *10000 + j * 5000 + (n-i-j) * 1000 == y:
            print(str(i) + ' ' + str(j) + ' ' + str(n-i-j))
            exit(0)

print("-1 -1 -1")