from roleta import premiado as tentativa


def menu():
    prim_valor = int(input('Informe um valor: '))
    valor_premiado = tentativa(prim_valor)[0]
    print('-' * 10, 'Girando a roleta da sorte', '-' * 10)
    print('O valor que vc ganhou foi: ', valor_premiado)
    soma = prim_valor + valor_premiado
    print('Vc acaba de ficar com: ', soma)
    valor_azarado = tentativa(prim_valor)[1]
    print('-' * 10, 'Girando a roleta do azar', '-' * 10)
    print('O valor que vc perdeu foi: ', valor_azarado)
    print('Vc acaba de ficar com: ', (soma - valor_azarado))


while True:
    menu()
