import collections as cl

n = int(input())
s = [""]*n
for i in range(0, n):
    s[i] = input()
    s[i] = ''.join(sorted(s[i]))

cs = cl.Counter(s)
num = list(cs.values())
count = 0

for j in range(0, len(num)):
    if num[j] != 1:
        count = count + (num[j] * (num[j] - 1)) / 2

print(int(count))
