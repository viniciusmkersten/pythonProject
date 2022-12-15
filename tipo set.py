"""setTeste = {4, 5, 6}
print(type(setTeste))

outroTeste = {}
print(type(outroTeste))
outroTeste = set()
print(type(outroTeste))"""


dicionario = {}

for x in range(2):
    nome = str(input('Nome: '))
    tel = int(input('telefone: '))
    dicionario[nome] = tel

print(dicionario)