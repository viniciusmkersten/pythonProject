setPessoas = set()

setPessoas = {'maria', 'ana', 'paulo', 'julia'}

nomePut = input('Informe o nome que deseja adicionar: ')
setPessoas.add(nomePut)

print(f'O nome adicionado foi: {nomePut}')
print(f'Lista atualizada: {setPessoas}')
print('-'*75)

nomeRem = input('Informe o nome que deseja remover: ')
setPessoas.remove(nomeRem)

print(f'O nome removido foi: {nomeRem}')
print(f'Lista atualizada: {setPessoas}')
print('-'*75)


