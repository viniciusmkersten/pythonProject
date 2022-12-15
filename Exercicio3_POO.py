class Pessoa:
    def __init__(self, nome_pessoa, idade_pessoa, altura_pessoa, peso_pessoa):
        self.nome = nome_pessoa
        self.idade = idade_pessoa
        self.altura = altura_pessoa
        self.peso = peso_pessoa

    def mostrar_dados(self):
        print(f'O nome do funcionário é {self.nome},\n a sua idade é {self.idade}, \n'
              f' a sua altura é {self.altura}, e o peso eh {self.peso}')

    def envelhecer(self):
        update_idade = int(input('Digite a sua idade: '))
        idade_atualizada = update_idade + self.idade
        print(idade_atualizada)

    def engordar(self):
        update_peso = float(input('Digite: '))
        peso_atualizado = update_peso + self.peso
        print(peso_atualizado)

    def emagrecer(self):
        update_peso = float(input('Digite: '))
        peso_atualizado = self.peso - update_peso
        print(peso_atualizado)


class Opcoes:
    
