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
# datos.describe(include='O')  # Estadísticas descriptivas para las variables del tipo “object”
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

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)  # Divide los datos en conjuntos de entrenamiento (80%, X_train y y_train) 
# y prueba (20%, X_test y y_test, definido por el test_size=0.2) y establece una semilla aleatoria (random_state=42) para reproducibilidad, funciona como un seed.
# Stratify=y asegura que la división mantenga la proporción de clases en la variable dependiente y (es decir tanto el 80% como el 20% mantienen el mismo porcentaje de variables negativas o positivas),
#  lo que es importante si se tiene una variable categórica como objetivo.
# los datos de entrenamiento se utilizan para ajustar el modelo ya que el modelo podra ver los resultados de como se comportan las variables, 
# mientras que los datos de prueba se utilizan para evaluar su desempeño con datos que nunca ha visto antes.

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

# OVERFITTING Y UNDERFITTING
# Overfitting ocurre cuando el modelo se ajusta demasiado a los datos de entrenamiento, capturando el ruido y las fluctuaciones aleatorias en lugar de la tendencia general.
# Esto puede llevar a un rendimiento deficiente en los datos de prueba, ya que el modelo no generaliza bien a nuevos datos.
# Características del overfitting:

#Error muy bajo en las predicciones en datos de entrenamiento;
#Error muy alto en las predicciones en datos de prueba;
#Modelo muy complejo que intenta memorizar los datos de entrenamiento en lugar de aprender el patrón de los datos.

# Underfitting ocurre cuando el modelo es demasiado simple para capturar la complejidad de los datos, 
# lo que resulta en un rendimiento deficiente tanto en los datos de entrenamiento como en los de prueba.
# Características del underfitting:
# Error alto en las predicciones en datos de entrenamiento;
# Error alto en las predicciones en datos de prueba;
# Modelo demasiado simple que no puede aprender el patrón de los datos.

# para evaluar si un modelo se encuentra balanceado o no se puede tener una primera valorcion on un dummy
# from sklearn.dummy import DummyClassifier
# dummy = DummyClassifier()
# dummy.fit(X_train, y_train)  # Ajusta el clasificador dummy a los datos de entrenamiento
# dummy.score(X_test, y_test)  # Evalúa el clasificador dummy en los datos de prueba, proporcionando una línea base para comparar con modelos más complejos que intentaremos crear mas adelante.

# ARBOLES DE DECISION
# Los árboles de decisión son modelos de Machine Learning que se utilizan para clasificación y regresión,
# que dividen los datos en subconjuntos basados en características específicas, creando una estructura jerárquica similar a un árbol.
# Cada nodo interno del árbol representa una prueba en una característica, por ejemplo X<=25, se ejecuta sobre laas columnas abc en donde cada columna contiene unos valores,
# idealmente los valores dentro de las columnas deberian retornar verdadero o falso segun la condicion que se establezca en el nodo (x<=25), de no retornar los valores 1 o 0 esperados
# se genera una nueva condicion que logre aplicar para todos. Cada rama representa el resultado de la prueba es decir devolverá verdadero o falso segun la hipotesis del nodo sea correcta o no,
# y cada hoja representa una etiqueta de clase o un valor de predicción.

# from sklearn.tree import DecisionTreeClassifier  # Importa la clase para crear un árbol de decisión para clasificación
# modelo_arbol = DecisionTreeClassifier(random_state=42)  # Crea una instancia del árbol de decisión con una semilla aleatoria para reproducibilidad
# modelo_arbol.fit(X_train, y_train)  # Ajusta el árbol de decisión a los datos de entrenamiento
# modelo_arbol.score(X_test, y_test)  # Evalúa el árbol de decisión en los datos de prueba, proporcionando una medida de precisión del modelo.
# GRAFICAR EL ARBOL DE DECISION
# plt.figure(figsize=(80,30))  # Establece el tamaño de la figura para el gráfico del árbol
# plot_tree (modelo_arbol, filled=True, class_names=['no', 'si'], fontsize=6, feature_names=X.columns)  # Grafica el árbol de decisión, 
# rellenando los nodos con colores según las clases, y etiquetando las clases y características.

