nome = str(input('Digite o nome: '))
telefone = int(input('Digite o telefone: '))

telefone = str(telefone)

print('O nome eh: ',nome, 'e o telefone eh: ',telefone)

print(f'O nome eh {nome} e o telefone eh {telefone} ')

print('O nome eh ' + nome + 'e o telefone eh ' + telefone)

print('O nome eh {}'.format(nome), 'e o telefone eh {}'.format(telefone))