from math import sqrt, ceil
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dados = pd.Series([507,389,305,291,336,310,514,442,373,428,387,454,323,441,388,426,411,382,320,450,309,416,359,388,307,337,469,351,422,413])

# Valores importantes
total = dados.count()
v_max = dados.max()
v_min = dados.min()
amp = v_max - v_min
qtde_classes = 8
h = ceil(amp/qtde_classes)

freq = dados.value_counts(bins=qtde_classes).sort_index()
df = pd.DataFrame(freq)
df = df.reset_index()
df.columns = ["Classe", "Frequência"]

end_cor = v_min + h * qtde_classes
intervalos = pd.interval_range(start=v_min, end=end_cor, freq=h)
df["Classe"] = intervalos

pts_medios = [inter.mid for inter in intervalos]
df["Pontos Médios"] = pts_medios

df["Frequência Relativa"] = df["Frequência"] / total
df["Frequência Acumulada"] = df["Frequência"].cumsum()
# print(df)


# ------------- Histograma -------------
# Frequência
classes = [inter.left for inter in intervalos]

plt.figure(figsize=(6,5))
plt.hist(x=df["Pontos Médios"], bins=classes, weights=df["Frequência"], edgecolor="black")
plt.title("Histograma de Frequência")
plt.xlabel("Tempo de Reação")
plt.ylabel("Frequência")
plt.xticks(np.concatenate([classes, df["Pontos Médios"]]), rotation=45)

# Frequência Relativa
plt.figure(figsize=(6,5))
plt.hist(x=df["Pontos Médios"], bins=classes, weights=df["Frequência Relativa"], edgecolor="black")
plt.title("Histograma de Frequência Relativa")
plt.xlabel("Tempo de Reação")
plt.ylabel("Frequência")
plt.xticks(np.concatenate([classes, df["Pontos Médios"]]), rotation=45)

plt.show()