'''El árbol de decisión es un algoritmo de machine learning supervisado que tiene una buena interpretabilidad. Esto significa que es posible tener una comprensión fácil de los pasos que se realizaron para llegar al resultado final de la predicción del modelo. Estos pasos pueden ser representados de forma visual, a partir de un diagrama que indica cada una de las decisiones que se tomaron para llegar a la clasificación de un dato.

Para llegar a una regla que clasifique los datos con una buena tasa de acierto, las decisiones del árbol no pueden ser totalmente aleatorias. Debe haber un sentido en cada elección hecha por el árbol de decisión. Ahora entendamos cómo se hacen estas elecciones:

El primer paso es seleccionar una columna de la base de datos que se utilizará para dividir los datos en 2 subconjuntos. El objetivo es que la mayor cantidad posible de datos se separe en relación con la variable objetivo. Entonces, el mejor resultado posible sería si uno de los subconjuntos tuviera solo datos de una categoría de la variable objetivo y el otro subconjunto tuviera solo datos de la otra categoría restante. Para hacer la mejor elección posible, se prueban diferentes columnas y valores, y aquella que proporcione la mejor separación se elige como la primera regla del árbol de decisión.

Para definir qué es una buena separación, se realizan cálculos matemáticos para obtener la proporción de datos de cada categoría de la variable objetivo dentro de los subconjuntos. El resultado de este cálculo se conoce como métrica de impureza. Existen diferentes tipos de métricas, siendo las más utilizadas la entropía y el índice de Gini. A continuación, se presentan las características de cada una.

Índice Gini
Este índice informa el grado de heterogeneidad de los datos. Su objetivo es medir la frecuencia de que un elemento aleatorio de un nodo sea etiquetado de manera incorrecta. En otras palabras, este índice cuantifica y determina la impureza de un nodo, idealmente debería ser 0 si todos los elementos pertenecen a una sola clase y 0.5 si hay una mezcla equitativa de clases.'''

# modelo_arbol = DecisionTreeClassifier (max_depth=3, random_state=42)  # Crea un árbol de decisión con una profundidad máxima de 3 para evitar el sobreajuste 
# y se mantiene el random state para mantener el seed, ajustar la profundidad del árbol puede ayudar a evitar el sobreajuste, ya que limita la complejidad del modelo.

# PASOS RESUMIDOS PARA CREAR UN ARBOL DE DECISION
#Separar la base de datos entre entrenamiento y prueba;
#Construir un modelo base con el DummyClassifier;
#Construir un modelo de árbol de decisión con el DecisionTreeClassifier;
#Evaluar un modelo de machine learning usando la tasa de acierto del método score;
#Visualizar las decisiones de un árbol de decisión con el método plot_tree.

# NORMALIZACION DE DATOS para modelo KNN
# La normalización de datos es un proceso que ajusta los valores de las características para que tengan una escala común,
# esto sirve para que valores numericos de diferentes magnitudes no dominen el modelo de machine learning, por ejemplo la variable edad y la variable ingreso,
# una edad maxima llegaria a 100 y un ingreso maximo a 20000, por lo que la edad no tendria tanto peso en el modelo como el ingreso,
# por lo que se normalizan los datos para que todas las variables tengan el mismo peso en el modelo.

#from sklearn.preprocessing import MinMaxScaler  # Importa la clase para normalizar los datos
# normalization = MinMaxScaler()  # Crea una instancia del normalizador
# X_train_normalized = normalization.fit_transform(X_train)  # Ajusta y transforma los datos de entrenamiento, normalizando las características para que estén en el rango [0, 1]

# from sklearn.neighbors import KNeighborsClassifier  # Importa la clase para crear un clasificador k-NN que define una variable en función de sus vecinos más cercanos
# modelo_knn = KNeighborsClassifier(n_neighbors=5)  # Crea una instancia del clasificador k-NN con 5 vecinos más cercanos, tambien dejar vacio los ()
# x_test_normalized = normalization.transform(X_test)  # Transforma los datos de prueba utilizando el mismo normalizador ajustado a los datos de entrenamiento
# modelo_knn.score(X_test_normalized, y_test)  # Evalúa el clasificador k-NN en los datos de prueba normalizados, proporcionando una medida de precisión del modelo.

# PICKLE PARA EXPORTAR MODELOS
# import pickle  # Importa la biblioteca para la serialización de objetos

