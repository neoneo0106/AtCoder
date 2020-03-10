n = int(input())
r = input()

sum = 0

for i in range(n):
    if r[i] == "A":
        sum = sum + 4
    elif r[i] == "B":
        sum = sum + 3
    elif r[i] == "C":
        sum = sum + 2
    elif r[i] == "D":
        sum = sum + 1

print(sum/n)