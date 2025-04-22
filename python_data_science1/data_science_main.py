import data_science_functions as lib
import math
import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.__version__


# Este archivo contiene funciones que se pueden usar en el archivo data_science_py.py
#VARIABLES
lista = [1, 2 ,3 ,4 ,5]

#return me permite devolver un valor/resultado de una función en una variable que puedo usar despues como si fuera global
#lambda functions: no necesitan ser definidas con def, se pueden usar para funciones pequeñas y simples, no necesitan nombre, se pueden usar como argumentos de otras funciones
# se suelen escribir en una sola línea, no se pueden usar en funciones que necesiten más de una línea de código
# def cualitativa(nota):
#     nota = float(input('digite una nota: '))
#     return nota +0.5
# EN LAMBDA seria asi
# cualitativa = lambda nota: nota + 0.5  # definimos la función lambda, y luego de los dos putnos se define lo que hace función
# usualmente se usa para algo pequeño y del momento
# 16 obtener promedio ponderado de un estudiante, se solicitan 3 notas y los pesos de las notas son respectivamente 3, 2 y 5
#   n1= float(input('digite la primera nota: '))
#   n2= float(input('digite la segunda nota: '))
#   n3= float(input('digite la tercera nota: '))
   
#   ponderado = lambda x,y,z: (x*3 + y*2 + z*5)/10  aqui se define la fucion y los argumentos que necesita
#    ponderado (n1,n2,n3) luego aqui se ejecuta la funcion al darse los argumentos

# MAPEAR VALORES
# map(lmbda function, lo que se quiere iterar) # se usa para aplicar una función a cada elemento de un iterable (lista, tupla, etc.)
# notas_actualizadas = map(lambda x: x +0.5, notas) # se le suma 0.5 a cada elemento de la lista notas
# print(list(notas_actualizadas)) # se convierte el resultado en una lista para poder imprimirlo

# LIST COMPREHENSION
# Nombre de lista nueva = [funcion(nota) for x in x] # se usa para crear una nueva lista a partir de una lista existente aplicando una función a cada elemento de la lista original
# nombre_lista [lo que quiero que haga con X informacion] # se puede pensar como un query y lo que devuelva ese query es lo que uqeda como valor de la lista
# EX: promedios =[round(nota) for nota in notas] # se redondea cada elemento de la lista notas y se guarda en la lista promedios
# ex: estudiantes = list(zip(nombres, promedios)) # se crea una lista de tuplas con los nombres y promedios de los estudiantes
    #estudiantes = [('Juan', 3.5), ('Pedro', 4.0), ('Maria', 4.5)] # se crea una lista de tuplas con los nombres y promedios de los estudiantes
# candidatos_beca = [estudiantes[0] for estudiante in estudiantes if estudiante[1] >= 4] # añade estudiantes [0] que es el nombre de caja conjunto de nombre, nota ya que 0 es el primer index
    # luego se utiliza el if para ver el segundo index (estudiante[1]) es decir la nota, es mayor o igual a  4, 
    # asi al final la lista 'candidatos_beca' solo tendra los estudiantes que cumplan con la condicion

# DICTIONARY COMPREHENSION
# {llave: valor for item in lista}

# lib.num_in_list(lista)
lib.jardin()
