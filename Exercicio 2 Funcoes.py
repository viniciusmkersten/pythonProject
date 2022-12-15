def soma_tres_num(n1,n2,n3):
    soma = n1 + n2 + n3
    return soma


def media_numeros(soma):
    mediaAtualizada = soma / 3
    return mediaAtualizada

def menu_interacao():
    n1 = float(input('Digite o primeiro numero: '))
    n2 = float(input('Digite o segundo numero: '))
    n3 = float(input('Digite o terceiro numero: '))
    print('A soma é: ', soma_tres_num(n1,n2,n3))
    print('A média é: ', media_numeros(soma_tres_num(n1,n2,n3)))

while True:
    menu_interacao()
