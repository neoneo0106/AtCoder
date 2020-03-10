n, m = map(int, input().split())

problem = [0] * n
count = [0] * n

penal = 0

for i in range(m):
    p, x = map(str, input().split())
    p = int(p) - 1
    if x == "AC":
        if problem[p] == 0:
            problem[p] = 1
    elif x == "WA":
        if problem[p] == 0:
            count[p] += 1

for i in range(n):
    if problem[i] == 0:
        count[i] = 0

print("{}".format(sum(problem)) + " {}".format(sum(count)))

