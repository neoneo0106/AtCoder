s = input()

a = [0]* (len(s)+1)

for i in range(len(s)):
    if s[i] == '<':
        a[i+1] = a[i]+1

s = s[::-1]

for i in range(len(s)):
    if s[i] == '>':
        a[len(s)-i-1] = max(a[len(s)-i-1], a[len(s)-i]+1)


print(sum(a))
