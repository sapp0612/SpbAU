def extendedeuclid(a, b):
    if b == 0:
        return 1, 0, a
    x, y, d = extendedeuclid(b, a % b)
    return y, x - int(a / b) * y, d
    
    
print(extendedeuclid(35, 84))
