s = input()

i = len(s)
index = 0

while(1):
    i = i-1
    s = s[:i]
    if len(s) % 2 == 0:
        if s[:i//2] == s[i//2:]:
            index = i
            break
    if i == 0:
        break


print(index)