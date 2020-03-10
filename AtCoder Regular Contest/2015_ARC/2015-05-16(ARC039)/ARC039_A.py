a, b = map(int,input().split())

if 999-a >= b-100:
    a = str(a)
    if a[0] != '9':
        a = '9' + a[1:]
    else:
        if a[1] != '9':
            a = a[0] + '9' + a[2]
        else:
            a = a[:2] + '9'
    a = int(a)
else:
    b = str(b)
    if b[0] != '1':
        b = '1' + b[1:]
    else:
        if b[1] != '0':
            b = b[0] + '0' + b[2]
        else:
            b = b[:2] + '0'
    b = int(b)

print(a-b)