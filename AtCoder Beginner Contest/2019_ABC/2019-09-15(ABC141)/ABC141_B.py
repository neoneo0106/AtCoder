s = input()

for i in range(len(s)):
    if i % 2 == 0:
        if s[i] != 'R' and s[i] != 'U' and s[i] != 'D':
            print("No")
            exit(0)
    else:
        if s[i] != 'L' and s[i] != 'U' and s[i] != 'D':
            print("No")
            exit(0)

print("Yes")