##Implementado el uso de funciones

def imprimir_mensaje():
    print("Mensaje especial")
    print("Estoy aprendiendo a implementar funciones")


##Mandando a llamar a mi función

imprimir_mensaje()
imprimir_mensaje()
imprimir_mensaje()




"""Las funciones son utilizadas cuando queremos o tenemos que utilizar muchas veces las mismas líneas o alguna parte del código,
por ello conviene crear las funciones así cuando desee implementarlas sólo tengo que llamar a la función para implemetarla donde
desee."""



"""POara este caso segun la opcion que elija 1,2,3 es el mensaje que debe arrojar, por ello para mi función me conviene pasar como
parámetro el mensaje y cuando mando a llamar a mi función lo cambio o personalizo según sea el caso y así solo mando a llamar a la 
funcion para no repetir el código"""


def conversacion(mensaje):
    print("Hola")
    print("Cómo estás")
    print(mensaje)
    print("Adios")

opcion= int(input("Elige la opción (1,2,3);"))

if opcion == 1:
    conversacion("Elegiste la opción 1")

elif  opcion == 2:
    conversacion("Elegiste la opción 2")

elif opcion == 3:
    conversacion("Elegiste la opción 3")

else:
    print("Elegiste una opción no válida")       




def suma (a, b):

    print("Ésta función suma 2 números")

    resultado = a + b 

    return resultado


sumatoria = suma(1,4)

print(suma)


"""En esta función que recibe el nombre de suma, se pasan 2 valores como parámetro para los cuales se define que dentro de la función
se sumen por ello cuando entra en proceso mi función lo que hace es:

1.-Imprime "Esta funcion suma dos números

2.-Crea la variable resultado que suma a+b

3.-Devuelve el valor de la variable resultado, para ello debo usar la palabra reservada return

En la parte de abajo cuando invoco la suma paso lo valores que deso sumar como parámetro y mando a imprimir suma que es la que me 
devuelve el valor"""