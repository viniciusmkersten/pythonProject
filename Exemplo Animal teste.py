class Animal:
    def __init__(self, nome_animal, idade_animal):
        self.nome = nome_animal
        self.idade = idade_animal

    def info(self):
        print("sei la:")

    def dormir(self):
        print('ablblbalbalbalal')

    def passear(self):
        print('o que eh a vida?')


class teste(Animal):
    def print_teste(self):
        print('Apenas mostrando; ')


objeto = teste()
objeto.info()
objeto.print_teste()
