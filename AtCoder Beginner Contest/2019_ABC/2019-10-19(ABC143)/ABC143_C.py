N = int(input())
s = input()

sum = 0

for i in range(0, N-1):
    if s[i] != s[i+1]:
        sum += 1

print(sum + 1)
