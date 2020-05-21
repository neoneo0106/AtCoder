n = int(input())
a = [int(x) for x in input().split()]

cnt = [0] * n

ans = (n*(n-1))//2

for i in range(n):
    cnt[a[i]-1] += 1

for i in range(n):
    print(ans-cnt[a[i]-1]*(cnt[a[i]-1]-1)//2)

