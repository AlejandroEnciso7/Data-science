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
'''