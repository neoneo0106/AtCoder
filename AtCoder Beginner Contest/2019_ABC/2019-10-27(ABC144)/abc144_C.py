import math

N = int(input())

sqrtN = int(math.sqrt(N))

for i in reversed(range(1, sqrtN+1)):
    if N % i == 0:
        print(int(i + N/i - 2))
        quit(0)
