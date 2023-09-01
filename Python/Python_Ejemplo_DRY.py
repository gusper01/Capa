# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 08:18:36 2020

@author: Gusper
"""

# Ejemplo DRY 
# Dont repeat yourself 

# Ejemplo de código con estructuras demasiados IF  
def mostrar_mes(numero):
    if numero == 1:
        return "Enero"
    if numero == 2:
        return "Febrero"
    if numero == 3:
        return "Marzo"
    if numero == 4:
        return "Abril"
    if numero == 5:
        return "Mayo"
    if numero == 6:
        return "Junio"
    if numero == 7:
        return "Julio"
    if numero == 8:
        return "Agosto"
    if numero == 9:
        return "Septiembre"
    if numero == 10:
        return "Octubre"
    if numero == 11:
        return "Noviembre"
    if numero == 12:
        return "Diciembre"
    else:
        return "Número no coincide con ningún mes"
numero = 22    
print(mostrar_mes(numero))

#################################################

meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

def mostrar_mes_DRY(numero):
    if numero < 1 or numero > 12:
        return "Número no coincide con ningún mes"
    else:
       return meses[numero-1]
    
numero = 11    
print(mostrar_mes_dry(numero))
    

