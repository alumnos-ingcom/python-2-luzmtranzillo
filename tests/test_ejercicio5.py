################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest

from ejercicio5 import balanceo

"""
Test de la funcion balanceo() perteneciente al ejercicio5.py
"""


def test_balanceo_true():
    """
    Función que testea la entrada y salida sean del tipo correcto, ademas de que el balanceo devuelva el valor correcto para casos verdaderos.
    """
    corchetes='[][]'
    balancear=balanceo(corchetes)
    assert isinstance (corchetes, str), 'Corchetes debe ser del tipo string.'
    assert isinstance (balancear, bool), 'Balanceo debe guardar un valor del tipo booleano.'
    assert balancear==True, 'El balanceo arrojo un resultado erroneo.'
    
def test_balanceo_false():
    """
    Función que testea la entrada y salida sean del tipo correcto, ademas de que el balanceo devuelva el valor correcto para casos falsos. 
    """
    corchetes='[[]'
    balancear=balanceo(corchetes)
    assert isinstance (corchetes, str), 'Corchetes debe ser del tipo string.'
    assert isinstance (balancear, bool), 'Balanceo debe guardar un valor del tipo booleano.'
    assert balancear==False, 'El balanceo arrojo un resultado erroneo.'
    