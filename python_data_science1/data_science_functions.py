import math
import random
def nota_admision():    
    nota_admision = float(input("introduce el año de admision: "))
    print(f' la notade admision fue {nota_admision}') #esto imprime la variable entre llaves, importante poner la "f" al comienzo

    nombre = str(input('cual es tu nombre?'))
    edad = int(input('cual es tu edad?'))
    print(f'hola, {nombre}, y tengo {edad} años')

    num1 =int(input('introduce el primer numero que deseas sumar: '))
    num2 =int(input('introduce el segundo numero que deseas sumar: '))
    suma = num1 + num2
    print(f'{num1} + {num2} = {suma}')

    frase = str(input('escribe una frase: '))
    print(frase.upper()) #esto convierte la frase a mayusculas
    print(frase.lower().strip()) #para ejecutar varias funciones sobre la misma variable solo se coloca '.funcion()' luego de la primera funcion y asi sucesivamente

    #CONDICIONALES

    if 2<7:
        print('la condicion es verdadera')
    elif 2>7:
        print('la condicion es falsa')
    else:
        print('fin del programa')



def num_in_list(lista):
    numero_1= 2
    numero_2 = 8
    if numero_1 in lista:
        print(f'el numero {numero_1} esta en la lista')
    else:
        print(f'el numero {numero_1} no esta en la lista')

    if numero_2 in lista:
        print(f'el numero {numero_2} esta en la lista')
    else:
        print(f'el numero {numero_2} no esta en la lista')

def get_list(n):
    lista = []
    for i in range(n):
        valor = int(input(f'Introduce el valor {i+1}: '))
        lista.append(valor)
    return lista

def bigger_number():
    num_1=int(input('introduce el primer numero: '))
    num_2=int(input('introduce el segundo numero: '))
    if num_1 > num_2:
        print(f'el numero {num_1} es el mayor')
    elif num_1 == num_2:
        print(f'los numeros son iguales')
    else:
        print(f'el numero {num_2} es el mayor')

def porcentaje_crecimiento():
    porcentaje_base = float(input('introduce el porcentaje base: '))
    porcentaje_final = float(input('introduce el porcentaje final: '))
    if porcentaje_base < porcentaje_final:
        print(f'el porcentaje crecio {round(porcentaje_final - porcentaje_base, 2)} %')
    elif porcentaje_base == porcentaje_final:
        print(f'el porcentaje no crecio')
    else: 
        print(f'el procentaje disminuyo {round(porcentaje_base - porcentaje_final,2)}%')   

def tipo_letra():
    letra = str(input('introduce una letra: '))
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print(f'{letra} es una vocal')
    else:
        print(f'{letra} es una consonante')

def valor_auto():
    precios = {}  # Diccionario para almacenar los precios
    for i in range(1, 4):
        precio = float(input(f"Ingrese el precio del año {i}: "))
        precios[f"Año {i}"] = precio
    precio_maximo = max(precios.values())
    precio_minimo = min(precios.values())
    año_maximo = [año for año, precio in precios.items() if precio == precio_maximo][0]
    año_minimo = [año for año, precio in precios.items() if precio == precio_minimo][0]

    print(f"El precio más alto es {precio_maximo}, que pertenece al {año_maximo}.")
    print(f"El precio más bajo es {precio_minimo}, que pertenece al {año_minimo}.")
    print(f'el precio promedio es {round(sum(precios.values())/len(precios),2)}')

#while - for
#contador = 1
#while contador <=5:
    #print(f'contador: {contador}')
    #contador += 1

#precio = 2.00
#precio += 3  al hacerlo con += se suma el valor a la variable precio y se le asigna el nuevo valor a la variable precio
#print(precio)

def contador_nota():
    contador = 1
    while contador <= 3:
        nota_1 = float(input('digita laprimera nota: '))
        nota_2 = float(input('digita la segunda nota: '))
        print(f'elpromedio del estudiante es {(nota_1 + nota_2)/2}')
        contador +=1

