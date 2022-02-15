
#Programa para calcular el primedio de las calificaciones que ingrese el usuario


def promedio():
    calificaciones = [] #Lista que guarda las calificaciones ingresadas por el usuario
    
    input("Bienvenido al sistema para calcular tú promedio")
    for i in range(1,7):
        calificacion = int( input( "Ingresa la calififcacion {}: ".format(i) ))

        if calificacion < 0:
            print("La calificacion que ingresaste no es válida, intentalo de nuevo")

            break
           
        calificaciones.append(calificacion)
        
    print("Tus calificaciones son: "+ str(calificaciones))   

    #Calculando el primedio de las calificaciones
    promedio = sum(calificaciones)/len(calificaciones)
    print("Tú promedio final es: "+ str(promedio))

if __name__ == '__main__':

    promedio()





    """La función Format me permite que pueda llevar a cabo dentro del ciclo la union de tipo string con el ingreso de datos que estoy
    pasado de string a entero
    
    **La funcion. append permite que los valores que vaya ingresando el usuario vayan colocándose delante de el último valor ingreado
    en éste caso"""
    
    