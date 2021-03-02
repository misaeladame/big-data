# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 08:36:28 2021

@author: jmas_
Programa 1. -Iniciando con python ciclos
"""
#----------------------------------------------------------
#Manera 1

# entrada = ""
# suma = 0
# while suma < 3 and entrada != "bye":
#     entrada = input("Clave: ")
#     suma += 1
#     print("Intento %d " % suma)
# print ("Utilizaste %d intentos" % suma)
#-----------------------------------------------------------
#Manera 2

entrada = ""
suma = 0
fallido = 0
while suma < 3:
    suma += 1
    print("Intento %d " % suma)
    entrada = input("Clave: ")
    print()
    #Al ingresar "bye", se evita que 
    #la variable fallido se incremente
    if entrada == "bye":
        continue
    fallido += 1
print("Tuviste %d intentos fallidos." % fallido)
#-----------------------------------------------------------
