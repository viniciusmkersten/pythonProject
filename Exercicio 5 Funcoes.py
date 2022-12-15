def velocidade_media(dist_percorrida, tempo_gasto):
    deltav = dist_percorrida / tempo_gasto
    return deltav


def menu():
    opcao = int(input('Digite a sua opcao: '))
    if opcao == 1:
        dist = float(input('Digite a distancia percorrida: '))
        temp = float(input('Digite o tempo: '))
        print(f'A velocidade media eh: {velocidade_media(dist, temp)}')
    else:
        print('Opcao invalida. ')


while True:
    menu()
