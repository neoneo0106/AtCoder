n,k = map(int, input().split())
s = input()

u = s.lower()

print(s[:k-1]+u[k-1:k]+s[k:])