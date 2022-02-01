###Funcion que se ocupa para validar si el numero cumple con lo estipulado para que sea primo o no

def es_primo(numero):
    contador = 0

    for i in range(1, numero+1): ##Este for va del numero 1 hasta el numero que ingresó el usuario
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1

    if contador == 0:
        return True
    else:
        return
        False            




###Funcion que imprime si el número ingreso es primo o no
def run():
    numero = int(input("Ingresa un número: ")) #transformando a entero el número ingresado por el usuario
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")    




if __name__ == '__main__':
    run()





"""Cuando en el if valido si numero es_primo ya no hay necesidad de hacer uso del true debido a que el lenguaje entiende que lo que 
estoy buscando es validar si el numero que ingreso es primo o no

En el if de la funcion es_primo validamos si i= 1 o i=numero (ue ingreso el usuario) se salta la línea
En el otro if si al dividir el resultado es cero entonces se le suma 1 al contador, en este caso se aumenta en 1 cuando el numero no
sea primo"""    