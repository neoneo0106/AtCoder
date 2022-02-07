n = int(input())
a = [int(x) for x in input().split()]
q = int(input())

num = [0] * (10**5)
for i in range(len(a)):
    num[a[i]-1] += 1

ans = sum(a)

for j in range(q):
    b, c = map(int, input().split())
    ans -= num[b-1] * b
    num[c-1] += num[b-1]
    ans += c * num[b-1]
    num[b-1] = 0
    print(ans)