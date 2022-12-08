# -*- coding: utf-8 -*-
from collections import Counter # Para a solução alternativa "questao_2_B()"


## Solução sem pacotes
def questao_2_A(lista):

    dicionario = dict.fromkeys(lista, 0) # Cria um dicionário com Key = elemento da lista e Valor = 0

    # Atribui a frequência de cada elemento da lista no Valor correspondente de cada Key do dicionário.
    for nota in lista:
        dicionario[nota] += 1

    max_freq = max(dicionario.values()) # Retorna a frequência do elemento(s) mais comum

    # Percorre os items do dicionario e salva na lista_temp o valor dos maiores elemento mais frequentes
    lista_temp = []
    for nota, freq in dicionario.items():
        if freq == max_freq:
            lista_temp.append(nota)

    # Seleciona o maior valor que corresponde a resposta esperada
    resposta = max(lista_temp)
    return resposta



## Usando Counter
def questao_2_B(lista):

    dicionario = Counter(lista) # Counter() retorna um dicionario onde: Key = valor do elemento da lista e Valor = frequência do elemento na lista
    max_freq = dicionario.most_common(1)[0][1] # Retorna a frequência do elemento(s) mais comum

    # Retorna o valor do maior elemento mais frequente considerando os casos em que podem existir dois elementos com a mesma frequência
    # Análogo ao código com a mesma função da solução A, apenas reescrita de forma mais enxuta. 
    resposta = max(nota for nota, freq in dicionario.most_common() if freq == max_freq)
    return resposta





##### Testes #####

lista1 = [1,2,3,3,4,5]                      # Resposta esperada = 3

lista2 =  [1,2,2,3,3,4,5]                    # Resposta esperada = 3
lista21 = [1,3,3,2,2,4,5]                   # Resposta esperada = 3

lista3 = [1,2,3,3,4,10,10,10,10,10,5]       # Resposta esperada = 10
lista4 = [0,0,0,0,1]                        # Resposta esperada = 0
lista5 = [3,3,3,2,2,2,10,10,20,20,20]       # Resposta esperada = 20
lista6 = [3,3,3,3,3,2,2,2,10,10,20,20,20]   # Resposta esperada = 3

testeA = questao_2_A(lista1)
testeB = questao_2_B(lista1)
print(testeA, testeB)