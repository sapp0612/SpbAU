def prime(number):
    if number in [1, 2, 3]:
        return True
    sqrt_number = int(number ** 0.5)
    for el in range(2, sqrt_number + 1):
        if number % el == 0:
            return False
    return True 
    
print(prime(3571))
