# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
#Tarefa 6

import numpy as np
import matplotlib.pyplot as plt

#Exercício 1

t = np.arange(0, 10.5, 0.05) #Define a variação do vetor do tempo em segundos

e = 2.71 #Define a variavel do número de Euler

v = e**(-0.5*t)*np.cos(np.pi/180*(2*np.pi*0.8*t)) #Define a variação do vetor da tensão em função do tempo

print("o valor do tempo sem segundos é", t) #Impime a variavel t do tempo em segundos

print ("o valor da tensão em volts é", v) #Imprime a variavel v da tensão em volts

plt.figure() #Abre uma figura
plt.plot(t,v, marker = "o", color = "aqua", linestyle = ':') #Plota as variaveis no gráfico
plt.xlabel ('tempo(s)')
plt.ylabel ('tensão(v)')
plt.title ('Gráfico da função')
plt.show #Mostra o gráfico no console

#Exercício 2

c = np.linspace(-20, 100, 100) #Define a variação do vetor da temperatura em graus celsius

f=9/5*c+32 #Define a variação do vetor da temperatura em fahrenheit

print ("O valor de Graus Celsius em fahrenheit é:",f)

plt.figure() #Abre uma figura
plt.plot(f,c, marker = "o", color = "aqua", linestyle = ':') #Plota as variaveis no gráfico
plt.xlabel ('Graus Fahrenheit')
plt.ylabel ('Graus Celsius')
plt.title ('Equivalência da temperatura em Fahrenheits em função da temperatura em Celsius')
plt.show #Mostra o gráfico no console


#Exercício 3 

a= np.arange (1994, 2021, 1) #Define a variação do vetor dos anos

P= 800000*e*((a-1994)/40) #Define a variação do vetor da quantidade de habitantes

z= np.max(P) #Define uma variavel para o valor máximo do vetor P

plt.figure() #Abre uma Figura
plt.plot(a,P, marker = "o", color = "aqua", linestyle = ':') #Plota as variaveis no gráfico
plt.xlabel ('anos')
plt.ylabel ('Número de habitantes')
plt.title ('Crescimento aproximado da população')
plt.show #Mostra o gráfico no console
print("a populcação em 2020 será de", z,"habitantes") #Imprime a variavel do valor máximo do vetor P 
