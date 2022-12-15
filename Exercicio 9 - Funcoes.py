def receba_dados():
    nome = str(input('Digite seu nome: '))
    idade = str(input('Digite sua idade: '))
    est_civil = str(input('Digite seu estado civil: '))
    if nome == '' and idade == '' and est_civil == '':
        nome = 'Nao informado'
        idade = 0
        est_civil = 'Nao informado'
    return nome, idade, est_civil


def menu():
    lista = receba_dados()
    nome1 = lista[0]
    idade1 = lista[1]
    est_civil1 = lista[2]
    print(f'Seu nome eh {nome1}, sua idade eh {idade1} e seu estado civil eh {est_civil1}')


while True:
    menu()
