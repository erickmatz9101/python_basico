def palindromo(palabra):

    ##quitando los espacios a la palabra o frase por un srtring vacio 

    palabra = palabra.replace(' ','')

    ##pasando todos los caracteres a minúsculas

    palabra = palabra.lower()

    ##generando una nueva variable que contenga la palabra invertida utilizando slices

    palabra_invertida = palabra[::-1]

    ##validando si palabra == palabra_invertida

    if palabra == palabra_invertida:

        return True
    else:

        return False    



##Funcion run que en este programa realiza la funcion para validar si la pabara ingresada es palindromo o mo
def run():

    #Variable que guarda la palabra que ingrese el usuario
    palabra = input("Escribe una palabra: ")


    #Valida si la palabra es palindromo o no pero con la función que más adelante se va a crear
    es_palindromo = palindromo(palabra)

    #Creando las condicionales para validar si la palabra es o no palindromo

    if es_palindromo ==True:

        print("Es palindromo")

    else:

        print("No es palindromo")    


if __name__ == '__main__':

    run()

