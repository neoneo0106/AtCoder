w,h,x,y = map(int, input().split())

midw = w/2
midh = h/2

menseki = (w * h) / 2
check = 0
if midw == x and midh == y:
    check = 1

print(str("{:.6f}".format(menseki))+ " " + str(check))