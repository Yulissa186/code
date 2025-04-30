#Código Bidireccional en Python
#Ambas computadoras ejecutan este mismo programa y seleccionan si desean enviar o recibir en cada interacción.
import socket
import os
import threading

def recibir_archivo(conexion, carpeta_destino="."):
    try:
        # Recibir nombre del archivo
        nombre_archivo = conexion.recv(1024).decode()
        ruta_archivo = os.path.join(carpeta_destino, nombre_archivo)
        print(f"Recibiendo archivo: {nombre_archivo}")

        # Recibir datos del archivo
        with open(ruta_archivo, "wb") as archivo:
            while True:
                datos = conexion.recv(4096)
                if not datos:
                    break
                archivo.write(datos)

        print(f"Archivo recibido y guardado en {ruta_archivo}")
    except Exception as e:
        print(f"Error al recibir archivo: {e}")

def enviar_archivo(conexion, ruta_archivo):
    try:
        if not os.path.exists(ruta_archivo):
            print("El archivo especificado no existe.")
            return

        # Enviar nombre del archivo
        nombre_archivo = os.path.basename(ruta_archivo)
        conexion.send(nombre_archivo.encode())

        # Enviar contenido del archivo
        with open(ruta_archivo, "rb") as archivo:
            while True:
                datos = archivo.read(4096)
                if not datos:
                    break
                conexion.send(datos)

        print(f"Archivo {nombre_archivo} enviado correctamente.")
    except Exception as e:
        print(f"Error al enviar archivo: {e}")

def manejar_cliente(socket_conexion, carpeta_destino="."):
    print("Cliente conectado.")
    while True:
        try:
            # Recibir opción del cliente
            opcion = socket_conexion.recv(1024).decode()

            if opcion == "enviar":
                recibir_archivo(socket_conexion, carpeta_destino)
            elif opcion == "recibir":
                ruta_archivo = input("Ingrese la ruta del archivo a enviar: ")
                enviar_archivo(socket_conexion, ruta_archivo)
            elif opcion == "salir":
                print("Cliente desconectado.")
                break
            else:
                print("Opción no válida.")
        except Exception as e:
            print(f"Error en la comunicación: {e}")
            break

    socket_conexion.close()

def iniciar_servidor(puerto=12345, carpeta_destino="."):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(("0.0.0.0", puerto))
    servidor.listen(5)
    print(f"Servidor escuchando en el puerto {puerto}...")

    while True:
        conn, addr = servidor.accept()
        hilo_cliente = threading.Thread(target=manejar_cliente, args=(conn, carpeta_destino))
        hilo_cliente.start()

def iniciar_cliente(ip_destino, puerto=12345):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((ip_destino, puerto))
    print("Conectado al servidor.")

    while True:
        print("\nOpciones:")
        print("1. Enviar archivo")
        print("2. Recibir archivo")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cliente.send("recibir".encode())
            ruta_archivo = input("Ingrese la ruta del archivo a enviar: ")
            enviar_archivo(cliente, ruta_archivo)
        elif opcion == "2":
            cliente.send("enviar".encode())
            recibir_archivo(cliente)
        elif opcion == "3":
            cliente.send("salir".encode())
            print("Desconectándose...")
            break
        else:
            print("Opción no válida.")

    cliente.close()

if __name__ == "__main__":
    print("Seleccione el modo de operación:")
    print("1. Servidor (Esperar conexiones)")
    print("2. Cliente (Conectarse a otro equipo)")

    modo = input("Ingrese el número de la opción (1 o 2): ")

    if modo == "1":
        puerto = int(input("Ingrese el puerto para el servidor (por defecto 12345): ") or 12345)
        iniciar_servidor(puerto)
    elif modo == "2":
        ip_destino = input("Ingrese la IP del servidor: ")
        puerto = int(input("Ingrese el puerto del servidor (por defecto 12345): ") or 12345)
        iniciar_cliente(ip_destino, puerto)
    else:
        print("Opción no válida.")