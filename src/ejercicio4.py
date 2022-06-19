################
# Nombre - @usuario_github
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
4. Fibonacci
La sucesión de Fibonacci es una sucesión infinita donde cada elemento es la suma de los dos anteriores.
En la misma, los dos primeros términos son 1. (En algunos lugares se toma el primer término en 0 y el segundo en 1)
Implementar una función que permita obtener el n-esimo termino de la sucesión de Fibonacci.
Siendo este número un entero positivo mayor a 2.
"""
# Reemplazar por las funciones del ejercicio

def es_nesimo_fibonacci(numero):
    """
    Funcion que retira el n-esimo termino de la secuencia fibonacci.
    """
    primero=0
    segundo=1
    suma=0
    contador=1
    lista=[]
    while(contador<=numero):    
        lista.append(suma)
        contador+=1
        primero=segundo
        segundo=suma
        suma=primero+segundo
    posicion_numero=numero-1
    return lista[posicion_numero]

def principal():
    """
    Función que pide el ingreso del n-esimo término de la secuencia fibonacci y retorna el número de esa posicion.
    """
    numero=int(input("Ingrese un número para el n-esimo término de la secuencia fibonacci: "))
    if numero > 4:
        resultado=es_nesimo_fibonacci(numero)
    else:
        resultado='Debe ingresar un número mayor a 4.'
    print(resultado)
    

if __name__ == "__main__":
    principal()