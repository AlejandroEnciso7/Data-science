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
