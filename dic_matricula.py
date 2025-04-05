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
