# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 19:08:41 2019

@author: joao.alencar
"""
import numpy as np #importa a biblioteca numpy (np)

import matplotlib.pyplot as plt #importa a bilioteca matlplot (plt)

t= np.arange(0, 5, 0.1) #Defini a variavel do vetor tempo e seu alcance

h= -t**2+4*t #Defini a variavel do vetor da altura

Hmax = np.max(h) #Defini a variavel para a Aultura máxima e a Altura máxima da parábola

print ("Altura máxima da parábola é:",Hmax) #imprime a altura máxima

plt.figure()

plt.plot(t,h, marker = "d", color = "aqua", linestyle = '--') #Plota o gráfico com o estilo de linha e cor desejada

plt.xlabel ('t')

plt.ylabel ('h')

plt.title ('Parábola')#Entitula o gráfico

plt.ylim (0, 5) #limita o eixo 

plt.show() #Exibe o Gráfico no console
