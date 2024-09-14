import numpy as np
import pandas as pd
import random
from math import ceil

nums = [39, 18, 27, 29, 20, 48, 30, 35, 76, 50, 33, 87, 69, 100, 4, 59, 95, 35, 98, 14, 21, 4, 97, 38, 98, 48, 85, 87, 90, 26, 10, 63, 83, 8, 70, 3, 56, 39, 73, 100, 82, 17, 55, 84, 98, 79, 101, 51, 24, 6, 26, 11, 76, 8, 60, 50, 50, 41, 65, 52, 12, 48, 7, 82, 72, 86, 33, 80, 20, 88, 17, 55, 75, 38, 83, 9, 14, 13, 68, 91, 80, 75, 17, 48, 32, 85, 55, 87, 71, 46, 97, 94, 86, 24, 15, 61, 62, 38, 58, 39]

# for i in range(100):
#     nums.append(random.randint(0, 101))

dados = pd.Series(nums)

total = dados.count()
v_max = dados.max()
v_min = dados.min()
qtde_classes = total ** (1/2) 
amplitude = v_max - v_min
h = ceil(amplitude / qtde_classes)
media = dados.mean()
print(media)

freq = dados.value_counts(bins= int(qtde_classes)).sort_index()

end_corrigido = v_min + int(qtde_classes) * h
intervalos = pd.interval_range(start= v_min, end= end_corrigido, freq= h)

df = pd.DataFrame(freq)
df = df.reset_index()
df.columns = ["Classe", "Frequência"]
df["Classe"] = intervalos

df["Frequência Relativa"] = df["Frequência"] / total

print(df)