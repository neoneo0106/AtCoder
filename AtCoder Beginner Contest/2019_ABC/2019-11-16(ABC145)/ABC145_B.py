n = int(input())
s = input()

if n % 2 == 1:
    print("No")
    exit(0)

for i in range(n//2):
    if s[i] != s[i + n //2]:
        print("No")
        exit(0)

print("Yes")