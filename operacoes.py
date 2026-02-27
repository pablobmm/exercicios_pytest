import math

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não permitida")
    return a / b

def raiz_quadrada(numero):
    if numero < 0:
        raise ValueError("Não existe raiz de número negativo")
    return math.sqrt(numero)

def calcular_media(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

def e_positivo(numero):
    if numero > 0:
        return True
    else:
        return False