class Funcionario:
    def __init__(self, nome_funcionario, _cpf_funcionario, __salario_funcionario):
        self.nome = nome_funcionario
        self.cpf = _cpf_funcionario
        self.salario = __salario_funcionario

    def mostrar_info(self):
        print(f'O nome do funcionário é {self.nome},\n o seu CPF é {self.cpf}, \n'
              f' e o seu salário é de R$ {self.salario}')


class Gerente(Funcionario):
    def __init__(self, nome_funcionario, _cpf_funcionario, __salario_gerente, __senha_gerente):
        super().__init__(self, nome_funcionario, _cpf_funcionario)
        self.__senha_gerente = 'admin'

    def validar_senha(self):
        validacao = input('Digite a senha: ')
        if validacao != self.__senha_gerente:
            print('Senha inválida. ')
        else:
            print('Senha válida. ')
            Gerente.mostrar_info(self)


objeto = Gerente('Vinicius', '071797', '3000', 'admin')
objeto.validar_senha()
