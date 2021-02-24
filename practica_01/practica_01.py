# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 07:32:59 2021

@author: Angel Moreno
"""

from math import exp, trunc
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
replicas = 100

integrales = []
for i in range(replicas):
    integral = simulacion_MC(f, desde, hasta, 1000000)
    integrales.append(integral)
    #print(f'Replica {i + 1}: {integral}')


import pandas as pd
df_resultados = pd.DataFrame()

df_resultados['replica'] = range(1, 101)
df_resultados['wolfram'] = 0.048834
df_resultados['100k'] = integrales


def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return trunc(stepper * number) / stepper

def comparar_digitos(valor):
    cantidad = 0
    for i in range(1, 7):
        montecarlo = truncate(valor, i)
        wolfram = truncate(0.048834, i)
        if montecarlo != wolfram:
            return cantidad
        cantidad += 1
    return cantidad

df_resultados['dig_50k'] = df_resultados['100k'].apply(comparar_digitos)




