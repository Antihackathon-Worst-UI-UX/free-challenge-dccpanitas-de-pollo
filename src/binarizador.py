def binarizador(number):
    def binarizacion(numero):
        binario = []
        while numero > 0:
            resto = numero % 2
            binario.append(str(resto))
            numero //= 2
        return binario[::-1]

    num = binarizacion(number)
    return "".join(num)
