import random


def criar_num_aleatorio():
    num_aleatorio = random.randint(1, 10)
    return num_aleatorio


def func_princ():
    x = criar_num_aleatorio()
    palpite = int(input('Digite um numero: '))
    if x > palpite:
        print(x)
        print('O número é maior que o seu palpite.')
    elif x < palpite:
        print(x)
        print('O número é menor que o seu palpite.')
    else:
        print(x)
        print('Você acertou o número! ')


while True:
    func_princ()
