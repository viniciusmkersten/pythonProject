class Bola:
    def __init__(self, cor, marca):
        self.marca_bola = None
        self.cor_bola = None
        self.cor = cor
        self.marca = marca
        print('Valores iniciais: ', self.cor, self.marca)

    def mudar_cor(self):
        self.cor_bola = input('Informe uma nova cor: ')
        self.marca_bola = input('Informe a marca nova: ')
        print(f'A cor anterior eh: {self.cor}')
        print(f'A nova cor eh: {self.cor_bola}')
        print(f'A marca anterior eh: {self.marca}')
        print(f'A nova cor eh: {self.marca_bola}')


objeto = Bola('amarela', 'bic')
objeto.mudar_cor()
