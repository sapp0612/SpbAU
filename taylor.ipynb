#!/usr/bin/env python
# coding: utf-8
import math

ITERATIONS = 20

def my_sinh(x):
    """
    Вычисление гиперболического синуса при помощи частичного суммирования
    ряда Тейлора для окрестности 0
    """
    x_pow = x
    multiplier = 1
    partial_sum = x
    for n in range(1, ITERATIONS):
        x_pow *= x**2  # В цикле постепенно считаем степень
        multiplier *= 1 / (2*n) / (2*n + 1) # 1^n и факториал
        partial_sum += x_pow * multiplier
    
    return partial_sum

print(help(math.sinh), math.sinh(0.4))
print(help(my_sinh), my_sinh(0.4))
Help on built-in function sinh in module math:

sinh(x, /)
    Return the hyperbolic sine of x.

None 0.4107523258028155
Help on function my_sinh in module __main__:

my_sinh(x)
    Вычисление гиперболического синуса при помощи частичного суммирования
    ряда Тейлора для окрестности 0

None 0.4107523258028155
import math
import cmath

complex_angle = cmath.asinh(5)
print('"Угол", на котором гиперболический синус достигает пяти:', complex_angle)

print("Достигает ли пяти наш гиперболический синус?", my_sinh(complex_angle))
print("А библиотечный?", cmath.sinh(complex_angle))
"Угол", на котором гиперболический синус достигает пяти: (2.3124383412727525+0j)
Достигает ли пяти наш гиперболический синус? (5+0j)
А библиотечный? (4.999999999999999+0j)
get_ipython().run_line_magic('matplotlib', 'inline')
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('pdf', 'svg')


import matplotlib.pyplot as plt
import numpy as np

vs = np.vectorize(my_sinh)
print(my_sinh, vs)

angles = np.r_[-16.25:16.25:0.01]
plt.plot(angles, np.sinh(angles))
plt.plot(angles, vs(angles))
plt.show()

