n = int(input())
s = input()

cs = ""


for i in range(len(s)):
    temp = ord(s[i]) + n
    if temp > 90:
        temp = temp - 26
    cs = cs + chr(temp)

print(cs)

