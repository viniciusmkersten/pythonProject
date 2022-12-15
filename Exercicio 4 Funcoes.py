
def voto(ano_atual, ano_nascimento):
    idade = ano_atual - ano_nascimento
    print(idade)
    return idade


def checagem_voto(idade):
    if idade <= 16 or idade <= 18:
        print('Você deve votar: ')
    elif idade > 65:
        print('O seu voto é opcional: ')
    else:
        print('Você não vota: ')


ano_nascimento = int(input('Digite o seu ano de nascimento: '))
idade = voto(2022, ano_nascimento)
checagem_voto(idade)
