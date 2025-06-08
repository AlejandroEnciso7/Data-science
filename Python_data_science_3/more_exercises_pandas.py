'''Calcular el promedio de habitaciones por departamento.

Verificar cuántas colonias únicas existen en nuestra base de datos.

Analizar qué colonias tienen el promedio de alquiler más alto.

Crear un gráfico de barras horizontales que muestre las 5 colonias con los promedios de alquiler más altos.

url_alumnos = https://gist.githubusercontent.com/ahcamachod/807a2c1cf6c19108b2b701ea1791ab45/raw/fb84f8b2d8917a89de26679eccdbc8f9c1d2e933/alumnos.csv

Este archivo es el mismo que se utilizó para resolver los desafíos de las aulas 1 y 3 y contiene datos de estudiantes de un curso superior. Con base en esto, resolvamos los problemas propuestos a continuación utilizando los conocimientos adquiridos hasta ahora.

Los estudiantes participaron en una actividad extracurricular y ganaron puntos extras. Estos puntos extras corresponden al 40% de su nota actual. Por lo tanto, crea una columna llamada "Puntos_extras" que contenga los puntos extras de cada estudiante, es decir, el 40% de su nota actual.

Crea otra columna llamada "Notas_finales" que contenga las notas de cada estudiante sumadas con los puntos extras.

Dado que hubo una puntuación extra, algunos estudiantes que no habían sido aprobados antes pueden haber sido aprobados ahora. En función de esto, crea una columna llamada "Aprobado_final" con los siguientes valores:

True: si el estudiante está aprobado (la nota final debe ser mayor o igual a 7.0).
False: si el estudiante está reprobado (la nota final debe ser menor que 7.0).
Realiza una selección y verifica qué estudiantes no habían sido aprobados anteriormente, pero ahora fueron aprobados después de sumar los puntos extras.

R:= https://app.aluracursos.com/course/pandas-conociendo-biblioteca/task/87042
'''