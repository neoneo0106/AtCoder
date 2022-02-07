n = int(input())
a = [int(x) for x in input().split()]


ans = 1
a.sort()

for i in range(n):
    ans = ans * a[i]
    if a[i] == 0:
        print("0")
        exit(0)
    if ans > 10 ** 18:
        print("-1")
        exit(0)

print(ans)