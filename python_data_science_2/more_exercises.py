import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def ejercicio_naranjas():
    '''diametro_naranja = dato[:5000, 0]
    diametro_toronja = dato[5000:, 0]
    peso_naranja = dato[:5000, 1]
    peso_toronja = dato[5000:, 1]

    plt.plot(diametro_naranja, peso_naranja)
    plt.plot(diametro_toronja, peso_toronja)'''

# debes calcular el coeficiente angular y lineal para la recta de las naranjas y para la recta de las toronjas. 
# Utiliza la fórmula de mínimos cuadrados para encontrar cada uno.

Y = peso_naranja
X = diametro_naranja
n = np.size(X)

a = (n*np.sum(X*Y) - np.sum(X)*np.sum(Y))/(n*np.sum(X**2)-np.sum(X)**2)
b = np.mean(Y) - a*np.mean(X)
# Para las toronjas, simplemente reemplaza "naranja" por "toronja" en el nombre de las variables.

# debes calcular el coeficiente angular utilizando la generación de números aleatorios. Supongamos que ya conoces el valor de b y que este es igual a 17.
norma = np.array([])
np.random.seed(84)
coeficientes_angulares = np.random.uniform(low=0.0, high=30.0, size=100)

for i in range(100):
  norma = np.append(norma, np.linalg.norm(Y - (coeficientes_angulares[i]*X + b)))