# with open('modelo_knn.pkl', 'wb') as archivo:  # Abre un archivo en modo escritura binaria
#     pickle.dump(modelo_knn, archivo)  # Serializa y guarda el modelo k-NN en el archivo, también se puede usar para guardar otros modelos como DecisionTreeClassifier, 
# LinearRegression, one hot encoder, etc.

'''  El módulo pickle en Python es una herramienta poderosa y versátil que permite la serialización y deserialización de objetos Python.
 Este proceso de serialización implica la conversión de objetos Python en una representación binaria que puede ser almacenada en un archivo. 
 Más tarde, esta representación puede ser deserializada para recrear el objeto original.

Así, es posible almacenar modelos de machine learning en archivos pickle, para que puedan ser utilizados en otros programas. 
Él preserva completamente el estado del objeto, incluyendo todos los parámetros y configuraciones. 
Además, el formato binario generado por el pickle es independiente de la plataforma, lo que significa que es posible crear un archivo en un sistema operativo y 
cargarlo en otro sin problema de compatibilidad. Vale destacar que en versiones diferentes de Python esto puede ser un problema. 
Objetos serializados en una versión específica pueden no ser cargados correctamente en otra versión. Por lo tanto, es muy importante saber cuál es la versión del lenguaje y 
de las bibliotecas utilizadas en el proyecto para que sean replicadas dentro del sistema en el que se va a utilizar.

El proceso para utilizar el pickle involucra principalmente dos funciones:

pickle.dump(objeto, archivo): Esta función permite almacenar un objeto Python en un archivo. El argumento objeto es el objeto que deseas serializar, 
y el argumento archivo es el objeto de archivo donde deseas almacenar la representación binaria.
pickle.load(archivo): Esta función permite que deserialices (cargues) un objeto Python de un archivo. 
El argumento archivo es el archivo de donde deseas cargar la representación binaria.
También podemos usar la biblioteca pandas para hacer la lectura de archivos pickle. Para esto, basta con utilizar el método pd.read_pickle.

Para obtener una evaluación más completa del desempeño de modelos de clasificación, podemos utilizar una herramienta conocida como matriz de confusión. Esta matriz ofrece ventajas a la persona científica de datos, ya que permite entender cuántos errores y aciertos tiene las predicciones de un modelo. En lugar de una tasa de acierto general, la matriz es capaz de proporcionar información en una visualización para cada una de las categorías de la variable objetivo.

Piensa en un sistema de seguridad de un edificio que utiliza cámaras para identificar personas que entran. La "matriz de confusión" se vuelve valiosa, ya que permite verificar cuántas veces el sistema acertó al identificar correctamente a las personas autorizadas, cuántas veces acusó erróneamente a personas y cuántas veces dejó pasar a personas no autorizadas. Con estos números, es posible ajustar el sistema para minimizar falsos positivos y negativos, mejorando su precisión en la detección de visitantes.

En la representación general de una matriz de confusión, para más detalles analiza la imagen a continuación, las filas de la matriz corresponden a los valores reales de la base de datos, mientras que las columnas corresponden a los valores previstos por el modelo de clasificación. Las categorías de la variable objetivo están representadas por el valor 0 (ausencia del atributo), también llamado negativo, y por el valor 1 (presencia del atributo), también llamado positivo.

Cada elemento de la matriz está identificado por un nombre de acuerdo con la intersección entre la predicción y el valor real. La diagonal principal de la matriz, que está destacada por el color verde, representa los elementos que tienen la predicción igual al valor real, por lo tanto son los aciertos del modelo. Por otro lado, la diagonal secundaria, que está destacada por el color rojo, representa los elementos con predicciones diferentes del valor real, por lo tanto son los errores del modelo. La descripción de cada uno de los elementos es la siguiente:

Verdaderos Negativos (VN): Cuando el valor real es 0 y la predicción también es 0. Indica que el modelo clasificó correctamente los valores de la clase negativa.
Falsos Positivos (FP): Cuando el valor real es 0 y la predicción es 1. Indica que el modelo clasificó erróneamente un elemento de la clase negativa como si fuera de la clase positiva.
Falsos Negativos (FN): Cuando el valor real es 1 y la predicción es 0. Indica que el modelo clasificó erróneamente un elemento de la clase positiva como si fuera de la clase negativa.
Verdaderos Positivos (VP): Cuando el valor real es 1 y la predicción también es 1. Indica que el modelo clasificó correctamente los valores de la clase positiva.

visualmente la distrubicion de la matriz de confusión se puede ver con el siguiente codigo:
 '''
