import pandas as pd

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
