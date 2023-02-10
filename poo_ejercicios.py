#Crear un programa que pida al usuario ingresar su nombre y edad y los imprima en pantalla.
"""nombre=input("ingrese su nombre: ")
edad=(input("ingrese su edad"))
print("el nombre es "+nombre )
print("la edad es "+edad)"""""

#Escribir una función que calcule el área de un círculo dado su radio.
"""pi=3.1416
radio=float(input("ingrese el radio del circulo: "))
area=pi*radio*radio
print(area)"""

#Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.
"""import random
def aleatorio():
    lista=[]
    for i in range(0,20):
        lista.append(random.randint(0,50))
    return lista
print(aleatorio())"""

#Escribir un programa que determine si un número dado es par o impar.
"""numero=int(input("ingrese un numero:"))
if numero %2==0:
    print("el numero es par")
else:
    print("el numero es impar")"""

#Crear una función que convierta grados Fahrenheit a grados Celsius.
"""fahrenheit=float(input("ingrese la temperatura de grados fahrenheit:"))
celsius=(fahrenheit-32)*5/9
print(celsius)"""

#Crear un programa que calcule la suma de los números en una lista dada
"""lista=[1,2,3,4,5,6,7,8,9,10]
suma=0
for i in lista:
    suma=suma+i
    print(suma)"""

#Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.
"""lista=[1,2,5,8,3,5,7,9,3]
recorrelista=lista[0]
for i in range(0,len(lista)):
    if lista[i]>recorrelista:
        recorrelista=lista[i]
print("el numero mayor es: ",recorrelista)

for x in range(0,len(lista)):
    if lista[x]<recorrelista:
        recorrelista=lista[x]
print("el numero menor es:",recorrelista)"""

#Crear una función que invierta el orden de los elementos en una lista dada.
"""lista=[2,3,6,8]
print("lista 1")
print(lista)
lista2=lista[::-1]
print("lista 1 invertida")
print(lista2)"""

#Crear un programa que genere una matriz de números y la imprima en pantalla.
"""matriz=[]
filas=int(input("ingrese la cantidad de filas: "))
columnas=int(input("ingrese la cantidad de columnas: "))
for i in range(filas):
    matriz.append([0]*columnas)
print(matriz)"""

#Escribir una función que calcule el factorial de un número dado.
"""numero=int(input("ingrese el numero"))
if numero >=0:
    x=1
    f=1
    while x <=numero:
        f=f*x
        x+=1
print(f)"""

#Crear un programa que genere una lista de números pares entre 1 y 100.
"""def generar_numeros(n):
    pares = []
    for i in range(2, n+1, 2):
        pares.append(i)
    return pares

print(generar_numeros(100))

#Crear un programa que imprima los números del 1 al 10 utilizando un ciclo for
for i in range(1,11):
    print(i)"""

#Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y división.
"""numero1=int(input("ingrese un numero:"))
numero2=int(input("ingrese un numero"))
suma=numero1+numero2
resta=numero1-numero2
multiplicacion=numero1*numero2
division=numero1/numero2

print("la solucion de la suma es: ",suma)
print("la solucion de la tresta: ", resta)
print("la solucion de la multipliacaion es: ", multiplicacion)
print("la solucion de la division es: ", division)"""

#Escribir una función que calcule la media aritmética de una lista de números
"""numero1=int(input("ingrese un numero: "))
numero2=int(input("ingrese un numero: "))
numero3=int(input("ingrese un numero: "))

resultado=(numero1+numero2+numero3)/3
print(resultado)"""
