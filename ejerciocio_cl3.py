"""Ejercicios

Generar un commit por objetivo cumplido y pushear a GitHub

1- Crear una lista vacía en una variable mi_lista e imprimirla por consola mostrando el tipo de dato al que pertenece.

2- extender el ejercicio anterior pedirle al usuario que ingresé 4 ciudades y almacenarlas en una tupla. Desempaquetar la tupla e imprimir la primera y la última.

3- extender el ejercicio para calcular el área de un círculo pedirle por consola al usuario que ingresé los datos de su círculo. Imprimir por consola el área. 

4- ingresar por consola 7 números y almacenarlos en mi_lista recorrerlos con un bucle for para mostrar por consola el mensaje índice i elemento. 

5- Crear una colección que acepte elementos de tipo clave-valor y almacenar 5 elementos: 
     nombreDeUsuario - DNI

6- crear un menú de usuario con las siguientes opciones: 
   Menú
   1- Mostrar los números de la lista
   2- Mostrar ciudades 
   3- Calcular el área de un círculo
   4- Agregar número a la lista y        mostrar los números distintos
   5- Agregar usuario y DNI 
   6- Buscar usuario por nombre e imprimir su DNI


Para simular el menú de opciones hacer uso del bucle while y para la selección de opciones utilizar if elif else."""


mi_lista = []

""" 
# print(type(mi_lista))

ciudades = input("ingrese 4 ciudades: ")
t_ciudades = tuple(ciudades.split())
print(t_ciudades)

a,b,c,d = t_ciudades
print(a)
# print(b)
# print(c)
print(d) """

""" calculo de un circulo """
""" diametro = float(input("ingrese el diametro: "))
radio = diametro / 2
print(radio)

PI = 3.141592
area = PI * (radio**2)
print(area) """

"""punto 4 """

"ingrese 7 numeros y almacenarlos en mi_lista , recorrerlos con for para mostrar por consola el mensaje indice pertenece a tal elemento"


""" mis_numeros = input("ingrese 7 numeros: ")
numeros_split = mis_numeros.split()
mi_lista.extend(numeros_split) """

""" for elem in numeros_split:
   mi_lista.append(elem) """

""" for elem in mi_lista:
   print( mi_lista.index(elem), " => ", elem) """
   
   
""" 5- Crear una colección que acepte elementos de tipo clave-valor y almacenar 5 elementos: 
     nombreDeUsuario - DNI """


# name_dni = dict( ruben=40182328, martin=8437812, agustina=20946831)
name_dni = { 'ruben' : 40182328, 'martin' : 8437812, 'agustina' : 20946831}
print(name_dni)



