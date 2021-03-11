# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 08:33:18 2021

@author: misael
Programa 8. Archivos
"""
#Escritura
# arch = open("prueba.txt", "w")
# arch.write("Linea 1")
# for i in range(10):
#     arch.write("Linea %d \n" %(i+1))
# arch.close()

# arch = open("prueba.txt", "a")
# for i in range(2):
#     arch.write("Agregando linea %d \n"%(i+1))
# arch.close()

#Lectura 
# arch = open("prueba.txt", "r")
# lineas = arch.readlines()
# for i in lineas:
#     print(i)
# arch.close()

# arch = open("prueba.txt", "r")
# lista = ["hola", "mundo", "desde", "Python"]
# arch.writelines(lista)
# for linea in arch.readlines():
#     print(linea)
# arch.close()

#Forma estable y segura : cierra el archivo automaticamente
# with open ("prueba.txt", "w") as arch:
#     arch.write("Prueba con with--as")
#     arch.close()

# with open("prueba.txt", "r") as arch:
#     linea = arch.read()
#     print(linea)
#     arch.close()
    
for linea in open("prueba.txt"):
    print(linea, end='')

