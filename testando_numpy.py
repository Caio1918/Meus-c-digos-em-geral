import numpy as np

# Criando um array
d1 = np.array([1,2,3,4,5,6]) # 1 dimensão
d2 = np.array([[6,5,4,3,2,1], [1,2,3,4,5,6]]) # 2 dimensões

# print(f"1D: {d1} \n2D: {d2}")

# utilizando o método zero
x = np.zeros(shape= (1,3,2)) # Qtde de arrays; tamanho de y; tamanho de x
# print(x)

# método ones
y = np.ones((3,2)) # Tamanho de y; tamanho de x
# print(y)

# empty. Valores não vazios
vazio = np.empty((2,3)) # Tamanho de y: tamanho de x
# print(vazio)

# np.arange. Retornar valores específicos
arr = np.arange(10, 16, 0.5, float) # start, stop, step, tipo
arr2 = np.arange(stop= 14) # Caso queira usar um único parâmetro
# print(arr)
# print(arr2)

# Valores lineares np.linspace
al = np.linspace(1, 100, 100) # inicio, final, qtde
print(al)