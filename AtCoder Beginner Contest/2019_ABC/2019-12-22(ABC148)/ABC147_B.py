n = int(input())
s, t = map(str, input().split())

st = ""

for i in range(0, n):
    st += s[i]
    st += t[i]

print(st)