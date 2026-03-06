def calcular_valor_final(valor_original, percentual_desconto):

    if percentual_desconto < 0 or percentual_desconto > 100:
        raise ValueError("Percentual deve estar entre 0 e 100")
    
    valor_final = valor_original - (valor_original * percentual_desconto / 100)
    
    if valor_final < 0:
        return 0
        
    return valor_final