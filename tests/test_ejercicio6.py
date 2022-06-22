################
# Nombre - @luzmtranzillo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest

from ejercicio6 import codificar, descodificar, principal

"""
Tests de la funcion codificar y descodificar del ejercicio6.py
"""


def test_codificar():
    """
    Test que verifica que la entrada, salida sean del tipo correcto y el codificado se haya realizado de manera correcta.
    """
    texto=['h','o','l','a',' ','m','u','n','d','o',' ','9','8']
    posiciones=2
    codificado=codificar(texto, posiciones)
    assert isinstance (texto, list), 'El texto ingresado debe procesarse como una lista de elementos.'
    assert isinstance (codificado, str), 'El texto codificado debe ser del tipo string.'
    assert codificado=='jqnc owpfq 10', 'El texto esta mal codificado.'
    
def test_descodificar():
    """
    Test que verifica que la entrada, salida sean del tipo correcto y el descodificado se haya realizado de manera correcta.
    """
    texto=['j','q','n','c',' ','o','w','p','f','q',' ','1','0']
    posiciones=2
    descodificado=descodificar(texto, posiciones)
    assert isinstance (texto, list), 'El texto ingresado debe procesarse como una lista de elementos.'
    assert isinstance (descodificado, str), 'El texto codificado debe ser del tipo string.'
    assert descodificado=='hola mundo 98', 'El texto esta mal codificado.'
    
    
