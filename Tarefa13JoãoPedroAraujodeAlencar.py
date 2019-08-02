# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 20:19:03 2019

@author: joao.alencar
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

brasileirao = pd.read_csv('brasileirao.csv')


x = brasileirao[brasileirao['Mandante']=='Corinthians']['Público']

SCCPpumedia = brasileirao[brasileirao['Mandante']=='Corinthians']['Público'].mean()
print(SCCPpumedia)

plt.figure()
plt.hist(x,30)
plt.show()