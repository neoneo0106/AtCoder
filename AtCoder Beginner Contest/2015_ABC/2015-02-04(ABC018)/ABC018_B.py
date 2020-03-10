s = input()
n = int(input())
l = [0] * n
r = [0] * n
for i in range(n):
    l[i], r[i] = map(int, input().split())


for i in range(n):
    a = s[:l[i]-1]
    temp = s[l[i]-1:r[i]]
    b = temp[::-1]
    c = s[r[i]:]
    s = a + b + c

print(s)

