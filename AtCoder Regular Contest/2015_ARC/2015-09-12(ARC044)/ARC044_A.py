def n_prime(x):
    for i in range(2, int(n**(1/2))+1):
        if x % i == 0:
            return 0
    return 1

n = int(input())
s = str(n)

sum = 0
for i in range(len(s)):
    sum += int(s[i])

if n == 1:
    print("Not Prime")
elif n_prime(n) == 1:
    print("Prime")
elif n % 2 != 0 and n % 5 != 0 and sum % 3 != 0:
    print("Prime")
else:
    print("Not Prime")
