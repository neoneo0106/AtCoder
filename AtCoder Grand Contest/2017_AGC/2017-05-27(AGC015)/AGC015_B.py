s = input()

sum = 0

for i in range(1, len(s)-1):
    if s[i] == 'D':
        sum += len(s)-i-1
    else:
        sum += i

sum = sum + len(s)*(len(s)-1)
print(sum)
