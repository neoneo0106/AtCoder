h = int(input())
i= 0

if h == 1:
    print(1)
    exit(0)

while(1):
    if h >= 2**(i+1) and h < 2**(i+2):
        print(2**(i+2)-1)
        exit(0)

    i = i + 1