acu = 0
while True: #al menos ejecuta una vez 
    n1=(input("teclea un numero: o presione x para salir del programa     "))
    if (n1=="x"):
        break #rompe el ciclo
    else:
        acu=acu + int (n1) #toma n1 como entero
        # esta fuera del ciclo lo siguiente
if (acu>0):
    print ("el resultado final del acumulador es------>:", acu)
else:
    print("se puso x para salir del bucle")
    