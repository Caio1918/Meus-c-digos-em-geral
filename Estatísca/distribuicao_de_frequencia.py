import pandas as pd
from math import sqrt

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