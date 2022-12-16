nome = []
idade = []
profissao = []

for i in range(2):
    nome.append(input('Digite o nome: '))
    idade.append(input('Digite a idade: '))
    profissao.append(input('Digite a profissao: '))



for j in range(2):
    print(f'O nome digitado foi {nome[j]}, a idade digitada foi {idade[j]}, e a profissao eh {profissao[j]}')

    for k in range(2):
        print(nome[k])