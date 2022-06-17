################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
1. Pares e impares
Escribir una función que retorne True cuando un número entero es par y False cuando no lo sea, sin utilizar módulo. (%)
"""

def es_par(numero):
    """
    Función que mediante sumas o restas, guarda en la variable resultado un número 1 para el caso de números pares y un 0 para los impares. Y retorna un booleano True para resultado==1. 
    """
    if numero>0:
        while numero>=2:
            numero-=2
        if numero==0:
            resultado=1
        else:
            resultado=0
    else:
        while numero<2:
            numero+=2
        if numero==2:
            resultado=1
        else:
            resultado=0
    return resultado==1
    

def principal():
    """
    Funcíon que pide un número al usuario y declara mediante el retorno de la funciones es_par(numero) si es par o impar, tanto para números positivos como negativos.
    """
    numero=int(input('Ingrese un número '))
    resultado=es_par(numero)
    if resultado:
        print(f'{numero} es un número PAR.')
    else:
        print(f'{numero} es un número IMPAR.')


if __name__ == "__main__":
    principal()