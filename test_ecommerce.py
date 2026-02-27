import pytest
from ecommerce import calcular_preco_final

def test_preco_invalido():
    with pytest.raises(ValueError):
        calcular_preco_final(0)

def test_sem_cupom_com_frete():
    assert calcular_preco_final(100) == 120

def test_cupom_promo10():
    assert calcular_preco_final(100, cupom="PROMO10") == pytest.approx(110.0)

def test_cupom_promo20():
    assert calcular_preco_final(200, cupom="PROMO20") == pytest.approx(180.0)

def test_cupom_invalido():
    assert calcular_preco_final(100, cupom="INVALIDO") == 120

def test_frete_gratis_por_parametro():
    assert calcular_preco_final(100, frete_gratis=True) == 100

def test_frete_gratis_por_valor_alto():
    assert calcular_preco_final(600) == 600