n = int(input())
w = []
w.append(input())

for i in range(1, n):
    s = input()
    if i % 2 == 0:
        if s in w or w[i-1][-1] != s[0]:
            print("LOSE")
            exit(0)
    elif i % 2 == 1:
        if s in w or w[i-1][-1] != s[0]:
            print("WIN")
            exit(0)
    w.append(s)

print("DRAW")
