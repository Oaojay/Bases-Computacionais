# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 13:53:42 2019

@author: João Pedo Araújo de Alencar
"""
# Tarefa 16

#A

import numpy as np #importando a biblioteca numpy
import matplotlib.pyplot as plt # importando a biblioteca matplotlib.pyplot

def xemfunçaodeta(): #definindo a função do exercício a
    t = np.arange(0,10,0.1)
    a = 2
    b = 0.5
    c = 0
    x = a*np.sqrt(1+(b*t)**2+c)
    
    plt.figure()
    plt.plot(x,t, marker = "o", color = "purple", linestyle = '-')
    plt.xlabel ('tempo')
    plt.ylabel ('x')
    plt.title ('x em função de t A')
    plt.show
    return(x)
    
def xemfunçaodetb(): #definindo a função do exercício b
    t = np.arange(0,15,0.2)
    a = 10
    b = 0.2
    c = 1
    x = a*np.sqrt(1+(b*t)**2+c)
    plt.figure()
    plt.plot(x,t, marker = "o", color = "purple", linestyle = '-')
    plt.xlabel ('tempo')
    plt.ylabel ('x')
    plt.title ('x em função de t B')
    plt.show
    return(x)
    
    
def xemfunçaodetc(): #definindo a função do exercício c
    t = np.arange(-0.5,0.5,0.002) #variavel do tempo
    a = -3 
    b = -1.5
    c = -10
    x = a*(np.sqrt(1+(b*t))**2+c) #variavel com a fórmula
    plt.figure()
    plt.plot(x,t, marker = "o", color = "purple", linestyle = '-')
    plt.xlabel ('tempo')
    plt.ylabel ('x')
    plt.title ('x em função de t')
    plt.show
    return(x)

xemfunçaodeta() #chamando a função a
xemfunçaodetb() #chamando a função b
xemfunçaodetc() #chamando a função c

#B

def caraoucoroa(): #Define a função da cara ou coroa
    m = np.random.rand(1) #Variável com um numero aleatório entre 0 e 1
    if m < 0.5: # condição para o numero gerado na variavle m
        print("Cara")
    else:
        print("Coroa")
    return(m)
    
caraoucoroa() #chamando a função
caraoucoroa()
caraoucoroa()
caraoucoroa()
caraoucoroa()
caraoucoroa()
caraoucoroa()
caraoucoroa()
caraoucoroa()
caraoucoroa()
    

#C

def modadosestadios(): #função da moda dos estádios
    bras = pd.read_csv("bras.csv") #Leitura do arquivo da tabela do brasileirao
    l = bras['Estádio'].value_counts().index[0] #variável com a moda 
    print(l)
    return(l)
    
modadosestadios() #Chama a função





