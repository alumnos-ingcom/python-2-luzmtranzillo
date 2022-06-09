################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio1 import es_par

"""
Describir aquí que es lo que se esta probando.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""


def test_es_par_positivo_true():
    """
    Función que prueba la funcione es_par(numero) para los casos de números pares positivos.
    """
    numero=4
    resultado=es_par(numero)
    assert isinstance (numero, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance (resultado, bool), 'La función debe retornar un valor de tipo booleano.'
    assert resultado==True, 'La función debe retornar True.'
    
def test_es_par_negativo_true():
    """
    Función que prueba la funcione es_par(numero) para los casos de números pares negativos.
    """
    numero=-4
    resultado=es_par(numero)
    assert isinstance (numero, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance (resultado, bool), 'La función debe retornar un valor de tipo booleano.'
    assert resultado==True, 'La función debe retornar True.'
    
def test_es_par_positivo_false():
    """
    Función que prueba la funcione es_par(numero) para los casos de números impares positivos.
    """
    numero=3
    resultado=es_par(numero)
    assert isinstance (numero, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance (resultado, bool), 'La función debe retornar un valor de tipo booleano.'
    assert resultado==False, 'La función debe retornar False.'
    
def test_es_par_negativo_false():
    """
    Función que prueba la funcione es_par(numero) para los casos de números impares negativos.
    """
    numero=-3
    resultado=es_par(numero)
    assert isinstance (numero, int), 'Debe ingresar un número de tipo entero.'
    assert isinstance (resultado, bool), 'La función debe retornar un valor de tipo booleano.'
    assert resultado==False, 'La función debe retornar False.' 
    