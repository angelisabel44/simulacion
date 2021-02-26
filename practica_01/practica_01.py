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

desde = 3
hasta = 7
replicas = 30

import pandas as pd
df_datos = pd.DataFrame({'replica': [], 'muestra': [], 'integral': [], 'digitos': []})

muestras = [ 10 ** i for i in range(4, 7) ]
for cantidad in muestras:
    valores = [ simulacion_MC(f, desde, hasta, cantidad) for i in range(replicas) ]
    digitos = [ comparar_digitos(valor) for valor in valores ]
    df_datos = df_datos.append(pd.DataFrame({'replica': range(replicas),
                                             'muestra': [cantidad] * replicas,
                                             'integral': valores,
                                             'digitos': digitos}),
                               ignore_index = True)

df_resultados = df_datos.groupby('muestra').agg({'digitos': ['min', 'mean', 'median']})
df_resultados.columns = df_resultados.columns.droplevel()
df_resultados.reset_index(level = 0, inplace = True)

barplot = df_resultados.plot.bar(x = 'muestra', y = 'min')
boxplot = df_datos.boxplot(column = ['digitos'], by = 'muestra')

import seaborn as sns
violinplot = sns.violinplot(x = "muestra", y = 'digitos', data = df_datos)



