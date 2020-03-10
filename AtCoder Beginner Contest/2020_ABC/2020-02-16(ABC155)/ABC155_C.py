from collections import Counter

n = int(input())
s = [input() for _ in range(n)]

c = Counter(s)

max_count = c.most_common()[0][1]

c = sorted(c.items())

for i in range(len(c)):
    if max_count == c[i][1]:
        print(c[i][0])
