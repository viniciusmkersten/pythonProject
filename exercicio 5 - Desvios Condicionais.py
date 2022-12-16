print('-'*30, 'Cardapio','-'*30, end = '\n')
print('Codigo',' Especificacao', 'Valores', sep = '\t\t\t')
print('100', 'Cachorro quente', 'R$ 5,00', sep = '\t\t|\t\t')
print('101', '    Hamburguer    ', '   R$ 10,00', sep = '\t\t|\t')
print('102', 'Coxinha      ', 'R$ 4,00', sep = '\t\t|\t\t')

codigo = int(input('Informe o codigo do pedido: '))
qtde = 0

if codigo == 100 or codigo == 101 or codigo == 102:
    qtde = int(input('Digite a quantidade desejada: '))
    if codigo == 100:
        valor = qtde * 5
        print('Pedido: Cachorro quente')
        print(f'Quantidade:{qtde}')
        print(f'Valor total: R$ {valor},00')
    if codigo == 101:
        valor = qtde * 10
        print('Pedido: Hamburguer')
        print(f'Quantidade:{qtde}')
        print(f'Valor total: R$ {valor},00')
    if codigo == 102:
        valor = qtde * 4
        print('Pedido: Coxinha')
        print(f'Quantidade:{qtde}')
        print(f'Valor total: R$ {valor},00')
