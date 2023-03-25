"""Esse módulo contém as representações gráficas dos dados"""

import matplotlib.pyplot as plt 

def get_boxplot(data):
    """
    Cria o gráfico boxplot
    Arg: 
        data: Dados formatados
    Return:
        Criação gráfica do boxplot a partir dos dados inseridos
    """
    return plt.boxplot(data)


def get_histograma(data):
    """
    Cria o gráfico histograma
    Arg: 
        data: Dados formatados
    Return:
        Criação gráfica em histograma a partir dos dados inseridos
    """
    return plt.hist(data)

def get_linechart(data):
    """
    Cria o gráfico de linha
    Arg:
        data: Dados formatados
    Return:
        Criação gráfica do gráfico de linha a partir dos dados inseridos
    """
    x = []
    for i in range(len(data)):
        x.append(i*5)
    return plt.plot(x, data, linewidth=0.9)