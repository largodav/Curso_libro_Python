import socket
host="127.0.0.1"
puerto=1338
try:
    mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tupla_host_puerto=(host,puerto)
    mysocket.connect(tupla_host_puerto)
    mysocket.send(bytes("Hola mundo",'utf-8'))
    buffer = mysocket.recv(1024)
    print("Datos recibidos",buffer)
    mensaje="Mensaje desde el cliente\n"
    mysocket.sendall(bytes(mensaje.encode('utf-8')))
except socket.errno as error:
    print("Socket error ",error)
finally:
    mysocket.close()

