def calcular_calorias_en_reposo(peso, altura, edad, valor_genero):
    altura_cm = altura * 100
    tmb = (10 * peso) + (6.25 * altura_cm) - (5 * edad) + valor_genero
    return tmb