# from sklearn.metrics import confusion_matrix  # Importa la función para calcular la matriz de confusión
# y_previsto = modelo.predict(x_val)  # Realiza predicciones en el conjunto de validación utilizando el modelo ajustado
# matriz_confusion = confusion_matrix(y_val, y_previsto)  # Calcula la matriz de confusión comparando los valores reales (y_val) con las predicciones (y_previsto)
# print)matriz_confusion)  # Imprime la matriz de confusión
# la matriz se vera asi:
#[[10256(verdadero negativo)  123(falso positivo)]
#[ [  98(falso negativo)  523(verdadero positivo)]]

# VALIDAR MODELOS
# otra forma de validar los modelos es por medio del recall Mide la proporción de datos positivos que fueron correctamente identificados por el modelo, es decir, 
# revela la capacidad del modelo en evitar la clasificación incorrecta de datos positivos como negativos. 
# Se usa cuando el riesgo o costo de clasificar falsos negativos es alto. 
# Por ejemplo, en casos de diagnóstico de enfermedades graves, donde es fundamental detectar correctamente la presencia de la enfermedad.

# A continuación, podemos constatar el cálculo del recall a partir de la matriz de confusión. El recall solo toma en cuenta los valores positivos reales, es decir,
#  los valores de la segunda fila de la matriz. Se calcula a partir de la división entre Verdaderos Positivos (VP) y la suma de todos los positivos reales (VP + FN):

#tambien se puede utilizar la precision, Mide la proporción de datos clasificados como positivos que son realmente positivos, es decir, 
# revela la capacidad del modelo en evitar la clasificación incorrecta de datos negativos como positivos. 
# Se usa cuando el riesgo o costo de clasificar falsos positivos es alto, por ejemplo, en casos de selección de acciones en el mercado financiero, 
# donde lo importante es seleccionar acciones que tengan gran probabilidad de retorno, 
# reduciendo la cantidad de acciones malas (falsos positivos) incluso si otras buenas acciones no han sido detectadas por el modelo (falso negativo). 
# La precisión también es importante en el ejemplo de detección de enfermedades, donde queremos evitar que pacientes sanos sean erróneamente clasificados como enfermos.

#A continuación, podemos analizar el cálculo de la precisión a partir de la matriz de confusión.
#  La precisión solo toma en cuenta los valores positivos previstos por el modelo, es decir, los valores de la segunda columna de la matriz.
#  Se calcula a partir de la división entre Verdaderos Positivos (VP) y la suma de todos los positivos previstos (VP + FP):

# finalmente se puede utilizar la f1-score, que es una métrica que combina la precisión y el recall en un solo valor,
# F1-Score proporciona un equilibrio entre el recall y la precisión, siendo útil cuando las clases de la variable objetivo están desbalanceadas, es decir, 
# cuando hay una cantidad de datos muy diferente para cada clase. Además, es aplicable cuando el riesgo o costo de falsos positivos y de falsos negativos es alto simultáneamente.
# En casos de detección de tumores en pacientes, es necesario tener un equilibrio entre evitar errores en la detección de tumores cuando la persona realmente los tiene y 
# evitar errores al informar que una persona tiene un tumor cuando en realidad no lo tiene.

#El cálculo del F1-Score se realiza a partir de la media armónica entre la precisión y el recall. 
# Por lo tanto, equivale a 2 veces la precisión por el recall, dividido por la suma entre la precisión y el recall

# CURVA ROC
# La curva ROC (Receiver Operating Characteristic) es una herramienta gráfica utilizada para evaluar el desempeño de modelos de clasificación binaria.
# se hace de la siguiente manera:
# from sklearn.metrics import RocCurveDisplay  # Importa la clase para crear la curva ROC
# RocCurveDisplay.from_predictions(y_val, y_previsto, name='arbol de decisión')  # Crea la curva ROC a partir de las predicciones del modelo y los valores reales del conjunto de validación


