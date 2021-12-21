def repeat(n):  # Вот это и надо реализовать
    def decorator(function):
        def fake_function(*args, **kwargs):  # Создаёт внутри фальшивую функцию
            result = 0
            if n == 0:
                result = args[0]
            for i in range(n):
                result = function(*args, **kwargs)
                lst = list(args)
                lst[0] = result
                args = tuple(lst)
            return result  # И возвращает значение

        return fake_function  # Ещё не забыли? Декоратор получает функцию и возвращает тоже функцию
    return decorator

@repeat(2)
def plus_1(x, y):
    return x + 1


@repeat(0)
def mul_2(x):
    return x * 2

print(plus_1(3, 4))  # должно выдать 5
print(mul_2(4))  # должно выдать 4
