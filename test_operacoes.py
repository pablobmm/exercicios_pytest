import pytest
from operacoes import somar, subtrair, multiplicar, dividir, raiz_quadrada, calcular_media, e_positivo

def test_somar():
    assert somar(2, 3) == 5

def test_subtrair():
    assert subtrair(10, 5) == 5

def test_multiplicar():
    assert multiplicar(3, 4) == 12

def test_dividir_sucesso():
    assert dividir(10, 2) == 5

def test_dividir_por_zero():
    with pytest.raises(ValueError, match="Divisão por zero"):
        dividir(10, 0)

def test_raiz_quadrada_sucesso():
    assert raiz_quadrada(9) == 3

def test_raiz_quadrada_negativa():
    with pytest.raises(ValueError):
        raiz_quadrada(-1)

def test_calcular_media_float():
    resultado = calcular_media([10.5, 8.2, 9.1])
    assert resultado == pytest.approx(9.26666666)

def test_e_positivo_caminhos():
    assert e_positivo(5) is True
    assert e_positivo(-2) is False

def test_calcular_media_lista_vazia():
    assert calcular_media([]) == 0