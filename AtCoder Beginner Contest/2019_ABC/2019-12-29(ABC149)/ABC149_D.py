n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()

t_n = ""
count = 0

for i in range(n):
    if i >= k:
        if t[i] == "r" and t_n[i-k] == "p":
            t_n += "p"
        if t[i] == "r" and t_n[i-k] != "p":

            t_n += "p"

    else:
        if t[i] == "r":
            t_n += "p"
            count += p
        elif t[i] == "s":
            t_n += "r"
            count += r
        elif t[i] == "p":
            t_n += "s"
            count += s

print(count)
