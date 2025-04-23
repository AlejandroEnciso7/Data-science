import math
import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

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

def grafico_barras():
    plt.bar(['A', 'B', 'C'], [10, 20, 15]) #.bar toma como parametros el eje x y el eje y, en este caso las letras son el eje "x" y los numeros son el eje "y"
    plt.title('Gráfico de Barras')

def grafico_estudiantes():
    estudiantes = ['Juan', 'María', 'Pedro']
    estudiante = random.choice(estudiantes) #esto elige un elemento aleatorio de la lista estudiantes

def random_number():
    lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
    print(random.choice(lista) )

def sorteo_participantes():
    cantidad_participantes = int(input("Ingrese la cantidad de participantes: "))
    numero_sorteado = random.randint(1, cantidad_participantes)
    print(f"El número sorteado es: {numero_sorteado}")

def token_generator():
    token = 9998
    token_generado = random.randint(1000, token)
    nombre_usuario= str(input(' escribe tu nombre: '))
    print(f' hola {nombre_usuario}, tu token es {token_generado}')

def ensalada_random():
    frutas = ["manzana", "banana", "uva", "pera", "mango", "coco", "sandia", "fresa", "naranja", "maracuya", "kiwi", "cereza"]
    ensalada = random.sample(frutas, 3) #esto elige 3 elementos aleatorios de la lista frutas y los coloca en una nueva lista llamada ensalada
    print(f'ensalada de frutas: {ensalada}')
def raiz_entera():
    numero = [2,8,15,23,91,112,256]
    raices_enteras = [num for num in numero if math.sqrt(num).is_integer()] #esto crea una nueva lista con los numeros que son raices enteras, no decimales
    print('numeros con raices enteras:', raices_enteras)

def raiz():
    numeros = [2, 8, 15, 23, 91, 112, 256]
    raices_enteras = [num for num in numeros if math.sqrt(num) % 1 == 0]
    print("Números con raíces enteras:", raices_enteras)

def jardin():
    precio = 25.00
    cantidad = float(input(' cuanto cesped necesitas?'))
    area = math.pi * math.pow(cantidad, 2) #esto calcula el area de un circulo, el area es igual a pi por el radio al cuadrado
    total = precio * area
    print(f'el precio total es {total}')

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(11):
        print(f"{numero} x {i} = {numero * i}")

def multiplos_de_tres(lista):
    lista_original = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
    return [num for num in lista if num % 3 == 0]
    mult_3 = multiplos_de_tres(lista_original)
    print(mult_3)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cuadrados = list(map(lambda x: x**2, numeros)) #devuelve el cuadrado de los numero en la lista
print(cuadrados)

def nota_skater():
    notas = [float(input(f"Ingrese la nota {i + 1}: ")) for i in range(5)]
    notas.sort()
    media = sum(notas[1:4]) / 3
    print(f"Nota de la maniobra: {media:.2f}")

def analisis_notas(notas):
    mayor = max(notas)
    menor = min(notas)
    media = sum(notas) / len(notas)
    situacion = "Aprobado" if media >= 6 else "Reprobado"
    return mayor, menor, media, situacion

# Uso de la función
# notas_estudiante = [float(input(f"Ingrese la nota {i + 1}: ")) for i in range(4)]
# resultado = analisis_notas(notas_estudiante)
# print(f"El estudiante obtuvo una media de {resultado[2]:.2f}, con la mayor nota de {resultado[0]:.2f} puntos y la menor nota de {resultado[1]:.2f} puntos y fue {resultado[3]}")

# nombres = ["juan", "MaRia", "JOSÉ"]
# sobrenombres = ["SILVA", "sosa", "Tavares"]

# Normalizar nombres y apellidos y crear una nueva lista con los nombres completos
# nombres_normalizados = map(lambda x: x.capitalize(), nombres)
# sobrenombres_normalizados = map(lambda x: x.capitalize(), sobrenombres)
# nombres_completos = list(map(lambda x, y: f"Nome completo: {x} {y}", nombres_normalizados, sobrenombres_normalizados))
# print(nombres_completos)

dias = int(input("¿Cuántas diarias? "))
ciudad = input("¿Cuál es la ciudad? [Salvador, Fortaleza, Natal o Aracaju]: ")
distancias = [850, 800, 300, 550]
paseo = [200, 400, 250, 300]
km_l = 14
gasolina = 5

def gasto_hotel(dias):
    return 150 * dias

def gasto_gasolina(ciudad):
    if ciudad == "Salvador":
        return (2 * distancias[0] * gasolina) / km_l 
    elif ciudad == "Fortaleza":
        return (2 * distancias[1] * gasolina) / km_l 
    elif ciudad == "Natal":
        return (2 * distancias[2] * gasolina) / km_l 
    elif ciudad == "Aracaju":
        return (2 * distancias[3] * gasolina) / km_l 

def gasto_paseo(ciudad, dias):
    if ciudad=="Salvador":
        return paseo[0] * dias
    elif ciudad=="Fortaleza":
        return paseo[1] * dias
    elif ciudad=="Natal":
        return paseo[2] * dias 
    elif ciudad=="Aracaju":
        return paseo[3] * dias 

# gastos = gasto_hotel(dias) + gasto_gasolina(ciudad) + gasto_paseo(ciudad, dias)
# print(f"Con base en los gastos definidos, un viaje de {dias} días a {ciudad} desde Recife costaría {round(gastos, 2)} reales")

