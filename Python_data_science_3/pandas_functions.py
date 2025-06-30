import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = 'https://gist.githubusercontent.com/ahcamachod/a572cfcc2527046db93101f88011b26e/raw/ffb13f45a79d31223e645611a119397dd127ee3c/alquiler.csv'

datos = pd.read_csv(url)

datos.groupby('Tipo')['Valor'].mean() # esto agrupa los datos por la columna Tipo y calcula el promedio de la columna Valor para cada Tipo
datos.groupby('Tipo')[['Valor']].mean().sort_values('Valor') 
# esto agrupa los datos por la columna Tipo, calcula el promedio de la columna Valor para cada Tipo y ordena los resultados por Valor en orden ascendente (de menor a mayor)
# y permite visualiarlo de mejor manera 
# datos.groupby(['Animal', 'Color'])[['Cantidad']].sum(), groupby tambien permite agrupor por multiples columnas a la vez

df_tipo_precio = datos.groupby('Tipo')[['Valor']].mean().sort_values('Valor')
df_tipo_precio.plot(kind='barh', figdize=(10, 6), title='Precio promedio por tipo de propiedad', color='purple')
# esto crea un gráfico de barras horizontales con el promedio de precios por tipo de propiedad y las barras son moradas

datos.query('@lista in Tipo') # esto filtra los datos donde los elementos de la lista '@lista' se encuentren dentrode la columna 'Tipo'
datos.query('@lista not in Tipo') # esto filtra los datos donde los elementos de la lista '@lista' NO se encuentren dentro de la columna 'Tipo'

datos.Tipo.value_counts() # esto cuenta la cantidad de veces que aparece cada valor unico en la columna Tipo

datos.query('Tipo == "Departamento"') # esto filtra los datos donde la columna Tipo sea igual a "Departamento"

df = datos.query('Tipo == "Departamento"') # esto filtra los datos donde la columna Tipo sea igual a "Departamento" y los guarda en un nuevo DataFrame
df.head(5) # esto muestra las primeras 5 filas del DataFrame filtrado, es buena practica para ver si el filtro se aplico correctamente

porcentaje_tipo = datos.Tipo.value_counts(normalize=True).to_frame() 
# esto cuenta la cantidad de veces que aparece cada valor unico en la columna Tipo y lo normaliza para obtener el porcentaje
porcentaje_tipo.plot(kind='bar', figsize=(12,8), color='green', xlabel='Tipos', ylabel='Porcentaje', title='Porcentaje de tipos de propiedades')

# Guardando el DataFrame en una variable
df_ejemplo = df['Tipo'].value_counts(normalize=True).to_frame().sort_values('Tipo')

# Cambiando el nombre de la columna "Tipo" a "Porcentajes"
df_ejemplo.rename(columns={'Tipo': 'Porcentajes'}, inplace=True)

# Visualizando el DataFrame
df_ejemplo

# TRATAR DATOS NULOS
df.isnull() # esto devuelve un DataFrame de booleanos donde True indica que el valor es nulo y False indica que el valor no es nulo
df.isnull().sum() # esto devuelve la cantidad de valores nulos por columna 
df = df.fillna(0, inplace=True) # esto reemplaza los valores nulos por 0 en el DataFrame df, no siempre se deben tratar asi, depende de lo que se solicite
# Además, también es posible utilizar argumentos específicos del método fillna(), como method="ffill" o method="bfill", 
# para llenar los valores nulos con el valor anterior o posterior, respectivamente.
df.dropna(inplace=True) # esto elimina las filas que tienen valores nulos en el DataFrame df, no siempre se deben tratar asi, depende de lo que se solicite
df.interpolate() # esto realiza una interpolación lineal para llenar los valores nulos en el DataFrame df, es decir se calcula basado en los valores vecinos, 
# no siempre se deben tratar asi, depende de lo que se solicite

#TRATAR REGISTROS INCONSISTENTES
#por ejemplo valores == 0
df.query('Valor == 0 | Condominio ==0') # esto filtra los datos donde la columna Valor sea igual a 0
df.query('Valor == 0 | Condominio ==0').index # esto devuelve los indices de las filas donde la columna Valor o condominio sea igual a 0

df_remover = df.query('Valor == 0 | Condominio ==0').index # se guarda en una variable los valores de indices de las filas donde la columna Valor o condominio sea igual a 0
df.drop(df_remover, inplace=True) # esto elimina las filas donde los indices de la columna Valor o condominio sea igual a 0
df.drop('Tipo', axis=1, inplace=True) # esto elimina la columna Tipo del DataFrame df, axis=1 indica que se eliminará una columna, axis=0 indica que se eliminará una fila

#APLICAR FILTROS
# se crea una mascara para filtrar los datos
mascara1= df['Habitaciones'] == 1 # esto crea una mascara que filtra los datos donde la columna Habitaciones sea igual a 1
df[mascara1] # esto aplica la mascara al DataFrame df y devuelve las filas donde la columna Habitaciones sea igual a 1

mascara2= df['Valor'] > 100000 # esto crea una mascara que filtra los datos donde la columna Valor sea mayor a 100000
df[mascara2] # esto aplica la mascara al DataFrame df y devuelve las filas donde la columna Valor sea mayor a 100000
# se pueden combinar las mascaras con el operador & (AND) o | (OR)

