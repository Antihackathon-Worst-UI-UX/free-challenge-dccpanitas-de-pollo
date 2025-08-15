from binarizador import *
from calculator import *

numero_1 = int(input("Selecciona un primer numero "))
operacion = (str(input("Selecciona tu operacion ")))
numero_2 = int(input("Selecciona un segundo numero "))

if operacion == "+":
    resultado = sumar(numero_1, numero_2)
elif operacion == "-":
    resultado = restar(numero_1, numero_2)
elif operacion == "*":
    resultado = multiplicacion(numero_1, numero_2)
elif operacion == "/":
    resultado = dividir(numero_1, numero_2)

xd = binarizador(int(resultado))
print(xd)