import random


def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    simbolos = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena


def run():
    contrasena = generar_contrasena()
    print('Tu nueva contraseña es: ' + contrasena)


if __name__ == '__main__':
    run()




"""Se guardan en 4 listas dierentes los distintos simbolos que se pueden ocupar para generar la contraseña
   La variable caracteres es la suma de estos simbolos para poder gebnerar la contraseña.
   En la lista contraseña se gusrda la suma de estos simbolos
   
   El ciclo for: Tiene un rango igual a 15 que son los ciclos que se cumplirán en éste caso porque quiero que la
   contraseña tenga 15 caracteres.
   
   La funcion .choice es propia de la clase random y sirve para poder seleccionar de la lista de caracteres un elemento al 
   azar cuando se esté ejecutando nuestro for.
   
   Contraseña.append como ya se habia aplicado antes la funcion .append lo que hace es agregar el caracter al final de la 
   lista, recuerda que en éste caso donde se esta guardando en la lista contraseña
   
   Para convertir nuestra lista a un String debo hacer uso de la funcion .join es decir, si bien loe elementos de la lista ya 
   estan de tipo String, debo unirlos, y para ello la funcion join me ayuda para quitar esos espacios vacios y que se unan
   esos caracteres """