filtro1= mascara1 & mascara2 # esto combina las mascaras con el operador AND, es decir, devuelve las filas donde la columna Habitaciones sea igual a 1 y la columna Valor sea mayor a 100000
df[filtro1] # esto aplica el filtro al DataFrame df y devuelve las filas donde la columna Habitaciones sea igual a 1 y la columna Valor sea mayor a 100000

# EXPORTAR 
df.to_csv('inmuebles_machine_learning.csv', index=False, sep =';') # esto exporta el DataFrame df a un archivo CSV llamado 'inmuebles_machine_learning.csv' sin incluir los indices
# esto se hace ya que al modificar el dataframe, los indices pueden cambiar y los originales no serian los mismos.
# SEP = ';' indica que se usará el punto y coma como separador de campos en el archivo CSV, por defecto es la coma (,)
df.to_excel('nombre_archivo.xlsx', index=False) # esto exporta el DataFrame df a un archivo Excel llamado 'nombre_archivo.xlsx' sin incluir los indices
df.to_json('nombre_archivo.json', orient='records', lines=True) # esto exporta el DataFrame df a un archivo JSON llamado 'nombre_archivo.json' en formato de registros,

# CREAR COLUMNAS NUEVAS 

df['Valor_total'] = df['Valor'] + df['Impuesto'] - df['Descuento']
df['Descripcion'] = df['Tipo'] + ' - ' + df['Ciudad'] # esto crea una nueva columna llamada Descripcion que concatena los valores de las columnas Tipo y Ciudad. si se usa \ al fina
# de la linea, se puede continuar en la siguiente linea sin problemas
df['descripcion 2'] = df['Tipo'] + ' Con ' + df['Habitaciones'].astype(str) + ' Habitaciones' # esto crea una nueva columna llamada descripcion 2 que concatena 
# los valores de las columnas Tipo y Habitaciones, .astype(str) convierte los valores de la columna Habitaciones a string para poder concatenarlos (originalmente son int)

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df['C'] = [7, 8, 9] # crea una columna C con los valores 7, 8 y 9

datos[' Tiene_suite'] = datos['Suites'].apply(lambda x: 'Si' if x > 0 else 'No') # esto crea una nueva columna llamada 'Tiene_suite' 
# que indica si la columna Suites es mayor a 0, si es asi, devuelve 'Si', si no, devuelve 'No'
# en le txt cuando una casilla no tenga suite se veran varias ;;;; seguidos (uno para cada casilla sin suite), esto es normal ya que no hay un valor para esa columna

plt.plot(datos['Valor'], datos['Habitaciones']) # esto crea un gráfico de dispersión donde el eje x es la columna Valor y el eje y es la columna Habitaciones
plt.xticks(['<100k', '100k-200k', '200k-300k', '>300k'], rotation=45) # esto cambia las etiquetas del eje x a los valores especificados y las rota 45 grados para una mejor visualización
plt.xlabel('Valor') # esto cambia el nombre del eje x a 'Valor'
plt.figure(figsize=(10, 6)) # esto cambia el tamaño de la figura a 10 de ancho y 6 de alto (en pulgadas), tambien puede facilitar la visualizacion de los graficos
plt.title('Gráfico de dispersión de Valor vs Habitaciones') # esto cambia el título del gráfico a 'Gráfico de dispersión de Valor vs Habitaciones'

fig, ax = plt.subplots(figsize=(10, 6)) # esto crea una figura y un eje para el gráfico con un tamaño de 10 de ancho y 6 de alto (en pulgadas)
ax.plot(datos['Valor'], datos['Habitaciones'], marker='o', linestyle='') # esto crea un gráfico de dispersión donde el eje x es la columna Valor y el eje y es la columna Habitaciones
ax.xaxis.set_major_locator(plt.MultipleLocator(100000)) # esto establece el intervalo de los ticks del eje x a 100000

figx, axs = plt.subplots(1,2, figsize=(12, 6)) # esto crea una figura con 1 fila y 2 columnas de subgráficos, con un tamaño de 12 de ancho y 6 de alto (en pulgadas)
# si fuera 2,2 se crearia una figura con 2 filas y 2 columnas de subgráficos, y asi sucesivamente

axs[0].plot(datos['Valor'], datos['Habitaciones'], marker='o', linestyle='') # esto crea un gráfico de dispersión en el primer subgráfico marcado como [0]
axs[0].set_title('Gráfico de dispersión de Valor vs Habitaciones') # se pueden incluir todos los parametros vistos antes, labels, titles, multiple locators, etc

axs[1].plot(datos['Valor'], datos['Suites'], marker='o', linestyle='') # esto crea un gráfico de dispersión en el segundo subgráfico marcado como [1]
axs[1].set_title('Gráfico de dispersión de Valor vs Suites') # se pueden incluir todos los parametros vistos antes, labels, titles, multiple locators, etc

# al final mostrara el grafico 1 (axs[0]) y el grafico 2 (axs[1]) uno al lado del otro
# tambien se pueden hacer anotaciones en los graficos, por ejemplo:
# for i, j in enumerate(datos['Valor']):
     #ax.text(j+20,i,str(j), fontsize=8, color='red') # esto agrega un texto al gráfico en la posición (j+20, i) con el valor de j como texto, fontsize=8 y color rojo
     #j es el valor de la columna Valor y i es el indice de la fila, por lo que se puede usar para agregar etiquetas a los puntos del gráfico