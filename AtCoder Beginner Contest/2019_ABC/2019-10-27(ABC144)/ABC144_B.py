N = int(input())
check = 0

kuku = []

for a in range(1, 10):
    for b in range(1, 10):
        kuku.append(a * b)

for x in range(0, 81):
    if N == kuku[x]:
        check = 0
        break
    else:
        check = 1

if check == 0:
    print("Yes")
elif check == 1:
    print("No")