a, v = map(int,input().split())
b, w = map(int, input().split())
t = int(input())


if w >= v:
    print("NO")
else:
    if abs(b-a) > (v-w) * t:
        print("NO")
    else:
        print("YES")

