
""" 4 - Desarrolla un programa que lea un conjunto indefinido de temperaturas en grados Celsius y calcule su promedio. 
La lectura debe detenerse al ingresar el valor -273°C.

5 - Escribe un programa que calcule el factorial de un número entero proporcionado por el usuario. 
Recuerda que el factorial de un número entero es el producto de ese número por todos sus antecesores hasta llegar al número 1. 
Por ejemplo, el factorial de 5 es 5 x 4 x 3 x 2 x 1 = 120.

7 - Los números primos tienen diversas aplicaciones en Ciencia de Datos, como en criptografía y seguridad. 
Un número primo es aquel que es divisible solo por sí mismo y por 1. Por lo tanto, crea un programa que solicite un número entero y determine si es un número primo o no.

8 - Vamos a comprender la distribución de edades de los pensionistas de una empresa de seguros. 
Escribe un programa que lea las edades de una cantidad no informada de clientes y muestre la distribución en los intervalos [0-25], [26-50], [51-75] y [76-100]. 
La entrada de datos se detendrá al ingresar un número negativo.

9 - En una elección para la gerencia de una empresa con 20 empleados, hay cuatro candidatos.
 Escribe un programa que calcule al ganador de la elección. La votación se realizó de la siguiente manera:
Cada empleado votó por uno de los cuatro candidatos (representados por los números 1, 2, 3 y 4).
También se contaron los votos nulos (representados por el número 5) y los votos en blanco (representados por el número 6).
Al final de la votación, el programa debe mostrar el número total de votos para cada candidato, los votos nulos y los votos en blanco.
 Además, debe calcular y mostrar el porcentaje de votos nulos con respecto al total de votos y el porcentaje de votos en blanco con respecto al total de votos.

7 - Para un estudio sobre la multiplicación de bacterias en una colonia, se recopiló el número de bacterias multiplicadas por día y se puede observar a continuación: 
[1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Con estos valores, crea un código que genere una lista que contenga el porcentaje de crecimiento de bacterias por día, 
comparando el número de bacterias en cada día con el número de bacterias del día anterior. Sugerencia: para calcular el porcentaje de crecimiento,
 utiliza la siguiente ecuación: 100 * (muestra_actual - muestra_anterior) / muestra_anterior.

8 - Para una selección de productos alimenticios, debemos separar el conjunto de IDs proporcionados por números enteros, 
sabiendo que los productos con ID par son dulces y los que tienen ID impar son amargos. Crea un código que recoja 10 IDs. 
Luego, calcula y muestra la cantidad de productos dulces y amargos.

9 - Desarrolla un programa que informe la puntuación de un estudiante de acuerdo con sus respuestas. 
Debe pedir la respuesta del estudiante para cada pregunta y verificar si la respuesta coincide con el resultado. Cada pregunta vale un punto y hay opciones A, B, C o D. 

Resultado del examen:
01 - D
02 - A
03 - C
04 - B
05 - A
06 - D
07 - C
08 - C
09 - A
10 - B

10 - Un instituto de meteorología desea realizar un estudio de la temperatura media de cada mes del año.
 Para ello, debes crear un código que recoja y almacene esas temperaturas medias en una lista. 
 Luego, calcula el promedio anual de las temperaturas y muestra todas las temperaturas por encima del promedio anual y en qué mes ocurrieron,
   mostrando los meses por su nombre (Enero, Febrero, etc.).

11 - Una empresa de comercio electrónico está interesada en analizar las ventas de sus productos. Los datos de ventas se han almacenado en un diccionario:
{'Producto A': 300, 'Producto B': 80, 'Producto C': 60, 'Producto D': 200, 'Producto E': 250, 'Producto F': 30}
Escribe un código que calcule el total de ventas y el producto más vendido.

12 - Se realizó una encuesta de mercado para decidir cuál diseño de marca infantil es más atractivo para los niños. Los votos de la encuesta se pueden ver a continuación:
Tabla de votos de la marca
Diseño 1 - 1334 votos
Diseño 2 - 982 votos
Diseño 3 - 1751 votos
Diseño 4 - 210 votos
Diseño 5 - 1811 votos

Adapta los datos proporcionados a una estructura de diccionario. A partir de ello, informa el diseño ganador y el porcentaje de votos recibidos.

13 - Los empleados de un departamento de tu empresa recibirán una bonificación del 10% de su salario debido a un excelente rendimiento del equipo.
 El departamento de finanzas ha solicitado tu ayuda para verificar las consecuencias financieras de esta bonificación en los recursos. 
 Se te ha enviado una lista con los salarios que recibirán la bonificación: [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903].
 La bonificación de cada empleado no puede ser inferior a 200. En el código, convierte cada uno de los salarios en claves de un diccionario y 
 la bonificación de cada salario en el valor correspondiente.
 Luego, informa el gasto total en bonificaciones, cuántos empleados recibieron la bonificación mínima y cuál fue el valor más alto de la bonificación proporcionada.

14 - Un equipo de científicos de datos está estudiando la diversidad biológica en un bosque.
 El equipo recopiló información sobre el número de especies de plantas y animales en cada área del bosque y almacenó estos datos en un diccionario. 
 En él, la clave describe el área de los datos y los valores en las listas corresponden a las especies de plantas y animales en esas áreas, respectivamente.
 {'Área Norte': [2819, 7236], 'Área Leste': [1440, 9492], 'Área Sul': [5969, 7496], 'Área Oeste': [14446, 49688], 'Área Centro': [22558, 45148]}

 Escribe un código para calcular el promedio de especies por área e identificar el área con la mayor diversidad biológica. 
 Sugerencia: utiliza las funciones incorporadas sum() y len().

15 - El departamento de Recursos Humanos de tu empresa te pidió ayuda para analizar las edades de los colaboradores de 4 sectores de la empresa.
 Para ello, te proporcionaron los siguientes datos:

 {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

 Dado que cada sector tiene 10 colaboradores, construye un código que calcule la media de edad de cada sector,
   la edad media general entre todos los sectores y cuántas personas están por encima de la edad media general.

   Respuestas: https://app.aluracursos.com/course/python-data-science-primeros-pasos/task/86368 
   

https://app.aluracursos.com/course/python-data-science-trabajar-funciones-estructuras-datos-excepciones/task/86874

1 - Crea un código para imprimir la suma de los elementos de cada una de las listas contenidas en la siguiente lista:
lista_de_listas = [[4, 6, 5, 9], [1, 0, 7, 2], [3, 4, 1, 8]]

2 - Crea un código para generar una lista que almacene el tercer elemento de cada tupla contenida en la siguiente lista de tuplas:
lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

3 - A partir de la lista: lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo'], crea un código para generar una lista de tuplas en la que cada tupla tenga el primer elemento como la posición del nombre en la lista original y el segundo elemento siendo el propio nombre.

4 - Crea una lista usando la comprensión de listas (list comprehension) que almacene solo el valor numérico de cada tupla en caso de que el primer elemento sea 'Apartamento', a partir de la siguiente lista de tuplas:

alquiler = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

5 - Crea un diccionario usando la comprensión de diccionarios (dict comprehension) en el que las claves estén en la lista meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'] y los valores estén en gasto = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360].

6 - Una tienda tiene una base de datos con la información de venta de cada representante y de cada año y necesita filtrar solo los datos del año 2022 con ventas mayores a 6000. La tienda proporcionó una muestra con solo las columnas de los años y los valores de venta para que puedas ayudar a realizar la filtración de los datos a través de un código:

ventas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]

Crea una lista usando la comprensión de listas para filtrar los valores de 2022 que sean mayores a 6000.

7 - Una clínica analiza datos de pacientes y almacena el valor numérico de la glucosa en una base de datos y le gustaría etiquetar los datos de la siguiente manera:

Glucosa igual o inferior a 70: 'Hipoglicemia'
Glucosa entre 70 y 99: 'Normal'
Glucosa entre 100 y 125: 'Alterada'
Glucosa superior a 125: 'Diabetes'
La clínica proporcionó parte de los valores y tu tarea es crear una lista de tuplas usando la comprensión de listas que contenga la etiqueta y el valor de la glucemia en cada tupla.

glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

8 - Un comercio electrónico tiene información de id de venta, cantidad vendida y precio del producto divididos en las siguientes listas:

id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cantidad = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
precio = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

La plataforma necesita estructurar estos datos en una tabla que contenga el valor total de la venta, que se obtiene multiplicando la cantidad por el precio unitario. Además, la tabla debe contener un encabezado indicando las columnas: 'id', 'cantidad', 'precio' y 'total'.
Crea una lista de tuplas en la que cada tupla tenga id, cantidad, precio y valor total, siendo la primera tupla el encabezado de la tabla.

9 - Una empresa tiene sucursales distribuidas en los estados de la región Sudeste de Brasil. En una de las tablas de registro de las sucursales, hay una columna que contiene la información de a qué estado pertenece: estados =['CMX', 'OAX', 'PUE', 'PUE', 'CMX', 'PUE', 'OAX', 'OAX', 'OAX', 'CMX', 'CMX', 'PUE', 'OAX', 'CMX', 'VER', 'PUE', 'VER', 'CMX', 'PUE', 'CMX', 'OAX', 'CMX', 'PUE'].
La empresa siempre está abriendo nuevas sucursales, por lo que la tabla está constantemente recibiendo nuevos registros y al gerente le gustaría tener la información actualizada de la cantidad de sucursales en cada estado.
A partir de la columna con la información de los estados, crea un diccionario utilizando la comprensión de diccionarios (dict comprehension) con la clave siendo el nombre de un estado y el valor siendo la cantidad de veces que aparece el estado en la lista.
Consejo: Puedes hacer un paso intermedio para generar una lista de listas en la que cada una de las listas tenga el nombre de solo un estado con valores repetidos.

10 - En esa misma tabla de registro de sucursales, hay una columna con la información de la cantidad de personas empleadas y el gerente quisiera tener un agrupamiento de la suma de esas personas para cada estado. Las informaciones contenidas en la tabla son:

 empleados = [('CMX', 16), ('OAX', 8), ('PUE', 9), ('PUE', 6), ('CMX', 10), ('PUE', 4), ('OAX',9),  ('OAX', 7), ('OAX', 12), ('CMX', 7), ('CMX', 11), ('PUE',8), ('OAX',8), ('CMX',9), ('VER', 13), ('PUE', 5),  ('VER', 9), ('CMX', 12), ('PUE', 10), ('CMX', 7), ('OAX', 14), ('CMX', 10), ('PUE', 12)]

 A partir de la lista de tuplas, crea un diccionario en el que las claves son los nombres de los estados únicos y los valores son las listas con el número de empleados referentes al estado. También crea un diccionario en el que las claves son los nombres de los estados y los valores son la suma de empleados por estado.
 


   """