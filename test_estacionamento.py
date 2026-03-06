import pytest
from estacionamento import calcular_valor_estacionamento

def test_ate_uma_hora():
    assert calcular_valor_estacionamento(30) == 10.0
    assert calcular_valor_estacionamento(60) == 10.0

def test_hora_adicional_e_fracao():
    assert calcular_valor_estacionamento(61) == 15.0
    assert calcular_valor_estacionamento(120) == 15.0
    assert calcular_valor_estacionamento(121) == 20.0

def test_valor_maximo_diaria():
    assert calcular_valor_estacionamento(600) == 50.0  
    assert calcular_valor_estacionamento(1440) == 50.0 

def test_tempo_invalido():
    with pytest.raises(ValueError):
        calcular_valor_estacionamento(0)
    with pytest.raises(ValueError):
        calcular_valor_estacionamento(-10)