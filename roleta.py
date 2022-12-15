from random import randint as aleatorio


def premiado(valor):
    valor1 = aleatorio(0, valor)
    valor2 = aleatorio(0, valor1)
    return [valor1, valor2]



