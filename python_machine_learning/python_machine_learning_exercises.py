import pandas as pd
datos = pd.read_csv('/content/churn.csv')
datos = datos.drop('id_cliente', axis=1)
datos
datos.info()
''' <class 'pandas.core.frame.DataFrame'>
RangeIndex: 10000 entries, 0 to 9999
Data columns (total 11 columns):
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   score_credito        10000 non-null  int64  
 1   pais                 10000 non-null  object 
 2   sexo_biologico       10000 non-null  object 
 3   edad                10000 non-null  int64  
 4   años_de_cliente      10000 non-null  int64  
 5   saldo                10000 non-null  float64
 6   servicios_adquiridos  10000 non-null  int64  
 7   tiene_tarjeta_credito   10000 non-null  object 
 8   miembro_activo         10000 non-null  object 
 9   salario_estimado     10000 non-null  float64
 10  churn                10000 non-null  object 
dtypes: float64(2), int64(4), object(5)
memory usage: 859.5+ KB '''

import plotly.express as px

px.histogram(datos, x = 'churn', text_auto = True)
px.histogram(datos, x = 'pais', text_auto = True, color = 'churn', barmode = 'group') #grafico de la columna pais
px.histogram(datos, x = 'sexo_biologico', text_auto = True, color = 'churn', barmode = 'group') #grafico de la columna sexo_biologico
px.histogram(datos, x = 'tiene_tarjeta_credito', text_auto = True, color = 'churn', barmode = 'group')# grafico de la columna tiene_tarjeta_credito
px.histogram(datos, x = 'miembro_activo', text_auto = True, color = 'churn', barmode = 'group') #grafico de la columna miembro_activo
px.box(datos, x = 'score_credito', color = 'churn') #grafico de la columna score_credito
px.box(datos, x = 'edad', color = 'churn') #grafico de la columna edad
px.box(datos, x = 'años_de_cliente', color = 'churn') #grafico de la columna años_de_cliente
px.box(datos, x = 'saldo', color = 'churn') #grafico de la columna saldo
px.box(datos, x = 'servicios_adquiridos', color = 'churn') #grafico de la columna servicios_adquiridos
px.box(datos, x = 'salario_estimado', color = 'churn') #grafico de la columna salario_estimado

