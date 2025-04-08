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