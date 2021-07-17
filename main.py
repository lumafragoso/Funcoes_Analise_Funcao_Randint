import random
def principal():
    lista = []
    inicial = int(input('Inteiro inicial do intervalo? '))
    final = int(input('Inteiro final do intervalo? '))
    n = int(input('Quantidade de escolhas? '))
    for i in range(n):
        elemento = random.randint(inicial, final)
        lista.append(elemento)
    for j in range(inicial, final+1):
        print('{} - {}'.format(j, quantidadeNumeros(lista,j)))
def quantidadeNumeros(lista, j):
    quant = lista.count(j)
    return quant
principal()
