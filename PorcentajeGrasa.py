import IMC
def porcentaje_grasa(peso,altura,edad,valor_genero):
    imc = IMC.calcular_imc(peso,altura)
    porcentaje = 1.2 * imc + 0.23 *edad - 5.4 - valor_genero
    return porcentaje

