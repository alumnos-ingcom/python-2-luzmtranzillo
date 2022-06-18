################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest

from ejercicio4 import es_nesimo_fibonacci

"""
Test de la funcion es_nesimo_fibonacci perteneciente al ejercicio.4py'
"""


def test_es_nesimo_fibonacci():
    """
    Funcion que testea que las entradas y salidas de la funcion es_nesimo_fibonacci sean correctas.
    """
    numero=10
    resultado=es_nesimo_fibonacci(numero)
    assert isinstance (numero, int), 'Debe ingresar un valor de tipo entero.'
    assert isinstance (resultado, int), 'El resultado debe ser un número de tipo entero.'
    assert resultado > 0, 'El resultado debe ser un número positivo.'
    assert resultado == 34, 'La funcion a devuelvo un valor incorrecto para el nesimo termino de la secuencia.'
    
    