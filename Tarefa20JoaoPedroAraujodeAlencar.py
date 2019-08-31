


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

#Autor: João Pedro Araujo de Alencar

#Tarefa 20

R = 1
C = 1000

i = np.arange(1,1000,1)                  

x=0.00011 #taxa de reprodução dos coelhos α 

y=0.00001 # β : taxa de morte de coelhos devido às raposas. Se não exixtirem raposas não há mortes de coelhos.

z=0.00007 # δ : taxa de morte das raposas.

w=0.00000009 # γ : taxa de reprodução das raposas. Como a alimentação de raposas são os coelhos, este termo depende da existência de coelhos.

deltat = 0.01 # Δt

deltaCdeltaT = x*C[i-1]-y*R[i-1]*C[i-1] #ΔC/Δt

deltaRdeltaT = w*R[i-1]*C[i-1]-z*R[i-1] #ΔR/Δt


C[i] = C*[i-1]+deltat*deltaCdeltaT # Coelhos

R[i] = R*[i-1]+deltat*deltaRdeltaT # Raposas


plt.figure()
plt.plot(C,i, marker = "d", color = "Red", linestyle = ':') # Coelhos
plt.plot(R,i, marker = "d", color = "Green", linestyle = ':') # Raposas
plt.xlabel ('Tempo')
plt.ylabel ('Raposas/Coelhos')
plt.title ('Parábola')
plt.show





