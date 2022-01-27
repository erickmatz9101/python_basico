
from ast import If

##Función que permite hacer la conversion de pesos a dólares según el país 

def conversor(tipo_pesos, valor_dolar):

    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes? ") #variable que guarda la cantidad de pesos a convertir

    pesos = float(pesos) #transformando a número decimal

    dolares = pesos/valor_dolar #variable que convierte de pesos a dolares

    dolares = round(dolares,2) #redondeando a 2 decimales la conversión

    dolares =str(dolares) #variable que convierte la cantidad de dolares en texto

    print("Tienes $ " + dolares + " dólares")



menu = """
Bienvenido al conversor de monedas 💵💵🤑

1.- Pesos Colombianos 

2.- Pesos Argentinos

3.- Pesos Mexicanos

Elige una opción:  """


opcion = int(input(menu))

if opcion == 1:

    conversor("Colombianos", 3875)


elif opcion ==2:

    conversor("Argentinos", 65)
    

elif opcion == 3:

    conversor("Mexicanos", 24)
else:

    print("Elegiste un opción que no es válida")












"""La  función round en Python es la que me permite redondear una cantidad al número de dígitos que yo le indique y devuelve un número
de punto flotante round(cantidad o variable, numero de dígitos despues del punto), en mi ejemplo quedó de la siguiente manera:
round(dolares, 2) lo cualquiere decir que después del punto decimal va a imprimir sólo 2 digitos

En ésta segunda modificación se usaron las funciones las cuales permiten que se pueda modularizar el código para no tener que escribir
demasiada líneas, para este caso se utilizó la función conversor a la cual se la pasó como parámetro el tipo de peso (colombianos,
argentinos, mexicanos) y el valor del dolar en este caso segun la moneda de cambio es el costo que tiene por dolar por tal 
motivo me convenia poner esos datos como parámetros de mi funcion y asi reutilizar mi código.

Por buenas prácticas las funciones deben colocarse en la parte superior de el código"""