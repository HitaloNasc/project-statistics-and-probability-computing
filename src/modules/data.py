"""Esse módulo contém os dados formatados"""


def read_data(path):
    """
    Lê o arquivo .txt com os dados
    Arg:
        path: endereço do arquivo.
    Return:
        Uma variável com o arquivo aberto em modo leitura.
    """
    data_set = open(path, 'r')
    return data_set


def format(data_set):
    """
    Formatar arquivo .txt que contém os dados
    Arg:
        data_set: variável com os dados em arquivo .txt.
    Return:
        Uma lista com dados formatados e no tipo float.
    """
    data = []
    for linha in data_set:
        data.append(float(linha.replace(',', '.')))
    return data