# for 'elemento' in 'grupo':
#     codigo a ejecutar

def ejemplo_for():
    for i in range (1,11): #la funcion range genera una lista de numeros desde el primer numero hasta el segundo numero -1
        print(i)

#for i in range(1, 6):
 #   if i == 4:
  #      continue   continue funciona como un "skip" y salta ese valor indicado en el condicional y empieza con la siguiente parte de la iteracion, en este caso imprime 1,2,3,5
   # print(i)

#for i in range(1, 6):
 #   if i == 4:
  #      break    break termina el ciclo en el momento que se le indique con el condicional y no imprime el 4 ni el 5, solo imprime 1,2,3
   # print(i)
def numeros_enteros_imp():
    num_1 = int(input('escribe el primer numero: '))
    num_2 = int(input('escribe el segundo numero: '))
    for i in range(num_1, num_2 +1):
        print(i)

def colonia_bacterias():
    bacteria_a = 4
    bacteria_b = 10
    crecimiento_a = 0.03
    crecimiento_b =0.015
    dias = 0
    while bacteria_a < bacteria_b:
        bacteria_a *= 1 + crecimiento_a
        bacteria_b *= 1 + crecimiento_b
        dias += 1
        print(f'bacteria A: alcanza a bacteria B en {dias} dias')

def calificacion_empresa():
    for i in range (15):
        calificacion = float(input(f'ingresa la nota del usuario {i}:'))
        while (calificacion < 0) or (calificacion > 5):
            nota = float(input(f'nota no valida, intente nuevamente'))
          #  if (calificacion >= 0) and (calificacion <= 5):
           #     break
    print('nota validadas')

