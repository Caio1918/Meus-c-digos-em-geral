import pandas as pd
import numpy as np
from math import sqrt, ceil
import matplotlib.pyplot as plt

dados = pd.Series([35,51,44,42,37,38,36,39,44,43,40,40,32,39,41,38,42,39,40,46,37,35,41,39])

# Valores importantes
total = dados.count()
v_max = dados.max()
v_min = dados.min()
amp = v_max - v_min
qtde_classes = 5
h = ceil(amp/qtde_classes)

# Definindo a frequência e criando DataFrame
freq = dados.value_counts(bins=qtde_classes).sort_index()
df = pd.DataFrame(freq)
df = df.reset_index()
df.columns = ["Classe", "Frequência"]



print(df)