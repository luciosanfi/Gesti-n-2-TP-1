import CaloriasReposo as reposo
def consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero):
    tmb = reposo.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    rango_inferior = tmb * 0.8
    rango_superior = tmb * 0.85
    return f"Para adelgazar es recomendado que consumas entre: {rango_inferior:.1f} y {rango_superior:.2f} calorías al día."
