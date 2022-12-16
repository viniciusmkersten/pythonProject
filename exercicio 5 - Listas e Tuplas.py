lista = []

for i in range(10):
    select = input('Digite um nome: ')
    lista.append(select)

print(lista)
print(list(map(lambda x: x.upper(), lista)))

