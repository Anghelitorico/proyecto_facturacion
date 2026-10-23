def calcular_descuento(monto, tipo_cliente):
    if tipo_cliente == "VIP" and monto < 500:
        return monto * 0.10

    if tipo_cliente == "REGULAR" and monto > 500:
        return monto * 0.08

    return 0.0


def validar_numero_positivo(numero):
    try:
        return float(numero) > 0
    except (ValueError, TypeError):
        return False
