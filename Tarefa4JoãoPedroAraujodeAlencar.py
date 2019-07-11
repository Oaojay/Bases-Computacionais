# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import numpy
import numpy as np

#O volume de uma esfera com raio contida em uma variável R

r=0.32 #valor do raio
v=4/3*np.pi*r**3  #Declarando o raio, o volume e inserindo a fórmula
print ("o volume da esfera de raio 0.32 é:",v,"m³")

r=1 #valor do raio
v=4/3*np.pi*r**3  #Declarando o raio, o volume e inserindo a fórmula
print ("o volume da esfera de raio 1 é:", v,"m³")

r=1.9#valor do raio
v=4/3*np.pi*r**3  #Declarando o raio, o volume e inserindo a fórmula
print ("o volume da esfera de raio 1.9 é:", v,"m³")

#Temperatura em Fahrenheit dada a temperatura em Celsius contida em uma variavel Tc.

Tc=-10 #Temperatura em Celcius
Tf=(Tc/5)*9+32 #Fórmula de Conversão
print (" A temperatura em Fahrenheit é",Tf,"°F")


Tc=30 #Temperatura em Celcius
Tf=(Tc/5)*9+32 #Fórmula de Conversão
print (" A temperatura em Fahrenheit é",Tf,"°F")


Tc=5 #Temperatura em Celcius
Tf=(Tc/5)*9+32 #Fórmula de Conversão
print (" A temperatura em Fahrenheit é",Tf,"°F")

#Lei dos Cossenos

a=1 #lado a
b=2 #lado b
θ=30 #ângulo θ
x=θ/180*np.pi #Conversão para radianos
c=np.sqrt(a**2+b**2-2*a*b*np.cos(x)) #Fórmula da lei dos cossenos
print ("o valor do lado c é",c)

a=3 #lado a
b=1 #lado b
θ=45 #ângulo θ
x=θ/180*np.pi #Conversão para radianos
c=np.sqrt(a**2+b**2-2*a*b*np.cos(x)) #Fórmula da lei dos cossenos
print ("o valor do lado c é",c)

a=10 #lado a
b=11 #lado b
θ=15 #ângulo θ
x=θ/180*np.pi #Conversão para radianos
c=np.sqrt(a**2+b**2-2*a*b*np.cos(x)) #Fórmula da lei dos cossenos
print ("o valor do lado c é",c)

#Resultados usando Fibonacci

i=30 #Valor declarado
Fi=(((((1+np.sqrt(5))/2)**i)-(((1-np.sqrt(5))/2)**i))/np.sqrt(5)) #Fórmula para o i-ésimo número
print ("O resultado da sequência é:",np.floor(Fi))

i=31 #Valor declarado
Fi=(((((1+np.sqrt(5))/2)**i)-(((1-np.sqrt(5))/2)**i))/np.sqrt(5)) #Fórmula para o i-ésimo número
print ("O resultado da sequência é:",np.floor(Fi))

i=32 #Valor declarado
Fi=(((((1+np.sqrt(5))/2)**i)-(((1-np.sqrt(5))/2)**i))/np.sqrt(5)) #Fórmula para o i-ésimo número
print ("O resultado da sequência é:",np.floor(Fi))
