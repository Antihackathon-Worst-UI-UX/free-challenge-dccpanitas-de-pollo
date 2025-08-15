import random

def sumar (numero1, numero2):
    resultado= numero1+numero2
    return resultado

def restar (numero1, numero2):
    resultado = numero1-numero2
    return resultado

def multiplicacion (numero1, numero2):
    resultado = numero1*numero2
    return resultado

def dividir (numero1, numero2):
    resultado = numero1//numero2
    return resultado

cachipun = random.randint(1,3)

def cachipun1v1 (eleccion):
    maquina = random.randint(1,3)
    #1 es tijera, 2 es roca, 3 es papel
    if maquina == 1 and eleccion == 3:
        return perder
    if maquina == 2 and eleccion == 3:
        return ganar
    if maquina == 3 and eleccion == 3:
        return empate
    if maquina == 1 and eleccion == 2:
        return perder
    if maquina == 2 and eleccion == 2:
        return ganar
    if maquina == 3 and eleccion == 2:
        return empate
    if maquina == 1 and eleccion == 2:
        return perder
    if maquina == 2 and eleccion == 2:
        return ganar
    if maquina == 3 and eleccion == 2:
        return empate