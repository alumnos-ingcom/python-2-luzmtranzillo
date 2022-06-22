################
# Nombre - luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
3. Súper-puestos
Desarrollar una función que indique el grado de superposición entre dos listas.
Siendo 0 sin superposición y uno para cada elemento superpuesto.
"""
def superposicion(lista1, lista2):
    """
    Funcion que recibe dos listas de caracteres y retorna la cantidad de valores repetidos.
    """
    grado=0
    for i in lista1:
        if i in lista2:
            grado+=1
            lista2.remove(i)
        else:
            continue
    return grado
                
    
def principal():
    """
    Funcion que pide el ingreso de dos cadenas de caracteres en forma de lista e imprime la cantidad de elementos superpuestos en la comparacion de ambas listas.
    """
    lista1=list(input('Ingrese una cadena de caracteres: '))
    lista2=list(input('Ingrese otra cadena de caracteres: '))
    grado_superpuestos=superposicion(lista1, lista2)
    print (f'El grado de superposición de caracteres es de: {grado_superpuestos} elementos.')
    
    

if __name__ == "__main__":
    principal()