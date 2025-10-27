def ra(a, b):
    """
    Feature RA - Subtração
    Retorna o resultado da subtração entre dois números.
    """
    try:
        return a - b
    except TypeError:
        raise ValueError("Os parâmetros devem ser números.")