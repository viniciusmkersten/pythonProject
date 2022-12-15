nome = input('Informe nome: ')
sexo = input('Informe sexo: [F] ou [M]: ')
estCivil = ' '

if sexo == 'f' or sexo == 'F' or sexo == 'm' or sexo == 'M':
    sexoUpdated = sexo.upper()
    estCivil = input('Informe estado civil [solteira][casada][viuva]: ')

    if estCivil.isprintable():
            print(f'Dados impressos! \nNome: {nome} \nSexo: {sexoUpdated} \nEstado civil: {estCivil} ')
    else:
            print('operacao errada')

else:
    print('Operador de sexo inexistente.')

