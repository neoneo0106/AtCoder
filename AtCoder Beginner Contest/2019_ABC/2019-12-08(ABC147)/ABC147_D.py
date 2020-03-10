n = int(input())

a = list(map(int, input().split()))

sum = 0
count = 0

for i in range(0, n-1):
    for j in range(i+1, n):
        sum = sum + ((a[i] ^ a[j]) % (10**9 + 7))

sum = sum % (10**9 + 7)
print(sum)