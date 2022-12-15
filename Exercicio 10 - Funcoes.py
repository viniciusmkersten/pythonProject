def reajuste_15(sal_atual):
    novo_sal = sal_atual * 0.15 + sal_atual
    print(f'O salario eh {novo_sal}')


def reajuste_10(sal_atual):
    novo_sal = sal_atual * 0.10 + sal_atual
    print(f'O salario eh {novo_sal}')


def reajuste_05(sal_atual):
    novo_sal = sal_atual * 0.05 + sal_atual
    print(f'O salario eh {novo_sal}')


def Principal():
    salario = float(input('Digite o seu salario: '))
    if salario < 500.0:
        reajuste_15(salario)
    elif 500.0 <= salario <= 1000.0:
        reajuste_10(salario)
    elif salario > 1000.0:
        reajuste_05(salario)


while True:
    Principal()
