

nome = input('Digite seu nome: ')
senha = input('Digite sua senha: ')

while nome and senha:
    if nome == senha:
        print('O nome do usuario nao deve ser igual a senha! ')
        nome = input('Digite seu nome: ')
        senha = input('Digite sua senha: ')
    else:
        print('Usuario cadastrado! ')
        break