def tabla_multiplicar():
    num = int(input('introduce el numero que deseas multiplicar: '))
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')

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
 Además, debe calcular y mostrar el porcentaje de votos nulos con respecto al total de votos y el porcentaje de votos en blanco con respecto al total de votos."""

lista = [1, 2 ,3 ,4 ,5]

def lista_iterar():
    for elemento in lista:
        print(elemento) #imprime cada elemento de la lista

#lista [2] = 10.0 #esto cambia el valor de la lista en la posicion 2 por el nuevo valor 10.0

promedio = (lista[1] + lista[2] + lista[3]) / 3 #esto suma los valores de la lista en las posiciones 1,2 y 3 y divide el resultado entre 3

#split() #esto separa una cadena de texto en partes y las coloca en una lista, por ejemplo: 'hola mundo' se convierte en ['hola', 'mundo'], entre los parentesis se puede colocar el separador que se desea usar, por defecto es un espacio
#join() #esto une una lista de cadenas de texto en una sola cadena, por ejemplo: ['hola', 'mundo'] se convierte en 'hola mundo', entre los parentesis se puede colocar el separador que se desea usar, por defecto es un espacio

def mezcla():
    mezclas = ['Pinturas: rojo, azul y amarillo',
                'Verde: mezcla de azul y amarillo',
                'Naranja: mezcla de rojo y amarillo',
                'Morado: mezcla de rojo y azul']
    unificador = '. '
    cadena_mezclas = unificador.join(mezclas)
    print(cadena_mezclas)

#len() #esto cuenta el numero de elementos de una lista o cadena de texto, por ejemplo: len(['hola', 'mundo']) = 2, len('hola mundo') = 10
#slice() #esto corta una lista o cadena de texto en partes, por ejemplo: ['hola', 'mundo'][1:3] = ['mundo'], 'hola mundo'[1:3] = 'ol', 
# los corchetes excluyen el ultimo valor, por lo que si se quiere incluir el 3 se debe colocar [1:4]
# .extend() #esto une dos listas, por ejemplo: lista1 = [1,2,3] y lista2 = [4,5,6], al hacer lista1.extend(lista2) la lista1 se convierte en [1,2,3,4,5,6]
# .remove() #esto elimina un elemento de una lista, por ejemplo: lista = [1,2,3], al hacer lista.remove(2) la lista se convierte en [1,3]

# insert(), que permite insertar un elemento en una posición específica de la lista. La sintaxis es lista.insert(indice, elemento), 
# donde "lista" es la lista que recibirá el nuevo elemento, "indice" es la posición donde se insertará el nuevo elemento y "elemento" es el nuevo elemento que se insertará.

razas_de_perros = ['Labrador Retriever',
                       'Bulldog Francés',
                       'Pastor Alemán',
                       'Poodle']

def razas_perros():
    # Crear una lista de razas de perros
    razas_de_perros = ['Labrador Retriever',
                       'Bulldog Francés',
                       'Pastor Alemán',
                       'Poodle']

    # Insertar un nuevo elemento con .insert() en la posición 1
    razas_de_perros.insert(1, 'Golden Retriever')

    # Imprimir la lista actualizada
    print(razas_de_perros)
# index() devuelve el índice de un elemento específico en la lista. Para hacerlo, especificamos el elemento entre paréntesis. 
# Para encontrar el índice de la raza "Pastor Alemán" en la lista, hacemos lo siguiente:

razas_de_perros.index('Pastor Alemán') # Esto devolverá el índice de la raza "Pastor Alemán" en la lista, que es 3.

# .pop() elimina el elemento en una posición específica de la lista y lo devuelve como salida al ejecutar el método. 
# Solo necesitamos especificar, entre paréntesis, el índice del elemento que deseamos eliminar, y se eliminará de la lista. 
# razas_de_perros.pop(1) elminara el primer elemento de la lista, en este caso 'golden retriever'
# .sort() ordena los elementos de la lista en orden ascendente o descendente. Si son palabras, el orden se basa en el orden alfabético

def razas_perro_orden():
    razas_de_perros.sort()
    print(razas_perros)

# DICCIONARIOS
# un diccionario es una estructura de datos que almacena pares de clave-valor.
# Las claves son únicas y se utilizan para acceder a los valores asociados.
# La sintaxis para crear un diccionario es la siguiente: nombre_diccionario = {'clave1': valor1, 'clave2': valor2, ...}
# Para acceder a un valor en un diccionario, utilizamos la clave entre corchetes. 
#por ejemplo: estudiante = {'nombre': 'Juan', 'edad': 25}
# Para acceder al nombre del estudiante, utilizamos "estudiante['nombre']", que devolverá 'Juan'.
# para modificar un valor en un diccionario, simplemente asignamos un nuevo valor a la clave correspondiente.
# Por ejemplo: estudiante['edad'] = 26 cambiará la edad del estudiante a 26.
# tambien se pueden agregar nuevos pares clave-valor al diccionario utilizando la sintaxis nombre_diccionario['nueva_clave'] = nuevo_valor.
# Por ejemplo: estudiante['ciudad'] = 'Madrid' agregará una nueva clave 'ciudad' con el valor 'Madrid' al diccionario.
# .pop() elimina un par clave-valor del diccionario y devuelve el valor asociado a la clave eliminada.
# Por ejemplo: estudiante.pop('edad') eliminará la clave 'edad' y devolverá el valor asociado a esa clave.
# .items() devuelve una lista de tuplas que representan los pares clave-valor en el diccionario.
# Por ejemplo: estudiante.items() devolverá [('nombre', 'Juan'), ('edad', 26), ('ciudad', 'Madrid')].
# .keys() devuelve una lista de las claves en el diccionario.
# Por ejemplo: estudiante.keys() devolverá ['nombre', 'edad', 'ciudad'].
# .values() devuelve una lista de los valores en el diccionario.
# Por ejemplo: estudiante.values() devolverá ['Juan', 26, 'Madrid'].

# tambien se puede iterar sobre un diccionario utilizando un bucle for.
# Por ejemplo:
estudiante = {'nombre': 'Juan', 'edad': 25}

for llave in estudiante:
    print(llave) # Esto imprimirá cada clave en el diccionario.

for llave, valor in estudiante.items():
    print(f'Llave: {llave}, Valor: {valor}') # Esto imprimirá cada par clave-valor en el diccionario.
# .clear() elimina todos los pares clave-valor del diccionario, dejándolo vacío.

tienda = {'nombres': ['televisión', 'celular', 'notebook', 'geladeira', 'estufa'],
          'precios': [2000, 1500, 3500, 4000, 1500]}

def diccionario_tienda(): # preguntar por que esto me imprime el dicionario de estudiante tambien y por que no me imprime los nombres de los productos
    tienda = {'nombres': ['televisión', 'celular', 'notebook', 'geladeira', 'estufa'],
          'precios': [2000, 1500, 3500, 4000, 1500]}
    for clave, elementos in tienda.items():
        print(f'Clave: {clave}\nElementos:')
    for dato in elementos:
        print(dato)

def papel_promedio():
    gastos_papel = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
    promedio = sum(gastos_papel) / len(gastos_papel)
    print(f'El promedio de gastos en papel es: {promedio}')

def porcentaje_papel():
    gastos_papel = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
    contador_3k = 0
    for i in gastos_papel:
        if i > 3000:
            contador_3k +=1
    porcentaje_3k = (contador_3k / len(gastos_papel)) * 100
    print(f'El porcentaje de gastos superiores a 3000 es: {porcentaje_3k}%')
    print(f'un total de {contador_3k} compras estuvieron por encima de 3000')

def lista_enteros_random():
    random_num=[]
    for i in range(5):
        random_num.append(round(random.random()*10))
    print(random_num)
    print(f'lista inversa: {random_num[::-1]}') #esto imprime la lista al reves, el [::-1] es un slice que indica 
    #que se quiere imprimir la lista desde el final hasta el principio
       
def numeros_primos():
    numero = int(input('ingresa un numero entero: '))
    lista_primos = []
    for num in range(2, numero): #se empieza desde 2 porque 1 no es primo, el loop recorre los numeros desde 2 hasta el numero ingresado -1
        primo = True # esto es un flag que indica si el numero es primo o no 
        for es_divisible in range(2, num): #aqui se va numero por numero probando si son divisibles por 0
            if num % es_divisible == 0: #si el residuo de la division es 0, significa que el numero no es primo
                primo = False
                break #si el numero no es primo, se sale del loop y se pasa al siguiente numero
        if primo:
            lista_primos.append(num)
    print(f'los numeros primos menores a {numero} son: {lista_primos}')

def fecha_valida():
        # Recopilamos la fecha
    dia = int(input('Ingrese el día: '))
    mes = int(input('Ingrese el mes: '))
    año = int(input('Ingrese el año: '))

    # Análisis de febrero
    if mes == 2:
    # Verificamos si es o no un año bisiesto
        if año % 4 == 0 and (año % 400 == 0 or año % 100 != 0):
            dias_febrero = 29
        else:
            dias_febrero = 28
        # Verificamos si el día ingresado coincide con el máximo de días de febrero
        if dia >= 1 and dia <= dias_febrero:
            print('Fecha válida')
        else:
            print('Fecha inválida')
        # Verificamos meses que terminan en 31 días
    elif mes in [1, 3, 5, 7, 8, 10, 12]:
        if dia >= 1 and dia <= 31:
            print('Fecha válida')
        else:
            print('Fecha inválida')
        # Verificamos meses que terminan en 30 días
    elif mes in [4, 6, 9, 11]:
        if dia >= 1 and dia <= 30:
            print('Fecha válida')
        else:
            print('Fecha inválida')
        # Si el mes no está entre 1 y 12
    else:
        print('Fecha invalida')