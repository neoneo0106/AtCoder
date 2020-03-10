s = input()
c = 'abcdefghijklmnopqrstuvwxyz'

ans = len(s)

if len(set(s)) == 1:
    print("0")
    exit(0)

for j in range(len(c)):
    cnt = 0
    t = ''
    if c[j] in s:
        m = s
        while(1):
            t = ''
            for i in range(len(m)-1):
                if m[i] == c[j]:
                    t = t + c[j]
                elif m[i+1] == c[j]:
                    t = t + c[j]
                else:
                    t = t + m[i]
            m = t
            cnt += 1
            if len(set(t)) == 1:
                break
        ans = min(cnt, ans)

print(ans)

