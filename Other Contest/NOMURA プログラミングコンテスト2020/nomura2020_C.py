n = int(input())
a = [int(x) for x in input().split()]

flag = 1

if a[0] != 0:
    print("-1")
    exit(0)

ans = 1
cnt = 1
max_list = [a[n]]

for i in reversed(range(0,n)):
    max_list.append(max_list[n-i-1]+a[i])

max_list = max_list[::-1]

for i in range(0,n):
    if i != 0:
        if max_list[i] < a[i]*2:
            print("-1")
            exit(0)
        else:
            ans += min(max_list[i], cnt*2)
            cnt = cnt * 2 - a[i]
            print(cnt)

print(ans+a[n])