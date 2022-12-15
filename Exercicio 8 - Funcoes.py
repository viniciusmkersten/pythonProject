

def dobro(mult):
        mult = mult * 2
        print(mult)


def divisao(div):
        div = div/2
        print(div)


def menu():
    valor = float(input('Digite o valor: '))
    if valor < 50.0:
        dobro(valor)
    else:
        divisao(valor)

while True:
    menu()