# CURVA PRECISION-RECALL
# La curva de precisión-recall es una herramienta gráfica utilizada para evaluar el desempeño de modelos de clasificación binaria,
#  especialmente en situaciones donde las clases están desbalanceadas. Como la curva de precisión x recall no evalúa la tasa de verdaderos negativos, 
# que generalmente contendrá la mayor cantidad de datos, el análisis se concentra más en la clase con menor cantidad de datos,
#  y esto hace que el análisis sea mejor en datos desbalanceados.
# se hace de la siguiente manera:
# from sklearn.metrics import PrecisionRecallDisplay  # Importa la clase para crear la curva de precisión-recall
# PrecisionRecallDisplay.from_predictions(y_val, y_previsto, name='arbol de decisión')  # Crea la curva de precisión-recall a partir de las predicciones del modelo y los valores reales del conjunto de validación


# MODELO K-FOLD
# modelo = DecisionTreeClassifier(max_depth=10)
# kf =KFold(n_splits=5, shuffle=True, random_state=42)  # Crea un objeto KFold para dividir los datos en 5 pliegues, 
# barajando los datos y estableciendo una semilla aleatoria para reproducibilidad
# cv_resultados =cross_validate(modelo, X, y, cv=kf, scoring='recall') # Realiza la validación cruzada del modelo utilizando el objeto KFold,
# print(cv_resultados)  # Imprime los resultados de la validación cruzada, que incluyen las puntuaciones de recall para cada pliegue.

# MODELO STRATIFIED K-FOLD
# from sklearn.model_selection import StratifiedKFold  # Importa la clase para crear un K-Fold estratificado
# modelo= DecisionTreeClassifier(max_depth=10)  # Crea un modelo de árbol de decisión con una profundidad máxima de 10
# skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)  # Crea un objeto StratifiedKFold para dividir los datos en 5 pliegues,
# barajando los datos y estableciendo una semilla aleatoria para reproducibilidad, StratifiedKFold garantiza que cada pliegue tenga una representación proporcional de las clases.
# cv_resultados =cross_validate(modelo, X, y, cv=kf, scoring='recall') # Realiza la validación cruzada del modelo utilizando el objeto KFold,
# print(cv_resultados)  # Imprime los resultados de la validación cruzada, que incluyen las puntuaciones de recall para cada pliegue.

'''
undersampling
Es una técnica que consiste en mantener todos los datos de la clase de menor frecuencia y reducir la cantidad de los de la clase de mayor frecuencia,
 haciendo que las observaciones del conjunto tengan datos con la variable objetivo balanceada.

Puede ser una ventaja usar undersampling para reducir el almacenamiento de datos y el tiempo de ejecución del código, 
ya que la cantidad de datos será mucho menor. Una de las técnicas más utilizadas es Near Miss, que disminuye aleatoriamente el número de valores de la clase mayoritaria.

Algo muy interesante de Near Miss es que utiliza la menor distancia promedio de los K-vecinos más cercanos, es decir, 
selecciona los valores en base al método KNN (K-nearest neighbors) para reducir la pérdida de información.

oversampling
Es una técnica que consiste en aumentar el número de registros de la clase con menor frecuencia hasta que la base de datos tenga un número equilibrado
 entre las clases de la variable objetivo. Para aumentar la cantidad de registros, podemos duplicar aleatoriamente los registros de la clase con menos frecuencia. 
 Sin embargo, esto hará que mucha información sea idéntica, lo que puede afectar el modelo.

Una ventaja de esta técnica es que no se pierde ninguna información de los registros que tenían la clase con mayor frecuencia. 
Esto hace que el conjunto de datos tenga muchos registros para alimentar los algoritmos de aprendizaje automático.
 A su vez, el tiempo de almacenamiento y procesamiento crece significativamente y existe la posibilidad de sobreajustar los datos que se han duplicado.
   Este sobreajuste ocurre cuando el modelo se vuelve muy bueno para predecir los resultados de los datos de entrenamiento, pero no generaliza bien los datos nuevos.

Para evitar tener demasiados datos idénticos, se puede utilizar la técnica SMOTE, que consiste en sintetizar nueva información a partir de información existente.
 Estos datos “sintéticos” están relativamente cerca de los datos reales, pero no son idénticos. 

Ambas técnicas de balanceo se pueden aplicar utilizando la biblioteca imbalanced-learn que se basa en sklearn y proporciona herramientas para tratar con datos desbalanceados.

Asi mismo se pueden combinar ambas tecnicas para balancear los puntos dengativos de ambas, existe el algortimo de SMOTEENN,
que combina SMOTE y Edited Nearest Neighbors (ENN) para crear un conjunto de datos balanceado.
'''

