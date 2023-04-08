"""Esse módulo contém as representações gráficas dos dados"""

import matplotlib.pyplot as plt 
import seaborn as sns
import matplotlib.pyplot as plt

def get_boxplot(data):
    """
    Cria o gráfico boxplot
    Arg: 
        data: Dados formatados
    Return:
        Criação gráfica do boxplot a partir dos dados inseridos
    """
    plt.boxplot(data)
    plt.title("Uso de CPU (%)")
    plt.ylabel("Uso de CPU (%)")
    return plt.show()


def get_histograma(data):
    """
    Cria o gráfico histograma
    Arg: 
        data: Dados formatados
    Return:
        Criação gráfica em histograma a partir dos dados inseridos
    """
    ax = sns.histplot(data, kde=True)
    
    # Definindo o título e rótulos dos eixos
    ax.set(title="Uso de CPU (%) X Frequência", xlabel="Uso de CPU (%)", ylabel="Frequência")
    return plt.show()

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
    plt.plot(x, data, linewidth=0.9)
    plt.title("Gráfico temporal do Desempenho da CPU")
    plt.xlabel('Tempo (s)')
    plt.ylabel('Uso de CPU (%)')
    return plt.show()