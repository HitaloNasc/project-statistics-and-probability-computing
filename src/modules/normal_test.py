"""
Esse módulo contém as funções para fazer o teste de hipótese para definir se é uma distribuição normal
"""


import matplotlib.pyplot as plt
from scipy.stats import normaltest, probplot

def normal_hypothesis_test(data):
    """
    Calcula o p-value dos dados
    Arg:
        data: dados formatados.
    Return:
        Um número real representando o valor do p-value.
    """
    stat, p = normaltest(data)
    return stat, p


def qq_plot(data):
    """
    Cria um Q-Q plot para um conjunto de dados.
    
    Args:
        data: conjunto de dados a ser plotado.
    Return:
        Plotagem de quantis teóricos contra os quantis reais dos dados.
    """
    fig, ax = plt.subplots(figsize=(8, 4))
    probplot(data, plot=ax)

    # Definir título e rótulos dos eixos
    ax.set_title("Q-Q plot dos dados")
    ax.set_xlabel("Quantis teóricos")
    ax.set_ylabel("Uso de CPU (%)")

    return plt.show()