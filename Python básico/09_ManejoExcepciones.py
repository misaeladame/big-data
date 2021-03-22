"""
TECNM Campus La Laguna

Big Data

Alumno: 18131209 - ADAME SANDOVAL JOSE MISAEL

Programa 09: Manejo de excepciones
"""

# Función para dividir dos números 
def dividir(x, y):
    try: # Bloque de codigo en el que se puede atrapar una 
         # excepción
        resultado = x / y
    except ZeroDivisionError: # Excepción que atrapa cuando el 
                              # parámetro y es 0
        print("Error: Estas dividiendo entre 0")
    except TypeError: # Excepción que atrapa cuando no se 
                      # ingresó un numero
        print("Error: Ingresaste algún caracter no numérico")
    else: # Bloque de cuando no ocurrió alguna excepción 
          # (si se realiza la división)
        print("El resultado es:", resultado)
    finally: # BLoque de código que siempre se ejecuta
        print("Programa terminado")

# Llamando a la función dividir 3 veces
#       x, y
dividir(4, 0) # Dividir 1
dividir(10, 2) # Dividir 2
dividir('Hola miss Lamia', 8) # Dividir 3
