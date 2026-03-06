import math

def calcular_valor_estacionamento(tempo_em_minutos):
    if tempo_em_minutos <= 0:
        raise ValueError("O tempo deve ser maior que zero")
    
    if tempo_em_minutos <= 60:
        valor = 10.0
    else:
        minutos_adicionais = tempo_em_minutos - 60
        horas_adicionais = math.ceil(minutos_adicionais / 60)
        valor = 10.0 + (horas_adicionais * 5.0)
    
    return min(valor, 50.0)