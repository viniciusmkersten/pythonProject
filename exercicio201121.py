a = int(input('Digite o primeiro valor'))
b = int(input('Digite o segundo valor'))
c = int(input('Digite o terceiro valor'))

somaAmaisB = a + b

if somaAmaisB > c:
    print('a soma dos dois primeiros valores eh maior que a terceira.')
elif(c > somaAmaisB):
    print('A soma dos dois primeiros valors eh menor que a terceira.')
else:
    print('Os valores sao iguais.')