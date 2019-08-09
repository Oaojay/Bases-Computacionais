# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 20:24:04 2019

@author: joao.alencar
"""

import numpy as np

def estaNoIntervalo(a, b, x):
    '''
    Verifica se x está entre a e b
    
    Parâmetros:
    -----------------------------
    x:
       número que será verificado
    
    Retorna
    ----------------------------
    
    '''
    if a<x<b: #condição para x
        print('x está entre a e b') #imprime caso a condição seja verdadeira
    else: print('x não está entre a e b') #imprime caso a condição seja falsa
    return x
a = estaNoIntervalo(-2.5,6.3,9.1)
b = estaNoIntervalo(-10,7,2.2)
c = estaNoIntervalo(67.2,87.2,8.1)