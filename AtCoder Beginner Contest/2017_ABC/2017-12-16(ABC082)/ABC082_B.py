s = list(input())
t = list(input())

s = sorted(s)
t = sorted(t)
t = t[::-1]

s_ = ''
t_ = ''

for i in s:
    s_ += i
for j in t:
    t_ += j

if s_ < t_:
    print("Yes")
else:
    print("No")
