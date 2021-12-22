from numbers import Number


class SetsTypeError(TypeError):
    pass


class SetsDomainError(ValueError):
    pass


class Sets:
    def __init__(self, arg=0):
        # numbers -- числа в множестве
        if isinstance(arg, Number):
            self.numbers = [arg]
        elif isinstance(arg, list):
            self.numbers = arg.copy()
        elif isinstance(arg, Sets):
            self.numbers = arg.numbers.copy()
        else:
            raise SetsTypeError("You are trying to create polynomial from " + repr(arg))
        self.cleanup(self.numbers)
        self.sort(self.numbers)

    @staticmethod
    def cleanup(numbers):
        """
        Удаление повторяющихся элементов в множестве
        """
        indxes = list()
        for i in range(len(numbers)):
            for j in range(i, len(numbers)):
                if i != j and numbers[i] == numbers[j]:
                    indxes.append(j)
        for i in range(len(indxes)):
            numbers.pop(indxes[i] - i)

    @staticmethod
    def sort(numbers):
        """
        Сортировка множества по возрастанию
        """
        numbers.sort()

    def __str__(self):
        return ", ".join([str(n) for n in self.numbers])

    def __add__(self, other):
        if isinstance(other, Number):
            other = Sets(other)

        sn = self.numbers.copy()
        on = other.numbers.copy()

        new_set = sn
        for i in range(len(on)):
            new_set.append(on[i])

        self.cleanup(new_set)
        self.sort(new_set)

        return new_set

    def __eq__(self, other):
        if isinstance(other, Number):
            other = Sets(other)

        if isinstance(other, Sets):
            return self.numbers == other.numbers
        else:
            raise SetsDomainError("Can't say if Polynomial is equal to " + str(type(other)))

    def __sub__(self, other):
        if isinstance(other, Number):
            other = Sets(other)

        sn = self.numbers.copy()
        on = other.numbers.copy()
        new_set = list()

        for i in range(len(sn)):
            for j in range(len(on)):
                if sn[i] == on[j]:
                    new_set.append(sn[i])

        self.sort(new_set)
        return new_set

    def __truediv__(self, other):
        if isinstance(other, Number):
            other = Sets(other)

        sn = self.numbers.copy()
        on = other.numbers.copy()
        new_set = list()
        counter = 0
        for i in range(len(sn)):
            for j in range(len(on)):
                if sn[i] == on[j] and i != j:
                    counter += 1
            if counter == 0:
                new_set.append(sn[i])
            counter = 0

        return new_set

    def __floordiv__(self, other):
        if isinstance(other, Number):
            other = Sets(other)

        sn = self.numbers.copy()
        on = other.numbers.copy()
        counter = 0
        new_set = list()

        for i in range(len(sn)):
            for j in range(len(on)):
                if sn[i] == on[j]:
                    counter += 1
            if counter == 0:
                new_set.append(sn[i])
            counter = 0

        for i in range(len(on)):
            for j in range(len(sn)):
                if sn[j] == on[i]:
                    counter += 1
            if counter == 0:
                new_set.append(on[i])
            counter = 0

        self.cleanup(new_set)
        self.sort(new_set)
        return new_set


if __name__ == '__main__':
    '''
    + - Объединение
    - - Пересечение
    / - Разность
    // - Симметрическая разность
    '''
    s1 = Sets([1, 2, 5, 7])
    s2 = Sets([1, 2, 3, 5, 6])
    s3 = Sets([2, 3, 4, 6])
    print(s2)
    print(s3)
    print(s2+s3)
    print(s2-s3)
    print(s2/s3)
    print(s1//s3)
    print(s1 == s2)





