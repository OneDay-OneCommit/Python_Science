# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 21:31:13 2023

@author: 220318
"""


from sympy import symbols, sin
import numpy as np
import matplotlib.pyplot as plt

A = symbols('A')
k = symbols('k')
x = symbols('x')
omega = symbols('omega')
t = symbols('t')
phi = symbols('phi')

waveFunction_1 = A * sin(k*x - omega*t)
waveFunction_2 = A * sin(k*x + omega*t)

waveFunction_superpositioned = waveFunction_1 + waveFunction_2

print(waveFunction_superpositioned.simplify())


A = 10
k = 1
omega = 0.25

x = np.linspace(-np.pi,np.pi,101)
y = np.sin(x)
plt.plot(x, y)
plt.xlabel("radius",fontsize = 20)
plt.ylabel("sin(x)",fontsize = 20)
plt.show()


