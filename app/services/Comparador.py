def extraer_numero(valor: str):
    """Extrae el primer número decimal de una cadena."""
    if not isinstance(valor, str):
        return None

    valor = valor.replace(",", ".")  # unificar formatos
    num = ''
    punto_encontrado = False

    for c in valor:
        if c.isdigit():
            num += c
        elif c == '.' and not punto_encontrado:
            num += c
            punto_encontrado = True
        elif num:  # si ya empezamos a formar el número y encontramos otra cosa, paramos
            break

    try:
        return float(num) if num else None
    except:
        return None

def TransBool(valor: str):
    """Convierte 'sí'/'no' (y variantes) en booleanos."""
    if not isinstance(valor, str):
        return None

    valor = valor.strip().lower()
    if valor in ["sí", "si", "true", "yes"]:
        return True
    if valor in ["no", "false"]:
        return False
    return None