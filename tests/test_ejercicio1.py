################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio1 import es_par

"""
Test que testea la funciones es_par(numero) del ejercico1.py para casos negativos y positivos, pares e impares.
"""


def test_es_par_positivo_true():
    """
    Función que prueba que el tipo de entrada y salida de la funcion es_par(numero) sea correcta y que el resultado para los casos de números pares positivos sea correcto.
    """
    numero=4
    resultado=es_par(numero)
    assert isinstance (numero, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance (resultado, bool), 'La función debe retornar un valor de tipo booleano.'
    assert resultado==True, 'La función debe retornar True.'
    
def test_es_par_negativo_true():
    """
    Función que prueba que el tipo de entrada y salida de la funcion es_par(numero) sea correcta y que el resultado para los casos de números pares negativos sea correcto.
    """
    numero=-4
    resultado=es_par(numero)
    assert isinstance (numero, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance (resultado, bool), 'La función debe retornar un valor de tipo booleano.'
    assert resultado==True, 'La función debe retornar True.'
    
def test_es_par_positivo_false():
    """
    Función que prueba que el tipo de entrada y salida de la funcion es_par(numero) sea correcta y que el resultado para los casos de números impares positivos sea correcto.
    """
    numero=3
    resultado=es_par(numero)
    assert isinstance (numero, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance (resultado, bool), 'La función debe retornar un valor de tipo booleano.'
    assert resultado==False, 'La función debe retornar False.'
    
def test_es_par_negativo_false():
    """
    Función que prueba que el tipo de entrada y salida de la funcion es_par(numero) sea correcta y que el resultado para los casos de números impares negativos sea correcto.
    """
    numero=-3
    resultado=es_par(numero)
    assert isinstance (numero, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance (resultado, bool), 'La función debe retornar un valor de tipo booleano.'
    assert resultado==False, 'La función debe retornar False.' 
    