# Conjunto de dados vendas 

import pandas as pd
import numpy as np
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

# Coluna de frequência absoluta -------------
df["Frequência Absoluta"] = df["Frequência"].cumsum()
# print(df)
# -----------------------


# -------------------- Gráficos histograma --------------------
# Histograma de frequência ------------

classes = []
for intervalo in intervalos:
    classes.append(intervalo.left)
classes.append(v_max)

plt.figure(figsize=(6,5))
plt.hist(x=df["Pontos Médios"], bins=classes, weights=df["Frequência"], edgecolor="black")
plt.title("Histograma - Distribuição de frequências das vendas")
plt.xlabel("Valor Vendido")
plt.ylabel("Frequência")

# Colocando os ticks e os limites das classes
plt.xticks(np.concatenate([classes, df["Pontos Médios"]]), rotation=45)

plt.show()
# --------------------------

# Histograma de frequência relativa ------------------
plt.figure(figsize=(6,5))
plt.hist(x=df["Pontos Médios"], bins=classes, weights=df["Frequência Relativa"], edgecolor="Black")
plt.title("Frequência Relativa")
plt.xlabel("Valor Vendido")
plt.ylabel("Frequência")

# Colocando os os limites das classes e os pontos médios
plt.xticks(np.concatenate([classes, df["Pontos Médios"]]), rotation=45)

plt.show()