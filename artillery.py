#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import numpy as np

MODEL_G = 9.81
MODEL_DT = 0.001
MODEL_DM = 0.2
MODEL_U = 28

class Body:
    def __init__(self, x, y, vx, vy):
        
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        
        self.trajectory_x = []
        self.trajectory_y = []
        

    def advance(self):

        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)
        
        self.x += self.vx * MODEL_DT
        self.y += self.vy * MODEL_DT
        self.vy -= MODEL_G * MODEL_DT
        
class Rocket(Body):
    def __init__(self, x, y):
        super().__init__(x, y, 10, 10) # Вызовем конструктор предка — тела, т.к. он для ракеты актуален
        self.m = 63

    def advance(self):
        super().advance() # вызовем метод предка — тела, т.к. и он для ракеты актуален.
        if self.m > 50:
            self.m -= MODEL_DM
            DV = MODEL_U * MODEL_DM / self.m
            V = (self.vx**2 + self.vy**2)**0.5
            self.vx += DV * self.vx / V
            self.vy += DV * self.vy / V

np.sin

b = Body(0, 0, 9, 9)
r = Rocket(0, 0)

bodies = [b, r]
# Дальше мы уже не будем думать, кто тут ёжик, кто ракета, а кто котлета —
# благодаря возможностям ООП будем просто работать со списком тел

for t in np.r_[0:2:MODEL_DT]: # для всех временных отрезков
    for b in bodies: # для всех тел
        b.advance() # выполним шаг
        
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as pp

for b in bodies: # для всех тел
    pp.plot(b.trajectory_x, b.trajectory_y) # нарисуем их траектории


# In[ ]:




