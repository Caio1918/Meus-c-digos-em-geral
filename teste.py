import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.random.normal(20, 10, 10,)
df = pd.DataFrame(x, columns=['Valores'])

print(df)
print(f'Organizado: {sorted(x)}')
print(f'{x[0]:.2f}')