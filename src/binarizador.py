def binarizacion(numero):
    binario = []
    while numero > 0:
        resto = numero % 2
        binario.append(str(resto))
        numero //= 2
    return binario[::-1]

num = int(input("Di un número: "))
x = binarizacion(num)
print("".join(x))