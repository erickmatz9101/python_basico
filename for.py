                                                ####Ciclo For###

"""También es un ciclo de repetición el cual permite que se repita eñ ciclo tantas veces se lo indique, en éste caso ocupa una 
posición de inicio y una posición final.

Funcion Range: Es un tipo de dato el cual nos permite que pueda ser utilizado como lista, además de que esxiste la opción de 
indicar no solo el rango de hasta que número debe llagar, sino en éste caso indicar dentro de sus parámetros como valor inicial
el número del que partimos y el número al que deseamos llegar, no hay que olvidar que toma el valor posición por lo cual empieza en
cero."""

### Ejemplo1:

for contador in range(1001):
    print(contador)


### Ejemplo 2: dando valor inicial y final:

for contador in range(1,1001):
    print(contador)    


##Pequeño programa que imprime la tabla de multiplicar del 11, en un rango del 0 al 9

for i in range(10):
    print(11*i) 

