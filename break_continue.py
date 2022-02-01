def run ():
    # for contador in range(1000):
      #  if contador % 2 !=   0:
       #     continue
       # print(contador)
   # for i in range(10000):
      #  print(i)
       # if i == 5678:
        #    break 
     texto = input('Ingresa la frase: ')
     for letra in texto:
         if letra == 'o':
             break
         print(letra)


       


if __name__ == '__main__':
    run()





"""Para este caso se tiene 3 ejemplos:

Caso 1: Uso de continue donde en caso de que el ciclo se encuentre con un número que no sea par, entonces salta la línea
del print y solo lo imprime si es par. Es decir cntinua el ciclo pero solo imprime los pares

Caso2: Uso de Break el ciclo corta en caso de que al iniciar el contador llegue al número 5678

Caso 3: Uso de Break, entra al ciclo la frase y en caso de que se encuentre con una letra igual "o" ahi corta el ciclo"""
