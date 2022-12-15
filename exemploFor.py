while True:
    calcular = input('1 - Para Somar ou 2 - Para Subtrair: ')
    if calcular == '1':
        print('Bem vindo a soma!')
        break
    if calcular == '2':
        print('Bem vindo a subtracao!')
        break
    else:
        print('Digitou numero invalido! Tente novamente!')

        sair = input('Sair do programa? [s]im ou [n]ao: ').lower().startswith('s')

        if sair is True or sair is False:
            break
        else:
            continue