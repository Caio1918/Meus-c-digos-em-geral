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
qtde_classes = round(sqrt(total))
amplitude = v_max - v_min
h = amplitude/qtde_classes
# ----------------------

# Tabela de categorias 
categorias = ['TVs', 'Laptops', 'Celulares', 'Tablets']
unidades_vendidas = [60, 80, 200, 50]
precos_medios = [2000, 3500, 1200, 1800]
# Construção do DataFrame
vendas_categoria = pd.DataFrame({
    'Categoria': categorias,
    'Unidades Vendidas': unidades_vendidas,
    'Preço Médio (R$)': precos_medios
})

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

#---------------- Coluna pontos médios --------------
pts_médios = []
for intervalo in intervalos:
    pts_médios.append(intervalo.mid)

df["Pontos Médios"] = pts_médios
# -------------------

#---------------- Coluna de frequência relativa -------------
df["Frequência Relativa"] = df["Frequência"] / total
# ----------------------

# Coluna de frequência acumulada -------------
df["Frequência Acumulada"] = df["Frequência"].cumsum()
# print(df)
# -----------------------


# -------------------- Gráficos histograma --------------------
#---------------- Histograma de frequência ------------

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

# plt.show()
# --------------------------

#---------------- Histograma de frequência relativa ------------------
plt.figure(figsize=(6,5))
plt.hist(x=df["Pontos Médios"], bins=classes, weights=df["Frequência Relativa"], edgecolor="Black")
plt.title("Frequência Relativa")
plt.xlabel("Valor Vendido")
plt.ylabel("Frequência")

# Colocando os os limites das classes e os pontos médios
plt.xticks(np.concatenate([classes, df["Pontos Médios"]]), rotation=45)

# plt.show()

#---------------- Poligono de frequência ----------------
# Calculando os pontos médios ficticios
fic_esq = [df["Pontos Médios"].iloc[0] - amplitude]
fic_dir = [df["Pontos Médios"].iloc[-1] + amplitude]

# Construção dos dados com inserção dos pontos médios ficticios
x_data = np.concatenate([fic_esq, df["Pontos Médios"], fic_dir])
y_data = np.concatenate([[0], df["Frequência"], [0]])

# Plotagem do gráfico
plt.figure(figsize=(6,5))
plt.plot(x_data, y_data, marker="o")
plt.title("Distribuição de Frequência")
plt.xlabel("Valores")
plt.ylabel("Frequência")

# plt.show()

# ---------------- Poligono de Frequência Relativa ----------------
# O calculo dos pontos médios continuam os mesmo de antes até o x_data
y_data = np.concatenate([[0], df["Frequência Relativa"], [0]])

# Plotagem do gráfico
plt.figure(figsize=(6,5))
plt.plot(x_data, y_data, marker="o")
plt.title("Distribuição de Frequencia Relativa")
plt.xlabel("Valores")
plt.ylabel("Frequência Relativa")

# plt.show()

# ---------------- Gráfico de Ogiva (Frequência Acumulada)----------------
# Calculo dos pontos médios fictícios
ini_ogiva = [classes[1]-amplitude]

# Adicionar as fronteiras superiores das classes ao eixo x e inserção do ponto inicial acumulado em zero
x_data = ini_ogiva + [limite for limite in classes[1:]]
y_data = np.concatenate([[0], df["Frequência Acumulada"]])

# Plotagem da ogiva 
plt.clf()
plt.plot(x_data, y_data, marker="o")

# Título 
plt.title("Ogiva - Frequécia Acumulada")
plt.xlabel("Valores")
plt.ylabel("Frequência Acumulada")

# Usa os pontos médios como maior ticks no eixo x
plt.xticks(x_data)

# Plotagem do gráfico
# plt.show()

# ---------------- Gráfico de Pareto ----------------
# Ordenando os valores em ordem decrescente
decrescente = vendas_categoria.sort_values(by="Unidades Vendidas", ascending=False)
decrescente["Frequência Acumulada"] = decrescente["Unidades Vendidas"].cumsum()

# Agora teremos 2 eixos y
fig, ax = plt.subplots(figsize=(6,5))

# Cria o primeiro eixo x vinculado ao eixo y à esquerda e plota o gráfico no eixo y à esquerda
ax.bar(decrescente["Categoria"], decrescente["Unidades Vendidas"])

# Copia o segundo eixo x vinculado ao eixo y à direita
ax2 = ax.twinx()
# Plota o gráfico vinculado ao eixo y à direita
ax2.plot(decrescente["Categoria"], decrescente["Frequência Acumulada"], 
         color="r", marker="o", label="Frequência Acumulada")

# Titulos 
ax.set_title("Gráfico de Pareto")
ax.set_xlabel("Categorias")
ax.set_ylabel("Unidades Vendidas")
ax2.set_ylabel("Frequência Acumulada")

# plt.show()

# ----------------Gráfico de pizza ----------------
plt.figure(figsize=(5,5))

plt.pie(vendas_categoria["Unidades Vendidas"], labels=vendas_categoria["Categoria"], autopct="1%.1f%%")

# Título
plt.title("Gráfico de pizza")

# Mostra o gráfico 
# plt.show()

# ---------------- Gráfico de dispersão ----------------
plt.figure(figsize=(6,5))
plt.scatter(vendas_categoria["Preço Médio (R$)"], vendas_categoria["Unidades Vendidas"])

# Títulos 
plt.title("Gráfico de Dispersão - Unidades vs. Preço")
plt.xlabel("Preço Médios (R$)")
plt.ylabel("Unidades Vendidas")

# Mostra o Gráfico
# plt.show()

# ---------------- Séries Temporais ----------------
plt.figure(figsize=(6,5))
plt.plot(dados.index + 1, dados, marker="o")

#Títulos
plt.title("Séries Temporais")
plt.xlabel("dias")
plt.ylabel("Valore")

# plt.show()

# ---------------- Gráfico de Boxplot ----------------
data = pd.DataFrame({
    "Total" : [dados]
})

plt.figure(figsize=(6,5))
plt.boxplot(data["Total"].values[0])

# Títulos
plt.title("Boxplot das Vendas")
plt.xlabel("Vendas")
plt.ylabel("Valores")

# Mostra o Gráfico
plt.show()