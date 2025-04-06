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