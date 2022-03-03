import math

def calculo_catetos(valor1, valor2): #Funcion para calcular el teorema segun los lados ingresados por el usuario
     #Elevar al cuadrado lado1 y lado2
     cuadrado1 = pow(valor1,2)
     cuadrado2 = pow(valor2,2)
     cuadrado1 = round(cuadrado1, 2)
     print("El cuadrado del lado 1 es: " + str(cuadrado1))
     cuadrado2 = round(cuadrado2,2)
     print("El cuadrado del lado 2 es: " + str(cuadrado2))
     #Haciendo la suma de los cuadrados
     resta= cuadrado1 - cuadrado2
     print("La resta de los cuadrados es: " + str(resta))
     #Calculando la raiz cuadrada de la suma de los cuadrados
     raiz = math.sqrt(resta)
     raiz = round(raiz,2)
     print("El valor del cateto es de: " + str(raiz))

def calculo_hipotenusa(valor1, valor2):
     cuadrado1 = pow(valor1,2)
     cuadrado2 = pow(valor2,2)
     cuadrado1 = round(cuadrado1, 2)
     print("El cuadrado del lado 1 es: " + str(cuadrado1))
     cuadrado2 = round(cuadrado2,2)
     print("El cuadrado del lado 2 es: " + str(cuadrado2))
     #Haciendo la suma de los cuadrados
     sumatoria= cuadrado1 + cuadrado2
     print("La suma de los cuadrados es: " + str(sumatoria))
     #Calculando la raiz cuadrada de la suma de los cuadrados
     raiz = math.sqrt(sumatoria)
     raiz = round(raiz,2)
     print("El valor de la hipotenusa es de: " + str(raiz))

def menu():

     print("Bienvenido al programa para calcular el teoréma de pitágoras 🏛️🌍\n")

     opcion = int(input("Menú:\n Selecciona 1: Para calcular el lado A\n Selecciona 2: Para calcular el lado B\n Selecciona 3: Para calcular el lado C "))

     if opcion == 1:
          print("Vamos a calcular el lado de A, para ello necesitamos los valores de C y B\n")
          C =float(input("Ingresa el valor de C "))
          B =float(input("Ingresa el valor de B "))
          calculo_catetos(C, B)

     elif opcion ==2:
          print("Vamos a calcular el lado de B, para ello necesitamos los valores de C y A\n")
          C =float(input("Ingresa el valor de C "))
          A =float(input("Ingresa el valor de B "))
          calculo_catetos(C, A)

     elif opcion ==3:
          print("Vamos a calcular el lado de C, para ello necesitamos los valores de a y b ")
          A= float(input("Ingresa el valor de A "))
          B = float(input("Ingresa el valor de B "))
          calculo_hipotenusa(A,B)

     else:
          print("Haz elegido una opción no valida, intentalo de nuevo \n")
          menu()
          



if __name__ == '__main__':

     menu()
     


















    


