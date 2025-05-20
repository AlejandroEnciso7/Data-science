import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def lista_a_array(lista):
        # crea una lista
    lista = [1, 2, 3, 4, 5]

    # convierte la lista en un array Numpy
    array = np.array(lista)

    print("Lista: ", lista)
    print("Array: ", array)
    
    return np.array(lista)

#se pueden convertir filas en columnas y columnas en filas (haciendo un pivot) con la funcoin transpose
def pivotear_array(array):
    # crea un array Numpy
    array = np.array([[1, 2, 3], [4, 5, 6]])

    # pivotea el array
    array_pivot = array.T

    print("Array original:\n", array)
    print("Array pivoteado:\n", array_pivot)
    
    return array.T

# Shape(archivodatos) devuelve la forma de un array o dataframe y se puede utilizar para conocer la dimensiones de ua matriz

def promedio_manzanas():
    pass
    #np.mean(moscu) #en este caso moscu es array de datos

def llenar_valor_nan():    # interpolar, solucion para llenar valores faltantes en una matrix o dataset
    #kalingrado[4] = kalingrado[3] + kalingrado[5]/2 #esto se hace cuando hay un valor nulo en la matriz se puede llenar con el promedio de los valores enterior y despues
    pass

def ejercicio_naranjas():
    '''diametro_naranja = dato[:5000, 0]
    diametro_toronja = dato[5000:, 0]
    peso_naranja = dato[:5000, 1]
    peso_toronja = dato[5000:, 1]

    plt.plot(diametro_naranja, peso_naranja)
    plt.plot(diametro_toronja, peso_toronja)'''