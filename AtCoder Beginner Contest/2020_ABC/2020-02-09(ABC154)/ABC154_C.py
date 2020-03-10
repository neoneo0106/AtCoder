n = int(input())
a = list(map(int, input().split()))

ac = set(a)

if len(ac) == len(a):
    print("YES")
else:
    print("NO")