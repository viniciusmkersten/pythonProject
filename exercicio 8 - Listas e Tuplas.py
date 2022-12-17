tupla = ()

qtde_elem = int(input('Digite a quantidade de elementos: '))

lista = list(tupla)

for i in range(qtde_elem):
    elem_novo = input('Digite o elemento novo: ')
    lista.append(elem_novo)

print(lista)

tupla = tuple(lista)
print(tupla)

