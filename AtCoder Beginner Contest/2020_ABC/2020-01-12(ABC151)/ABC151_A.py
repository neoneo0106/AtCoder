c = input()
s = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(s)):
    if s[i] == c:
        print(s[i+1])
