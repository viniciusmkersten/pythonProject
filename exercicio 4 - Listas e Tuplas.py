numeros = []

for i in range(10):
    select = int(input('Digite um número: '))
    numeros.append(select)

numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)
