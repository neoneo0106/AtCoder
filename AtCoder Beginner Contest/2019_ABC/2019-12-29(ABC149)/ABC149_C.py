import numpy

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(numpy.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

x = int(input())

while(1):
    if is_prime(x) == 1:
        break
    else:
        x = x + 1

print(x)