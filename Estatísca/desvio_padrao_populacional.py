import pandas as pd

def dpp(a):

    dados = pd.Series(a)

    media = dados.mean()
    total = dados.count()

    desvio_2 = []
    for i in a:
        desvio_2.append((i - media) ** 2)
    
    return sum(desvio_2) / total

dados = [0.42, 0.52, 0.61, 0.61, 0.54, 0.67, 0.63, 0.64, 0.54, 0.64, 0.72, 0.58, 0.62, 0.65, 0.74, 0.90, 0.99, 0.91, 0.83, 0.95, 1.02]

print(dpp(dados))

