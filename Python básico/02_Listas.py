# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 08:42:14 2021

@author: jmas_
Programa 2: listas
"""

lista = [1, 2, 1, 1, 1, 1, 3, 4, 5, 6, 7, 8]
print(lista)
print(lista[3])
print(lista[0])
#modificar un elemento
lista[3] = "Modificado"
print(lista[3])
print(lista)
#Eliminar un elemento de la lista
del lista[3]
print(lista)
#Extraccion de un segmento
print(lista)
print(lista[0:3])
print(lista)
print(lista[2:3])
print(lista)
#Agregar
lista.append(888)
print(lista)
lista.insert(3, "Insertado")
print(lista)
lista.remove("Insertado")
print(lista)
lista.reverse()
print(lista)
lista.sort()
print(lista)
lista.pop()
print(lista)
#Cuenta el número de veces que aparece dentro del objeto
#tipo list el objeto que se ingresa como argumento
print(lista.count(1))
lista.clear()
print(lista)
