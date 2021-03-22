"""
TECNM Campus La Laguna

Big Data

Alumno: 18131209 - ADAME SANDOVAL JOSE MISAEL

Programa 10: Funciones de Orden Superior
"""

#-----------------------------------------------------------
# Funciones de orden superior integradas en Python

# Función de mapa
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

# Función reduce
from functools import reduce

city = ['L', 'o', 'n', 'd', 'o', 'n', 2, 0, 2, 0]
city_to_str = reduce(lambda x, y: str(x) + str(y), city)
print(city_to_str)

# Función filter
names = ['yAnG', 'MASk', 'thoMas', 'LISA']
names = map(str.capitalize, names)
names = filter(lambda x: len(x) <= 4, names)
print(list(names))
#-----------------------------------------------------------
# Funciones de orden superior definida por el usuario

# Función de orden superior operar
def operar(v1,v2,fn): # El tercer parámetro de esta función
                      # se llama "fn" y es de tipo función.
    return fn(v1,v2)  # El algoritmo de la función operar 
    # consiste en llamar a la función fn y pasar los dos 
    # valores que espera dicha función:

# Funciones normales de las operaciones aritméticas
def sumar(x1,x2):
    return x1+x2

def restar(x1,x2):
    return x1-x2

def multiplicar(x1,x2):
    return x1*x2

def dividir(x1,x2):
    return x1/x2

# llamamos a la función operar y le pasamos tres datos, 
# dos enteros y uno con la referencia de una función
resu1 = operar(10,3,sumar)
print(resu1) # almacenamos en la variable resu1 que mostramos 
             # luego por pantalla:
# Llamamos a operar y le pasamos la referencia a la función restar
resu2 = operar(10,3,restar)
print(resu2)

# De forma similar llamamos a operar y le pasamos las referencias 
# a las otras funciones
print(operar(30,10,multiplicar))

print(operar(10,2,dividir))
