################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest

from ejercicio3 import superposicion

"""
Test  de la funcion superposicion del  ejercicio3.py perteneciente al TP2 Python. 
"""


def test_superposicion():
    """
    Test que testea que las entradas y la salida de la funcion superposicion sean del tipo correcto. Además de que la salida de un resultado correcto.
    """
    lista1="Hola mundo"
    lista2="Hola"
    grado=superposicion(lista1, lista2)
    assert isinstance (lista1, str), 'La entrada debe ser de tipo string.'
    assert isinstance (lista2, str), 'La entrada debe ser de tipo string.'
    assert isinstance (grado, int), 'El grado de superposicion debe ser un valor de tipo entero'
    assert grado==4, 'El grado de superposicion no es correcto.'