def separar_notas():
    notas_grupo = ['juan', 8, 9, 10, 'maria', 9, 7, 6, 'jose', 3, 7, 7, 'claudia', 5, 6, 8, 'ana', 6, 10, 9]
    nombres =[]
    notas =[]
    for i in range(len(notas_grupo)): #itera por toda la lista de notas grupo
        if i % 4 ==0: # cada elemento lo divide en 4 (0, 4, 8, 12, 16)y si da 0 de residuo lo añade a la lista de nombres, esto funciona ya que sabemos que solo hay 3 notas por estudiante
            nombres.append(notas_grupo[i]) #si cumple la condicion se añade a la lista de nombres
        else:
            notas.append(notas_grupo[i]) #si no cumple la condicion se añade a la lista de notas
    print(f'nombres: {nombres}')
    notas_separadas = []
    for i in range(0, len(notas), 3): #itera po la lista de notas, empezando desde el 0 y va de 3 en 3, es decir, 0, 3, 6, 9, 12, 15
        notas_separadas.append([notas[i], notas[i+1], notas[i+2]]) #añade la primera iteracion de i que seria el index 0, luego i+1 seria el index 1 y asi sucesivamente
    print(f'notas: {notas_separadas}')

def julia():
    registro = ("Julia", 23, "CDMX", "EM", "Python para DS 1")
    print(registro[0])  # imprime Julia
    print(registro[-1])  # imprime Python para DS 1

def entender_zip():
    a = ("John", "Charles", "Mike")
    b = ("Jenny", "Christy", "Monica")

    x = zip(a, b) #junta tuplas, donde los valores se juntan los primeros con los primeros, segundos con segundos y asi sucesivamente
    print(list(x)) #convierte el zip en una lista y lo imprime, en este caso imprime [('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica')]
    # si las tuplas/listas tienen diferente length, el mas corto define la longitud del resultado

    # Para realizar el proceso contrario, de transformar una tupla iterable en listas, 
    # basta con colocar el operador asterisco (*) al lado izquierdo del nombre de la tupla iterable que se desea extraer los datos, 
    # transmitiendo cada tupla a una variable.
def reverse_zip():
    tupla_iterable = [('J392', 'Juan'), ('M890', 'Maria'), ('J681', 'José'), ('C325', 'Claudia'), ('A49', 'Ana')]
    ids, nombres = zip(*tupla_iterable)

    ids = list(ids)
    nombres = list(nombres)

    print("IDs = ", ids) # IDs = ['J392', 'M890', 'J681', 'C325', 'A49']
    print("Nombres = ", nombres) # Nombres = ['Juan', 'Maria', 'José', 'Claudia', 'Ana']

# def lista_de_listas():
    # registros= [nombres, notas, promedios, situacion] # esto crea una lista de listas, donde cada lista es una lista de los nombres, notas, promedios y situacion
    # print(registros) # imprime la lista de listas
    
def IMC():
    alturas = [1.70, 1.80, 1.65, 1.75, 1.90]
    pesos = [65, 80, 58, 70, 95]

    imc = [round((peso / altura**2), 1) for altura, peso in zip(alturas, pesos)]
    print(imc)

def dictionario_comprehension():
    codigos_estudiantes = [('J392', 'Juan'), ('M890', 'Maria'), ('J681', 'José'), ('C325', 'Claudia'), ('A49', 'Ana')]
    #registro seria el nombre del diccionario
    ['estudiante'] = [codigos_estudiantes [0] [i] [0] for i in range(len(codigos_estudiantes[0]))]
    # esto crea una key del diccionario con los valores, [0] es para especificar que es sobre la primera lista
    #[i] es para identificar que es sobre cada elemento de la lista 
    # [0] el segundo cero es para identificar que solo se itera sobre el primer elemento de cada tupla de la lista seleccionada

def becas():
    nombres_estudiantes = ["Enrique Montero", "Luna Pereira", "Anthony Silva", "Leticia Fernandez", "Juan González", "Maira Caldera", "Diana Carvajo", "Mariana Rosas", "Camila Fernandez", "Levi Alves", "Nicolás Rocha", "Amanda Navas",  "Lara Morales", "Leticia Olivera", "Lucas Navas", "Lara Arteaga", "Beatriz Martinez", "Victor Acevedo", "Stephany Hernández", "Gustavo Lima"]
    medias_estudiantes = [5.4, 4.1, 9.1, 5.3, 6.9, 3.1, 9.0, 5.0, 8.2, 5.5,
                        8.1, 7.4, 5.0, 3.7, 8.1, 6.2, 6.1, 5.6, 10.0, 8.2]

def excepciones():
    notas = [5.4, 4.1, 9.1, 5.3, 6.9, 3.1, 9.0, 5.0, 8.2, 5.5, 8.1, 7.4, 5.0, 3.7, 8.1, 6.2, 6.1, 5.6, 10.0, 8.2]
    nombres = ["Enrique Montero", "Luna Pereira", "Anthony Silva", "Leticia Fernandez", "Juan González", "Maira Caldera", "Diana Carvajo"]
    try:
        nombre = input("Ingrese su nombre: ")
        resultado = notas [nombre]
    except KeyError:
        print("El nombre no existe en el diccionario.")
    else:
        print(f"El resultado es: {resultado}")
    finally:
        print("Fin del programa.")