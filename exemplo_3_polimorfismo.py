class Animal:
    def __init__(self, nome_animal, idade_animal):
        self.nome = nome_animal
        self.idade = idade_animal

    def __info(self):
        print(f'{self.nome}; {self.idade}')

    def dormir(self):
        print('Animal que gosta mto de dormir')


class testeSuper(Animal):
    def __init__(self, nome_animal, idade_animal, name):
        super().__init__(nome_animal, idade_animal)
        self.name = name

    def __info(self):
        print(f'Nome {self.nome}\nIdade:{self.idade} ano(s) {self.name}')

    def mostrar(self):
        self.__info()


objeto = testeSuper('animal 1', 2, 'gatinho')
objeto.mostrar()
