from math import sqrt, ceil
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dados = pd.Series([1595,1472,1820,1580,1804,1635,1959,2020,1480,1250,2083,1522,1306,1572,1778,2296,1445,1716,1618,1824])

# valores importantes
total = dados.count()
v_max = dados.max()
v_min = dados.min()
amp = v_max - v_min
qtde_classes = 8
h = ceil(amp/qtde_classes)

# Frequencia e DataFrame
freq = dados.value_counts(bins=qtde_classes).sort_index()
df = pd.DataFrame(freq)
df = df.reset_index()
df.columns = ["Classe", "Frequênciad"]
