# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 12:19:01 2023

@author: Gusper
"""
# Código generado por Humano no alineado a las buenas prácticas 
# del Zen de Python

def edad(edad):
    if edad >= 0:
        if edad < 18:
            categoria = 'Menor de edad'
        else:
            if edad < 65:
                categoria = 'Adulto'
            else:
                if edad < 100:
                    categoria = 'Adulto mayor'
                else:
                    categoria = 'Edad No Clasificada'
    else:
        categoria = 'Edad No Clasificada'
    return categoria

edad_persona = 25
print(f'La persona tiene {edad_persona} años y es {edad(edad_persona)}')


##########################################################################
# Código Mejorado con promt de CHATGPT (alineado al ZEN de Python)


def edad_zen(edad):
    if 0 <= edad < 18:
        return 'Menor de edad'
    elif 18 <= edad < 65:
        return 'Adulto'
    elif 65 <= edad < 100:
        return 'Adulto mayor'
    else:
        return 'Edad inválida'

# Ejemplo de uso:
edad_persona = 25
print(f'La persona tiene {edad_persona} años y es {edad_zen(edad_persona)}')

# comentarios de CHATGPT
# hemos utilizado una estructura de múltiples elif (else if) que hace que el 
# código sea más claro y conciso. Esto sigue el principio del "Zen de Python" 
# que enfatiza la legibilidad y la simplicidad del código.La segunda versión es 
# más fácil de entender y mantener, lo que la convierte en una práctica 
# recomendada en la escritura de código Python.
