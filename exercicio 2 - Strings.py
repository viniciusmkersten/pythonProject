texto = [input() for _ in range(3)]

texto1 = texto[0]
texto2 = texto[1]
texto3 = texto[2]


print(texto1.format(texto))
print(texto2.format(texto))
print(texto3.format(texto))
print(texto.__len__())