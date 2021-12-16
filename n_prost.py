def prime(number):
    if number in [1, 2, 3]:
        return 'Простое'
    sqrt_number = int(number ** 0.5)
    for el in range(2, sqrt_number + 1):
        if number % el == 0:
            return 'Составное'
    return 'простое'
    
print(prime(111))
