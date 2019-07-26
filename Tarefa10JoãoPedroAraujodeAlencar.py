# -*- coding: utf-8 -*-
"""

@author: João Pedro Araujo de Alencar
"""
#Atividade 10

#Exercíicio 1
import numpy as np #Importa a biblioteca numpy
import matplotlib.pyplot as plt #Importa a biblioteca matplotlib
import pandas as pd #Importa a biblioteca pandas

tabela = pd.read_csv('tabelabr.csv') #lê a tabela dos jogos do Brasileirao 2018


x = tabela['Placar do Mandante'].values > tabela['Placar do Visitante'].values #Variavel das vitórias 
w = tabela['Placar do Mandante'].values == tabela['Placar do Visitante'].values #Variavel dos empates
y=(np.sum(x)) #Soma das Vitorias do mandante
t=(np.sum(w)) #Soma dos Empates
z = (202*100)/379 #Porcentagem das vitórias
  

print('o Percentual de vitórias do Mandante é de aproximadamente',np.floor(z),'%') #Imprime as vitórias
print('O Percentual de vezes que o Mandante Não perdeu é de aproximadamente' #Porcentagme das vitórias somadas aos empates
      ,np.floor(((y+t)*100)/379),'%')   
#Exercício 2


inflacao = pd.read_csv('inflacao.csv') #Lê o a tabela da inflação

a = inflacao['Ano'] #Variavel do ano
b = inflacao['Inflação'] #Variavel da Inflação
c = inflacao['Mês'] #Variavel do Mês


plt.figure() #Imprime uma figura
plt.plot(x,y, marker = "", color = "Blue", linestyle = '--') #Plota as variaveis no gráfico
plt.xlabel ('x')
plt.ylabel ('y')
plt.title ('Gráfico da Inflação ao longo dos meeses dos anos') #Título do Gráfico
plt.show #Mostra o gráfico




