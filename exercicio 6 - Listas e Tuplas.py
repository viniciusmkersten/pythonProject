lista = []

qtde_elem = int(input('Digite a quantidade de elementos: '))

for i in range(qtde_elem):
    nov_elem = input('Entre com o elemento: ')
    lista.append(nov_elem)


print(lista)
lista.pop()
print(lista)