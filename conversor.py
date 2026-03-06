def celsius_para_fahrenheit(c):
    if not isinstance(c, (int, float)):
        raise TypeError("A entrada deve ser um número")
    f = c * 9/5 + 32
    return round(f, 2)

def fahrenheit_para_celsius(f):
    if not isinstance(f, (int, float)):
        raise TypeError("A entrada deve ser um número")
    c = (f - 32) * 5/9
    return round(c, 2)