import funciones1
def porcentaje_grasa(peso,altura,edad,valor_genero):
    imc = funciones1.calcular_imc(peso,altura)
    porcentaje = 1.2 * imc + 0.23 *edad - 5.4 - valor_genero
    return porcentaje
print("El porcentaje de grasa corporal es de:\n",porcentaje_grasa(100,1.70,30,0))

