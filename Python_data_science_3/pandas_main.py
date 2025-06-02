
import pandas as pd

url = 'https://gist.githubusercontent.com/ahcamachod/a572cfcc2527046db93101f88011b26e/raw/ffb13f45a79d31223e645611a119397dd127ee3c/alquiler.csv'

datos = pd.read_csv(url)

# File reading methods 
# read_csv()
# read_excel()
# read_json()
# read_html()
# read_sql()

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