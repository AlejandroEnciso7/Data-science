
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, inspect, text, Error
import matplotlib.pyplot as plt

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
#archivo = 'nombre_archivo.xlsx'
# pd.read_excel(archivo)
#pd.ExcelFile(archivo).sheet_names # me muestra el nombre de las hojas del archivo excel
# pd.read_excel(archivo, sheet_name='Hoja1') # me permite leer una hoja especifica del archivo excel
# pd.read_excel(archivo), sheet_name'hoja1', usecols = 'A:C') # me permite leer un rango de columnas especificas de la hoja del archivo excel que le solicite

# LEER ARCHIVOS DE EXCEL ONLINE
# pd.read_excel('https://url_del_archivo.xlsx')
# es recomendable quital la parte del edit y utilizar al final '/gviz/tq' esto indica que es una hoja de excel de google y permite visualizar el archivo en google colab
# tambien tener enceunta el ID del archivo, ¿Y dónde encontramos ese id? En el propio link. Es todo lo que aparece entre d/ y /edit.
# Una vez hecho esto, podemos leer los datos pasando la variable url a la función read_csv:, datos = pd.read_csv(url)
# Para guardar los datos en formato CSV, basta con utilizar la función to_csv y, entre paréntesis, darle un nombre al archivo agregando el parámetro index=False para que no se agregue una nueva columna de índice:
#datos.to_csv('datos_emisiones_co2.csv', index=False)

# pd.read_json('nombre_archivo.json')
# df_normalizado = pd.json_normalize(nombre_archivo.json ['nombre_columna_donde_hay_anidacion']) # esto permite normalizar un archivo json y convertirlo en un dataframe de pandas,
# para cuadno el archivo tiene una estructura anidada dentro de si misma 

# Una forma común de acceder a las API es a través de la biblioteca requests. Para eso, también es necesario importar el módulo json:
# import requests
# import json

# se utiliza requests.get para obtener los datos de la API
# datos_frutas = requests.get('https://fruityvice.com/api/fruit/all')
# para visualizar los datos obtenidos de la API se utiliza json.loads(archivo/variable.text)
# resultado = json.loads(datos_frutas.text)
#para finalmente visualirzar un dataframe:
# pd.DataFrame(resultado)

# pd.read_html()
# Para leer la página, simplemente pase la dirección a la función read_html. Para que se muestre la primera tabla asignamos el primer elemento de la lista, con [0]:
# pd.read_html('https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_y_territorios_dependientes_por_poblaci%C3%B3n')[0] (esto es para cuadno la pagina tiene varias tablas)

# pd.read_sql()
# import sqlalchemy
# from sqlalchemy import create_engine, MetaData, Table, inspect, text
#para volverlo sql hay que volverlo un dataframe primero y luego usar .to_sql()
# datos.to_sql('nombre_tabla', engine,  index=False)
# query = 'SELECT * FROM nombre_tabla WHERE columna_categoria = "empleado"'
# empleados= pd.read_sql(sql=text(query), con= engine.connect()) # esto permite leer una consulta sql y convertirla en un dataframe de pandas
# empleados.to_sql('empleados', con=engine.connect(), index=False) # esto permite guardar el dataframe como una tabla en la base de datos
#pd.read_sql_table('empleados', con = engine.connect(), columns=['columnas_que_quiero_leer']) 


#los parametors de skiprows= x # permite saltar las primeras x filas del archivo
# Skipfooter= x # permite saltar las ultimas x filas del archivo

# IMPORTAR/GUARDAR ARCHIVOS
#datos_seleccion.to_csv('nombre_arhchivo.csv', index=False)

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

# BORRAR REGISTROS
datos.drop('columna_a_borrar', axis=1, inplace=True)
# esto borra la columna que le indico, axis=1 indica que es una columna, inplace=True indica que se hace el cambio en el mismo dataframe

# ACTUALIZAR de SQL
# query = 'DELETE/UPDATE/INSERT FROM nombre_tabla WHERE columna_categoria = "empleado"'
'''try:
    r_set = engine.connect().execute(text(query)) # uno se debe conectar al motor de la base de datos y ejecutar la consulta, la consulta siempre se utiliza con text(query)
EXCEPT SQLAlchemyError as e:
    print(f"Error al eliminar registros: {e}")
else:
    print("Registros eliminados correctamente.")

# INSERTAR INFORMACION
from sqlalchemy.exc import SQLAlchemyError
query = 'INSERT INTO clientes (ID_Cliente, Edad, Grado_estudio, Estado_civil, ' \
        'Tamaño_familia, Categoria_de_renta, Ocupacion, Años_empleado, ' \
        'Rendimiento_anual, Tiene_carro, Vivienda) ' \
        'VALUES (6850985, 33, "Doctorado", "Soltero", 1, "Empleado", "TI", ' \
        '2, 290000, 0, "Casa/Departamento propio")'

try:
  r_set=engine.connect().execute(text(query))
except SQLAlchemyError as e:
  print(e)
else:
  print("#Registros insertados: ",r_set.rowcount) '''

