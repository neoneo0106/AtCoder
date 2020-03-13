n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

sum = 0

for i in range(n):
    sum = sum + b[a[i]-1]
    if i >= 1:
        if a[i] == a[i-1] + 1:
            sum = sum + c[a[i-1]-1]

print(sum)
