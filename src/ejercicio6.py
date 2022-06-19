################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingeniería en Computación
################

"""
6. El Cifrado del Cesar
El cifrado César o cifrado de rotación usa una encriptación de sustitución simple. Esto significa que cada caracter se sustituye por otro caracter de acuerdo con un sistema especifico.

La codificación debe ser tal que la palabra codificada contenga unicamente caracteres del tipo AZaz y 0 a 9, de manera que al codificar las ultimas letras del abecedario se vuelva a las primeras letras.

Por ejemplo, el método conocido y muy utilizado ROT13 rota el alfabeto con 13 posiciones, resultando en A->N, B->O... Y->L y Z->M.

Implementar una funcion que codifique un texto rotandolo una cantidad de posiciones ajustable.

Implementar la funcion que decodifique el texto rotado una cantidad de posiciones ajustable.
"""

def codificar(texto, posiciones):
    '''
    Función que codifica un texto en el cifrado del Cesar de acuerdo la posicion ingresada.
    '''
    codificado=''
    mayusculas='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minusculas='abcdefghijklmnopqrstuvwxyz'
    numeros='0123456789'
    for i in texto:
        if i == ' ':
            letra= ' '
        else:
            numero_letra=ord(i)
            numero_letra+=posiciones
            if i in mayusculas and numero_letra > 90:
                numero_letra-=26
                letra=chr(numero_letra)
            elif i in minusculas and numero_letra > 122:
                numero_letra-=26
                letra=chr(numero_letra)
            elif i in numeros and numero_letra > 57:
                numero_letra-=10
                letra=chr(numero_letra)
            else:
                letra=chr(numero_letra)
        codificado+=letra
    return codificado

def descodificar(texto, posiciones):
    """
    Función que descodifica un texto en el cifrado del Cesar de acuerdo la posicion ingresada.
    """
    descodificado=''
    mayusculas='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minusculas='abcdefghijklmnopqrstuvwxyz'
    numeros='0123456789'
    for i in texto:
        if i == ' ':
            letra= ' '
        else:
            numero_letra=ord(i)
            numero_letra-=posiciones
            if i in mayusculas and numero_letra < 65:
                numero_letra+=26
                letra=chr(numero_letra)
            elif i in minusculas and numero_letra < 97:
                numero_letra+=26
                letra=chr(numero_letra)
            elif i in numeros and numero_letra < 48:
                numero_letra+=10
                letra=chr(numero_letra)
            else:
                letra=chr(numero_letra)
        descodificado+=letra
    return descodificado


def principal():
    """
    Funcion que devuelve la codificacion o descodicacion de un texto ingresado de acuerdo al numero de posiciones ingresada. 
    """
    print('~ El cifrado del Cesar ~')
    eleccion=input('Pulse 1 para codificar un texto o 2 descodificar un texto: ')
    print('Ingrese un texto: ')
    texto = [x for x in input() if x in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "]
    posiciones=int(input('¿Cuantas posiciones desea rotar el texto? '))
    if eleccion == '1':
        codificado=codificar(texto, posiciones)
        print(f'Su texto codificado {posiciones} posiciones es: {codificado}')
    elif eleccion == '2':
        descodificado=descodificar(texto, posiciones)
        print(f'Su texto descodificado {posiciones} posiciones es: {descodificado}')
    else:
        print('No ha ingresado una opción valida')

if __name__ == "__main__":
    principal()