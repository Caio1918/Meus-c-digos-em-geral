import pandas as pd
from math import sqrt
from math import ceil

data = pd.Series([128, 100, 180, 150, 200, 90, 340, 105, 85, 270, 200, 65, 230, 150, 150, 120, 130, 80, 230, 200,
110, 126, 170, 132, 140, 112, 90, 340, 170, 190])

# print(data.head())
# print(data.info())
# print(data.describe())

v_max = data.max()
v_min = data.min()
total = data.count()
qtde_classes = round(sqrt(total))
amplitude = v_max - v_min
h =  amplitude/qtde_classes

# Frequência absoluta
freq = data.value_counts(bins= qtde_classes).sort_index()

# Dataframe Distribuição de frequência
df = pd.DataFrame(freq)
# Resetando o index
df = df.reset_index()
# Renomeando as colunas
df.columns = ["Classe", "Frequência"]



# Frequência relativa
df["Frequência Relativa"] = df["Frequência"]/total

# Novo Intervalo de Classe
# Corrigindo o Valor Final
amp_classe = ceil(h)
end_corrigido = v_min + h * qtde_classes

# Criando os intervalos
intervalos = pd.interval_range(start= v_min, end= end_corrigido, freq= h)

# Atribuindo os Intervalos na Coluna Classe
df["Classe"] = intervalos

# Calculando os Pontos Médios
pts_medios = []
for intervalo in intervalos:
    pts_medios.append(intervalo.mid)

df["Pontos Médios"] = pts_medios

# Frequência Acumulada
df["Frequência Acumulada"] = df["Frequência"].cumsum()
print(df)