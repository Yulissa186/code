def X_tabla():
    x = int(input("Dime qué tabla deseas: "))
    a = 1
    while a <= 10:  
        print(f"{x} * {a} = {x*a}")
        a += 1

def Num_Par_o_Impar():
    n1 = int(input("Ingresa el número: "))
    if n1 % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")

def if_anidado():
    n1 = int(input("Ingresa tu calificación: "))
    if n1 == 100:
        print("Excelente, Felicidades")
    elif 90 <= n1 <= 99:
        print("Muy bien")
    elif 80 <= n1 <= 89:
        print("Bien")
    elif 70 <= n1 <= 79:
        print("Alumno regular")
    else:
        print("Alumno no aprobado")

def formula():
    def potencias(N):
        s = 0
        for i in range(1, N+1):
           ter = i**(i+1)
           s += ter
    
        return s / N

    N = int(input("Ingresa un número: "))
    resFinal = potencias(N)
    print("El resultado es:", resFinal)

def No_DControl():
    import datetime

    fecha = datetime.datetime.now()
    año = datetime.datetime.strftime(fecha, "%Y")

    carreras = {
        "1": "Ing. Industrial",
        "2": "TIC'S",
        "3": "Ing. Sistemas Computacionales",
        "4": "Ing. Quimica",
        "5": "Ing. Civil",
        "6": "Ing. Mecatronica",
        "7": "Ing. Electrica",
        "8": "Ing. Logistica",
        "9": "Lic. Administracion"
    }

    x = int(input("Ingresa el periodo en el que ingresaste: "))

    if x == 1 or x == 2:
        num = int(input("¿Cuál es tu número de estudiante?: "))
        if num <= 999:
            numero = input(
                "Selecciona la carrera a la que perteneces:\n1.-Ing. Industrial, 2.-TIC'S, 3.-Ing. Sistemas Computacionales, 4.-Ing. Química, 5.-Ing. Civil, 6.-Ing. Mecatrónica, 7.-Ing. Eléctrica, 8.-Ing. Logística, 9.-Lic. Administración: ")
            if numero in carreras:
                carrera = carreras[numero]
                if 1 <= num <= 9:
                    num_str = f"00{num}"
                elif 10 <= num <= 99:
                    num_str = f"0{num}"
                else:
                    num_str = str(num)
                a = f"{año}{x}{numero}{num_str}"
                print("Tu matrícula es:", a, "y perteneces a la carrera de", carrera)
            else:
                print("Carrera no válida.")
        else:
            print("Número no válido.")
    else:
        print("Periodo no válido.")

def main():
    while True:
        
        print("1. Mostrar tabla de multiplicar")
        print("2. Determinar si un número es par o impar")
        print("3. Calificación ")
        print("4. Codigo de la Formula")
        print("5. Generar matricula de estudiante")
        print("6. Salir del programa")

        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:

            X_tabla()
        elif opcion == 2:
            Num_Par_o_Impar()
        elif opcion == 3:
            if_anidado()
        elif opcion == 4:
            formula()
        elif opcion == 5:
            No_DControl()
        elif opcion == 6:
            print("Saliendo")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
