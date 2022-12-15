peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))


imc = peso/(altura*altura)

if imc < 20:
    print('Vc esta abaixo do peso.')
if imc >= 20 and imc < 25:
    print('Seu peso esta normal.')
if imc >= 25 and imc < 30:
    print('Vc esta de sobre peso.')
if imc >= 30 and imc < 40:
    print('Vc esta com obesidade.')
if imc > 40:
    print('Vc esta com Obesidade morbida.')

