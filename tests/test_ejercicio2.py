################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest

from ejercicio2 import es_maximo_minimo, promediar

"""
Tests de las funciones es_maximo_minimo y promediar del ejercicio2.py
"""


def test_es_maximo_minimo():
    """
    Test de la funcion es_maximo_minimo() que verifica que el tipo de entrada y salida sean correctos. Además de que el resultado de retorno sea correcto. 
    """
    lista=['1', '-2', '3', '4', '5', '6']
    maximo_minimo=es_maximo_minimo(lista)
    assert isinstance (lista, list), 'Los elementos ingresados deben ser del tipo string.'
    assert isinstance (maximo_minimo, tuple), 'El retorno de la función es_maximo_minimo debe ser del tipo tuple.'
    assert maximo_minimo==(6, -2), 'La tupla de resultados maximo y minimo no es correcta.'
    
def test_promediar():
    """
    Test de la funcion promediar() que verifica que el tipo de entrada y salida sean correctos. Además de que el resultado de retorno sea correcto.
    """
    lista=['1', '-2', '3', '4', '5', '6']
    promedio=promediar(lista)
    assert isinstance (lista, list), 'Los elementos ingresados deben ser del tipo string.'
    assert isinstance (promedio, tuple), 'El retorno de la función promediar debe ser del tipo tuple.'
    assert promedio==(2.8333333333333335,) , 'El promedio se ha realizado de manera incorrecta.'
    
