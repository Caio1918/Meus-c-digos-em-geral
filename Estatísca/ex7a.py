# Conjunto de dados vendas 

import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt
from math import ceil

dados = pd.Series([2114, 2468, 7119, 1876, 4105, 3183, 1932, 1355, 4278, 1030, 2000, 1077, 5835, 1512, 1697, 2478, 3981, 1643, 1858, 1500, 4608, 1000])

# Valores ------------
v_max = dados.max()
v_min = dados.min()
total = dados.count()
qtde_classes = 8
amplitude = v_max - v_min
h = amplitude/qtde_classes
# ----------------------

# Construção da tabela -----------
freq = dados.value_counts(bins= qtde_classes).sort_index()

# DataFrame distribuição de frequência
df = pd.DataFrame(freq)
df = df.reset_index()
df.columns = ["Classe", "Frequência"]

# Ajustando o intervalo
amp_classe = ceil(h)
final_corrigido = v_min + h * qtde_classes

# Criando o novo intervalo
intervalos = pd.interval_range(start= v_min, end= final_corrigido, freq= h)

# Atribuindo o novo intervalo
df["Classe"] = intervalos
# ----------------------------

# Coluna pontos médios --------------
pts_médios = []
for intervalo in intervalos:
    pts_médios.append(intervalo.mid)

df["Pontos Médios"] = pts_médios
# -------------------

# Coluna de frequência relativa -------------
df["Frequência Relativa"] = df["Frequência"] / total
# ----------------------