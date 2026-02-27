def calcular_preco_final(preco_base, cupom=None, frete_gratis=False):
    if preco_base <= 0:
        raise ValueError("Preço base deve ser maior que zero")
    
    desconto = 0
    if cupom == "PROMO10":
        desconto = 0.10
    elif cupom == "PROMO20":
        desconto = 0.20
    
    preco_com_desconto = preco_base * (1 - desconto)

    valor_frete = 20.0
    if frete_gratis or preco_com_desconto > 500.0:
        valor_frete = 0.0
    
    return preco_com_desconto + valor_frete