import numpy as np
import pandas as pd

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

