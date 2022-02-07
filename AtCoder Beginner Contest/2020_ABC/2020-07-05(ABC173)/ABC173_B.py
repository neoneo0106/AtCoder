n = int(input())
num_ac = 0
num_wa = 0
num_tle = 0
num_re = 0

for i in range(n):
    s = input()
    if s == "AC":
        num_ac += 1
    elif s == "WA":
        num_wa += 1
    elif s == "TLE":
        num_tle += 1
    elif s == "RE":
        num_re += 1


print("AC x {}".format(num_ac))
print("WA x {}".format(num_wa))
print("TLE x {}".format(num_tle))
print("RE x {}".format(num_re))
