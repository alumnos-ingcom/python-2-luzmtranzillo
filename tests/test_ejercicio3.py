################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest

from ejercicio3 import superposicion

"""

"""


def test_superposicion():
    """
    Una breve descripción del caso de prueba aplicado a la función
    """
    lista1="Hola mundo"
    lista2="Hola"
    grado=superposicion(lista1, lista2)
    assert isinstance (lista1, str), 'La entrada debe ser de tipo string.'
    assert isinstance (lista2, str), 'La entrada debe ser de tipo string.'
    assert isinstance (grado, int), 'El grado de superposicion debe ser un valor de tipo entero'
    assert grado==4, 'El grado de superposicion no es correcto.'