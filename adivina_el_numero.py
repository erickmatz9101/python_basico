import random ##Tiene funciones para trabajar con la aletoriedad 


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un número del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un número más grande')
        else:
            print('Busca un número más pequeño')
        numero_elegido = int(input('Elige otro número: '))
    print('¡Ganaste!')


if __name__ == '__main__':
    run()






"""La función ramdon.randint, cumple con la funcion de generar un numero aleatorio entero que va de un numero inicial(a)
a un numero final (b)

El while, cumple con la funcion de que mientras el numero elegido sea distinto al numero aleatorio vamos a ejecutar el codigo y 
cuando deje de ser distinto el jugador habra ganado"""