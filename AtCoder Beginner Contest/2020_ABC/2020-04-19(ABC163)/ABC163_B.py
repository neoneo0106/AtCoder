n, m = map(int, input().split())
a = [int(x) for x in input().split()]

print(max(-1, n-sum(a)))