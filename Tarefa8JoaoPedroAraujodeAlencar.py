#Autor: João Pedro Araujo de Alencar
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import numpy as np #Importa a biblioteca numpy
import matplotlib.pyplot as plt

#1 Classificação de IMC

#Exercício a)

h=1.52 #variavel da Altura   
m=50 #Variavel do Peso

imc=(m/(h**2)) #Variavel com a fórmula do IMC

print('Seu imc é de:',imc) #Imprime o imc

if imc<17: #Condição (se) para a variavel imc
    print('Muito abaixo do peso')
else: #Condição (então) para a variavel imc
    
    if imc>17.0 or imc<18.5:
        print('Abaixo do peso')
    else:  
        
        if imc>18.5 or imc>25:
            print('Peso normal')
        else:    
            
            if imc>25 or imc<35:
                print('Obesidade grau 1')
            else:   
                
                if imc>35 or imc>40:
                    print('Obesidade grau 2')
                    
                else:
                    
                    if imc>40:
                        print('Obesidade grau 3')
#Exercício b)

h=1.75 #variavel da Altura   
m=83 #Variavel do Peso

imc=(m/(h**2)) #Variavel com a fórmula do IMC

print('Seu imc é de:',imc) #Imprime o imc

if imc<17: #Condição (se) para a variavel imc
    print('Muito abaixo do peso')
else: #Condição (então) para a variavel imc
    
    if imc>17.0 or imc<18.5:
        print('Abaixo do peso')
    else:  
        
        if imc>18.5 or imc>25:
            print('Peso normal')
        else:    
            
            if imc>25 or imc<35:
                print('Obesidade grau 1')
            else:   
                
                if imc>35 or imc>40:
                    print('Obesidade grau 2')
                    
                else:
                    
                    if imc>40:
                        print('Obesidade grau 3')
                        
                
                        
                        
                    

#2 Gráfico Acidez X concentração de íons hidrônio.


c=np.arange(1,8,1) #Variavel da concentração de íons hidrônio
A=((c**3+3*c**2)-54) #Variavel da Acidez
d=3 #concentração c do íon de hidrônio que resulta em solução saturada
C=((d**3+3*d**2)-54) #Função que resulta em uma solução saturada


plt.figure()
plt.plot(c,A, marker = "D", color = "blue", linestyle = '-')
plt.plot(d,C, marker= "D", color= "red", linestyle = '-') #Plota as variaveis e define no gráfico o marcador, a cor e o estilo da linha
plt.xlabel ('Acidez') #Mostra no gráfico o nome da variavel no eixo x
plt.ylabel ('concentração de íons hidrônio.') #Mostra no gráfico o nome da variavel no eixo y
plt.title ('Gráfico') #Define um título para o gráfico
plt.show #Mostra o gráfico no console

#3 Gráfico f(x)=|x−2|+|2x+1|−x−6


x=np.arange(-10,10,1) #Variavel X
f=(np.abs(x-2)+np.abs(2*x+1)-x-6) #Variavel com a funçao modular
B=np.logical_and(f>0, x>0) #Variavel para determinar uma condição para mostrar o menor valor de x
print(B) #Imprime a variavel B
D=x[B == True] #Define se a variavle W é verdadeira
print(np.min(D))


plt.figure()
plt.plot(x,f,marker = "D", color = "blue", linestyle = '-') #Plota as variaveis e define no gráfico o marcador, a cor e o estilo da linha
plt.xlabel ('x')#Mostra no gráfico o nome da variavel no eixo x
plt.ylabel ('y.')#Mostra no gráfico o nome da variavel no eixo y
plt.title ('Gráfico do exercício 3') #Define um título para o gráfico
plt.show #Mostra o gráfico no console

#4 Gráfico f(x)=x2–sin(0.784x2)–2

z=np.arange(-10,10, 1) #vriavel z
w=x**2 - np.sin(0.784*x**2)- 2 #variavel w

plt.figure()
plt.plot(z,w ,marker = "D", color = "blue", linestyle = '-') #Plota as variaveis e define no gráfico o marcador, a cor e o estilo da linha
plt.xlabel ('z') #Mostra no gráfico o nome da variavel no eixo x
plt.ylabel ('w.') #Mostra no gráfico o nome da variavel no eixo y
plt.title ('Gráfico do exercício 4') #Define um título para o gráfico
plt.show #Mostra o gráfico no console

W=np.logical_and(z>0, w>0) #variavel qpara determinar a condição para a função
h= z[W==True] #Define se a variavle W é verdadeira
print(np.min(h))





        
    


                    
    
                        



    
