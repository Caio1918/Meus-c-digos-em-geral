import numpy as py
import scipy.stats as stats

media_amostral = 494.5
media_fabricante = 500
dpp = 10
n = 36
nivel_sign = 0.05

z = (media_amostral - media_fabricante) / (dpp / n**0.5)
z_critico = stats.norm.ppf(1 - nivel_sign / 2)

p_value = 2 * (1 - stats.norm.cdf(abs(z)))

print(f"Nível de Siginificância: {nivel_sign * 100}% \nTeste z: {z:.2f} \nz crítico: {z_critico:.2f} \np value: {p_value:.4f}")

if abs(z) > z_critico:
    print("Rejeitamos a hipótese nula")
else:
    print("Aceitamos a hipótese nula")


