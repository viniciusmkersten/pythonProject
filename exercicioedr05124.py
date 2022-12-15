
nota = float(input('Digite sua nota: '))
while nota:
    if nota > 10.0:
        print('Nota errada! ')
        nota = float(input('Digite sua nota: '))
        continue
    else:
        print('Acertou! ')
        break
