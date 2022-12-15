import random


def aleat_int(int_inicial, int_final):
    valor_int = random.randrange(int_inicial, int_final)
    return valor_int


def aleat_float(int_inicial, int_final):
    valor_float = random.uniform(int_inicial, int_final)
    return valor_float


def menu(opcao):
    if opcao == 1:
        int_menor = int(input('Digite o numero menor: '))
        int_maior = int(input('Digite o numero maior: '))
        print(aleat_int(int_menor, int_maior))
    elif opcao == 2:
        float_menor = int(input('Digite o numero menor: '))
        float_maior = int(input('Digite o numero maior: '))
        print(aleat_float(float_menor, float_maior))
    else:
        print('comando invalido. ')


while True:
    opcao = int(input('Digite uma opcao: '))
    menu(opcao)
