n = int(input())
a = [int(x) for x in input().split()]

a = sorted(a)
alice = 0
bob = 0
for i in range(n):
    if i % 2 == 0:
        alice += a[i]
    else:
        bob += a[i]

print(abs(alice - bob))