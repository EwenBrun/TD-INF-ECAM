#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 13:40:00 2017

@author: ewen
"""

import numpy as np

def fct(x):
    return (np.cos(x)-np.sin(x))*np.exp(-x)

def rectm(f,a,b,n):
    h, res = (b-a)/n, 0
    for i in range(n):
        res += h*f(a+i*h+h/2)
    return res

x = np.arange(0,3*np.pi/2,1e-4)

valeur = -np.exp(-3*np.pi/2)

print("\r\n       Calculs d'integrales de mes 2")
print("        Methode du point du millieu")
print("_"*48+'\r\n')
print("Valeur theorique :",-np.exp(-3*np.pi/2))
print("_"*48+'\r\n')

for n in range(1,4,1):
    n = 10**n
    nValue = rectm(fct, 0, 3*np.pi/2, n)
    print("Valeur pratique pour n=",n,":",nValue)
    print("Erreur de",abs(nValue-valeur))
    print("_"*48+'\r\n')