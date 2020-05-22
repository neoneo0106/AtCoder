n, k = map(int, input().split())

member = [0]*n

for i in range(k):
    d = int(input())
    a = [int(x) for x in input().split()]
    for j in range(d):
        member[a[j]-1] += 1

print(member.count(0))