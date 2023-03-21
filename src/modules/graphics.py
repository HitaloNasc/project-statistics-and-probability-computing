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
