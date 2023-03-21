import matplotlib.pyplot as plt 

def get_histograma(data):
    """
    Cria o gráfico histograma
    Arg: 
        data: Dados formatados
    Return:
        Criação gráfica em histograma a partir dos dados inseridos
    """
    return plt.hist(data)