# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 07:32:59 2021

@author: Angel Moreno
"""

from math import exp
def f(x):
    return 1 / (exp(x) + exp(-x))

import random
def simulacion_MC(F, a, b, cantidad):
    acumulado = 0
    for j in range(cantidad):
        x = random.random()
        acumulado += F(a + (b - a) * x)
    return ((b - a) * acumulado)/cantidad

desde = 3
hasta = 7
cantidad = 50000
replicas = 30

for i in range(replicas):
    integral = simulacion_MC(f, desde, hasta, cantidad)
    print(f'Replica {i + 1}: {integral}')