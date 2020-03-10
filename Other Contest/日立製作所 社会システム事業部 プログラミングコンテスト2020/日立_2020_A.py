s = input()

for i in range(1, 7):
    if s == "hi"*i:
        print("Yes")
        exit(0)

print("No")