setNumeros = set()

for i in range(4):
    num = int(input('numeros: '))
    setNumeros.add(num)

print(f'Numeros adicionados pelo usuario: {setNumeros}')
numeroPego = setNumeros.pop()

print(f'Numero removido pelo comando pop: {numeroPego}')
print(f'Lista Atualizada: {setNumeros}')

print('hora de esvaziar a lista ')
setNumeros.clear()
print(f'Lista vazia: {setNumeros} ')
