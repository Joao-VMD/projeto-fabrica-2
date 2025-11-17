def calcular_salario(valor_hora, horas):
    if valor_hora < 0 or horas < 0:
        raise ValueError("Valores negativos não são permitidos.")
    return valor_hora * horas
