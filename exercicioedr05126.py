
contador = 0

while contador <= 2:
    nome = input('Digite seu nome: ')
    tamanhoNome = nome.__len__()
    while tamanhoNome < 3:
        nome = input('O nome deve ter mais do que 3 caracteres. redigite; ')

    idade = int(input('Digite sua idade: '))
    while idade > 150 or idade <= 0:
        idade = int(input('Nao satisfez a condicao de idade: '))

    salario = float(input('Digite seu salario: '))
    while salario < 0:
    salario = float(input('O salario nao pode ser negativo! '))

contador += 1

