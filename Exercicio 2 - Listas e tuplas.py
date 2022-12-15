



texto = str(input('Digite um texto: '))
lista = list(input('Digite a palavra: '))
#print(lista)
listaUnida = ''.join(lista)
print(listaUnida)
listaUnida = list(listaUnida)





stringEmLista = texto.split()
#print(stringEmLista)





for i in range(len(stringEmLista)):
    #elementoEncontrado = stringEmLista.find('laranja')
    if stringEmLista[i] in listaUnida[0]:
        print('O elemento esta na lista. ')
    else:
        print('O elemento n esta na lista. ')