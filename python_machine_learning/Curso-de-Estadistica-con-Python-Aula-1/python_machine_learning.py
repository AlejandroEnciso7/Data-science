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

# datos.describe # Muestra estadísticas descriptivas de las columnas numéricas del DataFrame, como la media, desviación estándar, valores mínimo y máximo, cuartiles, etc.
# datos.corr() # Muestra la matriz de correlación entre las columnas numéricas del DataFrame, indicando la relación lineal entre ellas, 
# si es positiva (cuando una aumenta la otra también) o negativa (cuando una aumenta y la otra disminuye).

# cuando las variables no tienene valores iguales a 0 se puede aplicar directamente la transformación logarítmica a las variables, por ejemplo:
# datos['log_Ingreso'] = np.log(datos['Ingreso']) # Aplica la transformación logarítmica a la columna 'Ingreso', lo que puede ayudar a normalizar la distribución de los datos y reducir la influencia de valores extremos.
# cuando tienen valores iguales a 0, se puede aplicar la transformación logarítmica con un desplazamiento, por ejemplo:
# datos['log_Ingreso'] = np.log(datos['Ingreso'] + 1) # Aplica la transformación logarítmica a la columna 'Ingreso' con un desplazamiento de 1, lo que evita problemas con valores cero y negativos.

# esta transofrmacion logaritmica se utiliza para mejorar la simetria de la distribución de los datos,
# lo que puede ser útil para cumplir con los supuestos de normalidad y homoced

# from sklearn.model_selection import train_test_split # Importa la función para dividir los datos en conjuntos de entrenamiento y prueba

# se crea una serie de variables independientes/explicativas (X) y una variable dependiente (y) para la regresión lineal
# X = datos[['Años de Estudio', 'Edad']]  # Variables independientes
# y = datos['Ingreso']  # Variable dependiente

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # Divide los datos en conjuntos de entrenamiento (80%, X_train y y_train) 
# y prueba (20%, X_test y y_test, definido por el test_size=0.2) y establece una semilla aleatoria (random_state=42) para reproducibilidad, funciona como un seed.

#sm.OLS(y_train, sm.add_constant(X_train)).fit()  # Ajusta un modelo de regresión lineal a los datos de entrenamiento, añadiendo una constante para el término independiente. 
# ejemplo de uso:
# modelo_0 = sm.OLS(y_train, sm.add_constant(X_train)).fit()
# print(modelo_statsmodels.summary())  # Muestra un resumen estadístico del modelo ajustado, incluyendo coeficientes, errores estándar, valores p, R², etc.
# de este summary es importante observar el R², que indica qué tan bien se ajusta el modelo a los datos, y los coeficientes de las variables independientes, 
# que indican la relación entre cada variable independiente y la variable dependiente.
# Asi mismo ver el f-statistic que deberia ser menor o igual a 0.05, lo que indica que al menos una de las variables independientes es significativa para predecir la variable dependiente.
# y el test p>|t| que también debería ser menor o igual a 0.05, lo que indica que la variable independiente es significativa para predecir la variable dependiente.

# ESTIMAR EL MODELO Y EVALUARLO
# from sklearn.linear_model import LinearRegression  # Importa la clase para crear un modelo de regresión lineal
# from sklearn import  metrics  # Importa el módulo para evaluar el modelo
# modelo = LinearRegression()  # Crea una instancia del modelo de regresión lineal
# modelo.fit(X_train, y_train)  # Ajusta el modelo de regresión lineal a los datos de entrenamiento

# se crea un dataframe utilizando predict()
# y_prediccion=modelo.predict(x_test)  # Realiza predicciones en el conjunto de prueba utilizando el modelo ajustado (lo que se hizo con el fit antes)

# entrada = x_test[0:1]  # Selecciona la primera fila del conjunto de prueba para hacer una predicción
# prediccion = modelo.predict(entrada)  # Realiza una predicción para la fila seleccionada
#np.exp(prediccion)  # Aplica la transformación exponencial a la predicción, si se utilizó una transformación logarítmica en los datos originales, 
# para volver a la escala original de los datos.

