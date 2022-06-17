################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Estadísticas
Implementar una función que obtenga los máximos, mínimos y promedio de una secuencia con números, retornando los valores como una tuple.

Sin utilizar lazos for o las funciones integradas del lenguaje que procesan secuencias.
"""
# Reemplazar por las funciones del ejercicio

def es_maximo_minimo(lista):
    lista_int=list(map(int, lista))
    i=0
    x=1
    minimo=[0]
    while i < len(lista_int) and x <= len(lista_int):
        if lista_int[i] < lista_int[x]:
            menor=lista_int[i]
            minimo.append(menor)
            minimo.remove(0)
        else:
            print('uwu')
        i+=1
        x+=1
    return minimo
        
        
    #return (menor, mayor)
        
def promediar(lista):
    lista_int=list(map(int, lista))
    suma=0
    i=0
    while i < len(lista_int):
        suma+=lista_int[i]
        i+=1
    promedio=suma%len(lista_int)
    return promedio



def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    num=input('Ingrese un número. Cuando haya finalizado coloque un punto ')
    lista=[]
    while num!='.':
        num=input('Ingrese un número ')
        lista.append (num)
    lista.remove('.')
    #numeritos=max_min_promedio(lista)
    promedio=promediar(lista)
    minimo=es_maximo_minimo(lista)
    print(f'{promedio}')
    print(minimo)


if __name__ == "__main__":
    principal()