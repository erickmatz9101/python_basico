
def prima_vacacional():

    print("Bienvenido al sistema que te atuda a calcular tú Prima Vacacional 💵\n")
    print("Para conocer tu prima vavacional necesitas conocer tú salario diario y los días de vacaciones que te corresponden.") 

    #Calculando el salario diario del empleado

    salario_mensual = float(input("Ingresa tu salario mensual para poder calcular tú salario diario:"))

    sdiario = salario_mensual/30
    sdiario = round(sdiario,2)
    print("Tú salario diario es de: $" + str(sdiario))

    dias_vacaciones = int(input("Ahora ingresa los días de vacaciones que te corresponden: "))

    if dias_vacaciones >= 29:
        print("Los días de vacaciones no pueden ser mayor a 29 ingresalos nuevamente")
        dias_vacaciones = int(input("Ingresa los días de vacaciones que te corresponden: "))
        prima_vacacional = sdiario*dias_vacaciones*0.25
        print("Tú prima vacacional es de: $" + str(prima_vacacional))

        
    else:
        prima_vacacional = sdiario*dias_vacaciones*0.25
        print("Tú prima vacacional es de: $" + str(prima_vacacional))


    

if __name__ == '__main__':  
    prima_vacacional()
