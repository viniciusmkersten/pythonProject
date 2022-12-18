class Funcionario:
    def __init__(self, nome_funcionario, salario_funcionario):
        self.nome = nome_funcionario
        self.salario = salario_funcionario

    def mostrarNome(self):
        print('O nome da pessoa eh Joao. ')

    def mostrarSalario(self):
        print('O salario de Joao eh 3000 reais. ')


class Saulo:
    def __init__(self, nome_instrumento):
        self.instrumento = nome_instrumento

    def mostrarInstrumento(self):
        print(f'O instrumento de Saulo é a {self.instrumento}')
        
print('Olha eu mexendo!')
