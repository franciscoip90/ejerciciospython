print("hola mundo")


#Suma

suma = 2+3
print(suma)

#Resta
resta = 2-3
print(resta)


#Multiplicacion
multiplicacion = 2*3
print(multiplicacion)

#Division
division = 2/3
print(division)

#variables y tipos de datos

nombre = "Juan"
edad = 25
altura = 1.62
es_estudiante = True
print(nombre, edad, altura, es_estudiante)

#Listas
frutas = ["Manzana","platano","frutilla"]
print (frutas)

#aaceder a un elemento de la lista
print(frutas[2])

#longitud de lista
print(len(frutas))

#agregar elemento a la lista
frutas.append("pera")
print(frutas)


#condicionales
numero = -2

if numero > 0:
    print("el numero es positivo")
else:
    print("el numero es negativo")

#bucles
for i in range(5):
    print(i)

#funciones
def suma(a, b):
    return a+b

resultado = suma(2, 5)
print(resultado)

#leer y escribir archivos
archivo = open("ejemplo.txt", "w")
archivo.write("hola python")
archivo.close()

archivo = open("ejemplo.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

#modulos

import random

numero_aleatorio = random.randint(1 ,100)
print(numero_aleatorio)

#excepciones
try:
    resultado = 10/0
    print(resultado)
except ZeroDivisionError:
    print("error division por cero")

#factorial

numero = int(input("ingresa un numero: "))

if numero % 2 == 0:
    print("es par")
else:
    print("es impar")



def factorial(n):
    resultado = 1
    for i in range(1,n+1):
        resultado *=i
    return resultado

print(f"el factorial de {numero} es {factorial(numero)}")

