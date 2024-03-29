import socket

def shell():
    command = sock.recv(1024)
    sock.send(b"Hola desde el cliente")
    print(command.decode('utf-8'))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.88.254", 54321))

shell()
sock.close()
