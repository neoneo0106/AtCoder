s = input()

s = s.replace("eraser", "")
s = s.replace("erase", "")
s = s.replace("dreamer", "")
s = s.replace("dream", "")


if len(s) > 0:
    print("NO")
else:
    print("YES")