# SACAR DATOS DE LAS LISTAS DE LAS COLUMNAS (EXPLODE)
# datos.explode('columna_con_listas')
# esto permite sacar los datos de las listas de las columnas y convertirlos en filas, por ejemplo si tengo una columna con listas de frutas, cada fruta se convertira en una fila
# el indice sera el mismo por cada fila, es decir si se so explode en una columna conuna lista de [manzanas, narnajas] el indice para ambas filas sera el mismo
# datos.reset_index('columna_con_listas', inplace=True) # esto permite resetear el indice del dataframe, es decir que el indice sera 0,1,2,3... y no sera el mismo para cada fila

# datos['columna_nombre'].astype('str/int64/float64') # esto permite cambiar el tipo de dato de una columna, por ejemplo si quiero cambiar una columna de string a entero, o de entero a decimal
# esto solo muestra el resultado, si quiero cambiarlo puedo hacerlo asi:
# datos['columna_nombre'] = datos['columna_nombre'].astype('str/int64/float64') # esto cambia el tipo de dato de la columna en el dataframe
# datos['nombre_columna'].apply(lambda x: x.replace('caracter_a_reemplazar', 'nuevo_caracter')) # esto permite reemplazar un caracter por otro en una columna, 
# por ejemplo si quiero reemplazar un espacio por un guion bajo en una columna de nombres, o remover algun caracter en especifico 
# para revisar mas de una columna se hace asi:
# datos[['columna1', 'columna2']] 
# cuando es una unica columna se  llama una "serie" y cuando son varias columnas se llama un "dataframe", para poder realizar el metodo apply, se utiliza applymap
# datos[['columna1', 'columna2']].applymap(lambda x: x.replace('caracter_a_reemplazar', 'nuevo_caracter')) # esto permite reemplazar un caracter por otro en varias columnas, por ejemplo si quiero reemplazar un espacio por un guion bajo en una columna de nombres, o remover algun caracter en especifico

# REGEX
# permiten buscar patrones en los datos, por ejemplo si quiero buscar todos los numeros en una columna de texto, o todos los correos electronicos en una columna de texto
# datos['nombre_columna'].str.replace('[^a-zA-Z0-9\-\']', '', regex=True), el acento circunflejo (^) indica que se haran los cambios sobre todo xcepto lo que se encuentre alli
# esto permite reemplazar todos los caracteres que no sean letras, numeros, guiones o apostrofes por un espacio en blanco. '\-' significa que se esta buscando lo que va luego del '\'
# en este caso el guion, lo mismo sucede con el apóstrofe, que se busca con "\'".
# datos['nombre_columna'].str.replace('(?<!\w)-(?<!\w)', '', regex=True) esto permite eliminar los guiones que no esten precedidos ni seguidos por una letra o un numero 
# es decir que solo se eliminan los guiones que no esten en medio de una palabra
# tambien se puede crear asi: datos['nombre_columna'].str.replace('\{|}|\"', '', regex=True) 
# esto permite eliminar las llaves y las comillas de una columna de texto, por ejemplo si tengo un json en una columna y quiero eliminar las llaves y las comillas", 
# el '|' significa "o", por lo que se esta buscando las llaves o las comillas, y se reemplazan por un espacio en blanco.

# TOKENIZAR
#datos['columna_texto'].str.split() # esto permite dividir el texto en palabras, es decir que cada palabra se convierte en una fila
# split() lo convierte en una lista con las palabras dentro de la columna sobre la que  se aplica, dentro del () de split() 
# se puede poner el caracter que se quiere usar como separador, por ejemplo si quiero separar por comas, se pone split(',')

#pd.to_datetime(datos['columna_fecha'], format='%Y-%m-%d') # esto permite convertir una columna de texto en una columna de fechas
#  el formato es el que se usa en la columna de texto
# dt_data['columna_con_fechas'].dt.strftime('%Y-%m-%d') # esto permite convertir una columna de fechas en una columna de texto con el formato que se le indique

