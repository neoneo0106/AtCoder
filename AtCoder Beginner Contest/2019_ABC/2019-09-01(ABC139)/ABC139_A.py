s = input()
t = input()
count = 0

for i in range(len(s)):
    if s[i] == t[i]:
        count = count + 1

print(count)