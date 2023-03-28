"""
Esse módulo contém as medidas de centralidade e de dispersão
"""

import statistics
import numpy as np
from scipy.stats import kurtosis


def get_mean(data):
    """
    Calcula a média dos dados
    Arg:
        data: dados formatados.
    Return:
        Um número real representando o valor da média.
    """
    return statistics.mean(data)


def get_median(data):
    """
    Calcula a mediana dos dados
    Arg:
        data: dados formatados.
    Return:
        Um número real representando o valor da mediana.
    """
    return statistics.median(data)


def get_mode(data):
    """
    Calcula a moda dos dados
    Arg:
        data: dados formatados.
    Return:
        Um número real representando o valor da moda.
    """
    return statistics.mode(data)


def get_standard_deviation(data):
    """
    Calcula o desvio padrão dos dados
    Arg:
        data: dados formatados.
    Return:
        Um número real representando o valor do desvio padrão.
    """
    return statistics.stdev(data)


def get_variance(data):
    """
    Calcula a variância dos dados
    Arg:
        data: dados formatados.
    Return:
        Um número real representando o valor da variância.
    """
    return statistics.variance(data)


def get_coefficient_variation(standard_deviation, mean):
    """
    Calcula o coeficiente de variação dos dados
    Arg:
        standard_deviation: desvio padrão dos dados.
        mean: média dos dados.
    Return:
        Um número real representando o coeficiente de variação.
    """
    return standard_deviation / mean


def get_quartiles(data):
    """
    Calcula os 1º, 2º, 3º e 4º quartis
    Arg:
        data: dados formatados.
    Return:
        Um lista com os valores dos 1º, 2º, 3º e 4º quartis, respectivamente.
    """
    return np.percentile(data, [25, 50, 75, 100])


def get_kurtosis(data):
    """
    Calcula a curtose dos dados
    Arg:
        data: dados formatados.
    Return:
        Um número real representando o valor da curtose.
    """
    return kurtosis(data)
