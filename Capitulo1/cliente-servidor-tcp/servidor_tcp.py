import socket
host = 'localhost'
puerto=1338
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tupla_host_puerto=(host,puerto)
s.bind(tupla_host_puerto)
s.listen(10)
print("Servidor tcp escuchando en el puerto",tupla_host_puerto)

while 1:
    cliente,addr = s.accept()
    print("conexion desde",addr)
    buffer=cliente.recv(1024)
    print("Datos recibidos",buffer)
    if buffer== b"Hola mundo":
        cliente.send(bytes("Servidor recibe Hola Mundo\n",'utf-8'))
    cliente.close()