# intercepto = modelo.intercept_  # Obtiene el término independiente del modelo, es decir el valor de la variable dependiente cuando todas las variables independientes son cero.
# coeficientes = modelo.coef_  # Obtiene los coeficientes de las variables independientes del modelo, que indican la relación entre cada variable independiente y la variable dependiente.
# residuos = y_train - y_prediccion_train # Calcula los residuos, que son las diferencias entre los valores observados y los valores predichos por el modelo en el conjunto de entrenamiento.
# Para graficar la distribución de frecuencia de los residuos, podemos usar la función distplot() de la biblioteca seaborn.

# pasos resumidos:
# Estimar el modelo lineal usando los datos de entrenamiento
# Obtener el coeficiente de determinación (R²) del modelo estimado
# Generar las predicciones para los datos de prueba del modelo
# Obtener el coeficiente de determinación (R²) para las predicciones del modelo
# Generar la predicción puntual del modelo
# Invertir la transformación para obtener la estimación en dólares
# Crear un simulador simple
# Obtener el intercepto del modelo
# Obtener los coeficientes de regresión
# Crear un DataFrame para almacenar los coeficientes del modelo
# Interpretar los coeficientes estimados
# Analizar gráficamente los resultados del modelo

# cuando se estan defininedo los pesos de las variables independientes, es importante estandarizarlas, para que todas tengan la misma escala y no se vean afectadas por la magnitud de los valores.
# por ejemplo, si hay una variable de estado civil, casado no deberia tener mas peso que soltero, 
# por lo que se puede usar OneHotEncoder para convertir variables categóricas en variables dummy/indicadoras.
# para ello se usa: 
# from sklearn.compose import make_column_transformer
# from sklearn.preprocessing import OneHotEncoder
# columnas = x.columns # obtiene las columnas del DataFrame x, que contiene las variables independientes.
# one_hot_encoder = make_column_transformer(
#     (OneHotEncoder(drop= 'if_binary'), 
#                   ['Sexo', 'Color']),  # Aplica OneHot a esas columnas
#                remainder='passthrough',  # Deja las demás columnas sin cambios
#               sparse_threshold=0)  # No crea matrices dispersas, garantiza que el modelo no quite informacion relevante de las columnas originales.
#               force_int_remainder_cols=False)  # Asegura que las columnas restantes no se conviertan a enteros, manteniendo su tipo de dato original.

# x = one_hot_encoder.fit_transform(X) # aqui se aplica el OneHotEncoder a las variables independientes X, transformando las variables categóricas en variables dummy/indicadoras.
# one_hot_encoder.get_feature_names_out(columnas)  # Obtiene los nombres de las nuevas columnas generadas por OneHotEncoder, 
# que corresponden a las variables dummy/indicadoras creadas a partir de las variables categóricas.

# Los algoritmos de Machine Learning no pueden comprender información que no esté en formato numérico. 
# Por lo tanto, si se desea utilizar variables categóricas en modelos, es necesario que pasen por algún tipo de tratamiento para que estén en formato numérico.
#  Esto no significa que se convertirán en variables numéricas, solo que estarán en un formato que sea comprendido por los modelos.
# Así, estas transformaciones deben preservar la información real de las categorías de la mejor manera posible, sin introducir sesgos en el modelo y 
# sin información que esté alejada de la realidad. La forma ideal de hacer este tipo de transformación, que mantiene la información original, 
# se conoce como one hot encoding. Esta acción transforma cada una de las clases de las variables categóricas en nuevas columnas,
# utilizando el valor 0 para representar la ausencia de la característica y 1 para la presencia de la característica en la muestra de la base de datos.

#pd.dataframe(x, columns=one_hot_encoder.get_feature_names_out(columnas))  # Crea un DataFrame a partir de la matriz transformada por OneHotEncoder,

# from sklearn.preprocessing import LabelEncoder # ayuda a convertir las variable tipo objeto en variables numéricas,
# label_encoder = LabelEncoder()  # Crea una instancia del codificador de etiquetas
# y = label_encoder.fit_transform(y)  # Aplica el codificador a la variable dependiente y, transformando las categorías (en este caso 'si' y 'no'en valores numéricos.
