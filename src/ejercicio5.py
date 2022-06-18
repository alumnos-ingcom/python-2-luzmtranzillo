################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Enunciado del ejercicio
"""

def balanceo(corchetes):
    """
    Funcion que devuelve True o False de acuerdo a si los corchetes tienen su inicio y cierre.
    """
    if len(corchetes) % 2 != 0 or len(corchetes) == 0:
        respuesta = False
    else:
        respuesta = True
        i = 0
        while i < len(corchetes) and respuesta == True:
            if corchetes[i] in "[":
                i += 1
            else:
                if corchetes[i - 1] + corchetes[i] in "[]": 
                    corchetes=corchetes[:i - 1] + corchetes[i + 1:]
                    i -= 1
                else:
                    respuesta = False
    return respuesta


def principal():
    """
    Función que pide el ingreso de corchetes y crea solo una lista con los elementos que sean corchetes y devuelve si estan balanceados o no. 
    """
    print('Ingrese corchetes: ')
    corchetes = [x for x in input() if x in "[]"]
    balanceado=balanceo(corchetes)
    print(balanceado)
    

if __name__ == "__main__":
    principal()