# Server
import socket
from termcolor import colored

def shell():
    command = input("* shell#%s: " % str(ip))  # Solicita al usuario que ingrese un comando y muestra la dirección IP del cliente
    target.send(command.encode('utf-8'))  # Envía el comando al cliente codificado en UTF-8
    message = target.recv(1024).decode('utf-8')  # Recibe un mensaje del cliente (hasta 1024 bytes) y lo decodifica
    print(message)  # Imprime el mensaje recibido del cliente

def server():
    global s
    global ip
    global target
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crea un socket TCP IPv4
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Configura la opción de socket para reutilizar direcciones

    s.bind(("192.168.88.254", 54321))  # Liga el socket a la dirección IP y puerto especificados
    s.listen(5)  # Pone el socket en modo de escucha para aceptar conexiones entrantes

    print(colored("[+] Listening for incoming connections", 'green'))  # Imprime un mensaje indicando que está esperando conexiones entrantes

    target, ip = s.accept()  # Acepta una conexión entrante y devuelve el socket de conexión y la dirección IP del cliente

    print(colored("[+] Connection established from %s" % str(ip), 'green'))  # Imprime un mensaje indicando que se ha establecido una conexión desde una dirección IP específica
    
    # Envía un mensaje al cliente después de que se haya establecido la conexión
    target.send("¡Hola coders!".encode('utf-8'))

server()  # Llama a la función server() para iniciar el servidor
shell()   # Llama a la función shell() para iniciar el shell interactivo después de que se haya establecido la conexión
