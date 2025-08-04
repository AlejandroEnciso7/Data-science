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