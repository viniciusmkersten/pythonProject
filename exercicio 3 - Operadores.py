
produto1 = str(input('Digite o nome do primeiro produto:'))
preco1 = float(input('Digite o preco do primeiro produto'))

produto2 = str(input('Digite o nome do segundo produto:'))
preco2 = float(input('Digite o preco do segundo produto'))

produto3 = str(input('Digite o nome do terceiro produto:'))
preco3 = float(input('Digite o preco do terceiro produto'))

print('-'*10,'Produtos', '-'*20)

print(f'Produto A: {produto1}  --> Preco: R$ {preco1}')
print(f'Produto B: {produto2}  --> Preco: R$ {preco2}')
print(f'Produto C: {produto3}  --> Preco: R$ {preco3}')

print('-'*40)

maisBarato = preco1
produtoMaisBarato = produto1

if(maisBarato>preco2):
    maisBarato = preco2
    produtoMaisBarato = produto2

if(maisBarato>preco3):
    maisBarato = preco3
    produtoMaisBarato = produto3


print(f'O produto mais barato eh o {produtoMaisBarato}, custando R$ {maisBarato} ')

