lista = []
lista_imp = []

qtde_elementos = int(input('Digite a quantidade de elementos: '))

for i in range(qtde_elementos):
    nov_elem = int(input('Entre com o elemento: '))
    lista.append(nov_elem)

for i in range(len(lista)):
    if lista[i] % 2 == 1:
        lista_imp.append(lista[i])

print(lista_imp)
