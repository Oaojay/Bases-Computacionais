# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 19:03:36 2019

@author: joao.alencar
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

i = 1000

ya=np.random.rand(i)

xa=np.random.rand(i)

r = 0.5

xc = r

yc = r

Aquadrado = 4*(r**2)

Acirculo = np.pi*(r**2)

d = np.sqrt((xc-xa)**2+(yc-ya)**2)


for i in range(1000):
    s = d[d<r]
print('há',len(s),'pontos dentro do círculo')

PI=4*(Acirculo/Aquadrado)
print('π é aproximadamente',PI)






