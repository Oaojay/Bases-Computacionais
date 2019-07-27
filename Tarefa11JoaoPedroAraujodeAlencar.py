# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 20:28:34 2019

@author: joao.alencar
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

v = np.zeros((250)) #Variavel da Velocidade
y = np.zeros((250)) #Variavel do Deslocamento
t = np.zeros((250)) #Variavel do tempo

v[0] = 10 #Valor da velocidade inicial
y[0] = 0  #Valor do Deslocamento inicial
t[0] = 0  #Valor do tempo  

for i in np.arange(1,250,1): #Condição para a variavel i
     
    v[i]=v[i-1]+0.01*(-9.81) #Série V
    y[i]=y[i-1]+0.01*v[i-1]  #Série y
    t[i]=t[i-1]+0.01         #Série t
   


plt.figure() #mostra a figura
plt.plot(y,t, marker = "d", color = "aqua", linestyle = ':') #ploca as vaviaveis no gráfico
plt.xlabel ('y') 
plt.ylabel ('t')
plt.title ('y em função de t')
plt.show

plt.figure()
plt.plot(v,t, marker = "d", color = "aqua", linestyle = ':')
plt.xlabel ('v')
plt.ylabel ('t')
plt.title ('v em função de t')
plt.show




       
          