
def questao_3(lista):

    soma = 0
    for i in lista:
        if i != 2*lista.index(i):
            soma += i
        else:
            return soma

    return soma


##### Testes #####
lista1 = [0,5,6,7]
lista2 = []
lista3 = [1,2,3,4,5]
lista4 = [9,0,1,3,7,10,9,8]

print(questao_3(lista4))