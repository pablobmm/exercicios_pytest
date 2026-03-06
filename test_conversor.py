import pytest
from conversor import celsius_para_fahrenheit, fahrenheit_para_celsius

def test_celsius_para_fahrenheit_basico():
    assert celsius_para_fahrenheit(0) == 32.0
    assert celsius_para_fahrenheit(100) == 212.0
    assert celsius_para_fahrenheit(25.5) == 77.9

def test_fahrenheit_para_celsius_basico():
    assert fahrenheit_para_celsius(32) == 0.0
    assert fahrenheit_para_celsius(212) == 100.0
    assert fahrenheit_para_celsius(70) == 21.11

def test_entrada_nao_numerica_levanta_erro():
    with pytest.raises(TypeError):
        celsius_para_fahrenheit("25")
    with pytest.raises(TypeError):
        fahrenheit_para_celsius(None)