
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

   Respuestas: https://app.aluracursos.com/course/python-data-science-primeros-pasos/task/86368 """