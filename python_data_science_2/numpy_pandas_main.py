import numpy_panda_functions as lib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://gist.githubusercontent.com/ahcamachod/9be09de793dc3bf1e6c3d98eb4e5b1ef/raw/21b85572693200040e11284ef6dcfc3457ec8e11/citrus.csv'
datos = np.loadtxt(url, delimiter=',', usecols=np.arange(1, 6, 1), skiprows=1)

#una lista se puede convertir en un array de numpy lo que permite trabajar con matrices y operaciones matematicas

fechas = lib.pivotear_array()[:,0]
#esto toma todas las filas  la primera columna del array y la convierte en una lista
precios = lib.pivotear_array()[:,1:]
#esto toma todas las filas y de la primera columna en adelante y la convierte en una lista

plt.plot(fechas, precios[:,0])
# hace un grafico con todas las fechas y el precio de la primera columna
moscu = precios[:.0]
kalinigrado = precios[:.1]
petersburgo = precios[:.2]
krasnodar = precios[:.3]
ekaterinburgo = precios[:.4]
plt.plot(fechas, moscu)

moscu_1= moscu[0:12] #aqui se comparan los primeros doce meses 
moscu_2= moscu[12:24]