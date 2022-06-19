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
    lista1=['H','o','l','a',' ','m','u','n','d','o']
    lista2=['H','o','l','a']
    grado_superpuestos=superposicion(lista1, lista2)
    assert isinstance (lista1, list), 'La entrada debe ser de tipo lista.'
    assert isinstance (lista2, list), 'La entrada debe ser de tipo lista.'
    assert isinstance (grado_superpuestos, int), 'El grado de superposicion debe ser un valor de tipo entero'
    assert grado_superpuestos==4, 'El grado de superposicion no es correcto.'