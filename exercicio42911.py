nome = str(input('Digite o seu nome: '))
idade = int(input('Digite a sua idade: '))

if(idade<18):
    print('Voce nao pode participar, eh menor de idade!')
else:
    print('Qual ingresso ira querer?  \n 1 - Padrao R$ 20,00 \n 2 - VIP R$ 50,00')
    tipoIngresso = int(input('Digite aqui: '))
    if (tipoIngresso == 1):
        print('Ingresso Padrao comprado com sucesso!')
    elif(tipoIngresso == 2):
        print('Ingresso VIP comprado com sucesso!')
    else:
        print('Tipo de ingresso errado. Fim da operacao')
