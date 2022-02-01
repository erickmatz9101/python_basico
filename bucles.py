                                            ##Blucle While##

"""Es un bucle que sirve n caso de que quiera que algo de mi código se esté repitiendo constantemente, en el cual la palabra while
significa MIENTRAS, esto quiere decir que mientras la condición se cumnpla, el código se seguirá ejecutando
Para éste ejemplo quiero sacar todos los numeros elevados a la potencia 2 hasta el número 1000"""

##Definiendo la función para mi programa

def run ():
    LIMITE = 1000


    contador = 0

    potencia_2 = 2**contador

    while potencia_2 < LIMITE:
        print('2 elevado a  ' + str(contador) + ' es igual a: ' + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador



if __name__ ==  '__main__':
    run()












"""En Python cuando deseo que mi valor sea una constante debo escribir su nombre en MAYUSCULAS. Una constante es un valor que no va 
a cambiar nunca dentro de mi programa"""    



