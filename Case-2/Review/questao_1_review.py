# -*- coding: utf-8 -*-
def questao_1(lista_itens, lista_preco, valor):

    total = 0
    lista_final = []

    lista = list(zip(lista_itens, lista_preco)) # Lista de tuplas com Nome e Preço de cada item

    # Percorre a lista na ordem recebida e compara o preço dos produtos com o valor recebido
    # Caso seja possível comprar, adiciona o nome do produto na lista dos itens comprados e adiciona o valor do produto ao total
    # Caso contrário, retorna a lista dos produtos comprados.
    for elem in lista:
        total += elem[1]
        if total <= valor:
            lista_final.append(elem[0])
        else:
            return lista_final

    return lista_final


##### Testes #####

teste1 = questao_1(['aaa','bbb','ccc'],[3.00, 1.00, 4.00, 12.0], 9)
print(teste1)