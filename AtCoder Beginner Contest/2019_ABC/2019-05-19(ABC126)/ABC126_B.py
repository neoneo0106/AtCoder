s = input()

a = int(s[0:2])
b = int(s[2:4])

if a >= 1 and a <= 12:
    if b >= 1 and b <= 12:
        print("AMBIGUOUS")
    else:
        print("MMYY")
elif b >= 1 and b <= 12:
    if a >= 1 and a <= 12:
        print("AMBIGUOUS")
    else:
        print("YYMM")
else:
    print("NA")

