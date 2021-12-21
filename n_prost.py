import math
def primality(n):
    a = 0
    if n < 2:
        return False
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            a += 1
    if a == 0:
        return True
    else:
        return False
# Пример
print( primality(-7) )
