import python_data_science_2.numpy_functions as lib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://gist.githubusercontent.com/ahcamachod/9be09de793dc3bf1e6c3d98eb4e5b1ef/raw/21b85572693200040e11284ef6dcfc3457ec8e11/citrus.csv'
datos = np.loadtxt(url, delimiter=',', usecols=np.arange(1, 6, 1), skiprows=1)

# en numpy siempre es importante convertir los datos en un array con la funcion np.array(datos) para poder trabajar con ellos
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

# np.allclose(base, medidas[:, 0], 0.01) #esto compara si los valores son iguales en un rango de 0.01 entre los datos de base y matriz
#np.linalg.norm(base - medidas[:, 0]) #esto compara si los valores son iguales entre los datos de base y matriz, por medio e una linea que atraviesa el grafico

precio_inmuebles = np.array([10000, 120000, 11000, 200000])
# Para crear un array independiente del array original, existe una función en Numpy, "np.copy()". Para crear la copia utilizando esta función, simplemente sigue este código:
precio_inmuebles_lima = np.copy(precio_inmuebles) 
# De esta manera, incluso si modificamos el array "precio_inmuebles", no afectará al array "precio_inmuebles_lima".

plt.plot(75, a*75+b, '+r') #aqui grafica el mes 75 como X y 'a*75+b' como el valor de Y, '*r' grafica en ese punto entre X y Y una estrella roja

# La regresión es ampliamente utilizada en ciencia de datos para la predicción y también para la interpolación de valores.

# Entero aleatorio
np.random.randint(40,100, 10) #esto genera un array de 10 valores aleatorios entre 40 y 100

#Decimanl aleatorio
np.random.uniform(0.1, 0.9, 10) #esto genera un array de 10 valores decimales aleatorios entre 0.1 y 0.9

#reproductibilidad
# es la capacidad de obtener los mismos resultados al ejecutar el mismo código de numeros aleatorios varias veces. (como seeded world)
np.random.seed(99) 
np.random.uniform(0.1, 0.9, 10) # esto genera el mismo array de 10 valores decimales aleatorios entre 0.1 y 0.9 cada vez que se ejecuta el código ya que utiliza el seed 99

np.column_stack((moscu, kalinigrado, petersburgo, krasnodar, ekaterinburgo)) #esto junta los datos de los arrays y vuelve cada uno una columna ( en este caso quedan 5 columnas)

np.savetxt('ruta del archivo', datos, delimiter=',') #esto guarda el archivo datos en un archivo de texto separado por comas
