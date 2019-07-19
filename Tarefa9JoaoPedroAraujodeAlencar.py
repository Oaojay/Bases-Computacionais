# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 19:26:21 2019

@author: Joao Pedro Araujo de Alencar
"""

import numpy as np #Importa a biblioteca numpy
import matplotlib.pyplot as plt #Importa a biblioteca matplotlib
import pandas as pd #Importa a biblioteca pandas


analfabetismo = pd.read_csv('analfabetismo.csv')#acessa dados disponiveis em arquivos com dados


plt.figure() #Faz o gráfico
plt.plot(analfabetismo['Ano'],analfabetismo['São Paulo'], #Plota as informações no gráfico e define a cor e o estilo da linha no gráfico
         linestyle = '-', color = 'blue')
plt.title('Gráfico da quantidade de Analfabetos em Sp com o passar dos anos') #Define um título para o gráfico.
plt.ylabel('Anos') #Define a variavel Anos como eixo y
plt.xlabel('São Paulo') ##Define a variavel Anos como eixo y
plt.show #Mostra o gráfico no console
