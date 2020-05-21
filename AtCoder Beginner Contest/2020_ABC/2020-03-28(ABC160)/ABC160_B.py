x = int(input())

cnt = 0

while(x >= 500):
    cnt += 1000
    x = x-500

while(x >= 5):
    cnt += 5
    x = x- 5

print(cnt)