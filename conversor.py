
from ast import If


menu = """
Bienvenido al conversor de monedas 💵💵🤑

1.- Pesos Colombianos 

2.- Pesos Argentinos

3.- Pesos Mexicanos

Elige una opción: """


opcion = int(input(menu))

if opcion == 1:

    pesos = input("¿Cuántos pesos Colombianos tienes?: ") #variable que guarda la cantidad de pesos colombianos a convertir

    #haciendo la transformación del valor al número decimal (casteo)

    pesos = float(pesos)

    #Variable que gusrada el valor del dolar en pesos colombianos 

    valor_dolar = 3875

    #Creando la variable para convertir de pesos a dolares

    dolares= pesos / valor_dolar

    #Para rendondear a 2 decimales la converión

    dolares = round(dolares,2)

    #Variable que convierte la cantidad de dolares en texto (casteo)

    dolares = str(dolares)

    print("Tienes $" + dolares + " dólares")


elif opcion ==2:

    pesos = input("¿Cuántos pesos Argentinos tienes?: ") #variable que guarda la cantidad de pesos colombianos a convertir

    #haciendo la transformación del valor al número decimal (casteo)

    pesos = float(pesos)

    #Variable que gusrada el valor del dolar en pesos colombianos 

    valor_dolar = 65

    #Creando la variable para convertir de pesos a dolares

    dolares= pesos / valor_dolar

    #Para rendondear a 2 decimales la converión

    dolares = round(dolares,2)

    #Variable que convierte la cantidad de dolares en texto (casteo)

    dolares = str(dolares)

    print("Tienes $" + dolares + " dólares")

    

elif opcion == 3:

    pesos = input("¿Cuántos pesos Mexicanos tienes?: ") #variable que guarda la cantidad de pesos colombianos a convertir

    #haciendo la transformación del valor al número decimal (casteo)

    pesos = float(pesos)

    #Variable que gusrada el valor del dolar en pesos colombianos 

    valor_dolar = 22

    #Creando la variable para convertir de pesos a dolares

    dolares= pesos / valor_dolar

    #Para rendondear a 2 decimales la converión

    dolares = round(dolares,2)

    #Variable que convierte la cantidad de dolares en texto (casteo)

    dolares = str(dolares)

    print("Tienes $" + dolares + " dólares")

else:

    print("Elegiste un opción que no es válida")












"""La  función round en Python es la que me permite redondear una cantidad al número de dígitos que yo le indique y devuelve un número
de punto flotante round(cantidad o variable, numero de dígitos despues del punto), en mi ejemplo quedó de la siguiente manera:
round(dolares, 2) lo cualquiere decir que después del punto decimal va a imprimir sólo 2 digitos"""