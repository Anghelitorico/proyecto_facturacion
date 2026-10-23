def calcular_descuento(monto, tipo_cliente):
    if tipo_cliente == "VIP" and monto < 500:
        return monto * 0.10

    if tipo_cliente == "VIP" and monto >= 500:
        return monto * 0.15

    if tipo_cliente == "REGULAR" and monto > 500:
        return monto * 0.08

    return 0.0


def validar_numero_positivo(numero):
    try:
        return float(numero) > 0
    except (ValueError, TypeError):
        return False


def procesar_factura(monto, tipo_cliente):
    if not validar_numero_positivo(monto):
        raise ValueError("El monto debe ser un número positivo.")

    monto = float(monto)
    descuento = calcular_descuento(monto, tipo_cliente)
    total = monto - descuento

    return {
        "monto_original": monto,
        "subtotal_bruto": monto,
        "tipo_cliente": tipo_cliente,
        "descuento": descuento,
        "total": total,
        "total_pagar": total,
    }
