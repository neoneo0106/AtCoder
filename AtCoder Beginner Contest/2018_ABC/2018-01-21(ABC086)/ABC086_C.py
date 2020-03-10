def dis(x_1, y_1, x_2, y_2):
    return ((x_1-x_2)**2 + (y_1-y_2)**2)**(1/2)

n = int(input())
t = [0] * n
x = [0] * n
y = [0] * n
for i in range(n):
    t[i], x[i], y[i] = map(int, input().split())

for i in range(n):
    if t[i] % 2 !=  (x[i] + y[i]) % 2:
        print("No")
        exit(0)
    if i != 0:
        if dis(x[i-1], y[i-1], x[i], y[i]) > t[i] - t[i-1]:
            print("No")
            exit(0)
    else:
        if x[i] + y[i] > t[i]:
            print("No")
            exit(0)

print("Yes")