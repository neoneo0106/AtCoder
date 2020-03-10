s = input()

count = 0

for i in range(0, len(s)//2):
    if s[i] != s[len(s)-i-1]:
        count = count + 1

print(count)