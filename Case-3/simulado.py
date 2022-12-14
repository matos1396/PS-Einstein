'''
1 - Média de acertos geral (em % e valor absoluto).
2 - Média de acertos de cada cada aluno (em % e valor absoluto)
3 - Total de acertos de cada aluno


import pandas as pd
openpyxl
'''
import sys
import pandas as pd

def corretor(path_respostas, path_gabarito):

    # Carregando as planilhas e convertendo em DataFrames
    df_respostas = pd.read_excel(path_respostas, engine ='openpyxl')
    df_respostas = pd.DataFrame(df_respostas) 

    df_gabarito = pd.read_excel(path_gabarito, engine ='openpyxl')
    df_gabarito = pd.DataFrame(df_gabarito)

    # Realizando a união dos dois DataFrames.
    df_unico = pd.merge(df_respostas, df_gabarito, left_on = "num_exercicio", right_on = "Questão")

    # Realizando modificações para deixar as respostas dos alunos em maiúsculo e que o nome/sobrenome(s) dos alunos comecem sempre com a letra maiúscula. 
    df_unico["resp_aluno"] = df_unico["resp_aluno"].str.upper()
    df_unico["aluno_nome"] = df_unico["aluno_nome"].str.title()

    # Adicionando a coluna "Acerto" que representa se o aluno acertou ou não a questão
    df_unico["Acerto"] = df_unico.apply(lambda x: True if x["resp_aluno"] == x["Gabarito"] else False, axis = 1)

    # Adicionando a coluna "Aluno_ID" que presenta um número único para cada aluno
    lista_IDs_aluno = list(range(int(3510/90))) # Como temos 3510 entradas e 90 questões o total de alunos será 3510/90 (Assumindo que não faltam entradas)
    lista_IDs_aluno = lista_IDs_aluno*90 # Como os dados já estão ordenados sendo que a cada 90 linhas em sequência representa cada aluno, repete-se o padrão dos IDs 90 vezes
    df_unico["Aluno_ID"] = lista_IDs_aluno # Adiciona a coluna

    # Ordena as linhas com base na coluna do "Aluno_ID e define a mesma como sendo o index do DataFrame"
    df_unico.sort_values(by=["Aluno_ID"], inplace = True)
    df_unico.set_index("Aluno_ID", inplace = True)


    # Média geral de acertos dos alunos
    media_geral = df_unico['Acerto'].mean().round(3)
    media_geral_proporcao = (media_geral*100).round(3)
    total_acertos_geral = df_unico['Acerto'].sum()
    total_erros_geral = (~df_unico['Acerto']).sum()

    print(f"Média de Acertos Geral: {str(media_geral)}",
          f"Média de Acertos Geral em %: {str(media_geral_proporcao)}",
          f'Total de Acertos Geral: {total_acertos_geral}',
          f'Total de Erros Geral: {total_erros_geral}',
          sep = '\n', end = '\n ----------------------- \n')


    # Salva em uma lista cada ID único.
    ids = df_unico.index.unique()

    # Para cada ID (aluno), calcula e mostra no console as informações requesitadas.
    for id in ids:

        nome = df_unico.loc[id, 'aluno_nome'].unique()
        total_acertos = df_unico.loc[id].Acerto.sum()
        total_erros = (~df_unico.loc[id].Acerto).sum()
        total_branco = df_unico.loc[id].resp_aluno.isna().sum()
        media_abs = df_unico.loc[id, 'Acerto'].mean().round(3)
        media_proporcao = (media_abs*100).round(3)

        print(f'Nome: {nome[0]}     ID = {id}',
              f'Média de acerto (absoluto): {str(media_abs)}',
              f'Média de acertos em %:  {str(media_proporcao)}',
              f'Total de acertos: {total_acertos}',
              f'Total de erros: {total_erros}',
              f'Total de questões em branco: {total_branco}',
              sep = '\n', end = '\n ----------------------- \n')

    return



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Não foram passados os arquivos nos argumentos")
        try:
            print("Tentando baixar pelos links do drive...")
            print("\n --------------------------------- \n ")
            link_respostas = "https://docs.google.com/spreadsheets/d/1qavRtAUGqDEsAfczPqfmL5S9z8aiH6LS/export"
            link_gabarito = "https://docs.google.com/spreadsheets/d/1L5IJsyAiCr5_A6oaH6ZEArrJrDL8p5J9/export"
            corretor(link_respostas, link_gabarito)

        except Exception as e:
            print("Não foi possível baixar :( programa finalizado \n")
            print(e)
            quit()
    else:
        for i, arg in enumerate(sys.argv):
            print(f"Argumento {i:>6}: {arg}")
            print("\n --------------------------------- \n ")
        
        path_arquivo_resposta = sys.argv[1]
        path_arquivo_gabarito = sys.argv[2] 

        try:
            corretor(path_arquivo_resposta, path_arquivo_gabarito)
        except Exception as e:
            print(e)