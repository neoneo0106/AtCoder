n = int(input())
d = list(map(int, input().split()))

d.sort()
count = 0

if n % 2 == 1:
    print("0")
    exit(0)
else:
    if d[int(n/2)-1] == d[int(n/2)]:
        print("0")
        exit(0)
    else:
        k = d[int(n/2)-1]
        while(1):
            if k != d[int(n/2)]:
                count += 1
                k = k + 1
            else:
                break

print(count)
