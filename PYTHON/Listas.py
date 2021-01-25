# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:23:54 2021

@author: Fausto López
"""
listasw=[]
listaR=[]
listaDF=[]
lista=['R1','R2','R3','S1','S2','S3','R4','R5','PC','Ps5']
for i in lista:
    if 'S' in i:
        listasw.append(i)
    elif 'R' in i:
        listaR.append(i)
    else:
        listaDF.append(i)
print('Switches: ',listasw,'\nRouters:',listaR,'\nDispositivos Finales:',listaDF)
