setLista = set()
setLista = {'laranja', 999, 'Maca', 777}

print(f'Lista Atual: {setLista} \n ',
      'Informe qual categoria voce quer encontrar na lista! \n',
      '(1) para texto \n',
      '(2) para inteiro')

opcao = int(input('Digite aqui: '))

try:
    if type(opcao) != int:
        print('Voce nao digitou nenhuma das opcoes acima :( ')
except:
        if opcao == 1:
            nome = input('Informe o nome: ')
            nomeSet = set(nome)
            if setLista.intersection(nome) is False:
                print(f'Lamento! Mas o nome {nome} nao esta dentro da lista')
            else:
                print('ok')
        elif opcao == 2:
            numero = int(input('Informe o numero: '))
            if numero in setLista:
                print(f'O numero ({numero}) esta dentro da lista! ')
            else:
                print('O numero nao esta na lista. ')










