valor = float(input('Digite o valor desejado; '))

if valor < 0:
    print(f'O valor atualizado eh {valor*3}')
elif valor > 0:
    print(f'O valor atualizado eh {valor*2}')