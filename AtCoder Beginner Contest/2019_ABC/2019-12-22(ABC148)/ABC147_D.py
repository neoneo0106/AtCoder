n = int(input())
a = list(map(int, input().split()))

count = 0

i = 1
k = 1
index = 0


for j in range(index, n):
    if a[j] == i:
        count += 1
        i += 1
        index = j

if index != 0 or (n == 1 and a[0] == 1) or (index == 0 and count == 1):
    print(n-count)
else:
    print("-1")