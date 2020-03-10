s = input()
flag = 0

if s[0] == s[1] and s[2] == s[3]:
    if s[1] != s[2]:
        flag = 1
elif s[0] == s[2] and s[1] == s[3]:
    if s[1] != s[2]:
        flag = 1
elif s[0] == s[3] and s[1] == s[2]:
    if s[0] != s[1]:
        flag = 1

if flag == 1:
    print("Yes")
else:
    print("No")
