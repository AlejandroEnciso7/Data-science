import pandas as pd

# Cargar el archivo CSV
datos = pd.read_csv("./Curso-de-Estadistica-con-Python-Aula-1/datos.csv")
print(datos.sample(10))  # Muestra 10 filas aleatorias del DataFrame
print(datos.head())  # Muestra las primeras filas del DataFrame
sorted(datos['Años de Estudio'].unique()) # Muestra los valores únicos de la columna 'Años de Estudio' ordenados
datos.Edad.max() # muestra el valor maximo de la columna 'Edad'
print(f"La edad mínima es {datos.Edad.min()} y la edad máxima es {datos.Edad.max()}") 

# DISTRIBUCION DE FRECUENCIAS
datos['Sexo'].value_counts()  # Cuenta la frecuencia de cada valor en la columna 'Sexo'
datos['Sexo'].value_counts(normalize=True) *100  # devuelve un decimal entre 0 y 1 por el normalize que seria un porcentaje, el '*100* es para convertirlo a porcentaje

frecuencia_sexo = datos['Sexo'].value_counts()

porcentaje_sexo = datos['Sexo'].value_counts(normalize=True) *100

dist_frec_cualitativa = pd.DataFrame({
    'frecuencia': frecuencia_sexo,
    'porcentaje': porcentaje_sexo   
})

dist_frec_cualitativa.rename(index = { 0: 'masculino', 1: 'femenino'}, inplace=True)  # Renombra los índices del DataFrame

dist_frec_cualitativa.rename_axis('Sexo', axis = 'columns', inplace=True)  # Renombra el eje de las columnas, por que no todas acaban llamandose sexo?
print(dist_frec_cualitativa)

# DISTRIBUCION DE FRECUENIAS METODO CROSSTAB

frecuencia = pd.crosstab(datos['Sexo'], datos['Color'], # Crea una tabla de contingencia entre 'Sexo' y 'Color'
                         aggfunc='mean', # Indica que queremos calcular la media de datos.Ingreso para cada combinación de Sexo y Color. Podríamos usar otras funciones de agregación como sum, count, etc., dependiendo del análisis que queramos realizar.
                         values = datos['Ingreso']) # Especifica la variable numérica cuyos valores se agregarán en cada celda de la tabla.

clases = [0, 1576, 3152, 7880, 15760, 20000] # Clases para agrupar los ingresos
label = [ 'E', 'D', 'C', 'B', 'A']  # Etiquetas para las clases de ingresos



frecuencia_ingresos = pd.value_copunts(pd.cut( x = datos['Ingreso'], # Corta los datos de la columna 'Ingreso' en las clases definidas
                              bins = clases, # Especifica los límites de las clases, con las clases definidas anteriormente
                              labels = label, # Asigna etiquetas a las clases segun la variable 'label'
                              include_lowest = True)) # Incluye el límite inferior en la primera clase

# MEDIA, MODAS Y MEDIANA
print(f"La media de la edad es {datos.Edad.mean()}")  # Calcula la media de la columna 'Edad'
print(f"La moda de la edad es {datos.Edad.mode()[0]}")  # Calcula la moda de la columna 'Edad', mode() devuelve una serie, por eso se pone [0] para obtener el primer valor
print(f"La mediana de la edad es {datos.Edad.median()}")  # Calcula la mediana de la columna 'Edad'

#REGRESION LINEAL
#como una variable depende de otra, por ejemplo, el seniority de una persona en una empresa y su ingreso, y como estas se relacionan entre sí. 

# El coeficiente de determinación, frecuentemente llamado R², es una medida estadística que indica cuánto de la variabilidad de la variable dependiente (respuesta) 
# es explicada por el modelo de regresión lineal.

# Interpretando el R²
# Varía de 0 a 1, un valor cercano a 1 indica que el modelo se ajusta bien a los datos, explicando la mayor parte de la variación en la variable dependiente/respuesta. 
# Por otro lado, un valor cercano a 0 indica que el modelo no puede explicar mucha variación en la variable dependiente/respuesta.

#RESIDUOS
# modelo_0.resid # Los residuos son las diferencias positivas y negativas entre los valores observados y los valores predichos por el modelo de regresión 
# (es decir la recta en los graficos). Por ejemplo si la recta dice que una persona con 10 años de estudio debería ganar 1000 y esa persona gana 1200, el residuo es 200.
# mientras menor sea el residuo, mejor se ajusta el modelo a los datos.

# PASOS IMPORTANTES PARA REALIZAR UNA REGRESION LINEAL SIMPLE
#Dividir la base de datos para entrenar y probar el modelo;
#Interpretar los coeficientes de regresión lineal simple;
#Calcular e interpretar el coeficiente de determinación R²;
#Analizar cuánto se desvía cada punto de datos de la línea de regresión ajustada a través de los residuos;
#Comprender qué tan bien se ajustan los valores observados al modelo de regresión con R²;
#Calcular el R² en el conjunto de prueba.

#sns.pairplot(datos) muestra graficos de dispersión entre todas las variables numéricas del DataFrame, permitiendo visualizar las relaciones entre ellas.
#sns.pairplot(datos, y_vars=['Ingreso'], x_vars=['Años de Estudio', 'Edad']) # Muestra gráficos de dispersión entre 'Ingreso' y las otras variables numéricas especificadas.
# tambien se pueden usar multiples variables  tanto en x_vars como en y_vars, por ejemplo: