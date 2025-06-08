
import pandas as pd

url = 'https://gist.githubusercontent.com/ahcamachod/a572cfcc2527046db93101f88011b26e/raw/ffb13f45a79d31223e645611a119397dd127ee3c/alquiler.csv'

datos = pd.read_csv(url)

# File reading methods 
# si el archivo no abre correctamente y presenta un erro de UTF-8
#se pude arreglar de la siguiente forma, primero 'import chardet'
# luego se escribe lo siguiente: with open('datos.csv', 'rb') as file:
    #print(chardet.detect(file.read()))
    # obtenemos como resultado: {'encoding': 'UTF-16', 'confidence': 1.0, 'language': ''}
    # asi que ya sabiendo el encoding hacemos lo siguiente:
    #df = pd.read_csv('datos.csv', encoding='UTF-16'), y permitira leer el archivo correctamente
# tambien se puede usar el argumento 'sep' para indicar el separador de columnas, por ejemplo:
# pd.read_csv('datos.csv', sep=';') # si el separador es un punto y coma
# pd.read_csv('datos.csv', usecols = ['Tipo', 'Valor', 'Condominio']) # si solo quiero leer ciertas columnas del archivo
# tambein se pueden usar los indices de las columnas con usecols=[0,1,4] # si quiero leer las columnas 0, 1 y 4 del archivo
# pd.read_csv()
# pd.read_excel()
# pd.read_json()
# pd.read_html()
# pd.read_sql()

# explore the dataset
datos.shape
# esto muestra la cantidad de filas y columnas (filas, columnas)
datos.sample(5)
#esto muestra 5 filas aleatorias del dataset
datos.columns
#esto muestra los nombres de las columnas
datos.info()
#esto me muestra la info del dataset, el tipo de dato de cada columna, el nombre de la columna, la cantidad de datos no nulos.
#object significa que es un string, int64 significa que es un entero, float64 significa que es un decimal
datos[['columna1', 'columna2']]
#esto muestra las columnas que le indico entre corchetes