def kaibun(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return 0

    return 1

s = input()
left = s[:((len(s)-1)//2)]
right = s[((len(s)+3)//2-1):]

if kaibun(s) == 1 and kaibun(left) == 1 and kaibun(right) == 1:
    print("Yes")
else:
    print("No")
