
print(' Digite a sua situacao especial. \n Sendo 1 idoso, \n 2 gestante, \n 3 cadeirante, \n ou 4 para nenhuma das anteriores. ')


situacao = int(input())


if(situacao == 1 or situacao == 2 or situacao == 3 ):
    print('Voce tem acesso a fila de prioridade;')
elif(situacao == 4):
    print('Entre em contato com o setor responsavel para avaliar a sua situacao.')
else:
    print('Comando invalido. Fim da operacao;')