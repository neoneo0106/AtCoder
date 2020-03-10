l, r = map(int, input().split())

mod = 2019
minij = 2020

for i in range(l, r):
    for j in range(i+1, r+1):
        if (i * j) % mod < minij:
            minij = (i*j) % mod
            if minij == 0:
                print(minij)
                exit(0)

print(minij)