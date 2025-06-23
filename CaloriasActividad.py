import CaloriasReposo

def calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad):
    tmb = CaloriasReposo.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    return tmb * valor_actividad