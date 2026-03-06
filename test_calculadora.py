import pytest
from calculadora import calcular_valor_final

def test_calcular_desconto_comum():
    assert calcular_valor_final(100,10) == 90
    assert calcular_valor_final(30,10) == 27

def test_percentual_fora_do_limite_deve_lancar_erro():
    with pytest.raises(ValueError, match="Percentual deve estar entre 0 e 100"):
        calcular_valor_final(100, -1)
    with pytest.raises(ValueError, match="Percentual deve estar entre 0 e 100"):
        calcular_valor_final(100, 101)

def test_valor_final_nao_pode_ser_negativo():
    assert calcular_valor_final(100, 100) == 0
    assert calcular_valor_final(100, 100) == 0