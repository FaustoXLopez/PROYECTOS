# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:23:54 2021

@author: Fausto López
"""

while True:
    x=input("Ingrese un número para contar hasta: ")
    if x== 'q' or x == 'quit':
        break
    
    x= int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y > x:
            break