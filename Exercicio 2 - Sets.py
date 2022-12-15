setUsuarios = set()

for recebe in range(5):
    nome = setUsuarios.add(input('Nome: '))
    estado = setUsuarios.add(input('Estado: '))

print(setUsuarios)

print(type(setUsuarios))