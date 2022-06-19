################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Estadísticas
Implementar una función que obtenga los máximos, mínimos y promedio de una secuencia con números, retornando los valores como una tuple.

Sin utilizar lazos for o las funciones integradas del lenguaje que procesan secuencias.
"""

def es_maximo_minimo(lista):
    """
    Funcion que retorna el mayor y el menor de una lista ingresada.
    """
    lista_int=list(map(int, lista))
    i=0
    mayor=lista_int[i] 
    menor=maximo=lista_int[i]
    while i < len(lista_int):
        if lista_int[i] < menor:
            menor=lista_int[i]
        if lista_int[i] > mayor:
            mayor=lista_int[i]
        i+=1
    return mayor, menor

        
def promediar(lista):
    """
    Función que retorna el promedio de los valores numericos de una lista ingresada.
    """
    lista_int=list(map(int, lista))
    suma=0
    i=0
    while i < len(lista_int):
        suma+=lista_int[i]
        i+=1
    promedio=suma/len(lista_int)
    return promedio,
    


def principal():
    """
    Función que pide el ingreso de numeros e imprime en forma de tupla el mayor, minimo y promedio de los mismos. 
    """
    print('Ingrese los numeros de la secuencia y cuando haya finalizado coloque un punto: ')
    numero=0
    lista=[]
    caracteres_validos=['1','2','3','4','5','6','7','8','9','0','-1','-2','-3','-4','-5','-6','-7','-8','-9','.']
    while numero != '.':
        numero=input('Ingrese un número ')
        if numero in caracteres_validos:
            lista.append(numero)
        else:
            continue
    lista.remove('.')
    #lista=[x for x in input() if x in caracteres_validos]
    maximo_minimo=es_maximo_minimo(lista)
    promedio=promediar(lista)
    tupla_resultados= maximo_minimo + promedio
    print(f'El maximo, minimo, y promedio de los numeros ingresados son {tupla_resultados}')
   


if __name__ == "__main__":
    principal()