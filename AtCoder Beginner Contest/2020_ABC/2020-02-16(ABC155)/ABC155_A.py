a, b, c = map(int, input().split())

if a == b and b == c:
    print("No")
    exit(0)
elif a == b or b == c or c == a:
    print("Yes")
    exit(0)
else:
    print("No")
    exit(0)