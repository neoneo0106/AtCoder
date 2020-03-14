x = input()

x = x.replace("o", "")
x = x.replace("k", "")
x = x.replace("u", "")
x = x.replace("ch", "")

if len(x) == 0:
    print("YES")
else:
    print("NO")
