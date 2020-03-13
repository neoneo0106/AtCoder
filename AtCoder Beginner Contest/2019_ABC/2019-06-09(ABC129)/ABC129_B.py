n = int(input())
w = list(map(int ,input().split()))

min = sum(w)

for t in range(0, n):
    mint = abs(sum(w[0:t+1]) - sum(w[t+1:n]))
    if mint < min:
        min = mint

print(min)