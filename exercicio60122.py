usuario = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')




if usuario and idade:
    print(f'Seu nome eh {usuario}')
    if ' ' in usuario:
        print('Seu nome contem espacos; ')
        qtdeEspacos = usuario.count(' ')
        print(f'Seu nome tem {qtdeEspacos} espacos em branco; ')

    else:
        print('Seu nome nao contem espacos; ')

        primeiroNome = usuario.split()[0]
        ultimaLetra = primeiroNome[-1]

        n = usuario.rstrip(' ')
        m = n.__len__()


        print('A primeira letra do seu nome eh ',usuario[0])
        print('A ultima letra do seu nome eh ',ultimaLetra)

        print(f'Seu nome tem {m} letras.')

else:
    print('Por favor, preencha todos os campos!')









