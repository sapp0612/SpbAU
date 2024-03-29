#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Модуль в строке ниже обеспечивает доступ к математическим функциям,определенным стандартом "С"
import math
# Модуль в строке ниже обеспечивает работу массива произвольных однородных элементов
# быстрые математические операции над массивами
# использование линейной алгебры, преобразование Фурье, случайные числа
import numpy
# Модуль в строке ниже представляет доступ к объектно-ориентированной библиотеке построения графиков
# Апроцедурный интерфейс обеспечивается сопутствующим модулем pyplot
import matplotlib.pyplot as mpp
# Эта программа рисует график функции, заданной выражением ниже
# Оператор if выполняет проверяемое условие, в строке ниже - равенство
# Затем указывает программе выполнить группу операций в случае истинности
if __name__=='__main__':
# Класс numpy.r_ объединяет срезы массивов
    arguments = numpy.r_[0:200:0.1]
# Команда plot строит график элементов однородного массива
    mpp.plot(
        arguments,
        [math.cosh(a) * math.cosh(a/20.0) for a in arguments]
   )
# Команда show отображает все открытые данные
    mpp.show()