'''
1 - Para hacer la separación de los datos entre variables explicativas y variable objetivo, necesitamos detectar cuáles columnas formarán parte de cada uno de estos conjuntos de datos. La variable objetivo es la columna churn. Las variables explicativas son las demás columnas, que explicarán el comportamiento de la variable objetivo.

Para almacenar la columna churn en y, podemos usar la selección de columnas de la biblioteca pandas. Lo mismo se puede hacer para seleccionar las columnas en x, sin embargo, de forma más simple, podemos usar el método drop para eliminar la columna churn y almacenar todo lo demás en x:

x = datos.drop('churn', axis = 1)
y = datos['churn'] 

¡Listo! Ahora tenemos la separación de las variables para indicar al modelo cuál es la respuesta y cuáles son las columnas que explican esa respuesta.

2 - Para realizar la transformación de las variables categóricas, primero necesitamos identificar cuáles son las columnas que requieren este tipo de transformación.

En la base de datos de churn, las columnas categóricas son:

pais: 3 categorías
sexo_biologico: 2 categorías
tiene_tarjeta_credito: 2 categorías
miembro_activo: 2 categorías
La columna país necesita pasar por una transformación para que al final se generen 3 columnas, una para cada país distinto. Cada columna indicará con 0 si el registro no es del respectivo país y 1 si lo es. Como las demás columnas solo necesitan cambiar los valores de las dos categorías a 0 y 1, podemos usar el parámetro drop = 'if_binary' para que al final del proceso se elimine una de las columnas generadas y se mantenga solo una.

Vamos a importar las funciones y usar el método make_column_transformer para indicar cuáles son las columnas que necesitan el tratamiento de datos y cuáles no:

from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder 
one_hot = make_column_transformer((
    OneHotEncoder(drop = 'if_binary'),
    ['sexo_biologico','pais', 'tiene_tarjeta_credito', 'miembro_activo']
),
    remainder = 'passthrough',
    sparse_threshold=0)

Para visualizar mejor los datos transformados, podemos almacenar el nombre de las columnas originales para obtener el nombre de las columnas después de la transformación. Luego de esto, usaremos el método fit_transform para realizar la transformación y visualizar los datos en un DataFrame:

columnas = x.columns 
x = one_hot.fit_transform(x)
one_hot.get_feature_names_out(columnas)
Resultado en el nombre de las columnas transformadas:
array(['onehotencoder__sexo_biologico_Mujer',
       'onehotencoder__pais_Alemania', 'onehotencoder__pais_España',
       'onehotencoder__pais_Francia',
       'onehotencoder__tiene_tarjeta_credito_sim',
       'onehotencoder__miembro_activo_si', 'remainder__score_credito',
       'remainder__edad', 'remainder__años_de_cliente',
       'remainder__saldo', 'remainder__servicios_adquiridos',
       'remainder__salario_estimado'], dtype=object)

pd.DataFrame(x, columns = one_hot.get_feature_names_out(columnas))

Resultado de las 5 primeras filas del DataFrame:
onehot encoder__sexo_biologico_Mujer  onehotencoder__pais_Alemania  \
0                                   0.0                           0.0
1                                   0.0                           0.0

3 - Después de transformar las variables explicativas, queda transformar la variable objetivo. Vamos a utilizar el LabelEncoder, que es el método recomendado para esta tarea. El proceso para utilizar este método es bastante simple. Primero tenemos que importar la función, luego inicializar en una variable y, por último, usar el método fit_transform en los datos y:

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

1 - Para hacer la normalización de los datos, vamos a utilizar el método MinMaxScaler. Primero, importamos la función y luego hacemos la transformación de los datos de entrenamiento de las variables explicativas, almacenando en una nueva variable x_entrenamiento_normalizado:

from sklearn.preprocessing import MinMaxScaler
normalizacion = MinMaxScaler()
x_entrenamiento_normalizado = normalizacion.fit_transform(x_entrenamiento)

Si queremos visualizar el resultado de la transformación, podemos utilizar el método pd.DataFrame para generar una tabla con los datos:
pd.DataFrame(x_entrenamiento_normalizado)

2 - Con los datos normalizados, podemos generar el modelo de vecinos más cercanos con el KNeighborsClassifier a partir de los datos de entrenamiento normalizados. Primero, importamos la función:
from sklearn.neighbors import KNeighborsClassifier

Ahora inicializamos el modelo y hacemos el ajuste con los datos de entrenamiento normalizados. Por último, podemos normalizar los datos de prueba y usar el método score para evaluar el rendimiento:
knn = KNeighborsClassifier()
knn.fit(x_entrenamiento_normalizado, y_entrenamiento)

x_test_normalizado = normalizacion.transform(x_test)

knn.score(x_test_normalizado, y_test)
El resultado obtenido fue el siguiente: 0.8172

3 - Para comparar los resultados de los modelos creados en los desafíos, vamos a usar el método score con los datos de prueba, para tener un comparactivo en la misma celda:
print(f'Exactitud Dummy: {dummy.score(x_test, y_test)}')
print(f'Exactitud Árbol: {arbol.score(x_test, y_test)}')
print(f'Exactitud KNN: {knn.score(x_test_normalizado, y_test)}') 

que otorga como resultado:
Exactitud Dummy: 0.7964
Exactitud Árbol: 0.8464
Exactitud KNN: 0.8172

El modelo de árbol de decisión, en este caso, se desempeñó mejor y, por lo tanto, será el modelo seleccionado. Vamos a utilizar pickle para almacenar el modelo de árbol y también el modelo OneHotEncoder, que realiza las transformaciones de las variables categóricas. Primero, debemos importar la biblioteca pickle y luego hacer la exportación de los archivos:
import pickle 
El OneHotEncoder será almacenado en el archivo modelo_onehotenc.pkl:
with open('modelo_onehotenc.pkl', 'wb') as archivo:
    pickle.dump(one_hot, archivo)

 El DecisionTreeClassifier será almacenado en el archivo modelo_arbol.pkl:
    with open('modelo_arbol.pkl', 'wb') as archivo:
    pickle.dump(arbol, archivo)

4 - Para hacer la predicción de un nuevo dato, primero vamos a crear una variable que almacene la información de este registro, que fue proporcionado en el enunciado del desafío:

nuevo_dato = pd.DataFrame({
    'score_credito': [850],
    'pais':['Francia'],
    'sexo_biologico':['Hombre'],
    'edad': [27],
    'anos_de_cliente': [3],
    'saldo': [56000],
    'servicios_adquiridos': [1],
    'tiene_tarjeta_credito': [1],
    'miembro _activo': [1],
    'salario_estimado': [85270.00]
}) 

Ahora, podemos hacer la lectura de los archivos pickle usando la función pd.read_pickle de pandas:

modelo_one_hot = pd.read_pickle('/content/modelo_onehotenc.pkl') #entre parentesis se coloca la ruta del archivo pickle
modelo_arbol = pd.read_pickle('/content/modelo_arbol.pkl') #entre parentesis se coloca la ruta del archivo pickle

Por último, podemos usar el modelo_one_hot para hacer la transformación del nuevo dato y, a continuación, usar ese resultado para hacer la predicción con el modelo_arbol:

nuevo_dato = modelo_one_hot.transform(nuevo_dato)
modelo_arbol.predict(nuevo_dato) 

El resultado obtenido fue el siguiente: array([0])
Esto indica que la predicción fue el valor 0, que indica que no habrá churn. Por lo tanto, el cliente no dejará de utilizar los servicios.

Recuerda que resolver desafíos y encontrar soluciones es una parte fundamental de cualquier jornada de aprendizaje, especialmente en Machine Learning. Por lo tanto, durante la resolución de problemas, busca explorar las diversas posibilidades. Enfrenta cada desafío como una oportunidad para alcanzar el desarrollo práctico de tus conocimientos en datos.


1 - Para la construcción de un modelo de machine learning se necesitan datos. Como tarea inicial, realiza la lectura de la base de datos de diabetes y divide los datos en variables explicativas y variable objetivo (x e y). La variable objetivo es la columna que quieres clasificar, que contiene la información de si el paciente tiene o no diabetes. Las variables explicativas son todas las columnas excepto la de diabetes. La separación de los datos se puede hacer con la selección de columnas con pandas.

2 - Una etapa muy importante en proyectos de clasificación es la validación de los modelos, para identificar si hay una generalización del modelo para datos nuevos. Realiza la división de los datos entre entrenamiento, validación y prueba. Utiliza el 5% de los datos para prueba y con el resto, deja el 25% para validación. En el momento de la separación, usa el parámetro stratify a partir de la variable objetivo para mantener la proporción de los datos.

3 - La etapa de modelado de datos consiste en utilizar un algoritmo capaz de identificar patrones en los datos y clasificar los valores. A partir del modelo es posible extraer una tasa de acierto para entender su desempeño. Crea 2 modelos utilizando los algoritmos DecisionTreeClassifier y RandomForestClassifier y evalúa la precisión de entrenamiento y prueba, eligiendo el valor 3 para el parámetro max_depth del algoritmo DecisionTreeClassifier y el valor 2 para el max_depth del algoritmo RandomForestClassifier, para que los modelos no se especialicen demasiado en el patrón de los datos de entrenamiento.

4 - La tasa de acierto generalmente no proporciona información suficiente para entender el comportamiento del modelo. La matriz de confusión es una herramienta más completa, capaz de proporcionar los aciertos y errores del modelo para cada clase. Construye una matriz de confusión para cada uno de los modelos para evaluar el desempeño de la predicción. Para construir la matriz, usa el método predict para generar las predicciones de los valores y comparar con los valores reales de la base de datos.

luego de explorar los datos, La base de datos tiene solo 394 filas y 6 columnas. Podemos observar 6 columnas de datos: glicemia, presion_sanguinea, pliegue_cutaneo_triceps, insulina, imc y diabetes. La clasificación del modelo debe hacerse para la columna de diabetes, que presenta valores de 0 para ausencia de diabetes y 1 para presencia de diabetes, por lo tanto, esta es la variable objetivo y el resto son variables explicativas. Podemos realizar la división de los datos usando el código:
x = datos.drop('diabetes', axis = 1)
y = datos['diabetes']

2 - Para realizar la división de datos entre entrenamiento, validación y prueba, podemos usar el método train_test_split de la biblioteca Scikit-Learn. Primero debemos importar la función con el código:
from sklearn.model_selection import train_test_split
La primera división se hará de los datos de prueba y luego con el resto se hará una nueva división entre entrenamiento y validación, usando el parámetro stratify = y para mantener la proporción de los datos de la variable objetivo entre los conjuntos. Dado que la base de datos tiene pocos registros, solo se dividirá el 5% de los datos para prueba para que haya una cantidad mayor de registros en la base de datos de entrenamiento:

x, x_prueba, y, y_prueba = train_test_split(x, y, stratify = y, test_size = 0.05, random_state = 5)
x_entrenamiento, x_val, y_entrenamiento, y_val = train_test_split(x, y, stratify = y, random_state = 5)

3 - La primera etapa para la creación de los modelos será la importación de los algoritmos DecisionTreeClassifier y RandomForestClassifier, usando el código:
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

Después de la importación de los algoritmos, podemos instanciar los modelos y almacenarlos en variables, aquí se eligieron los valores de max_depth = 3 para el DecisionTree y max_depth = 2 para el RandomForest:

arbol = DecisionTreeClassifier(max_depth = 3)
random_forest = RandomForestClassifier(max_depth = 2)

Para hacer el ajuste de los modelos podemos usar el método fit() y para evaluar la tasa de acierto, el método score():

arbol.fit(x_entrenamiento, y_entrenamiento)
print(f'Precisión de entrenamiento: {arbol.score(x_entrenamiento, y_entrenamiento)}')
print(f'Precisión de prueba: {arbol.score(x_val, y_val)}')

random_forest.fit(x_entrenamiento, y_entrenamiento)
print(f'Precisión de entrenamiento: {random_forest.score(x_entrenamiento, y_entrenamiento)}')
print(f'Precisión de prueba: {random_forest.score(x_val, y_val)}')

4 - Para generar la matriz de confusión, primero es necesario importar la función ConfusionMatrixDisplay, usando el código:

from sklearn.metrics import ConfusionMatrixDisplay

Hecho esto, basta con utilizar el método predict() para hacer la predicción de datos con los modelos y luego utilizar los valores reales y previstos en el método from_predictions() de la matriz de confusión:

prediccion_arbol = arbol.predict(x_val)
ConfusionMatrixDisplay.from_predictions(y_val, prediccion_arbol);

prediccion_rf = random_forest.predict(x_val)
ConfusionMatrixDisplay.from_predictions(y_val, prediccion_rf);
'''