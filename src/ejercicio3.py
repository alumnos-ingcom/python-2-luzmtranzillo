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
    lista1_set=set(lista1)
    lista2_set=set(lista2)
    listas=lista1_set and lista2_set
    if len(listas) > 0:
        resultado=len(listas)
    else:
        resultado=0
    #return resultado
    #for x in lista1:
    #    if x in lista2:
     #       posicion=lista1.index(x)
    return resultado #c posicion
                
    
def principal():
    """
    
    """
    cadena1=input('Ingrese una cadena de caracteres: ')
    cadena2=input('Ingrese otra cadena de caracteres: ')
    lista1=list(cadena1)
    lista2=list(cadena2)
    superpuestos=superposicion(lista1, lista2)
    print (f'El grado de superposición de caracteres es de: {superpuestos} elementos.')
    
    

if __name__ == "__main__":
    principal()