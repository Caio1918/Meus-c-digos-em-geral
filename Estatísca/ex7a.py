# Conjunto de dados vendas 

import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt

dados = pd.Series([2114, 2468, 7119, 1876, 4105, 3183, 1932, 1355, 4278, 1030, 2000, 1077, 5835, 1512, 1697, 2478, 3981, 1643, 1858, 1500, 4608, 1000])

v_max = dados.max()
v_min = dados.min()
total = dados.count()
qtde_classes = round(sqrt(total))
amplitude = v_max - v_min
h = amplitude/qtde_classes

